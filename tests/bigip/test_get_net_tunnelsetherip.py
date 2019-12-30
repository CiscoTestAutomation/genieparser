# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelsetherip
from genie.libs.parser.bigip.get_net_tunnelsetherip import NetTunnelsEtherip

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/etherip'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:etherip:etheripcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/etherip?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:etherip:etheripstate",
                    "name": "etherip",
                    "partition": "Common",
                    "fullPath": "/Common/etherip",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/etherip/~Common~etherip?ver=14.1.2.1",
                }
            ],
        }


class test_get_net_tunnelsetherip(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/etherip",
                "generation": 1,
                "kind": "tm:net:tunnels:etherip:etheripstate",
                "name": "etherip",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/etherip/~Common~etherip?ver=14.1.2.1",
            }
        ],
        "kind": "tm:net:tunnels:etherip:etheripcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/etherip?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsEtherip(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsEtherip(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
