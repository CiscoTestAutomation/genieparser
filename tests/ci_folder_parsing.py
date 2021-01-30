"""Testing strategy for dynamic testing via folder structure."""

# Python
import os
import re
import sys
import glob
import json
import logging
import inspect
import argparse
import importlib
from unittest.mock import Mock

# pyATS
from pyats import aetest
from ats.easypy import runtime
from pyats.topology import Device
from pyats.log.utils import banner
from pyats.aetest.steps import Steps


# Genie
from genie.utils.diff import Diff
from genie.libs import parser as _parser
from genie.metaparser.util.exceptions import SchemaEmptyParserError


log = logging.getLogger(__name__)

def read_from_file(file_path):
    """Helper function to read from a file."""
    with open(file_path, "r") as f:
        return f.read()


def read_json_file(file_path):
    """Helper function to read in json."""
    with open(file_path) as f:
        data = json.load(f)
    return data


def read_python_file(file_path):
    """Helper function to read in a Python file, and look for expected_output."""
    _module = importlib.machinery.SourceFileLoader("expected", file_path).load_module()
    return getattr(_module, "expected_output")


def get_operating_systems(_os):
    """Helper Script to get operating systems."""
    # Update and fix as more OS's converted to folder based tests
    if _os:
        return [_os]
    return ["asa", "ios", "iosxe", "junos", "viptela"]
    # operating_system = []
    # for folder in os.listdir("./"):
    #    if os.path.islink("./" + folder):
    #        operating_system.append(folder)
    # return operating_system


# The get_tokens function dynamically finds tokens by leveraging globs. This
# works based on the deterministic folder structure. Within a given OS root folder one can
# determine that a sub folder is in fact a token, if there is a "tests" directory. Upon removing
# the .py via [-2], there is now a list of files to import from.
def get_tokens(folder):
    tokens = []
    for path in glob.glob(f"{folder}/*/tests"):
        tokens.append(path.split("/")[-2])
    return tokens


def get_files(folder, token=None):
    files = []
    for parse_file in glob.glob(f"{folder}/*.py"):
        if parse_file.endswith("__init__.py"):
            continue
        files.append({"parse_file": parse_file, "token": token})
    return files


