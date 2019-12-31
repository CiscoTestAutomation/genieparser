# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_rst_cause
from genie.libs.parser.bigip.get_net_rst_cause import NetRstcause

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/rst-cause'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:rst-cause:rst-causestats",
            "selfLink": "https://localhost/mgmt/tm/net/rst-cause?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/net/rst-cause/0": {
                    "nestedStats": {
                        "entries": {
                            "count": {"value": 40},
                            "rstCause": {"description": "handshake timeout"},
                        }
                    }
                }
            },
        }


class test_get_net_rst_cause(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/net/rst-cause/0": {
                "nestedStats": {
                    "entries": {
                        "count": {"value": 40},
                        "rstCause": {"description": "handshake " "timeout"},
                    }
                }
            }
        },
        "kind": "tm:net:rst-cause:rst-causestats",
        "selfLink": "https://localhost/mgmt/tm/net/rst-cause?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetRstcause(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetRstcause(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
