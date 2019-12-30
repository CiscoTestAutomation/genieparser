# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_sflowinterface
from genie.libs.parser.bigip.get_sys_sflowinterface import SysSflowInterface

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/sflow/data-source/interface'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:sflow:data-source:interface:interfacestats",
            "selfLink": "https://localhost/mgmt/tm/sys/sflow/data-source/interface?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/sflow/data-source/interface/1.1": {
                    "nestedStats": {
                        "entries": {
                            "isActive": {"description": "no"},
                            "tmName": {"description": "1.1"},
                            "pollInterval": {"value": 10},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/sflow/data-source/interface/1.2": {
                    "nestedStats": {
                        "entries": {
                            "isActive": {"description": "no"},
                            "tmName": {"description": "1.2"},
                            "pollInterval": {"value": 10},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/sflow/data-source/interface/1.3": {
                    "nestedStats": {
                        "entries": {
                            "isActive": {"description": "no"},
                            "tmName": {"description": "1.3"},
                            "pollInterval": {"value": 10},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/sflow/data-source/interface/mgmt": {
                    "nestedStats": {
                        "entries": {
                            "isActive": {"description": "no"},
                            "tmName": {"description": "mgmt"},
                            "pollInterval": {"value": 10},
                        }
                    }
                },
            },
        }


class test_get_sys_sflowinterface(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/sflow/data-source/interface/1.1": {
                "nestedStats": {
                    "entries": {
                        "isActive": {"description": "no"},
                        "pollInterval": {"value": 10},
                        "tmName": {"description": "1.1"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/sflow/data-source/interface/1.2": {
                "nestedStats": {
                    "entries": {
                        "isActive": {"description": "no"},
                        "pollInterval": {"value": 10},
                        "tmName": {"description": "1.2"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/sflow/data-source/interface/1.3": {
                "nestedStats": {
                    "entries": {
                        "isActive": {"description": "no"},
                        "pollInterval": {"value": 10},
                        "tmName": {"description": "1.3"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/sflow/data-source/interface/mgmt": {
                "nestedStats": {
                    "entries": {
                        "isActive": {"description": "no"},
                        "pollInterval": {"value": 10},
                        "tmName": {"description": "mgmt"},
                    }
                }
            },
        },
        "kind": "tm:sys:sflow:data-source:interface:interfacestats",
        "selfLink": "https://localhost/mgmt/tm/sys/sflow/data-source/interface?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysSflowInterface(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysSflowInterface(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
