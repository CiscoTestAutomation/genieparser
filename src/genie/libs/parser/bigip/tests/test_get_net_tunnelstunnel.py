# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelstunnel
from genie.libs.parser.bigip.get_net_tunnelstunnel import NetTunnelsTunnel

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/tunnel'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:tunnel:tunnelcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/tunnel?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:tunnel:tunnelstate",
                    "name": "http-tunnel",
                    "partition": "Common",
                    "fullPath": "/Common/http-tunnel",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/tunnel/~Common~http-tunnel?ver=14.1.2.1",
                    "autoLasthop": "default",
                    "description": "Tunnel for http-explicit profile",
                    "idleTimeout": 300,
                    "ifIndex": 112,
                    "key": 0,
                    "localAddress": "any6",
                    "mode": "bidirectional",
                    "mtu": 0,
                    "profile": "/Common/tcp-forward",
                    "profileReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/tcp-forward/~Common~tcp-forward?ver=14.1.2.1"
                    },
                    "remoteAddress": "any6",
                    "secondaryAddress": "any6",
                    "tos": "preserve",
                    "transparent": "disabled",
                    "usePmtu": "enabled",
                },
                {
                    "kind": "tm:net:tunnels:tunnel:tunnelstate",
                    "name": "socks-tunnel",
                    "partition": "Common",
                    "fullPath": "/Common/socks-tunnel",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/tunnel/~Common~socks-tunnel?ver=14.1.2.1",
                    "autoLasthop": "default",
                    "description": "Tunnel for socks profile",
                    "idleTimeout": 300,
                    "ifIndex": 128,
                    "key": 0,
                    "localAddress": "any6",
                    "mode": "bidirectional",
                    "mtu": 0,
                    "profile": "/Common/tcp-forward",
                    "profileReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/tcp-forward/~Common~tcp-forward?ver=14.1.2.1"
                    },
                    "remoteAddress": "any6",
                    "secondaryAddress": "any6",
                    "tos": "preserve",
                    "transparent": "disabled",
                    "usePmtu": "enabled",
                },
            ],
        }


class test_get_net_tunnelstunnel(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "autoLasthop": "default",
                "description": "Tunnel for http-explicit profile",
                "fullPath": "/Common/http-tunnel",
                "generation": 1,
                "idleTimeout": 300,
                "ifIndex": 112,
                "key": 0,
                "kind": "tm:net:tunnels:tunnel:tunnelstate",
                "localAddress": "any6",
                "mode": "bidirectional",
                "mtu": 0,
                "name": "http-tunnel",
                "partition": "Common",
                "profile": "/Common/tcp-forward",
                "profileReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/tcp-forward/~Common~tcp-forward?ver=14.1.2.1"
                },
                "remoteAddress": "any6",
                "secondaryAddress": "any6",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/tunnel/~Common~http-tunnel?ver=14.1.2.1",
                "tos": "preserve",
                "transparent": "disabled",
                "usePmtu": "enabled",
            },
            {
                "autoLasthop": "default",
                "description": "Tunnel for socks profile",
                "fullPath": "/Common/socks-tunnel",
                "generation": 1,
                "idleTimeout": 300,
                "ifIndex": 128,
                "key": 0,
                "kind": "tm:net:tunnels:tunnel:tunnelstate",
                "localAddress": "any6",
                "mode": "bidirectional",
                "mtu": 0,
                "name": "socks-tunnel",
                "partition": "Common",
                "profile": "/Common/tcp-forward",
                "profileReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/tcp-forward/~Common~tcp-forward?ver=14.1.2.1"
                },
                "remoteAddress": "any6",
                "secondaryAddress": "any6",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/tunnel/~Common~socks-tunnel?ver=14.1.2.1",
                "tos": "preserve",
                "transparent": "disabled",
                "usePmtu": "enabled",
            },
        ],
        "kind": "tm:net:tunnels:tunnel:tunnelcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/tunnel?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsTunnel(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsTunnel(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
