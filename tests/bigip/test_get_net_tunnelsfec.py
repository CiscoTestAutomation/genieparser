# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelsfec
from genie.libs.parser.bigip.get_net_tunnelsfec import NetTunnelsFec

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/fec'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:fec:feccollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/fec?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:fec:fecstate",
                    "name": "fec",
                    "partition": "Common",
                    "fullPath": "/Common/fec",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/fec/~Common~fec?ver=14.1.2.1",
                    "decodeIdleTimeout": 1500,
                    "decodeMaxPackets": 512,
                    "decodeQueues": 32,
                    "encodeMaxDelay": 500,
                    "keepaliveInterval": 5,
                    "lzo": "enabled",
                    "repairAdaptive": "enabled",
                    "repairPackets": 15,
                    "sourceAdaptive": "enabled",
                    "sourcePackets": 15,
                    "udpPort": 8288,
                }
            ],
        }


class test_get_net_tunnelsfec(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "decodeIdleTimeout": 1500,
                "decodeMaxPackets": 512,
                "decodeQueues": 32,
                "encodeMaxDelay": 500,
                "fullPath": "/Common/fec",
                "generation": 1,
                "keepaliveInterval": 5,
                "kind": "tm:net:tunnels:fec:fecstate",
                "lzo": "enabled",
                "name": "fec",
                "partition": "Common",
                "repairAdaptive": "enabled",
                "repairPackets": 15,
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/fec/~Common~fec?ver=14.1.2.1",
                "sourceAdaptive": "enabled",
                "sourcePackets": 15,
                "udpPort": 8288,
            }
        ],
        "kind": "tm:net:tunnels:fec:feccollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/fec?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsFec(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsFec(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
