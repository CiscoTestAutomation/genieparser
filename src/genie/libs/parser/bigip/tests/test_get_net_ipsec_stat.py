# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_ipsec_stat
from genie.libs.parser.bigip.get_net_ipsec_stat import NetIpsecstat

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/ipsec-stat'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:ipsec-stat:ipsec-statstats",
            "selfLink": "https://localhost/mgmt/tm/net/ipsec-stat?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/net/ipsec-stat/0": {
                    "nestedStats": {
                        "entries": {
                            "cmdId": {"value": 0},
                            "inBytes": {"value": 0},
                            "inPackets": {"value": 0},
                            "mode": {"description": "TRANSPORT"},
                            "outBytes": {"value": 0},
                            "outPackets": {"value": 0},
                            "proto": {"description": "AH"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/net/ipsec-stat/1": {
                    "nestedStats": {
                        "entries": {
                            "cmdId": {"value": 0},
                            "inBytes": {"value": 0},
                            "inPackets": {"value": 0},
                            "mode": {"description": "TRANSPORT"},
                            "outBytes": {"value": 0},
                            "outPackets": {"value": 0},
                            "proto": {"description": "ESP"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/net/ipsec-stat/2": {
                    "nestedStats": {
                        "entries": {
                            "cmdId": {"value": 0},
                            "inBytes": {"value": 0},
                            "inPackets": {"value": 0},
                            "mode": {"description": "TUNNEL"},
                            "outBytes": {"value": 0},
                            "outPackets": {"value": 0},
                            "proto": {"description": "AH"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/net/ipsec-stat/3": {
                    "nestedStats": {
                        "entries": {
                            "cmdId": {"value": 0},
                            "inBytes": {"value": 0},
                            "inPackets": {"value": 0},
                            "mode": {"description": "TUNNEL"},
                            "outBytes": {"value": 0},
                            "outPackets": {"value": 0},
                            "proto": {"description": "ESP"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/net/ipsec-stat/4": {
                    "nestedStats": {
                        "entries": {
                            "cmdId": {"value": 1},
                            "inBytes": {"value": 0},
                            "inPackets": {"value": 0},
                            "mode": {"description": "TRANSPORT"},
                            "outBytes": {"value": 0},
                            "outPackets": {"value": 0},
                            "proto": {"description": "AH"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/net/ipsec-stat/5": {
                    "nestedStats": {
                        "entries": {
                            "cmdId": {"value": 1},
                            "inBytes": {"value": 0},
                            "inPackets": {"value": 0},
                            "mode": {"description": "TRANSPORT"},
                            "outBytes": {"value": 0},
                            "outPackets": {"value": 0},
                            "proto": {"description": "ESP"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/net/ipsec-stat/6": {
                    "nestedStats": {
                        "entries": {
                            "cmdId": {"value": 1},
                            "inBytes": {"value": 0},
                            "inPackets": {"value": 0},
                            "mode": {"description": "TUNNEL"},
                            "outBytes": {"value": 0},
                            "outPackets": {"value": 0},
                            "proto": {"description": "AH"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/net/ipsec-stat/7": {
                    "nestedStats": {
                        "entries": {
                            "cmdId": {"value": 1},
                            "inBytes": {"value": 0},
                            "inPackets": {"value": 0},
                            "mode": {"description": "TUNNEL"},
                            "outBytes": {"value": 0},
                            "outPackets": {"value": 0},
                            "proto": {"description": "ESP"},
                        }
                    }
                },
            },
        }


class test_get_net_ipsec_stat(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/net/ipsec-stat/0": {
                "nestedStats": {
                    "entries": {
                        "cmdId": {"value": 0},
                        "inBytes": {"value": 0},
                        "inPackets": {"value": 0},
                        "mode": {"description": "TRANSPORT"},
                        "outBytes": {"value": 0},
                        "outPackets": {"value": 0},
                        "proto": {"description": "AH"},
                    }
                }
            },
            "https://localhost/mgmt/tm/net/ipsec-stat/1": {
                "nestedStats": {
                    "entries": {
                        "cmdId": {"value": 0},
                        "inBytes": {"value": 0},
                        "inPackets": {"value": 0},
                        "mode": {"description": "TRANSPORT"},
                        "outBytes": {"value": 0},
                        "outPackets": {"value": 0},
                        "proto": {"description": "ESP"},
                    }
                }
            },
            "https://localhost/mgmt/tm/net/ipsec-stat/2": {
                "nestedStats": {
                    "entries": {
                        "cmdId": {"value": 0},
                        "inBytes": {"value": 0},
                        "inPackets": {"value": 0},
                        "mode": {"description": "TUNNEL"},
                        "outBytes": {"value": 0},
                        "outPackets": {"value": 0},
                        "proto": {"description": "AH"},
                    }
                }
            },
            "https://localhost/mgmt/tm/net/ipsec-stat/3": {
                "nestedStats": {
                    "entries": {
                        "cmdId": {"value": 0},
                        "inBytes": {"value": 0},
                        "inPackets": {"value": 0},
                        "mode": {"description": "TUNNEL"},
                        "outBytes": {"value": 0},
                        "outPackets": {"value": 0},
                        "proto": {"description": "ESP"},
                    }
                }
            },
            "https://localhost/mgmt/tm/net/ipsec-stat/4": {
                "nestedStats": {
                    "entries": {
                        "cmdId": {"value": 1},
                        "inBytes": {"value": 0},
                        "inPackets": {"value": 0},
                        "mode": {"description": "TRANSPORT"},
                        "outBytes": {"value": 0},
                        "outPackets": {"value": 0},
                        "proto": {"description": "AH"},
                    }
                }
            },
            "https://localhost/mgmt/tm/net/ipsec-stat/5": {
                "nestedStats": {
                    "entries": {
                        "cmdId": {"value": 1},
                        "inBytes": {"value": 0},
                        "inPackets": {"value": 0},
                        "mode": {"description": "TRANSPORT"},
                        "outBytes": {"value": 0},
                        "outPackets": {"value": 0},
                        "proto": {"description": "ESP"},
                    }
                }
            },
            "https://localhost/mgmt/tm/net/ipsec-stat/6": {
                "nestedStats": {
                    "entries": {
                        "cmdId": {"value": 1},
                        "inBytes": {"value": 0},
                        "inPackets": {"value": 0},
                        "mode": {"description": "TUNNEL"},
                        "outBytes": {"value": 0},
                        "outPackets": {"value": 0},
                        "proto": {"description": "AH"},
                    }
                }
            },
            "https://localhost/mgmt/tm/net/ipsec-stat/7": {
                "nestedStats": {
                    "entries": {
                        "cmdId": {"value": 1},
                        "inBytes": {"value": 0},
                        "inPackets": {"value": 0},
                        "mode": {"description": "TUNNEL"},
                        "outBytes": {"value": 0},
                        "outPackets": {"value": 0},
                        "proto": {"description": "ESP"},
                    }
                }
            },
        },
        "kind": "tm:net:ipsec-stat:ipsec-statstats",
        "selfLink": "https://localhost/mgmt/tm/net/ipsec-stat?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetIpsecstat(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetIpsecstat(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
