# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilesocks
from genie.libs.parser.bigip.get_ltm_profilesocks import LtmProfileSocks

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/socks'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:socks:sockscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/socks?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:socks:socksstate",
                    "name": "socks",
                    "partition": "Common",
                    "fullPath": "/Common/socks",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/socks/~Common~socks?ver=14.1.2.1",
                    "appService": "none",
                    "defaultConnectHandling": "deny",
                    "defaultsFrom": "none",
                    "description": "none",
                    "dnsResolver": "none",
                    "ipv6": "no",
                    "protocolVersions": ["socks4", "socks4a", "socks5"],
                    "routeDomain": "/Common/0",
                    "routeDomainReference": {
                        "link": "https://localhost/mgmt/tm/net/route-domain/~Common~0?ver=14.1.2.1"
                    },
                    "tunnelName": "/Common/socks-tunnel",
                    "tunnelNameReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/tunnel/~Common~socks-tunnel?ver=14.1.2.1"
                    },
                }
            ],
        }


class test_get_ltm_profilesocks(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultConnectHandling": "deny",
                "defaultsFrom": "none",
                "description": "none",
                "dnsResolver": "none",
                "fullPath": "/Common/socks",
                "generation": 1,
                "ipv6": "no",
                "kind": "tm:ltm:profile:socks:socksstate",
                "name": "socks",
                "partition": "Common",
                "protocolVersions": ["socks4", "socks4a", "socks5"],
                "routeDomain": "/Common/0",
                "routeDomainReference": {
                    "link": "https://localhost/mgmt/tm/net/route-domain/~Common~0?ver=14.1.2.1"
                },
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/socks/~Common~socks?ver=14.1.2.1",
                "tunnelName": "/Common/socks-tunnel",
                "tunnelNameReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/tunnel/~Common~socks-tunnel?ver=14.1.2.1"
                },
            }
        ],
        "kind": "tm:ltm:profile:socks:sockscollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/socks?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileSocks(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileSocks(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
