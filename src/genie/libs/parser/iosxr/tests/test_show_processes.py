# Python
import unittest
from unittest.mock import Mock

# Parser
from genie.libs.parser.iosxr.show_processes import ShowProcessesIsis

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Ats
from ats.topology import Device

class TestShowProcesses(unittest.TestCase):
    ''' Unit tests for commands:
        * 'show processes isis' : Parser ShowProcessesIsis
    '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "job_id": {
            "1011": {
                "available": "1.892s",
                "core": "COPY",
                "executable_path": "/opt/cisco/XR/packages/xrv9k-isis-2.1.0.0-r651/rp/bin/isis",
                "instance": "1",
                "last_started": "Wed Jan 30 20:43:04 2019",
                "max_core": "0",
                "package_state": "Normal",
                "pid": 22464,
                "placement": "Placeable",
                "process_cpu_time": {
                    "kernel": "0.640", 
                    "total": "3.330", 
                    "user": "2.690"},
                "process_group": "v4-routing",
                "process_name": "isis",
                "process_state": "Run",
                "processes": {
                    "tid": {
                        22464: {
                            "name": "Management",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22471: {
                            "name": "lwm_debug_threa",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22472: {
                            "name": "isis",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22473: {
                            "name": "lwm_service_thr",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22474: {
                            "name": "qsm_service_thr",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22475: {
                            "name": "aaa_tty_th",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22476: {
                            "name": "aaa_util_th",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22477: {
                            "name": "aaa_client_th",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22478: {
                            "name": "aaa_login_th",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22479: {
                            "name": "isis",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22480: {
                            "name": "isis",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22481: {
                            "name": "chkpt_evm",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22482: {
                            "name": "isis",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22485: {
                            "name": "isis",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22486: {
                            "name": "isis",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22487: {
                            "name": "lspv_lib ISIS",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22488: {
                            "name": "async",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22489: {
                            "name": "Hello",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22490: {
                            "name": "Update",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22491: {
                            "name": "SR-MPLS",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22492: {
                            "name": "NSR",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22493: {
                            "name": "LSD sync client",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22494: {
                            "name": "telemetry_evtli",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22511: {
                            "name": "Decision",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22512: {
                            "name": "TE",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22513: {
                            "name": "MIB Traps",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                        22514: {
                            "name": "Protect Infra",
                            "pri": 20,
                            "rt_pri": 0,
                            "stack": "0K",
                            "state": "Sleeping",
                        },
                    }
                },
                "ready": "1.804s",
                "respawn": "ON",
                "respawn_count": 1,
                "started_on_config": "cfg/gl/isis/instance/test/ord_A/running",
                "startup_path": "/opt/cisco/XR/packages/xrv9k-isis-2.1.0.0-r651/rp/startup/isis.startup",
                "version_id": "00.00.0000",
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
            Wed Jan 30 21:56:13.650 UTC
                          Job Id: 1011
                             PID: 22464
                    Process name: isis
                 Executable path: /opt/cisco/XR/packages/xrv9k-isis-2.1.0.0-r651/rp/bin/isis
                      Instance #: 1
                      Version ID: 00.00.0000
                         Respawn: ON
                   Respawn count: 1
                    Last started: Wed Jan 30 20:43:04 2019
                   Process state: Run
                   Package state: Normal
               Started on config: cfg/gl/isis/instance/test/ord_A/running
                   Process group: v4-routing
                            core: COPY
                       Max. core: 0
                       Placement: Placeable
                    startup_path: /opt/cisco/XR/packages/xrv9k-isis-2.1.0.0-r651/rp/startup/isis.startup
                           Ready: 1.804s
                       Available: 1.892s
                Process cpu time: 2.690 user, 0.640 kernel, 3.330 total
        JID    TID  Stack  pri  state        NAME             rt_pri
        1011   22464    0K  20   Sleeping     Management       0
        1011   22471    0K  20   Sleeping     lwm_debug_threa  0
        1011   22472    0K  20   Sleeping     isis             0
        1011   22473    0K  20   Sleeping     lwm_service_thr  0
        1011   22474    0K  20   Sleeping     qsm_service_thr  0
        1011   22475    0K  20   Sleeping     aaa_tty_th       0
        1011   22476    0K  20   Sleeping     aaa_util_th      0
        1011   22477    0K  20   Sleeping     aaa_client_th    0
        1011   22478    0K  20   Sleeping     aaa_login_th     0
        1011   22479    0K  20   Sleeping     isis             0
        1011   22480    0K  20   Sleeping     isis             0
        1011   22481    0K  20   Sleeping     chkpt_evm        0
        1011   22482    0K  20   Sleeping     isis             0
        1011   22485    0K  20   Sleeping     isis             0
        1011   22486    0K  20   Sleeping     isis             0
        1011   22487    0K  20   Sleeping     lspv_lib ISIS    0
        1011   22488    0K  20   Sleeping     async            0
        1011   22489    0K  20   Sleeping     Hello            0
        1011   22490    0K  20   Sleeping     Update           0
        1011   22491    0K  20   Sleeping     SR-MPLS          0
        1011   22492    0K  20   Sleeping     NSR              0
        1011   22493    0K  20   Sleeping     LSD sync client  0
        1011   22494    0K  20   Sleeping     telemetry_evtli  0
        1011   22511    0K  20   Sleeping     Decision         0
        1011   22512    0K  20   Sleeping     TE               0
        1011   22513    0K  20   Sleeping     MIB Traps        0
        1011   22514    0K  20   Sleeping     Protect Infra    0
    '''}

    def test_empty_output(self):
        self.device = Mock(**self.empty_output)
        obj = ShowProcessesIsis(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_parsed_output_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowProcessesIsis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()