# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelsgre
from genie.libs.parser.bigip.get_net_tunnelsgre import NetTunnelsGre

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/gre'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:gre:grecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/gre?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:gre:grestate",
                    "name": "gre",
                    "partition": "Common",
                    "fullPath": "/Common/gre",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/gre/~Common~gre?ver=14.1.2.1",
                    "encapsulation": "standard",
                    "floodingType": "none",
                    "rxCsum": "disabled",
                    "txCsum": "disabled",
                },
                {
                    "kind": "tm:net:tunnels:gre:grestate",
                    "name": "nvgre",
                    "partition": "Common",
                    "fullPath": "/Common/nvgre",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/gre/~Common~nvgre?ver=14.1.2.1",
                    "defaultsFrom": "/Common/gre",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/gre/~Common~gre?ver=14.1.2.1"
                    },
                    "encapsulation": "nvgre",
                    "floodingType": "none",
                    "rxCsum": "disabled",
                    "txCsum": "disabled",
                },
            ],
        }


class test_get_net_tunnelsgre(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "encapsulation": "standard",
                "floodingType": "none",
                "fullPath": "/Common/gre",
                "generation": 1,
                "kind": "tm:net:tunnels:gre:grestate",
                "name": "gre",
                "partition": "Common",
                "rxCsum": "disabled",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/gre/~Common~gre?ver=14.1.2.1",
                "txCsum": "disabled",
            },
            {
                "defaultsFrom": "/Common/gre",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/gre/~Common~gre?ver=14.1.2.1"
                },
                "encapsulation": "nvgre",
                "floodingType": "none",
                "fullPath": "/Common/nvgre",
                "generation": 1,
                "kind": "tm:net:tunnels:gre:grestate",
                "name": "nvgre",
                "partition": "Common",
                "rxCsum": "disabled",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/gre/~Common~nvgre?ver=14.1.2.1",
                "txCsum": "disabled",
            },
        ],
        "kind": "tm:net:tunnels:gre:grecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/gre?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsGre(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsGre(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
