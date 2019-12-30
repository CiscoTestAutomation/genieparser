# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelsmap
from genie.libs.parser.bigip.get_net_tunnelsmap import NetTunnelsMap

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/map'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:map:mapcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/map?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:map:mapstate",
                    "name": "map",
                    "partition": "Common",
                    "fullPath": "/Common/map",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/map/~Common~map?ver=14.1.2.1",
                    "eaBitsLength": 32,
                    "ip4Prefix": "0.0.0.0/8",
                    "ip6Prefix": "::/48",
                    "portOffset": 6,
                }
            ],
        }


class test_get_net_tunnelsmap(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "eaBitsLength": 32,
                "fullPath": "/Common/map",
                "generation": 1,
                "ip4Prefix": "0.0.0.0/8",
                "ip6Prefix": "::/48",
                "kind": "tm:net:tunnels:map:mapstate",
                "name": "map",
                "partition": "Common",
                "portOffset": 6,
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/map/~Common~map?ver=14.1.2.1",
            }
        ],
        "kind": "tm:net:tunnels:map:mapcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/map?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsMap(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsMap(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
