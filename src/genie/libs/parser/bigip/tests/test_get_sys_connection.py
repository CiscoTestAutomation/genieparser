# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_connection
from genie.libs.parser.bigip.get_sys_connection import SysConnection

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/connection'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:connection:connectionstats",
            "selfLink": "https://localhost/mgmt/tm/sys/connection?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/connection/0": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3841},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.201.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 6},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 3841},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.201.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 1},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/1": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3845},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.201.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 1},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 3845},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.201.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 1},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/2": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3839},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.231.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 9},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 37809},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.231.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 1},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/3": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3837},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.201.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 11},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 3837},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.201.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 1},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/4": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3843},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.231.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 4},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 43334},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.231.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 1},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/5": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3840},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.221.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 7},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 3840},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.221.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 0},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/6": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3842},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.101.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 5},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 52339},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.101.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 0},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/7": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3844},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.221.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 2},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 3844},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.221.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 0},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
            },
        }


class test_get_sys_connection(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:connection:connectionstats",
            "selfLink": "https://localhost/mgmt/tm/sys/connection?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/connection/0": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3841},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.201.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 6},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 3841},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.201.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 1},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/1": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3845},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.201.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 1},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 3845},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.201.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 1},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/2": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3839},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.231.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 9},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 37809},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.231.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 1},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/3": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3837},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.201.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 11},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 3837},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.201.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 1},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/4": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3843},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.231.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 4},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 43334},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.231.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 1},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/5": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3840},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.221.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 7},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 3840},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.221.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 0},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/6": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3842},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.101.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 5},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 52339},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.101.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 0},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/connection/7": {
                    "nestedStats": {
                        "entries": {
                            "connectionId": {"value": 0},
                            "csBytesIn": {"value": 416},
                            "csBytesOut": {"value": 0},
                            "csClientAddr": {"description": "192.168.40.233"},
                            "csClientPort": {"value": 3844},
                            "csPacketsIn": {"value": 8},
                            "csPacketsOut": {"value": 0},
                            "csServerAddr": {"description": "172.16.221.161"},
                            "csServerPort": {"value": 8},
                            "flowAccelType": {"description": "none"},
                            "idleTime": {"value": 2},
                            "idleTimeout": {"value": 10},
                            "lasthopInfo": {
                                "description": "/Common/External 00:0c:29:35:0d:c7"
                            },
                            "protocol": {"value": 1},
                            "slot": {"description": "1"},
                            "ssBytesIn": {"value": 0},
                            "ssBytesOut": {"value": 416},
                            "ssClientAddr": {"description": "192.168.40.233"},
                            "ssClientPort": {"value": 3844},
                            "ssPacketsIn": {"value": 0},
                            "ssPacketsOut": {"value": 8},
                            "ssServerAddr": {"description": "172.16.221.161"},
                            "ssServerPort": {"value": 8},
                            "tmm": {"value": 0},
                            "type": {"description": "self"},
                            "unitId": {"value": 0},
                            "virtualPathAddr": {
                                "description": "0.0.0.0%65535"
                            },
                            "virtualPathPort": {"value": 0},
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysConnection(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysConnection(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