class FileBasedTest(aetest.Testcase):
    """Standard pyats testcase class."""

    # removes screenhandler from root, but tasklog handler
    # is kept to allow all logs to be visible in the report
    def remove_logger(self):
        if log.root.handlers:
            self.temporary_screen_handler = log.root.handlers.pop(0)
    
    # adds screenhandler back to root
    def add_logger(self):
        if self.temporary_screen_handler:
            log.root.handlers.insert(0,self.temporary_screen_handler)

    # Decorator function. Calls remove_logger if _display_only_failed flag if used
    # and screenhandler is in log.root.handlers
    def screen_log_handling(func):
        def wrapper(self,*args, **kwargs):
            func(self,*args, **kwargs)
            if self.parameters['_display_only_failed'] and self.temporary_screen_handler in log.root.handlers:
                self.remove_logger()
        return wrapper

    # constructor used to initialize the class attribute temporary_screen_handler
    # which will point to the screenhandler log, which is used to display
    # data on stdout
    def __init__(self, *args, **kwargs):
        # init parent
        super().__init__(*args, **kwargs)
        self.temporary_screen_handler = None

    # setup portion used to define command line options
    @aetest.setup
    def setup(self, _os, _class, _token, _number, _display_only_failed):

        # removes screenhandler from root if _display_only_failed 
        # flag is passed
        if _display_only_failed and log.root.handlers:
            self.temporary_screen_handler = log.root.handlers.pop(0)

        aetest.loop.mark(self.test, operating_system=get_operating_systems(_os))

    @aetest.test
    def test(self,operating_system, steps, _os, _class, _token, _number, _display_only_failed):

        """Loop through OS's and run appropriate tests."""
        base_folder = f"../src/genie/libs/parser/{operating_system}"
        # Please refer to get_tokens comments for the how, the what is a genie token, such as
        # "asr1k" or "c3850" to provide namespaced parsing.
        tokens = get_tokens(base_folder)
        parse_files = []
        parse_files.extend(get_files(base_folder))
        for token in tokens:
            parse_files.extend(get_files(f"{base_folder}/{token}", token))
        start = False
        # Get all of the root level files
        for details in parse_files:
            parse_file = details["parse_file"]
            token = details["token"]
            # Load all of the classes in each of those files, and search for classes
            # that have a `cli` method
            _module = None
            module_name = os.path.basename(parse_file[: -len(".py")])
            if token:
                module_name = f"{operating_system}_{token}_{module_name}"
            else:
                module_name = f"{operating_system}_{module_name}"
            _module = importlib.machinery.SourceFileLoader(
                module_name, parse_file
            ).load_module()

            for name, local_class in inspect.getmembers(_module):
                # The following methods determin when a test is not warranted, further detail will be provided for each method.

                # If there is a token and the "class" was found to be a known whitelist (mainly since there was not existing tests),
                # skip. Whitelisted items should be cleaned up over time, and this removed to enforce testing always happens.
                if token and CLASS_SKIP.get(operating_system, {}).get(token, {}).get(
                    name
                ):
                    continue
                # Same as previous, but in cases without tokens (which is the majority.)
                elif not token and CLASS_SKIP.get(operating_system, {}).get(name):
                    continue

                # This is used in conjunction with the arguments that are run at command line, to skip over all tests you are
                # not concerned with. Basically, it allows a user to not have to wait for 100s of tests to run, to run their
                # one test.
                if _token and _token != token:
                    continue
                # Same as previous, however, for class
                if _class and _class != name:
                    continue
                # Each "globals()" is checked to see if it has a cli attribute, if so, assumed to be a parser. The _osxe, is
                # since the ios module often refers to the iosxe parser, leveraging this naming convention.
                if hasattr(local_class, "cli") and not name.endswith("_iosxe"):
                    # if name == 'SomeClassName':
                    #    start = True
                    # if not start:
                    #    continue
                    if token:
                        msg = f"{operating_system} -> Token -> {token} -> {name}"
                    else:
                        msg = f"{operating_system} -> {name}"
                    with steps.start(msg, continue_=True) as class_step:
                        with class_step.start(
                            f"Test Golden -> {operating_system} -> {name}",
                            continue_=True,
                        ) as golden_steps:
                            self.test_golden(
                                golden_steps, local_class, operating_system, _display_only_failed, token, _number
                            )

                        with class_step.start(
                            f"Test Empty -> {operating_system} -> {name}",
                            continue_=True,
                        ) as empty_steps:
                            self.test_empty(
                                empty_steps, local_class, operating_system, token
                            )


    @screen_log_handling
    def test_golden(self, steps, local_class, operating_system,_display_only_failed=None, token=None, number=None):
        """Test step that finds any output named with _output.txt, and compares to similar named .py file."""
        if token:
            folder_root = f"{operating_system}/{token}/{local_class.__name__}/cli/equal"
        else:
            folder_root = f"{operating_system}/{local_class.__name__}/cli/equal"

        # Get list of output files to parse and sort
        convert = lambda text: int(text) if text.isdigit() else text
        aph_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
        if number and not operating_system or not local_class:
            output_glob = sorted(
                glob.glob(f"{folder_root}/golden_output{number}_output.txt"),
                key=aph_key,
            )
        else:
            output_glob = sorted(glob.glob(f"{folder_root}/*_output.txt"), key=aph_key)

        if len(output_glob) == 0:
            steps.failed(f"No files found in appropriate directory for {local_class}")

        # Look for any files ending with _output.txt, presume the user defined name from that (based
        # on truncating that _output.txt suffix) and obtaining expected results and potentially an arguments file
        
        for user_defined in output_glob:
            user_test = os.path.basename(user_defined[: -len("_output.txt")])
            if token:
                msg = f"Gold -> {operating_system} -> Token {token} -> {local_class.__name__} -> {user_test}"
            else:
                msg = f"Gold -> {operating_system} -> {local_class.__name__} -> {user_test}"

            with steps.start(msg, continue_=True):
                golden_output_str = read_from_file(
                    f"{folder_root}/{user_test}_output.txt"
                )
                golden_output = {"execute.return_value": golden_output_str}

                golden_parsed_output = read_python_file(
                    f"{folder_root}/{user_test}_expected.py"
                )
                arguments = {}
                if os.path.exists(f"{folder_root}/{user_test}_arguments.json"):
                    arguments = read_json_file(
                        f"{folder_root}/{user_test}_arguments.json"
                    )

                device = Mock(**golden_output)
                obj = local_class(device=device)
                parsed_output = obj.parse(**arguments)
                
                # Use Diff method to get the difference between 
                # what is expected and the parsed output
                dd = Diff(parsed_output,golden_parsed_output)
                dd.findDiff()
                if parsed_output != golden_parsed_output:
                    # if -f flag provided, then add the screen handler back into
                    # the root.handlers to displayed failed tests. Decorator removes
                    # screen handler from root.handlers after failed tests are displayed
                    # to stdout
                    if _display_only_failed:
                        self.add_logger()
                        log.info(banner(msg))
                    # Format expected and parsed output in a nice format
                    parsed_json_data = json.dumps(parsed_output, indent=4, sort_keys=True)
                    golden_parsed_output_json_data = json.dumps(golden_parsed_output, indent=4, sort_keys=True)
                    
                    # Display device output, parsed output, and golden_output of failed tests
                    log.info("\nThe following is the device output before it is parsed:\n{}\n".format(golden_output['execute.return_value']), extra = {'colour': 'yellow'})
                    log.info("The following is your device's parsed output:\n{}\n".format(parsed_json_data), extra = {'colour': 'yellow'})
                    log.info("The following is your expected output:\n{}\n".format(golden_parsed_output_json_data), extra = {'colour': 'yellow'})
                    log.info("The following is the difference between the two outputs:\n", extra = {'colour': 'yellow'})

                    # Display the diff between parsed output and golden_output
                    log.info(str(dd), extra = {'colour': 'yellow'})
                    raise AssertionError("Device output and expected output do not match")
                else:
                    # If tests pass, display the device output in debug mode
                    # But first check if the screen handler is removed, if it is
                    # put it back into the root otherwise just display to stdout
                    if self.temporary_screen_handler not in log.root.handlers and self.temporary_screen_handler != None:
                        self.add_logger()
                        logging.debug(banner(msg))
                        logging.debug("\nThe following is the device output for the passed parser:\n{}\n".format(golden_output['execute.return_value']), extra = {'colour': 'yellow'})
                        self.remove_logger()
                    else:
                        logging.debug(banner(msg))
                        logging.debug("\nThe following is the device output for the passed parser:\n{}\n".format(golden_output['execute.return_value']), extra = {'colour': 'yellow'})


    @screen_log_handling
    def test_empty(self, steps, local_class, operating_system, token=None):
        """Test step that looks for empty output."""
        if token:
            folder_root = f"{operating_system}/{token}/{local_class.__name__}/cli/empty"

        else:
            folder_root = f"{operating_system}/{local_class.__name__}/cli/empty"
        output_glob = glob.glob(f"{folder_root}/*_output.txt")

        if len(output_glob) == 0 and not EMPTY_SKIP.get(operating_system, {}).get(
            local_class.__name__
        ):
            steps.failed(
                f"No files found in appropriate directory for {local_class} empty file"
            )

        for user_defined in output_glob:
            user_test = os.path.basename(user_defined[: -len("_output.txt")])
            if token:
                msg = f"Empty -> {operating_system} -> {token} -> {local_class.__name__} -> {user_test}"
            else:
                msg = f"Empty -> {operating_system} -> {local_class.__name__} -> {user_test}"
            with steps.start(msg, continue_=True) as step_within:
                empty_output_str = read_from_file(
                    f"{folder_root}/{user_test}_output.txt"
                )
                empty_output = {"execute.return_value": empty_output_str}
                arguments = {}
                if os.path.exists(f"{folder_root}/{user_test}_arguments.json"):
                    arguments = read_json_file(
                        f"{folder_root}/{user_test}_arguments.json"
                    )
                device = Mock(**empty_output)
                obj = local_class(device=device)
                try:
                    obj.parse(**arguments)
                    # if -f flag provided, then add the screen handler back into
                    # the root.handlers to display failed tests. Decorator removes
                    # screen handler from root.handlers after failed tests are displayed
                    # to stdout
                    if _display_only_failed:
                        self.add_logger()
                    step_within.failed(f"File parsed, when expected not to for {local_class}")
                except SchemaEmptyParserError:
                    return True
                except AttributeError:
                    return True

