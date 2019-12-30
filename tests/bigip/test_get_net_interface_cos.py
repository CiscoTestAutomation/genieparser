# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_interface_cos
from genie.libs.parser.bigip.get_net_interface_cos import NetInterfacecos

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/interface-cos'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:interface-cos:interface-coscollectionstats",
            "selfLink": "https://localhost/mgmt/tm/net/interface-cos?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/net/interface-cos/1.1": {
                    "nestedStats": {
                        "kind": "tm:net:interface-cos:interface-cosstats",
                        "selfLink": "https://localhost/mgmt/tm/net/interface-cos/1.1?ver=14.1.2.1",
                        "entries": {
                            "cosStat.pktsOutCos0": {"value": 0},
                            "cosStat.pktsOutCos1": {"value": 0},
                            "cosStat.pktsOutCos2": {"value": 0},
                            "cosStat.pktsOutCos3": {"value": 0},
                            "cosStat.pktsOutCos4": {"value": 0},
                            "cosStat.pktsOutCos5": {"value": 0},
                            "cosStat.pktsOutCos6": {"value": 0},
                            "cosStat.pktsOutCos7": {"value": 0},
                            "tmName": {"description": "1.1"},
                            "status": {"description": "up"},
                        },
                    }
                },
                "https://localhost/mgmt/tm/net/interface-cos/1.2": {
                    "nestedStats": {
                        "kind": "tm:net:interface-cos:interface-cosstats",
                        "selfLink": "https://localhost/mgmt/tm/net/interface-cos/1.2?ver=14.1.2.1",
                        "entries": {
                            "cosStat.pktsOutCos0": {"value": 0},
                            "cosStat.pktsOutCos1": {"value": 0},
                            "cosStat.pktsOutCos2": {"value": 0},
                            "cosStat.pktsOutCos3": {"value": 0},
                            "cosStat.pktsOutCos4": {"value": 0},
                            "cosStat.pktsOutCos5": {"value": 0},
                            "cosStat.pktsOutCos6": {"value": 0},
                            "cosStat.pktsOutCos7": {"value": 0},
                            "tmName": {"description": "1.2"},
                            "status": {"description": "up"},
                        },
                    }
                },
                "https://localhost/mgmt/tm/net/interface-cos/1.3": {
                    "nestedStats": {
                        "kind": "tm:net:interface-cos:interface-cosstats",
                        "selfLink": "https://localhost/mgmt/tm/net/interface-cos/1.3?ver=14.1.2.1",
                        "entries": {
                            "cosStat.pktsOutCos0": {"value": 0},
                            "cosStat.pktsOutCos1": {"value": 0},
                            "cosStat.pktsOutCos2": {"value": 0},
                            "cosStat.pktsOutCos3": {"value": 0},
                            "cosStat.pktsOutCos4": {"value": 0},
                            "cosStat.pktsOutCos5": {"value": 0},
                            "cosStat.pktsOutCos6": {"value": 0},
                            "cosStat.pktsOutCos7": {"value": 0},
                            "tmName": {"description": "1.3"},
                            "status": {"description": "up"},
                        },
                    }
                },
                "https://localhost/mgmt/tm/net/interface-cos/mgmt": {
                    "nestedStats": {
                        "kind": "tm:net:interface-cos:interface-cosstats",
                        "selfLink": "https://localhost/mgmt/tm/net/interface-cos/mgmt?ver=14.1.2.1",
                        "entries": {
                            "cosStat.pktsOutCos0": {"value": 0},
                            "cosStat.pktsOutCos1": {"value": 0},
                            "cosStat.pktsOutCos2": {"value": 0},
                            "cosStat.pktsOutCos3": {"value": 0},
                            "cosStat.pktsOutCos4": {"value": 0},
                            "cosStat.pktsOutCos5": {"value": 0},
                            "cosStat.pktsOutCos6": {"value": 0},
                            "cosStat.pktsOutCos7": {"value": 0},
                            "tmName": {"description": "mgmt"},
                            "status": {"description": "up"},
                        },
                    }
                },
            },
        }


