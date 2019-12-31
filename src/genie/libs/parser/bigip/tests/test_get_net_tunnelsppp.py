# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelsppp
from genie.libs.parser.bigip.get_net_tunnelsppp import NetTunnelsPpp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/ppp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:ppp:pppcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/ppp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:ppp:pppstate",
                    "name": "ppp",
                    "partition": "Common",
                    "fullPath": "/Common/ppp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/ppp/~Common~ppp?ver=14.1.2.1",
                    "ipcp": "enabled",
                    "ipv6cp": "enabled",
                    "lcpEchoFailure": 4,
                    "lcpEchoInterval": 30,
                    "vj": "disabled",
                }
            ],
        }


class test_get_net_tunnelsppp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/ppp",
                "generation": 1,
                "ipcp": "enabled",
                "ipv6cp": "enabled",
                "kind": "tm:net:tunnels:ppp:pppstate",
                "lcpEchoFailure": 4,
                "lcpEchoInterval": 30,
                "name": "ppp",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/ppp/~Common~ppp?ver=14.1.2.1",
                "vj": "disabled",
            }
        ],
        "kind": "tm:net:tunnels:ppp:pppcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/ppp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsPpp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsPpp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
