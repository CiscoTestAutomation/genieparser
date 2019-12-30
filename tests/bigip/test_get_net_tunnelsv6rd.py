# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelsv6rd
from genie.libs.parser.bigip.get_net_tunnelsv6rd import NetTunnelsV6rd

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/v6rd'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:v6rd:v6rdcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/v6rd?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:v6rd:v6rdstate",
                    "name": "v6rd",
                    "partition": "Common",
                    "fullPath": "/Common/v6rd",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/v6rd/~Common~v6rd?ver=14.1.2.1",
                    "ipv4prefix": "any",
                    "ipv4prefixlen": 0,
                    "v6rdprefix": "any6",
                    "v6rdprefixlen": 56,
                }
            ],
        }


class test_get_net_tunnelsv6rd(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/v6rd",
                "generation": 1,
                "ipv4prefix": "any",
                "ipv4prefixlen": 0,
                "kind": "tm:net:tunnels:v6rd:v6rdstate",
                "name": "v6rd",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/v6rd/~Common~v6rd?ver=14.1.2.1",
                "v6rdprefix": "any6",
                "v6rdprefixlen": 56,
            }
        ],
        "kind": "tm:net:tunnels:v6rd:v6rdcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/v6rd?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsV6rd(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsV6rd(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
