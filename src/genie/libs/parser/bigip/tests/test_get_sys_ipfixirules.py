# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_ipfixirules
from genie.libs.parser.bigip.get_sys_ipfixirules import SysIpfixIrules

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/ipfix/irules'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:ipfix:irules:irulesstats",
            "selfLink": "https://localhost/mgmt/tm/sys/ipfix/irules?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/ipfix/irules/0.0": {
                    "nestedStats": {
                        "entries": {
                            "destinationAllocs": {"value": 0},
                            "destinationsOutstanding": {"value": 0},
                            "messageAllocs": {"value": 0},
                            "messagesOutstanding": {"value": 0},
                            "sendFailures": {"value": 0},
                            "sendTotal": {"value": 0},
                            "templateAllocs": {"value": 0},
                            "templatesOutstanding": {"value": 0},
                            "tmmId": {"description": "0.0"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ipfix/irules/0.1": {
                    "nestedStats": {
                        "entries": {
                            "destinationAllocs": {"value": 0},
                            "destinationsOutstanding": {"value": 0},
                            "messageAllocs": {"value": 0},
                            "messagesOutstanding": {"value": 0},
                            "sendFailures": {"value": 0},
                            "sendTotal": {"value": 0},
                            "templateAllocs": {"value": 0},
                            "templatesOutstanding": {"value": 0},
                            "tmmId": {"description": "0.1"},
                        }
                    }
                },
            },
        }


class test_get_sys_ipfixirules(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/ipfix/irules/0.0": {
                "nestedStats": {
                    "entries": {
                        "destinationAllocs": {"value": 0},
                        "destinationsOutstanding": {"value": 0},
                        "messageAllocs": {"value": 0},
                        "messagesOutstanding": {"value": 0},
                        "sendFailures": {"value": 0},
                        "sendTotal": {"value": 0},
                        "templateAllocs": {"value": 0},
                        "templatesOutstanding": {"value": 0},
                        "tmmId": {"description": "0.0"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ipfix/irules/0.1": {
                "nestedStats": {
                    "entries": {
                        "destinationAllocs": {"value": 0},
                        "destinationsOutstanding": {"value": 0},
                        "messageAllocs": {"value": 0},
                        "messagesOutstanding": {"value": 0},
                        "sendFailures": {"value": 0},
                        "sendTotal": {"value": 0},
                        "templateAllocs": {"value": 0},
                        "templatesOutstanding": {"value": 0},
                        "tmmId": {"description": "0.1"},
                    }
                }
            },
        },
        "kind": "tm:sys:ipfix:irules:irulesstats",
        "selfLink": "https://localhost/mgmt/tm/sys/ipfix/irules?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysIpfixIrules(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysIpfixIrules(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