CLASS_SKIP = {
    "asa": {
        "ShowVpnSessiondbSuper": True,
        },
    "iosxe": {
        "c9300": {
            "ShowInventory": True,
        },
        "c9200": {
            "ShowEnvironmentAllSchema": True,
            "ShowEnvironmentAll_C9300": True,
        },
        "ShowPimNeighbor": True,
        "ShowIpInterfaceBrief": True,
        "ShowIpInterfaceBriefPipeVlan": True,
        "ShowBfdSessions": True,
        "ShowBfdSessions_viptela": True,
        "ShowBfdSummary": True,
        "ShowDot1x": True,
        "ShowEnvironmentAll": True,
        "ShowControlConnections_viptela": True,
        "ShowControlConnections": True,
        "ShowEigrpNeighborsSuperParser": True,
        "ShowIpEigrpNeighborsDetailSuperParser": True,
        "ShowIpOspfInterface": True,
        "ShowIpOspfNeighborDetail": True,
        "ShowIpOspfShamLinks": True,
        "ShowIpOspfVirtualLinks": True,
        "ShowIpOspfMplsTrafficEngLink": True,
        "ShowIpOspfDatabaseOpaqueAreaTypeExtLink": True,
        "ShowIpOspfDatabaseOpaqueAreaTypeExtLinkAdvRouter": True,
        "ShowIpOspfDatabaseOpaqueAreaTypeExtLinkSelfOriginate": True,
        "ShowIpOspfDatabaseTypeParser": True,
        "ShowIpOspfLinksParser": True,  # super class
        "ShowIpOspfLinksParser2": True, # super class
        "ShowIpRouteDistributor": True, # super class
        "ShowIpv6RouteDistributor": True, # super class
        "ShowControlLocalProperties_viptela": True,
        "ShowControlLocalProperties": True,
        "ShowVrfDetailSuperParser": True,
        "ShowBgp": True,
        "ShowBgpAllNeighborsRoutesSuperParser": True,
        "ShowBgpDetailSuperParser": True,
        "ShowBgpNeighborSuperParser": True,
        "ShowBgpNeighborsAdvertisedRoutesSuperParser": True,
        "ShowBgpNeighborsReceivedRoutes": True,
        "ShowBgpNeighborsReceivedRoutesSuperParser": True,
        "ShowBgpNeighborsRoutes": True,
        "ShowBgpSummarySuperParser": True,
        "ShowBgpSuperParser": True,
        "ShowIpBgpAllNeighborsAdvertisedRoutes": True,
        "ShowIpBgpAllNeighborsReceivedRoutes": True,
        "ShowIpBgpNeighborsReceivedRoutes": True,
        "ShowIpBgpNeighborsRoutes": True,
        "ShowIpBgpRouteDistributer": True,
        "ShowPolicyMapTypeSuperParser": True,
        "ShowIpLocalPool": True,
        "ShowInterfaceDetail": True,
        "ShowInterfaceIpBrief": True,
        "ShowInterfaceSummary": True,
        "ShowAuthenticationSessionsInterface": True,
        "ShowVersion_viptela": True,
        "ShowOmpPeers_viptela": True,
        "ShowBfdSummary_viptela": True,
        "ShowOmpTlocPath_viptela": True,
        "ShowOmpTlocs_viptela": True,
        "ShowSoftwaretab_viptela": True, # PR submitted
        "ShowRebootHistory_viptela": True,
        "ShowOmpSummary_viptela": True,
        "ShowSystemStatus_viptela": True,
        "ShowTcpProxyStatistics": True, # PR submitted
        "ShowTcpproxyStatus": True, # PR submitted
        "ShowPlatformTcamUtilization": True, # PR submitted
        "ShowLicense": True, # PR submitted
        "Show_Stackwise_Virtual_Dual_Active_Detection": True, # PR submitted
        "ShowSoftwaretab": True, # PR submitted
        "ShowOmpPeers_viptela": True,
        "ShowOmpTlocPath_viptela": True,
        "ShowOmpTlocs_viptela": True,
        "genie": True, # need to check
    },
    "ios": {
        "ShowPimNeighbor": True,
        "ShowInterfacesTrunk": True,
        "ShowIpInterfaceBrief": True,
        "ShowIpInterfaceBriefPipeVlan": True,
        "ShowDot1x": True,
        "ShowBoot": True,
        "ShowPagpNeighbor": True,
        "ShowIpProtocols": True,
        "ShowIpv6Rpf": True,
        "ShowIpOspfDatabaseRouter": True,
        "ShowIpOspfInterface": True,
        "ShowIpOspfMplsTrafficEngLink": True,
        "ShowIpOspfNeighborDetail": True,
        "ShowIpOspfShamLinks": True,
        "ShowIpOspfVirtualLinks": True,
        "ShowIpRouteDistributor": True, # super class
        "ShowIpv6RouteDistributor": True, # super class
        "ShowIpv6Route": True,
        "ShowIpBgp": True,
        "ShowMplsLdpNeighbor": True,
        "ShowInterfaceDetail": True,
        "ShowInterfaceIpBrief": True,
        "ShowInterfaceSummary": True,
        "ShowInterfaceTransceiverDetail": True,
        "ShowSdwanSystemStatus": True,
        "ShowSdwanSoftware": True,
    },
    "junos": {
        "MonitorInterfaceTraffic": True, # issue with Mac
        "ShowBgpGroupDetailNoMore": True, # need to check
        "ShowBgpGroupBriefNoMore": True, # need to check
        "ShowTaskMemory": True, # need to check
        "ShowConfigurationSystemNtp": True, # need to check
        "ShowLDPSession": True, # need to check
        "ShowOspfNeighborInstance": True, # need to check
        "ShowOspfDatabaseAdvertisingRouterExtensive": True, # need to check
        "ShowArpNoMore": True, # need to check
        "ShowRouteProtocolNoMore": True, # need to check
        "ShowRouteLogicalSystem": True, # need to check
        "ShowInterfacesTerseInterface": True, # need to check
        "ShowInterfacesExtensiveNoForwarding": True, # need to check
        "ShowInterfacesExtensiveInterface": True, # need to check
        "ShowOspf3NeighborInstance": True, # need to check
    }
}