class test_get_net_interface_cos(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/net/interface-cos/1.1": {
                "nestedStats": {
                    "entries": {
                        "cosStat.pktsOutCos0": {"value": 0},
                        "cosStat.pktsOutCos1": {"value": 0},
                        "cosStat.pktsOutCos2": {"value": 0},
                        "cosStat.pktsOutCos3": {"value": 0},
                        "cosStat.pktsOutCos4": {"value": 0},
                        "cosStat.pktsOutCos5": {"value": 0},
                        "cosStat.pktsOutCos6": {"value": 0},
                        "cosStat.pktsOutCos7": {"value": 0},
                        "status": {"description": "up"},
                        "tmName": {"description": "1.1"},
                    },
                    "kind": "tm:net:interface-cos:interface-cosstats",
                    "selfLink": "https://localhost/mgmt/tm/net/interface-cos/1.1?ver=14.1.2.1",
                }
            },
            "https://localhost/mgmt/tm/net/interface-cos/1.2": {
                "nestedStats": {
                    "entries": {
                        "cosStat.pktsOutCos0": {"value": 0},
                        "cosStat.pktsOutCos1": {"value": 0},
                        "cosStat.pktsOutCos2": {"value": 0},
                        "cosStat.pktsOutCos3": {"value": 0},
                        "cosStat.pktsOutCos4": {"value": 0},
                        "cosStat.pktsOutCos5": {"value": 0},
                        "cosStat.pktsOutCos6": {"value": 0},
                        "cosStat.pktsOutCos7": {"value": 0},
                        "status": {"description": "up"},
                        "tmName": {"description": "1.2"},
                    },
                    "kind": "tm:net:interface-cos:interface-cosstats",
                    "selfLink": "https://localhost/mgmt/tm/net/interface-cos/1.2?ver=14.1.2.1",
                }
            },
            "https://localhost/mgmt/tm/net/interface-cos/1.3": {
                "nestedStats": {
                    "entries": {
                        "cosStat.pktsOutCos0": {"value": 0},
                        "cosStat.pktsOutCos1": {"value": 0},
                        "cosStat.pktsOutCos2": {"value": 0},
                        "cosStat.pktsOutCos3": {"value": 0},
                        "cosStat.pktsOutCos4": {"value": 0},
                        "cosStat.pktsOutCos5": {"value": 0},
                        "cosStat.pktsOutCos6": {"value": 0},
                        "cosStat.pktsOutCos7": {"value": 0},
                        "status": {"description": "up"},
                        "tmName": {"description": "1.3"},
                    },
                    "kind": "tm:net:interface-cos:interface-cosstats",
                    "selfLink": "https://localhost/mgmt/tm/net/interface-cos/1.3?ver=14.1.2.1",
                }
            },
            "https://localhost/mgmt/tm/net/interface-cos/mgmt": {
                "nestedStats": {
                    "entries": {
                        "cosStat.pktsOutCos0": {"value": 0},
                        "cosStat.pktsOutCos1": {"value": 0},
                        "cosStat.pktsOutCos2": {"value": 0},
                        "cosStat.pktsOutCos3": {"value": 0},
                        "cosStat.pktsOutCos4": {"value": 0},
                        "cosStat.pktsOutCos5": {"value": 0},
                        "cosStat.pktsOutCos6": {"value": 0},
                        "cosStat.pktsOutCos7": {"value": 0},
                        "status": {"description": "up"},
                        "tmName": {"description": "mgmt"},
                    },
                    "kind": "tm:net:interface-cos:interface-cosstats",
                    "selfLink": "https://localhost/mgmt/tm/net/interface-cos/mgmt?ver=14.1.2.1",
                }
            },
        },
        "kind": "tm:net:interface-cos:interface-coscollectionstats",
        "selfLink": "https://localhost/mgmt/tm/net/interface-cos?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetInterfacecos(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetInterfacecos(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
