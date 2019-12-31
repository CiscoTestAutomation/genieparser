# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelsgeneve
from genie.libs.parser.bigip.get_net_tunnelsgeneve import NetTunnelsGeneve

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/geneve'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:geneve:genevecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/geneve?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:geneve:genevestate",
                    "name": "geneve",
                    "partition": "Common",
                    "fullPath": "/Common/geneve",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/geneve/~Common~geneve?ver=14.1.2.1",
                    "floodingType": "multipoint",
                    "port": 6081,
                }
            ],
        }


class test_get_net_tunnelsgeneve(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "floodingType": "multipoint",
                "fullPath": "/Common/geneve",
                "generation": 1,
                "kind": "tm:net:tunnels:geneve:genevestate",
                "name": "geneve",
                "partition": "Common",
                "port": 6081,
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/geneve/~Common~geneve?ver=14.1.2.1",
            }
        ],
        "kind": "tm:net:tunnels:geneve:genevecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/geneve?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsGeneve(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsGeneve(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
