# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_self_allow
from genie.libs.parser.bigip.get_net_self_allow import NetSelfallow

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/self-allow'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:self-allow:self-allowstate",
            "selfLink": "https://localhost/mgmt/tm/net/self-allow?ver=14.1.2.1",
            "defaults": [
                "igmp:0",
                "ospf:0",
                "pim:0",
                "tcp:161",
                "tcp:22",
                "tcp:4353",
                "tcp:443",
                "tcp:53",
                "udp:1026",
                "udp:161",
                "udp:4353",
                "udp:520",
                "udp:53",
            ],
        }


class test_get_net_self_allow(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "defaults": [
            "igmp:0",
            "ospf:0",
            "pim:0",
            "tcp:161",
            "tcp:22",
            "tcp:4353",
            "tcp:443",
            "tcp:53",
            "udp:1026",
            "udp:161",
            "udp:4353",
            "udp:520",
            "udp:53",
        ],
        "kind": "tm:net:self-allow:self-allowstate",
        "selfLink": "https://localhost/mgmt/tm/net/self-allow?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetSelfallow(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetSelfallow(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
