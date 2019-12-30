# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelstcp_forward
from genie.libs.parser.bigip.get_net_tunnelstcp_forward import (
    NetTunnelsTcpforward,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/tcp-forward'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:tcp-forward:tcp-forwardcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/tcp-forward?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:tcp-forward:tcp-forwardstate",
                    "name": "tcp-forward",
                    "partition": "Common",
                    "fullPath": "/Common/tcp-forward",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/tcp-forward/~Common~tcp-forward?ver=14.1.2.1",
                    "description": "TCP forwarding without encapsulation",
                }
            ],
        }


class test_get_net_tunnelstcp_forward(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "description": "TCP forwarding without encapsulation",
                "fullPath": "/Common/tcp-forward",
                "generation": 1,
                "kind": "tm:net:tunnels:tcp-forward:tcp-forwardstate",
                "name": "tcp-forward",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/tcp-forward/~Common~tcp-forward?ver=14.1.2.1",
            }
        ],
        "kind": "tm:net:tunnels:tcp-forward:tcp-forwardcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/tcp-forward?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsTcpforward(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsTcpforward(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
