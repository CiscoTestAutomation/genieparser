"""Testing strategy for dynamic testing via folder structure."""

# Python
import os
import re
import sys
import glob
import json
import logging
import inspect
import pathlib
import argparse
import importlib
from unittest.mock import Mock

# pyATS
from pyats import aetest
from ats.easypy import run
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
    return ["asa", "ios", "iosxe", "junos", "iosxr", "nxos"]
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
    for path in glob.glob(str(folder / '*' / 'tests')):
        tokens.append(path.split("/")[-2])
    return tokens


def get_files(folder, token=None):
    files = []
    for parse_file in glob.glob(str(folder / "*.py")):
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
    def setup(self, _os, _class, _token, _display_only_failed, _number):

        # removes screenhandler from root if _display_only_failed 
        # flag is passed
        if _display_only_failed and log.root.handlers:
            self.temporary_screen_handler = log.root.handlers.pop(0)

        aetest.loop.mark(self.test, operating_system=get_operating_systems(_os))

    @aetest.test
    def test(self,operating_system, steps, _os, _class, _token, _number, _display_only_failed, _external_folder):

        """Loop through OS's and run appropriate tests."""
        if _external_folder:
            base_folder = _external_folder / operating_system
        else:
            base_folder = pathlib.Path(f"{pathlib.Path(_parser.__file__).parent}/{operating_system}")
        # Please refer to get_tokens comments for the how, the what is a genie token, such as
        # "asr1k" or "c3850" to provide namespaced parsing.
        tokens = get_tokens(base_folder)
        parse_files = []
        parse_files.extend(get_files(base_folder))
        for token in tokens:
            parse_files.extend(get_files(base_folder / token, token))
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
    def test_golden(self, steps, local_class, operating_system, display_only_failed=None, token=None, number=None):
        """Test step that finds any output named with _output.txt, and compares to similar named .py file."""
        if token:
            folder_root = pathlib.Path(f"{operating_system}/{token}/{local_class.__name__}/cli/equal")
        else:
            folder_root = pathlib.Path(f"{operating_system}/{local_class.__name__}/cli/equal")

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
                    if display_only_failed:
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
    def test_empty(self, steps, local_class, operating_system, token=None, display_only_failed=None):
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
                    if display_only_failed:
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
    "nxos": {
        "ShowAccessLists": True, # Not migrated
        "ShowAccessListsSummary": True, # Not migrated
        "ShowEnvironment": True, # Not migrated
        "ShowEnvironmentFan": True, # Not migrated
        "ShowEnvironmentFanDetail": True, # Not migrated
        "ShowEnvironmentPower": True, # Not migrated
        "ShowEnvironmentPowerDetail": True, # Not migrated
        "ShowEnvironmentTemperature": True, # Not migrated
        "ShowInterfaceCapabilities": True, # Not migrated
        "ShowInterfaceFec": True, # Not migrated
        "ShowInterfaceHardwareMap": True, # Not migrated
        "ShowEnvironmentTemperature": True, # Not migrated
        "ShowInterfaceTransceiver": True, # Not migrated
        "ShowInterfaceTransceiverDetails": True, # Not migrated
        "ShowIpArp": True, # Not migrated
        "ShowIpArpDetailVrfAll": True, # Not migrated
        "ShowIpArpSummaryVrfAll": True, # Not migrated
        "ShowIpArpstatisticsVrfAll": True, # Not migrated
        "ShowBgpAllDampeningFlapStatistics": True, # Not migrated
        "ShowBgpAllNexthopDatabase": True, # Not migrated
        "ShowBgpIpMvpn": True, # Not migrated
        "ShowBgpIpMvpnSaadDetail": True, # Not migrated
        "ShowBgpIpMvpnRouteType": True, # Not migrated
        "ShowBgpL2vpnEvpn": True, # Not migrated
        "ShowBgpL2vpnEvpnNeighbors": True, # Not migrated
        "ShowBgpL2vpnEvpnNeighborsAdvertisedRoutes": True, # Not migrated
        "ShowBgpL2vpnEvpnRouteType": True, # Not migrated
        "ShowBgpL2vpnEvpnSummary": True, # Not migrated
        "ShowBgpL2vpnEvpnWord": True, # Not migrated
        "ShowBgpLabels": True, # Not migrated
        "ShowBgpPeerPolicy": True, # Not migrated
        "ShowBgpPeerSession": True, # Not migrated
        "ShowBgpPeerTemplate": True, # Not migrated
        "ShowBgpPeerTemplateCmd": True, # Not migrated
        "ShowBgpPolicyStatisticsDampening": True, # Not migrated
        "ShowBgpPolicyStatisticsNeighbor": True, # Not migrated
        "ShowBgpPolicyStatisticsParser": True, # Not migrated
        "ShowBgpPolicyStatisticsRedistribute": True, # Not migrated
        "ShowBgpProcessVrfAll": True, # Not migrated
        "ShowBgpSessions": True, # Not migrated
        "ShowBgpVrfAllAll": True, # Not migrated
        "ShowBgpVrfAllAllDampeningParameters": True, # Not migrated
        "ShowBgpVrfAllAllNextHopDatabase": True, # Not migrated
        "ShowBgpVrfAllAllSummary": True, # Not migrated
        "ShowBgpVrfAllNeighbors": True, # Not migrated
        "ShowBgpVrfAllNeighborsAdvertisedRoutes": True, # Not migrated
        "ShowBgpVrfAllNeighborsReceivedRoutes": True, # Not migrated
        "ShowBgpVrfAllNeighborsRoutes": True, # Not migrated
        "ShowBgpVrfIpv4Unicast": True, # Not migrated
        "ShowRunningConfigBgp": True, # Not migrated
        "ShowCdpNeighbors": True, # Not migrated
        "ShowCheckpointSummary": True, # Not migrated
        "ShowDot1xAllDetails": True, # Not migrated
        "ShowDot1xAllStatistics": True, # Not migrated
        "ShowDot1xAllSummary": True, # Not migrated
        "ShowEigrpNeighborsDetailSuperParser": True, # Not migrated
        "ShowEigrpNeighborsSuperParser": True, # Not migrated
        "ShowEigrpTopology": True, # Not migrated
        "ShowIpv4EigrpNeighbors": True, # Not migrated
        "ShowIpv4EigrpNeighborsDetail": True, # Not migrated
        "ShowIpv6EigrpNeighbors": True, # Not migrated
        "ShowIpv6EigrpNeighborsDetail": True, # Not migrated
        "ShowFabricpathIsisAdjacency": True, # Not migrated
        "ShowMacAddressTable": True, # Not migrated
        "ShowMacAddressTableAgingTime": True, # Not migrated
        "ShowMacAddressTableBase": True, # Not migrated
        "ShowMacAddressTableLimit": True, # Not migrated
        "ShowMacAddressTableVni": True, # Not migrated
        "ShowFeature": True, # Not migrated
        "ShowFeatureSet": True, # Not migrated
        "ShowForwardingIpv4": True, # Not migrated
        "ShowHsrpAll": True, # Not migrated
        "ShowHsrpDelay": True, # Not migrated
        "ShowHsrpSummary": True, # Not migrated
        "ShowIpIgmpGroups": True, # Not migrated
        "ShowIpIgmpInterface": True, # Not migrated
        "ShowIpIgmpLocalGroups": True, # Not migrated
        "ShowIpIgmpSnooping": True, # Not migrated
        "ShowInterface": True, # Not migrated
        "ShowInterfaceSwitchport": True, # Not migrated
        "ShowIpInterfaceBrief": True, # Not migrated
        "ShowIpInterfaceBriefPipeVlan": True, # Not migrated
        "ShowIpInterfaceBriefVrfAll": True, # Not migrated
        "ShowIpv6InterfaceVrfAll": True, # Not migrated
        "ShowNveInterface": True, # Not migrated
        "ShowRunningConfigInterface": True, # Not migrated
        "ShowVrfAllInterface": True, # Not migrated
        "ShowIsis": True, # Not migrated
        "ShowIsisAdjacency": True, # Not migrated
        "ShowIsisHostname": True, # Not migrated
        "ShowIsisHostnameDetail": True, # Not migrated
        "ShowIsisInterface": True, # Not migrated
        "ShowIsisSpfLogDetail": True, # Not migrated
        "ShowL2routeEvpnMac": True, # Not migrated
        "ShowL2routeEvpnMacEvi": True, # Not migrated
        "ShowLacpCounters": True, # Not migrated
        "ShowLacpNeighbor": True, # Not migrated
        "ShowLacpSystemIdentifier": True, # Not migrated
        "ShowPortChannelDatabase": True, # Not migrated
        "ShowPortChannelSummary": True, # Not migrated
        "ShowLldpAll": True, # Not migrated
        "ShowLldpTimers": True, # Not migrated
        "ShowLldpTlvSelect": True, # Not migrated
        "ShowLldpTraffic": True, # Not migrated
        "ShowLoggingLogfile": True, # Not migrated
        "ShowForwardingDistributionMulticastRoute": True, # Not migrated
        "ShowIpMrouteVrfAll": True, # Not migrated
        "ShowIpStaticRouteMulticast": True, # Not migrated
        "ShowIpv6MrouteVrfAll": True, # Not migrated
        "ShowIpv6StaticRouteMulticast": True, # Not migrated
        "ShowIpv6MldGroups": True, # Not migrated
        "ShowIpv6MldInterface": True, # Not migrated
        "ShowIpMsdpPeerVrf": True, # Not migrated
        "ShowIpMsdpPolicyStatisticsSaPolicyIn": True, # Not migrated
        "ShowIpMsdpPolicyStatisticsSaPolicyInOut": True, # Not migrated
        "ShowIpMsdpPolicyStatisticsSaPolicyOut": True, # Not migrated
        "ShowIpMsdpSaCacheDetailVrf": True, # Not migrated
        "ShowIpv6IcmpNeighborDetail": True, # Not migrated
        "ShowIpv6NdInterface": True, # Not migrated
        "ShowIpv6Routers": True, # Not migrated
        "ShowNtpPeerStatus": True, # Not migrated
        "ShowNtpPeers": True, # Not migrated
        "ShowIpOspf": True, # Not migrated
        "ShowIpOspfDatabaseDetailParser": True, # Not migrated
        "ShowIpOspfDatabaseExternalDetail": True, # Not migrated
        "ShowIpOspfDatabaseNetworkDetail": True, # Not migrated
        "ShowIpOspfDatabaseOpaqueAreaDetail": True, # Not migrated
        "ShowIpOspfDatabaseRouterDetail": True, # Not migrated
        "ShowIpOspfDatabaseSummaryDetail": True, # Not migrated
        "ShowIpOspfInterface": True, # Not migrated
        "ShowIpOspfLinksParser": True, # Not migrated
        "ShowIpOspfMplsLdpInterface": True, # Not migrated
        "ShowIpOspfNeighborDetail": True, # Not migrated
        "ShowIpOspfShamLinks": True, # Not migrated
        "ShowIpOspfVirtualLinks": True, # Not migrated
        "ShowIpPimDf": True, # Not migrated
        "ShowIpPimGroupRange": True, # Not migrated
        "ShowIpPimInterface": True, # Not migrated
        "ShowIpPimNeighbor": True, # Not migrated
        "ShowIpPimPolicyStaticticsRegisterPolicy": True, # Not migrated
        "ShowIpPimRoute": True, # Not migrated
        "ShowIpPimRp": True, # Not migrated
        "ShowIpPimVrfDetail": True, # Not migrated
        "ShowIpv6PimDf": True, # Not migrated
        "ShowIpv6PimGroupRange": True, # Not migrated
        "ShowIpv6PimInterface": True, # Not migrated
        "ShowIpv6PimNeighbor": True, # Not migrated
        "ShowIpv6PimRoute": True, # Not migrated
        "ShowIpv6PimRp": True, # Not migrated
        "ShowIpv6PimVrfAllDetail": True, # Not migrated
        "ShowPimRp": True, # Not migrated
        "ShowRunningConfigPim": True, # Not migrated
        "Dir": True, # Not migrated
        "ShowBoot": True, # Not migrated
        "ShowCores": True, # Not migrated
        "ShowInstallActive": True, # Not migrated
        "ShowInventory": True, # Not migrated
        "ShowProcessesCpu": True, # Not migrated
        "ShowProcessesMemory": True, # Not migrated
        "ShowRedundancyStatus": True, # Not migrated
        "ShowSystemRedundancyStatus": True, # Not migrated
        "ShowVdcCurrent": True, # Not migrated
        "ShowVdcDetail": True, # Not migrated
        "ShowVdcMembershipStatus": True, # Not migrated
        "ShowVersion": True, # Not migrated
        "ShowIpPrefixList": True, # Not migrated
        "ShowIpv6PrefixList": True, # Not migrated
        "ShowProcesses": True, # Not migrated
        "ShowIpRipInterfaceVrfAll": True, # Not migrated
        "ShowIpRipNeighborVrfAll": True, # Not migrated
        "ShowIpRipRouteVrfAll": True, # Not migrated
        "ShowIpRipStatistics": True, # Not migrated
        "ShowIpRipVrfAll": True, # Not migrated
        "ShowIpv6RipInterfaceVrfAll": True, # Not migrated
        "ShowIpv6RipNeighborVrfAll": True, # Not migrated
        "ShowIpv6RipRouteVrfAll": True, # Not migrated
        "ShowIpv6RipStatistics": True, # Not migrated
        "ShowIpv6RipVrfAll": True, # Not migrated
        "ShowRunRip": True, # Not migrated
        "ShowRouteMap": True, # Not migrated
        "ShowIpRoute": True, # Not migrated
        "ShowIpRouteSummary": True, # Not migrated
        "ShowIpv6Route": True, # Not migrated
        "ShowRouting": True, # Not migrated
        "ShowRoutingIpv6VrfAll": True, # Not migrated
        "ShowRoutingVrfAll": True, # Not migrated
        "ShowErrdisableRecovery": True, # Not migrated
        "ShowSpanningTreeDetail": True, # Not migrated
        "ShowSpanningTreeMst": True, # Not migrated
        "ShowSpanningTreeSummary": True, # Not migrated
        "ShowIpStaticRoute": True, # Not migrated
        "ShowIpv6StaticRoute": True, # Not migrated
        "ShowSystemInternalL2fwderMac": True, # Not migrated
        "ShowSystemInternalSysmgrServiceName": True, # Not migrated
        "ShowRunningConfigTrm": True, # Not migrated
        "ShowVdcResourceDetail": True, # Not migrated
        "ShowGuestshell": True, # Not migrated
        "ShowVirtualServiceCore": True, # Not migrated
        "ShowVirtualServiceDetail": True, # Not migrated
        "ShowVirtualServiceGlobal": True, # Not migrated
        "ShowVirtualServiceList": True, # Not migrated
        "ShowVirtualServiceUtilization": True, # Not migrated
        "ShowVlan": True, # Not migrated
        "ShowVlanAccessMap": True, # Not migrated
        "ShowVlanFilter": True, # Not migrated
        "ShowVlanIdVnSegment": True, # Not migrated
        "ShowVlanInternalInfo": True, # Not migrated
        "ShowVxlan": True, # Not migrated
        "ShowVpc": True, # Not migrated
        "ShowRunningConfigVrf": True, # Not migrated
        "ShowVrfDetail": True, # Not migrated
        "ShowVrfInterface": True, # Not migrated
        "ShowFabricMulticastGlobals": True, # Not migrated
        "ShowFabricMulticastIpL2Mroute": True, # Not migrated
        "ShowFabricMulticastIpSaAdRoute": True, # Not migrated
        "ShowL2routeEvpnEternetSegmentAll": True, # Not migrated
        "ShowL2routeEvpnImetAllDetail": True, # Not migrated
        "ShowL2routeFlAll": True, # Not migrated
        "ShowL2routeEvpnMacIpEvi": True, # Not migrated
        "ShowL2routeMacAllDetail": True, # Not migrated
        "ShowL2routeMacIpAllDetail": True, # Not migrated
        "ShowL2routeSummary": True, # Not migrated
        "ShowL2routeTopologyDetail": True, # Not migrated
        "ShowNveInterface": True, # Not migrated
        "ShowNveInterfaceDetail": True, # Not migrated
        "ShowNveMultisiteDciLinks": True, # Not migrated
        "ShowNveMultisiteFabricLinks": True, # Not migrated
        "ShowNvePeers": True, # Not migrated
        "ShowNveVni": True, # Not migrated
        "ShowNveVniIngressReplication": True, # Not migrated
        "ShowNveVniSummary": True, # Not migrated
        "ShowRunningConfigNvOverlay": True, # Not migrated
        "ShowCdpNeighborsDetail": True, # Not migrated
        "ShowInterfaceDescription": True, # Not migrated
        "ShowInterfaceStatus": True, # Not migrated
        "ShowIpInterfaceVrfAll": True, # Not migrated
        "ShowIsisDatabaseDetail": True, # Not migrated
        "ShowIpv6MldLocalGroups": True, # Not migrated
        "ShowIpMsdpSummary": True, # Not migrated
        "ShowRunningConfigMsdp": True, # Not migrated
        "ShowIpv6NeighborDetail": True, # Not migrated
        "ShowL2routeEvpnMacIpAll": True, # Not migrated
        "ShowNveEthernetSegment": True, # Not migrated
        "aci":{
            "ShowPlatformInternalHalPolicyRedirdst": True, # Not migrated
            "ShowServiceRedirInfoGroup": True, # Not migrated
        },
    },
    "iosxr": {
        "Ping": True, # Not migrated
        "ShowAclAfiAll": True, # Not migrated
        "ShowAclEthernetServices": True, # Not migrated
        "ShowArpDetail": True, # Not migrated
        "ShowArpTrafficDetail": True, # Not migrated
        "ShowBfdSessionDestinationDetails": True, # Not migrated
        "ShowBgpEgressEngineering": True, # Not migrated
        "ShowBgpInstanceAfGroupConfiguration": True, # Not migrated
        "ShowBgpInstanceAllAll": True, # Not migrated
        "ShowBgpInstanceAllSessions": True, # Not migrated
        "ShowBgpInstanceNeighborsAdvertisedRoutes": True, # Not migrated
        "ShowBgpInstanceNeighborsDetail": True, # Not migrated
        "ShowBgpInstanceNeighborsReceivedRoutes": True, # Not migrated
        "ShowBgpInstanceNeighborsRoutes": True, # Not migrated
        "ShowBgpInstanceProcessDetail": True, # Not migrated
        "ShowBgpInstanceSessionGroupConfiguration": True, # Not migrated
        "ShowBgpInstanceSessions": True, # Not migrated
        "ShowBgpL2vpnEvpn": True, # Not migrated
        "ShowBgpL2vpnEvpnAdvertised": True, # Not migrated
        "ShowBgpL2vpnEvpnNeighbors": True, # Not migrated
        "ShowBgpNeighbors": True, # Not migrated
        "ShowBgpSummary": True, # Not migrated
        "ShowBgpVrfDbVrfAll": True, # Not migrated
        "ShowEthernetTags": True, # due to duplication
        "ShowPlacementProgramAll": True, # Not migrated
        "ShowL2VpnBridgeDomainBrief": True, # Not migrated
        "ShowL2VpnBridgeDomainDetail": True, # Not migrated
        "ShowL2VpnBridgeDomainSummary": True, # Not migrated
        "ShowCdpNeighbors": True, # Not migrated
        "ShowCdpNeighborsDetail": True, # Not migrated
        "ShowControllersCoherentDSP": True, # Not migrated
        "ShowControllersFiaDiagshellDiagCosqQp": True, # Not migrated
        "ShowControllersFiaDiagshellDiagEgrCal": True, # Not migrated
        "ShowControllersFiaDiagshellL2showLoca": True, # Not migrated
        "ShowControllersNpuInterfaceInstanceLo": True, # Not migrated
        "ShowControllersOptics": True, # Not migrated
        "ShowImDampening": True, # Not migrated
        "ShowImDampeningIntf": True, # Not migrated
        "ShowBgpInstances": True, # Not migrated
        "ShowSegmentRoutingLocalBlockInconsistencies": True, # Not migrated
        "ShowSegmentRoutingMappingServerPrefixSidMapIPV4": True, # Not migrated
        "ShowSegmentRoutingMappingServerPrefixSidMapIPV4Detail": True, # Not migrated
        "ShowControllersFiaDiagshellDiagCosqQpairEgpMap": True, # Not migrated
        "ShowControllersFiaDiagshellDiagEgrCalendarsLocation": True, # Not migrated
        "ShowControllersFiaDiagshellL2showLocation": True, # Not migrated
        "ShowControllersNpuInterfaceInstanceLocation": True, # Not migrated
        "ShowL2vpnForwardingProtectionMainInterface": True, # Not migrated
        "ShowEigrpIpv4Neighbors": True, # Not migrated
        "ShowEigrpIpv4NeighborsDetail": True, # Not migrated
        "ShowEigrpIpv6Neighbors": True, # Not migrated
        "ShowEigrpIpv6NeighborsDetail": True, # Not migrated
        "ShowEigrpNeighborsDetailSuperParser": True, # Not migrated
        "ShowEigrpNeighborsSuperParser": True, # Not migrated
        "ShowEthernetCfmMeps": True, # Not migrated
        "ShowEthernetTrunkDetail": True, # Not migrated
        "ShowEvpnEthernetSegment": True, # Not migrated
        "ShowEvpnEthernetSegmentDetail": True, # Not migrated
        "ShowEvpnEthernetSegmentEsiDetail": True, # Not migrated
        "ShowEvpnEthernetSegmentPrivate": True, # Not migrated
        "ShowEvpnEvi": True, # Not migrated
        "ShowEvpnEviDetail": True, # Not migrated
        "ShowEvpnEviMac": True, # Not migrated
        "ShowEvpnEviMacPrivate": True, # Not migrated
        "ShowEvpnInternalLabel": True, # Not migrated
        "ShowEvpnInternalLabelDetail": True, # Not migrated
        "ShowHsrpDetail": True, # Not migrated
        "ShowHsrpSummary": True, # Not migrated
        "ShowIgmpGroupsDetail": True, # Not migrated
        "ShowIgmpGroupsSummary": True, # Not migrated
        "ShowIgmpInterface": True, # Not migrated
        "ShowIgmpSummary": True, # Not migrated
        "ShowInterfaceBrief": True, # Not migrated
        "ShowIpv4InterfaceBrief": True, # Not migrated
        "ShowIpv6Neighbors": True, # Not migrated
        "ShowIpv6NeighborsDetail": True, # Not migrated
        "ShowIsis": True, # Not migrated
        "ShowIsisAdjacency": True, # Not migrated
        "ShowIsisDatabaseDetail": True, # Not migrated
        "ShowIsisFastRerouteSummary": True, # Not migrated
        "ShowIsisHostname": True, # Not migrated
        "ShowIsisInterface": True, # Not migrated
        "ShowIsisLspLog": True, # Not migrated
        "ShowIsisNeighbors": True, # Not migrated
        "ShowIsisPrivateAll": True, # Not migrated
        "ShowIsisProtocol": True, # Not migrated
        "ShowIsisSegmentRoutingLabelTable": True, # Not migrated
        "ShowIsisSpfLog": True, # Not migrated
        "ShowIsisSpfLogDetail": True, # Not migrated
        "ShowIsisStatistics": True, # Not migrated
        "ShowL2routeEvpnMacAll": True, # Not migrated
        "ShowL2routeEvpnMacIpAll": True, # Not migrated
        "ShowL2routeTopology": True, # Not migrated
        "ShowL2vpnBridgeDomain": True, # Not migrated
        "ShowL2vpnBridgeDomainBrief": True, # Not migrated
        "ShowL2vpnBridgeDomainDetail": True, # Not migrated
        "ShowL2vpnBridgeDomainSummary": True, # Not migrated
        "ShowL2vpnForwardingBridgeDomainMacAdd": True, # Not migrated
        "ShowL2vpnForwardingProtectionMainInte": True, # Not migrated
        "ShowL2vpnMacLearning": True, # Not migrated
        "ShowBundle": True, # Not migrated
        "ShowBundleReasons": True, # Not migrated
        "ShowLacp": True, # Not migrated
        "ShowLacpSystemId": True, # Not migrated
        "ShowLldp": True, # Not migrated
        "ShowLldpEntry": True, # Not migrated
        "ShowLldpNeighborsDetail": True, # Not migrated
        "ShowLldpTraffic": True, # Not migrated
        "ShowLogging": True, # Not migrated
        "ShowMfibPlatformEvpnBucketLocation": True, # Not migrated
        "ShowMldGroupsDetail": True, # Not migrated
        "ShowMldGroupsGroupDetail": True, # Not migrated
        "ShowMldInterface": True, # Not migrated
        "ShowMldSummaryInternal": True, # Not migrated
        "ShowMplsForwarding": True, # Not migrated
        "ShowMplsForwardingVrf": True, # Not migrated
        "ShowMplsInterfaces": True, # Not migrated
        "ShowMplsLabelRange": True, # Not migrated
        "ShowMplsLabelTableDetail": True, # Not migrated
        "ShowMplsLabelTablePrivate": True, # Not migrated
        "ShowMplsLdpDiscovery": True, # Not migrated
        "ShowMplsLdpNeighbor": True, # Not migrated
        "ShowMplsLdpNeighborBrief": True, # Not migrated
        "ShowMplsLdpNeighborDetail": True, # Not migrated
        "ShowMribEvpnBucketDb": True, # Not migrated
        "ShowMribVrfRoute": True, # Not migrated
        "ShowMribVrfRouteSummary": True, # Not migrated
        "ShowMsdpContext": True, # Not migrated
        "ShowMsdpPeer": True, # Not migrated
        "ShowMsdpSaCache": True, # Not migrated
        "ShowMsdpStatisticsPeer": True, # Not migrated
        "ShowMsdpSummary": True, # Not migrated
        "ShowNtpStatus": True, # Not migrated
        "ShowRunningConfigNtp": True, # Not migrated
        "ShowOspfMplsTrafficEngLink": True, # Not migrated
        "ShowOspfVrfAllInclusive": True, # Not migrated
        "ShowOspfVrfAllInclusiveDatabaseExternal": True, # Not migrated
        "ShowOspfVrfAllInclusiveDatabaseNetwork": True, # Not migrated
        "ShowOspfVrfAllInclusiveDatabaseOpaqu": True, # Not migrated
        "ShowOspfVrfAllInclusiveDatabaseParser": True, # Not migrated
        "ShowOspfVrfAllInclusiveDatabaseRouter": True, # Not migrated
        "ShowOspfVrfAllInclusiveDatabaseSummary": True, # Not migrated
        "ShowOspfVrfAllInclusiveInterface": True, # Not migrated
        "ShowOspfVrfAllInclusiveLinksParser": True, # Not migrated
        "ShowOspfVrfAllInclusiveNeighborDetail": True, # Not migrated
        "ShowOspfVrfAllInclusiveShamLinks": True, # Not migrated
        "ShowOspfVrfAllInclusiveVirtualLinks": True, # Not migrated
        "ShowPimTopologySummary": True, # Not migrated
        "ShowPimVrfInterfaceDetail": True, # Not migrated
        "ShowPimVrfMstatic": True, # Not migrated
        "ShowPimVrfRpfSummary": True, # Not migrated
        "AdminShowDiagChassis": True, # Not migrated
        "Dir": True, # Not migrated
        "ShowInstallActiveSummary": True, # Not migrated
        "ShowInstallCommitSummary": True, # Not migrated
        "ShowInstallInactiveSummary": True, # Not migrated
        "ShowPlatformVm": True, # Not migrated
        "ShowProcessesMemory": True, # Not migrated
        "ShowRedundancy": True, # Not migrated
        "ShowRedundancySummary": True, # Not migrated
        "ShowSdrDetail": True, # Not migrated
        "ShowVersion": True, # Not migrated
        "ShowRplPrefixSet": True, # Not migrated
        "ShowProcesses": True, # Not migrated
        "ShowProcessesCpu": True, # Not migrated
        "ShowProtocolsAfiAllAll": True, # Not migrated
        "ShowRibTables": True, # Not migrated
        "ShowImDampeningIntf": True, # Not migrated
        "ShowIpInterfaceBriefPipeVlan": True, # Not migrated
        "ShowL2vpnForwardingBridgeDomainMacAddress": True, # Not migrated
        "ShowL2vpnForwardingProtectionMainInter": True, # Not migrated
        "ShowLldpInterface": True, # Not migrated
        "ShowMfibRouteSummary": True, # Not migrated
        "ShowNtpAssociations": True, # Not migrated
        "ShowOspfVrfAllInclusiveDatabaseOpaque": True, # Not migrated
        "ShowInventory": True, # Not migrated
        "ShowProcessesMemoryDetail": True, # Not migrated
        "ShowRibTablesSummary": True, # Not migrated
        "ShowOspfVrfAllInclusiveDatabaseOpaqueArea": True, # Not migrated
        "ShowRip": True, # Not migrated
        "ShowRipDatabase": True, # Not migrated
        "ShowRipInterface": True, # Not migrated
        "ShowRipStatistics": True, # Not migrated
        "ShowRouteIpv4": True, # Not migrated
        "ShowRouteIpv6": True, # Not migrated
        "ShowRplRoutePolicy": True, # Not migrated
        "ShowRunKeyChain": True, # Not migrated
        "ShowRunRouterIsis": True, # Not migrated
        "ShowIsisSegmentRoutingPrefixSidMap": True, # Not migrated
        "ShowOspfSegmentRoutingPrefixSidMap": True, # Not migrated
        "ShowPceIPV4Peer": True, # Not migrated
        "ShowPceIPV4PeerDetail": True, # Not migrated
        "ShowPceIPV4PeerPrefix": True, # Not migrated
        "ShowPceIpv4TopologySummary": True, # Not migrated
        "ShowPceLsp": True, # Not migrated
        "ShowPceLspDetail": True, # Not migrated
        "ShowSegmentRoutingLocalBlockInconsist": True, # Not migrated
        "ShowSegmentRoutingMappingServerPrefix": True, # Not migrated
        "ShowSpanningTreeMst": True, # Not migrated
        "ShowSpanningTreeMstag": True, # Not migrated
        "ShowSpanningTreePvrsTag": True, # Not migrated
        "ShowSpanningTreePvrst": True, # Not migrated
        "ShowSpanningTreePvsTag": True, # Not migrated
        "ShowSsh": True, # Not migrated
        "ShowSshHistory": True, # Not migrated
        "ShowStaticTopologyDetail": True, # Not migrated
        "ShowTrafficCollecterExternalInterface": True, # Not migrated
        "ShowTrafficCollecterIpv4CountersPrefi": True, # Not migrated
        "ShowVrfAllDetail": True, # Not migrated
        "ShowL2VpnXconnectBrief": True, # Not migrated
        "ShowL2VpnXconnectSummary": True, # Not migrated
        "ShowL2vpnXconnect": True, # Not migrated
        "ShowL2vpnXconnectDetail": True, # Not migrated
        "ShowL2vpnXconnectMp2mpDetail": True, # Not migrated
        "Traceroute": True, # Not migrated
        "ShowRouteAllSummary": True, # Not migrated
        "ShowSegmentRoutingLocalBlockInconsiste": True, # Not migrated
        "ShowSegmentRoutingMappingServerPrefixS": True, # Not migrated
        "ShowBgpSessions": True, # Not migrated
        "ShowTrafficCollecterIpv4CountersPrefixDetail": True, # Not migrated
        "ShowL2vpnXconnectSummary": True, # Not migrated
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

def _parse_args(
        operating_system=None,
        class_name=None,
        token=None,
        display_only_failed=None,
        number=None,
        external_folder=None,
        o=None,c=None,t=None,f=None,n=None,e=None,
        **kwargs):
    
    # Create the parser
    my_parser = argparse.ArgumentParser(description="Optional arguments for 'nose'-like tests")

    my_parser.add_argument('-o', "--operating_system",
                        type=str,
                        help='The OS you wish to filter on',
                        default=None or operating_system or o)
    my_parser.add_argument('-c', "--class_name",
                        type=str,
                        help="The Class you wish to filter on, (not the Test File)",
                        default=None or class_name or c)
    my_parser.add_argument('-t', "--token",
                        type=str,
                        help="The Token associated with the class, such as 'asr1k'",
                        default=None or token or t)
    my_parser.add_argument('-f', "--display_only_failed",
                        help="Displaying only failed classes",
                        action='store_true',
                        default=False or display_only_failed or f)
    my_parser.add_argument('-n', "--number",
                        type=int,
                        help="The specific unittest we want to run, such as '25'",
                        default=None or number or n)
    my_parser.add_argument('-e', "--external-folder",
                        type=pathlib.Path,
                        help="An external parser folder to work with",
                        default=None or external_folder or e)
    args = my_parser.parse_known_args()[0]

    _os = args.operating_system
    _class = args.class_name
    _token = args.token
    _display_only_failed = args.display_only_failed
    _number = args.number
    _external_folder = args.external_folder

    return _os, _class, _token, _display_only_failed, _number, _external_folder

def main(**kwargs):
    
    _os, _class, _token, _display_only_failed, _number, _external_folder = _parse_args(**kwargs)

    if _number and (not _class or not _number):
        sys.exit("Unittest number provided but missing supporting arguments:"
                "\n* '-c' or '--class_name' for the parser class"
                "\n* '-o' or '--operating_system' for operating system")


    if _display_only_failed and log.root.handlers:
        temporary_screen_handler = log.root.handlers.pop(0)
    
    if runtime.job:
        # Used for `pyats run job folder_parsing_job.py`
        run(
            testscript=__file__,
            runtime=runtime,
            _os=_os,
            _class=_class,
            _token=_token,
            _display_only_failed=_display_only_failed,
            _number=_number,
            _external_folder=_external_folder,
        )
    else:
        # Used for `python folder_parsing_job.py`
        aetest.main(
            testable=__file__,
            runtime=runtime,
            _os=_os,
            _class=_class,
            _token=_token,
            _display_only_failed=_display_only_failed,
            _number=_number,
            _external_folder=_external_folder,
        )


if __name__ == "__main__":
    main()