"""Testing strategy for dynamic testing via folder structure."""

# Python
import os
import re
import sys
import glob
import json
import inspect
import argparse
import importlib
from unittest.mock import Mock

# pyATS
from pyats import aetest
from pyats.topology import Device
from pyats.aetest.steps import Steps

# Genie
from genie.libs import parser as _parser
from genie.metaparser.util.exceptions import SchemaEmptyParserError


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
my_parser.add_argument('-n', "--number",
                       type=int,
                       help="The specific unittest we want to run, such as '25'",
                       default=None)
args = my_parser.parse_args()

_os = args.operating_system
_class = args.class_name
_token = args.token
_number = args.number

if _number and (not _class or not _number):
    sys.exit("Unittest number provided but missing supporting arguments:"
             "\n* '-c' or '--class_name' for the parser class"
             "\n* '-o' or '--operating_system' for operating system")

# This is the list of Classes that currently have no testing. It was found during the process
# of converting to folder based testing strategy
CLASS_SKIP = {
    "asa": {
        "ShowVpnSessiondbSuper": True,
        },
    "iosxe": {
        "c9300": {
            "ShowInventory": True,
        },
        "ShowDeviceTrackingDatabaseInterface": True,
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
        "ShowIpOspfLinksParser": True,
        "ShowIpRouteDistributor": True,
        "ShowIpv6RouteDistributor": True,
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
}

EMPTY_SKIP = {
    "iosxe": {"ShowVersion": True},
    "ios": {
        "ShowVersion": True,
        "ShowIpv6EigrpNeighbors": True,
        "ShowIpv6EigrpNeighborsDetail": True,
    },
}


def read_from_file(file_path):
    """Helper function to read from a file."""
    f = open(file_path, "r")
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


def get_operating_systems():
    """Helper Script to get operating systems."""
    # Update and fix as more OS's converted to folder baed tests
    if _os:
        return [_os]
    return ["asa", "ios", "iosxe"]
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
        tokens.append(path.split('/')[-2])
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

    OPERATING_SYSTEMS = get_operating_systems()
    @aetest.test
    @aetest.test.loop(operating_system=OPERATING_SYSTEMS)
    def check_os_folder(self, steps, operating_system, number=_number):
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
            _module = importlib.machinery.SourceFileLoader(module_name, parse_file).load_module()

            for name, local_class in inspect.getmembers(_module):
                # The following methods determin when a test is not warranted, further detail will be provided for each method.

                # If there is a token and the "class" was found to be a known whitelist (mainly since there was not existing tests),
                # skip. Whitelisted items should be cleaned up over time, and this removed to enforce testing always happens.
                if token and CLASS_SKIP.get(operating_system, {}).get(token, {}).get(name):
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
                    #if name == 'SomeClassName':
                    #    start = True
                    #if not start:
                    #    continue
                    if token:
                        msg = f"{operating_system} -> Token -> {token} -> {name}"
                    else:
                        msg = f"{operating_system} -> {name}"
                    with steps.start(msg) as class_step:
                        with class_step.start(
                            f"Test Golden -> {operating_system} -> {name}",
                            continue_=True,
                        ) as golden_steps:
                            self.test_golden(
                                golden_steps, local_class, operating_system, token, _number
                            )
                        with class_step.start(
                            f"Test Empty -> {operating_system} -> {name}",
                            continue_=True,
                        ) as empty_steps:
                            self.test_empty(empty_steps, local_class, operating_system, token)

    def test_golden(self, steps, local_class, operating_system, token=None, number=None):
        """Test step that finds any output named with _output.txt, and compares to similar named .py file."""
        if token:
            folder_root = f"{operating_system}/{token}/{local_class.__name__}/cli/equal"
        else:
            folder_root = f"{operating_system}/{local_class.__name__}/cli/equal"

        # Get list of output files to parse and sort
        convert = lambda text: int(text) if text.isdigit() else text
        aph_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        if number and not operating_system or not local_class:
            output_glob = sorted(glob.glob(f"{folder_root}/golden_output{number}_output.txt"), key=aph_key)
        else:
            output_glob = sorted(glob.glob(f"{folder_root}/*_output.txt"), key=aph_key)

        if len(output_glob) == 0:
            self.failed(f"No files found in appropriate directory for {local_class}")

        # Look for any files ending with _output.txt, presume the user defined name from that (based
        # on truncating that _output.txt suffix) and obtaining expected results and potentially an arguments file
        for user_defined in output_glob:
            user_test = os.path.basename(user_defined[: -len("_output.txt")])
            if token:
                msg = f"Gold -> {operating_system} -> Token {token} -> {local_class.__name__} -> {user_test}",
            else:
                msg = f"Gold -> {operating_system} -> {local_class.__name__} -> {user_test}",
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
                assert parsed_output == golden_parsed_output, "{parsed_output} \n!=\n{golden_parsed_output}".format(parsed_output=parsed_output, golden_parsed_output=golden_parsed_output)

    def test_empty(self, steps, local_class, operating_system, token=None):
        """Test step that looks for empty output."""
        if token:
            folder_root = f"{operating_system}/{token}/{local_class.__name__}/cli/empty"

        else:
            folder_root = f"{operating_system}/{local_class.__name__}/cli/empty"
        output_glob = glob.glob(f"{folder_root}/*_output.txt")

        if (
            len(output_glob) == 0
            and not EMPTY_SKIP.get(operating_system, {}).get(local_class.__name__)
        ):
            self.failed(
                f"No files found in appropriate directory for {local_class} empty file"
            )

        for user_defined in output_glob:
            user_test = os.path.basename(user_defined[: -len("_output.txt")])
            if token:
                msg = f"Empty -> {operating_system} -> {token} -> {local_class.__name__} -> {user_test}"
            else:
                msg = f"Empty -> {operating_system} -> {local_class.__name__} -> {user_test}"
            with steps.start(msg, continue_=True):
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
                    self.failed(f"File parsed, when expected not to for {local_class}")
                except SchemaEmptyParserError:
                    return True
                except AttributeError:
                    return True


if __name__ == "__main__":
    aetest.main()