EMPTY_SKIP = {
    "iosxe": {"ShowVersion": True},
    "ios": {
        "ShowVersion": True,
        "ShowIpv6EigrpNeighbors": True,
        "ShowIpv6EigrpNeighborsDetail": True,
    },
}

if __name__ == "__main__":

    # Create the parser
    my_parser = argparse.ArgumentParser(description="Optional arguments for 'nose'-like tests")

    my_parser.add_argument('-o', "--operating_system",
                        type=str,
                        help='The OS you wish to filter on',
                        default=None)
    my_parser.add_argument('-c', "--class_name",
                        type=str,
                        help="The Class you wish to filter on, (not the Test File)",
                        default=None)
    my_parser.add_argument('-t', "--token",
                        type=str,
                        help="The Token associated with the class, such as 'asr1k'",
                        default=None)
    my_parser.add_argument('-f', "--display_only_failed",
                        help="Displaying only failed classes",
                        action='store_true')
    my_parser.add_argument('-n', "--number",
                        type=int,
                        help="The specific unittest we want to run, such as '25'",
                        default=None)
    args = my_parser.parse_args()

    _os = args.operating_system
    _class = args.class_name
    _token = args.token
    _display_only_failed = args.display_only_failed
    _number = args.number

    if _number and (not _class or not _number):
        sys.exit("Unittest number provided but missing supporting arguments:"
                "\n* '-c' or '--class_name' for the parser class"
                "\n* '-o' or '--operating_system' for operating system")


    if _display_only_failed and log.root.handlers:
        temporary_screen_handler = log.root.handlers.pop(0)
    

    aetest.main(
        _os=_os,
        _class=_class,
        _token=_token,
        _display_only_failed=_display_only_failed,
        _number=_number
    )

else:
    aetest.main() 
    
