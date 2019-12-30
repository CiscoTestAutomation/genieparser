# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelsipip
from genie.libs.parser.bigip.get_net_tunnelsipip import NetTunnelsIpip

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/ipip'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:ipip:ipipcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:ipip:ipipstate",
                    "name": "dslite",
                    "partition": "Common",
                    "fullPath": "/Common/dslite",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~dslite?ver=14.1.2.1",
                    "defaultsFrom": "/Common/ip4ip6",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ip4ip6?ver=14.1.2.1"
                    },
                    "description": "Dual-stack lite IPv4 in IPv6",
                    "dsLite": "enabled",
                    "proto": "IPv4",
                },
                {
                    "kind": "tm:net:tunnels:ipip:ipipstate",
                    "name": "ip4ip4",
                    "partition": "Common",
                    "fullPath": "/Common/ip4ip4",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ip4ip4?ver=14.1.2.1",
                    "defaultsFrom": "/Common/ipip",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ipip?ver=14.1.2.1"
                    },
                    "description": "IPv4 in IPv4",
                    "dsLite": "disabled",
                    "proto": "IPv4",
                },
                {
                    "kind": "tm:net:tunnels:ipip:ipipstate",
                    "name": "ip4ip6",
                    "partition": "Common",
                    "fullPath": "/Common/ip4ip6",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ip4ip6?ver=14.1.2.1",
                    "defaultsFrom": "/Common/ipip",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ipip?ver=14.1.2.1"
                    },
                    "description": "IPv4 in IPv6",
                    "dsLite": "disabled",
                    "proto": "IPv4",
                },
                {
                    "kind": "tm:net:tunnels:ipip:ipipstate",
                    "name": "ip6ip4",
                    "partition": "Common",
                    "fullPath": "/Common/ip6ip4",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ip6ip4?ver=14.1.2.1",
                    "defaultsFrom": "/Common/ipip",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ipip?ver=14.1.2.1"
                    },
                    "description": "IPv6 in IPv4",
                    "dsLite": "disabled",
                    "proto": "IPv6",
                },
                {
                    "kind": "tm:net:tunnels:ipip:ipipstate",
                    "name": "ip6ip6",
                    "partition": "Common",
                    "fullPath": "/Common/ip6ip6",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ip6ip6?ver=14.1.2.1",
                    "defaultsFrom": "/Common/ipip",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ipip?ver=14.1.2.1"
                    },
                    "description": "IPv6 in IPv6",
                    "dsLite": "disabled",
                    "proto": "IPv6",
                },
                {
                    "kind": "tm:net:tunnels:ipip:ipipstate",
                    "name": "ipip",
                    "partition": "Common",
                    "fullPath": "/Common/ipip",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ipip?ver=14.1.2.1",
                    "dsLite": "disabled",
                    "proto": "IPv4",
                },
            ],
        }


class test_get_net_tunnelsipip(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "defaultsFrom": "/Common/ip4ip6",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ip4ip6?ver=14.1.2.1"
                },
                "description": "Dual-stack lite IPv4 in IPv6",
                "dsLite": "enabled",
                "fullPath": "/Common/dslite",
                "generation": 1,
                "kind": "tm:net:tunnels:ipip:ipipstate",
                "name": "dslite",
                "partition": "Common",
                "proto": "IPv4",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~dslite?ver=14.1.2.1",
            },
            {
                "defaultsFrom": "/Common/ipip",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ipip?ver=14.1.2.1"
                },
                "description": "IPv4 in IPv4",
                "dsLite": "disabled",
                "fullPath": "/Common/ip4ip4",
                "generation": 1,
                "kind": "tm:net:tunnels:ipip:ipipstate",
                "name": "ip4ip4",
                "partition": "Common",
                "proto": "IPv4",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ip4ip4?ver=14.1.2.1",
            },
            {
                "defaultsFrom": "/Common/ipip",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ipip?ver=14.1.2.1"
                },
                "description": "IPv4 in IPv6",
                "dsLite": "disabled",
                "fullPath": "/Common/ip4ip6",
                "generation": 1,
                "kind": "tm:net:tunnels:ipip:ipipstate",
                "name": "ip4ip6",
                "partition": "Common",
                "proto": "IPv4",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ip4ip6?ver=14.1.2.1",
            },
            {
                "defaultsFrom": "/Common/ipip",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ipip?ver=14.1.2.1"
                },
                "description": "IPv6 in IPv4",
                "dsLite": "disabled",
                "fullPath": "/Common/ip6ip4",
                "generation": 1,
                "kind": "tm:net:tunnels:ipip:ipipstate",
                "name": "ip6ip4",
                "partition": "Common",
                "proto": "IPv6",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ip6ip4?ver=14.1.2.1",
            },
            {
                "defaultsFrom": "/Common/ipip",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ipip?ver=14.1.2.1"
                },
                "description": "IPv6 in IPv6",
                "dsLite": "disabled",
                "fullPath": "/Common/ip6ip6",
                "generation": 1,
                "kind": "tm:net:tunnels:ipip:ipipstate",
                "name": "ip6ip6",
                "partition": "Common",
                "proto": "IPv6",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ip6ip6?ver=14.1.2.1",
            },
            {
                "dsLite": "disabled",
                "fullPath": "/Common/ipip",
                "generation": 1,
                "kind": "tm:net:tunnels:ipip:ipipstate",
                "name": "ipip",
                "partition": "Common",
                "proto": "IPv4",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip/~Common~ipip?ver=14.1.2.1",
            },
        ],
        "kind": "tm:net:tunnels:ipip:ipipcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipip?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsIpip(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsIpip(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
