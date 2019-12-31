# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_mac_address
from genie.libs.parser.bigip.get_sys_mac_address import SysMacaddress

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/mac-address'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:mac-address:mac-addressstats",
            "selfLink": "https://localhost/mgmt/tm/sys/mac-address?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/mac-address/00:0c:29:35:0d:bd": {
                    "nestedStats": {
                        "entries": {
                            "component": {
                                "description": "sys hardware platform"
                            },
                            "entry": {"description": "00:0c:29:35:0d:bd"},
                            "macAddress": {"description": "00:0c:29:35:0d:bd"},
                            "objectId": {"description": "n/a"},
                            "property": {"description": "base-mac"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/mac-address/00:0c:29:35:0d:c7": {
                    "nestedStats": {
                        "entries": {
                            "component": {"description": "net interface"},
                            "entry": {"description": "00:0c:29:35:0d:c7"},
                            "macAddress": {"description": "00:0c:29:35:0d:c7"},
                            "objectId": {"description": "1.1"},
                            "property": {"description": "mac-address"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/mac-address/00:0c:29:35:0d:d1": {
                    "nestedStats": {
                        "entries": {
                            "component": {"description": "net interface"},
                            "entry": {"description": "00:0c:29:35:0d:d1"},
                            "macAddress": {"description": "00:0c:29:35:0d:d1"},
                            "objectId": {"description": "1.2"},
                            "property": {"description": "mac-address"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/mac-address/00:0c:29:35:0d:db": {
                    "nestedStats": {
                        "entries": {
                            "component": {"description": "net interface"},
                            "entry": {"description": "00:0c:29:35:0d:db"},
                            "macAddress": {"description": "00:0c:29:35:0d:db"},
                            "objectId": {"description": "1.3"},
                            "property": {"description": "mac-address"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/mac-address/00:50:56:f0:f7:81": {
                    "nestedStats": {
                        "entries": {
                            "component": {"description": "net arp"},
                            "entry": {"description": "00:50:56:f0:f7:81"},
                            "macAddress": {"description": "00:50:56:f0:f7:81"},
                            "objectId": {"description": "192.168.40.2"},
                            "property": {"description": "mac-address"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/mac-address/none": {
                    "nestedStats": {
                        "entries": {
                            "component": {
                                "description": "net packet-filter-trusted"
                            },
                            "entry": {"description": "none"},
                            "macAddress": {"description": "none"},
                            "objectId": {"description": "n/a"},
                            "property": {"description": "mac-addresses"},
                        }
                    }
                },
            },
        }


class test_get_sys_mac_address(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/mac-address/00:0c:29:35:0d:bd": {
                "nestedStats": {
                    "entries": {
                        "component": {
                            "description": "sys " "hardware " "platform"
                        },
                        "entry": {"description": "00:0c:29:35:0d:bd"},
                        "macAddress": {"description": "00:0c:29:35:0d:bd"},
                        "objectId": {"description": "n/a"},
                        "property": {"description": "base-mac"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/mac-address/00:0c:29:35:0d:c7": {
                "nestedStats": {
                    "entries": {
                        "component": {"description": "net " "interface"},
                        "entry": {"description": "00:0c:29:35:0d:c7"},
                        "macAddress": {"description": "00:0c:29:35:0d:c7"},
                        "objectId": {"description": "1.1"},
                        "property": {"description": "mac-address"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/mac-address/00:0c:29:35:0d:d1": {
                "nestedStats": {
                    "entries": {
                        "component": {"description": "net " "interface"},
                        "entry": {"description": "00:0c:29:35:0d:d1"},
                        "macAddress": {"description": "00:0c:29:35:0d:d1"},
                        "objectId": {"description": "1.2"},
                        "property": {"description": "mac-address"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/mac-address/00:0c:29:35:0d:db": {
                "nestedStats": {
                    "entries": {
                        "component": {"description": "net " "interface"},
                        "entry": {"description": "00:0c:29:35:0d:db"},
                        "macAddress": {"description": "00:0c:29:35:0d:db"},
                        "objectId": {"description": "1.3"},
                        "property": {"description": "mac-address"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/mac-address/00:50:56:f0:f7:81": {
                "nestedStats": {
                    "entries": {
                        "component": {"description": "net " "arp"},
                        "entry": {"description": "00:50:56:f0:f7:81"},
                        "macAddress": {"description": "00:50:56:f0:f7:81"},
                        "objectId": {"description": "192.168.40.2"},
                        "property": {"description": "mac-address"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/mac-address/none": {
                "nestedStats": {
                    "entries": {
                        "component": {
                            "description": "net " "packet-filter-trusted"
                        },
                        "entry": {"description": "none"},
                        "macAddress": {"description": "none"},
                        "objectId": {"description": "n/a"},
                        "property": {"description": "mac-addresses"},
                    }
                }
            },
        },
        "kind": "tm:sys:mac-address:mac-addressstats",
        "selfLink": "https://localhost/mgmt/tm/sys/mac-address?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysMacaddress(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysMacaddress(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
