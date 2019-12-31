# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_ip_address
from genie.libs.parser.bigip.get_sys_ip_address import SysIpaddress

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/ip-address'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:ip-address:ip-addressstats",
            "selfLink": "https://localhost/mgmt/tm/sys/ip-address?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/ip-address/none": {
                    "nestedStats": {
                        "entries": {
                            "component": {
                                "description": "sys state-mirroring"
                            },
                            "entry": {"description": "none"},
                            "ipAddress": {"description": "none"},
                            "objectId": {"description": "n/a"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ip-address/any6": {
                    "nestedStats": {
                        "entries": {
                            "component": {
                                "description": "sys management-ovsdb"
                            },
                            "entry": {"description": "any6"},
                            "ipAddress": {"description": "any6"},
                            "objectId": {"description": "n/a"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ip-address/4.4.4.4": {
                    "nestedStats": {
                        "entries": {
                            "component": {"description": "sys dns"},
                            "entry": {"description": "4.4.4.4"},
                            "ipAddress": {"description": "4.4.4.4"},
                            "objectId": {"description": "n/a"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ip-address/8.8.8.8": {
                    "nestedStats": {
                        "entries": {
                            "component": {"description": "sys dns"},
                            "entry": {"description": "8.8.8.8"},
                            "ipAddress": {"description": "8.8.8.8"},
                            "objectId": {"description": "n/a"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ip-address/200.200.2.2": {
                    "nestedStats": {
                        "entries": {
                            "component": {"description": "sys dns"},
                            "entry": {"description": "200.200.2.2"},
                            "ipAddress": {"description": "200.200.2.2"},
                            "objectId": {"description": "n/a"},
                        }
                    }
                },
            },
        }


class test_get_sys_ip_address(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/ip-address/200.200.2.2": {
                "nestedStats": {
                    "entries": {
                        "component": {"description": "sys " "dns"},
                        "entry": {"description": "200.200.2.2"},
                        "ipAddress": {"description": "200.200.2.2"},
                        "objectId": {"description": "n/a"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ip-address/4.4.4.4": {
                "nestedStats": {
                    "entries": {
                        "component": {"description": "sys " "dns"},
                        "entry": {"description": "4.4.4.4"},
                        "ipAddress": {"description": "4.4.4.4"},
                        "objectId": {"description": "n/a"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ip-address/8.8.8.8": {
                "nestedStats": {
                    "entries": {
                        "component": {"description": "sys " "dns"},
                        "entry": {"description": "8.8.8.8"},
                        "ipAddress": {"description": "8.8.8.8"},
                        "objectId": {"description": "n/a"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ip-address/any6": {
                "nestedStats": {
                    "entries": {
                        "component": {
                            "description": "sys " "management-ovsdb"
                        },
                        "entry": {"description": "any6"},
                        "ipAddress": {"description": "any6"},
                        "objectId": {"description": "n/a"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ip-address/none": {
                "nestedStats": {
                    "entries": {
                        "component": {"description": "sys " "state-mirroring"},
                        "entry": {"description": "none"},
                        "ipAddress": {"description": "none"},
                        "objectId": {"description": "n/a"},
                    }
                }
            },
        },
        "kind": "tm:sys:ip-address:ip-addressstats",
        "selfLink": "https://localhost/mgmt/tm/sys/ip-address?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysIpaddress(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysIpaddress(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
