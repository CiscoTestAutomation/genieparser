# Python
import unittest
from unittest.mock import Mock

# Parser
from genie.libs.parser.iosxr.show_processes import (ShowProcesses,
                                                    ShowProcessesCpu)

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Ats
from pyats.topology import Device

class TestShowProcesses(unittest.TestCase):
    ''' Unit tests for commands:
        * 'show processes isis' : Parser ShowProcesses
    '''

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "job_id": {
            "1011": {
                "available": "1.892s",
                "core": "COPY",
                "executable_path": "/opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/bin/isis",
                "instance": "1",
                "last_started": "Wed Jan 30 20:43:04 2019",
                "max_core": 0,
                "package_state": "Normal",
                "pid": 22464,
                "placement": "Placeable",
                "process_cpu_time": {
                    "kernel": 0.640, 
                    "total": 3.330, 
                    "user": 2.690},
                "process_group": "v4-routing",
                "process_name": "isis",
                "process_state": "Run",                
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
                },
                "ready": "1.804s",
                "respawn": "ON",
                "respawn_count": 1,
                "started_on_config": "cfg/gl/isis/instance/test/ord_A/running",
                "startup_path": "/opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/startup/isis.startup",
                "version_id": "00.00.0000",
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
            Wed Jan 30 21:56:13.650 UTC
                          Job Id: 1011
                             PID: 22464
                    Process name: isis
                 Executable path: /opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/bin/isis
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
                    startup_path: /opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/startup/isis.startup
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

    golden_parsed_output_2 = {
        "job_id": {
            "1": {
                "tid": {
                    1: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "init",
                        "rt_pri": 0,
                    }
                }
            },
            "67110": {
                "tid": {
                    1574: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "oom.sh",
                        "rt_pri": 0,
                    }
                }
            },
            "67134": {
                "tid": {
                    1598: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "cgroup_oom.sh",
                        "rt_pri": 0,
                    }
                }
            },
            "67135": {
                "tid": {
                    1599: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "oom.sh",
                        "rt_pri": 0,
                    }
                }
            },
            "67168": {
                "tid": {
                    1632: {
                        "stack": "0K",
                        "pri": 0,
                        "state": "Sleeping",
                        "name": "cgroup_oom",
                        "rt_pri": 0,
                    }
                }
            },
            "67677": {
                "tid": {
                    2141: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "app_config_back",
                        "rt_pri": 0,
                    }
                }
            },
            "67684": {
                "tid": {
                    2148: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "bash",
                        "rt_pri": 0,
                    }
                }
            },
            "67697": {
                "tid": {
                    2161: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "inotifywait",
                        "rt_pri": 0,
                    }
                }
            },
            "67698": {
                "tid": {
                    2162: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "bash",
                        "rt_pri": 0,
                    }
                }
            },
            "67741": {
                "tid": {
                    2205: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "dbus-daemon",
                        "rt_pri": 0,
                    }
                }
            },
            "67775": {
                "tid": {
                    2239: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "sshd",
                        "rt_pri": 0,
                    }
                }
            },
            "67785": {
                "tid": {
                    2249: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "rpcbind",
                        "rt_pri": 0,
                    }
                }
            },
            "67870": {
                "tid": {
                    2334: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "rngd",
                        "rt_pri": 0,
                    }
                }
            },
            "67879": {
                "tid": {
                    2343: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "syslogd",
                        "rt_pri": 0,
                    }
                }
            },
            "67910": {
                "tid": {
                    2374: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "xinetd",
                        "rt_pri": 0,
                    }
                }
            },
            "67945": {
                "tid": {
                    2409: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "crond",
                        "rt_pri": 0,
                    }
                }
            },
            "69064": {
                "tid": {
                    3528: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "ds_startup.sh",
                        "rt_pri": 0,
                    }
                }
            },
            "53": {
                "tid": {
                    3529: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "dsr",
                        "rt_pri": 0,
                    },
                    3614: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "lwm_debug_threa",
                        "rt_pri": 0,
                    },
                }
            },
        }
    }

    golden_output_2 = {'execute.return_value': '''
        RX#show processes
        Fri Oct  4 18:35:26.878 UTC
        JID    TID  Stack  pri  state        NAME             rt_pri
        1      1       0K  20   Sleeping     init             0
        67110  1574    0K  20   Sleeping     oom.sh           0
        67134  1598    0K  20   Sleeping     cgroup_oom.sh    0
        67135  1599    0K  20   Sleeping     oom.sh           0
        67168  1632    0K  0    Sleeping     cgroup_oom       0
        67677  2141    0K  20   Sleeping     app_config_back  0
        67684  2148    0K  20   Sleeping     bash             0
        67697  2161    0K  20   Sleeping     inotifywait      0
        67698  2162    0K  20   Sleeping     bash             0
        67741  2205    0K  20   Sleeping     dbus-daemon      0
        67775  2239    0K  20   Sleeping     sshd             0
        67785  2249    0K  20   Sleeping     rpcbind          0
        67870  2334    0K  20   Sleeping     rngd             0
        67879  2343    0K  20   Sleeping     syslogd          0
        67910  2374    0K  20   Sleeping     xinetd           0
        67945  2409    0K  20   Sleeping     crond            0
        69064  3528    0K  20   Sleeping     ds_startup.sh    0
        53     3529    0K  20   Sleeping     dsr              0
        53     3614    0K  20   Sleeping     lwm_debug_threa  0
    '''}

    golden_parsed_output_3 = {
        "job_id": {
            "1011": {
                "pid": 10711,
                "process_name": "isis",
                "executable_path": "/opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/bin/isis",
                "instance": "1",
                "version_id": "00.00.0000",
                "respawn": "ON",
                "respawn_count": 1,
                "last_started": "Fri Oct  4 15:47:07 2019",
                "process_state": "Run",
                "package_state": "Normal",
                "started_on_config": "cfg/gl/isis/instance/test/ord_A/running",
                "process_group": "v4-routing",
                "core": "COPY",
                "max_core": 0,
                "placement": "Placeable",
                "startup_path": "/opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/startup/isis.startup",
                "ready": "18.220s",
                "available": "18.536s",
                "process_cpu_time": {
                    "user": 134.74, 
                    "kernel": 40.88, 
                    "total": 175.62},
                "tid": {
                    10711: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "Management",
                        "rt_pri": 0,
                    },
                    11198: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "lwm_debug_threa",
                        "rt_pri": 0,
                    },
                    11199: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "isis",
                        "rt_pri": 0,
                    },
                    11201: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "lwm_service_thr",
                        "rt_pri": 0,
                    },
                    11202: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "qsm_service_thr",
                        "rt_pri": 0,
                    },
                    11218: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "aaa_tty_th",
                        "rt_pri": 0,
                    },
                    11219: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "aaa_util_th",
                        "rt_pri": 0,
                    },
                    11221: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "aaa_client_th",
                        "rt_pri": 0,
                    },
                    11232: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "aaa_login_th",
                        "rt_pri": 0,
                    },
                    11233: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "isis",
                        "rt_pri": 0,
                    },
                    11236: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "isis",
                        "rt_pri": 0,
                    },
                    11283: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "chkpt_evm",
                        "rt_pri": 0,
                    },
                    11284: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "isis",
                        "rt_pri": 0,
                    },
                    11298: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "isis",
                        "rt_pri": 0,
                    },
                    11308: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "isis",
                        "rt_pri": 0,
                    },
                    11311: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "lspv_lib ISIS",
                        "rt_pri": 0,
                    },
                    11312: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "async",
                        "rt_pri": 0,
                    },
                    11315: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "Hello",
                        "rt_pri": 0,
                    },
                    11316: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "Update",
                        "rt_pri": 0,
                    },
                    11317: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "SR-MPLS",
                        "rt_pri": 0,
                    },
                    11318: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "NSR",
                        "rt_pri": 0,
                    },
                    11319: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "LSD sync client",
                        "rt_pri": 0,
                    },
                    11320: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "telemetry_evtli",
                        "rt_pri": 0,
                    },
                    11980: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "Decision",
                        "rt_pri": 0,
                    },
                    11985: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "TE",
                        "rt_pri": 0,
                    },
                    11989: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "MIB Traps",
                        "rt_pri": 0,
                    },
                    11996: {
                        "stack": "0K",
                        "pri": 20,
                        "state": "Sleeping",
                        "name": "Protect Infra",
                        "rt_pri": 0,
                    },
                },
            },
            "1012": {
                "pid": 10709,
                "process_name": "isis",
                "executable_path": "/opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/bin/isis",
                "instance": "2",
                "version_id": "00.00.0000",
                "respawn": "ON",
                "respawn_count": 1,
                "last_started": "Fri Oct  4 15:47:07 2019",
                "process_state": "Exited",
                "package_state": "Normal",
                "registered_item": "cfg/gl/isis/instance/.*/ord_A/",
                "process_group": "v4-routing",
                "core": "COPY",
                "max_core": 0,
                "placement": "Placeable",
                "startup_path": "/opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/startup/isis.startup",
                "ready": "18.046s",
            },
        }
    }

    golden_output_3 = {'execute.return_value': '''
        show processes isis
        Wed Oct  9 20:56:33.874 UTC
                          Job Id: 1011
                             PID: 10711
                    Process name: isis
                 Executable path: /opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/bin/isis
                      Instance #: 1
                      Version ID: 00.00.0000
                         Respawn: ON
                   Respawn count: 1
                    Last started: Fri Oct  4 15:47:07 2019
                   Process state: Run
                   Package state: Normal
               Started on config: cfg/gl/isis/instance/test/ord_A/running
                   Process group: v4-routing
                            core: COPY
                       Max. core: 0
                       Placement: Placeable
                    startup_path: /opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/startup/isis.startup
                           Ready: 18.220s
                       Available: 18.536s
                Process cpu time: 134.740 user, 40.880 kernel, 175.620 total
        JID    TID  Stack  pri  state        NAME             rt_pri
        1011   10711    0K  20   Sleeping     Management       0
        1011   11198    0K  20   Sleeping     lwm_debug_threa  0
        1011   11199    0K  20   Sleeping     isis             0
        1011   11201    0K  20   Sleeping     lwm_service_thr  0
        1011   11202    0K  20   Sleeping     qsm_service_thr  0
        1011   11218    0K  20   Sleeping     aaa_tty_th       0
        1011   11219    0K  20   Sleeping     aaa_util_th      0
        1011   11221    0K  20   Sleeping     aaa_client_th    0
        1011   11232    0K  20   Sleeping     aaa_login_th     0
        1011   11233    0K  20   Sleeping     isis             0
        1011   11236    0K  20   Sleeping     isis             0
        1011   11283    0K  20   Sleeping     chkpt_evm        0
        1011   11284    0K  20   Sleeping     isis             0
        1011   11298    0K  20   Sleeping     isis             0
        1011   11308    0K  20   Sleeping     isis             0
        1011   11311    0K  20   Sleeping     lspv_lib ISIS    0
        1011   11312    0K  20   Sleeping     async            0
        1011   11315    0K  20   Sleeping     Hello            0
        1011   11316    0K  20   Sleeping     Update           0
        1011   11317    0K  20   Sleeping     SR-MPLS          0
        1011   11318    0K  20   Sleeping     NSR              0
        1011   11319    0K  20   Sleeping     LSD sync client  0
        1011   11320    0K  20   Sleeping     telemetry_evtli  0
        1011   11980    0K  20   Sleeping     Decision         0
        1011   11985    0K  20   Sleeping     TE               0
        1011   11989    0K  20   Sleeping     MIB Traps        0
        1011   11996    0K  20   Sleeping     Protect Infra    0
        -------------------------------------------------------------------------------
                          Job Id: 1012
                             PID: 10709
                    Process name: isis
                 Executable path: /opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/bin/isis
                      Instance #: 2
                      Version ID: 00.00.0000
                         Respawn: ON
                   Respawn count: 1
                    Last started: Fri Oct  4 15:47:07 2019
                   Process state: Exited
                   Package state: Normal
              Registered item(s): cfg/gl/isis/instance/.*/ord_A/
                   Process group: v4-routing
                            core: COPY
                       Max. core: 0
                       Placement: Placeable
                    startup_path: /opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/startup/isis.startup
                           Ready: 18.046s
    '''}

    def test_empty_output(self):
        self.device = Mock(**self.empty_output)
        obj = ShowProcesses(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(process='isis')

    def test_parsed_output_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowProcesses(device=self.device)
        parsed_output = obj.parse(process='isis')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_parsed_output_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowProcesses(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_parsed_output_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowProcesses(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

class TestShowProcessesCpu(unittest.TestCase):
    ''' Unit tests for commands:
        * show processes cpu
    '''

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = \
        {
            'location': {
                'node0_RP0_CPU0': {
                    'one_min_cpu': 0,
                    'five_min_cpu': 0,
                    'fifteen_min_cpu': 0,
                    'index': {
                        1: {
                            'pid': 1,
                            'one_min_cpu': 0,
                            'five_min_cpu': 0,
                            'fifteen_min_cpu': 0,
                            'process': 'init'
                        },
                        2: {
                            'pid': 1763,
                            'one_min_cpu': 0,
                            'five_min_cpu': 0,
                            'fifteen_min_cpu': 0,
                            'process': 'bash'
                        },
                        3: {
                            'pid': 1789,
                            'one_min_cpu': 0,
                            'five_min_cpu': 0,
                            'fifteen_min_cpu': 0,
                            'process': 'sh'
                        }
                    }
                }
            }
        }

    golden_output = {'execute.return_value': '''
Mon Sep 28 11:54:48.352 UTC
---- node0_RP0_CPU0 ----

CPU utilization for one minute: 0%; five minutes: 0%; fifteen minutes: 0%

PID    1Min    5Min    15Min Process
1        0%      0%       0% init
1763     0%      0%       0% bash
1789     0%      0%       0% sh
    '''}

    def test_empty_output(self):
        self.device = Mock(**self.empty_output)
        obj = ShowProcessesCpu(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_parsed_output(self):
        self.device = Mock(**self.golden_output)
        obj = ShowProcessesCpu(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
