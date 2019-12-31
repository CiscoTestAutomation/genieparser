# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelslw4o6
from genie.libs.parser.bigip.get_net_tunnelslw4o6 import NetTunnelsLw4o6

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/lw4o6'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:lw4o6:lw4o6collectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/lw4o6?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:lw4o6:lw4o6state",
                    "name": "lw4o6",
                    "partition": "Common",
                    "fullPath": "/Common/lw4o6",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/lw4o6/~Common~lw4o6?ver=14.1.2.1",
                    "allProtocolsPass": "disabled",
                    "psidLength": 0,
                }
            ],
        }


class test_get_net_tunnelslw4o6(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "allProtocolsPass": "disabled",
                "fullPath": "/Common/lw4o6",
                "generation": 1,
                "kind": "tm:net:tunnels:lw4o6:lw4o6state",
                "name": "lw4o6",
                "partition": "Common",
                "psidLength": 0,
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/lw4o6/~Common~lw4o6?ver=14.1.2.1",
            }
        ],
        "kind": "tm:net:tunnels:lw4o6:lw4o6collectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/lw4o6?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsLw4o6(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsLw4o6(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
