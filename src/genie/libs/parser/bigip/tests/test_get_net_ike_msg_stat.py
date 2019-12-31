# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_ike_msg_stat
from genie.libs.parser.bigip.get_net_ike_msg_stat import NetIkemsgstat

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/ike-msg-stat'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:ike-msg-stat:ike-msg-statstats",
            "selfLink": "https://localhost/mgmt/tm/net/ike-msg-stat?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/net/ike-msg-stat/0": {
                    "nestedStats": {
                        "entries": {
                            "bytesIn": {"value": 0},
                            "bytesOut": {"value": 0},
                            "childExchIn": {"value": 0},
                            "childExchInvalidIn": {"value": 0},
                            "childExchInvalidOut": {"value": 0},
                            "childExchOut": {"value": 0},
                            "childExchRejectIn": {"value": 0},
                            "childExchRejectOut": {"value": 0},
                            "dpdMsgsIn": {"value": 0},
                            "dpdMsgsOut": {"value": 0},
                            "dropPacketsIn": {"value": 0},
                            "dropPacketsOut": {"value": 0},
                            "ikeDeleteIn": {"value": 0},
                            "ikeDeleteOut": {"value": 0},
                            "ipsecDeleteIn": {"value": 0},
                            "ipsecDeleteOut": {"value": 0},
                            "notifysIn": {"value": 0},
                            "notifysOut": {"value": 0},
                            "packetsIn": {"value": 0},
                            "packetsOut": {"value": 0},
                        }
                    }
                }
            },
        }


class test_get_net_ike_msg_stat(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/net/ike-msg-stat/0": {
                "nestedStats": {
                    "entries": {
                        "bytesIn": {"value": 0},
                        "bytesOut": {"value": 0},
                        "childExchIn": {"value": 0},
                        "childExchInvalidIn": {"value": 0},
                        "childExchInvalidOut": {"value": 0},
                        "childExchOut": {"value": 0},
                        "childExchRejectIn": {"value": 0},
                        "childExchRejectOut": {"value": 0},
                        "dpdMsgsIn": {"value": 0},
                        "dpdMsgsOut": {"value": 0},
                        "dropPacketsIn": {"value": 0},
                        "dropPacketsOut": {"value": 0},
                        "ikeDeleteIn": {"value": 0},
                        "ikeDeleteOut": {"value": 0},
                        "ipsecDeleteIn": {"value": 0},
                        "ipsecDeleteOut": {"value": 0},
                        "notifysIn": {"value": 0},
                        "notifysOut": {"value": 0},
                        "packetsIn": {"value": 0},
                        "packetsOut": {"value": 0},
                    }
                }
            }
        },
        "kind": "tm:net:ike-msg-stat:ike-msg-statstats",
        "selfLink": "https://localhost/mgmt/tm/net/ike-msg-stat?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetIkemsgstat(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetIkemsgstat(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
