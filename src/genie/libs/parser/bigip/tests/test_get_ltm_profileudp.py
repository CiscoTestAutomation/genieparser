# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileudp
from genie.libs.parser.bigip.get_ltm_profileudp import LtmProfileUdp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/udp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:udp:udpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/udp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:udp:udpstate",
                    "name": "udp",
                    "partition": "Common",
                    "fullPath": "/Common/udp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp?ver=14.1.2.1",
                    "allowNoPayload": "disabled",
                    "appService": "none",
                    "bufferMaxBytes": 655350,
                    "bufferMaxPackets": 0,
                    "datagramLoadBalancing": "disabled",
                    "defaultsFrom": "none",
                    "description": "none",
                    "idleTimeout": "60",
                    "ipDfMode": "pmtu",
                    "ipTosToClient": "0",
                    "ipTtlMode": "proxy",
                    "ipTtlV4": 255,
                    "ipTtlV6": 64,
                    "linkQosToClient": "0",
                    "noChecksum": "disabled",
                    "proxyMss": "disabled",
                    "sendBufferSize": 655350,
                },
                {
                    "kind": "tm:ltm:profile:udp:udpstate",
                    "name": "udp_decrement_ttl",
                    "partition": "Common",
                    "fullPath": "/Common/udp_decrement_ttl",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp_decrement_ttl?ver=14.1.2.1",
                    "allowNoPayload": "disabled",
                    "appService": "none",
                    "bufferMaxBytes": 655350,
                    "bufferMaxPackets": 0,
                    "datagramLoadBalancing": "disabled",
                    "defaultsFrom": "/Common/udp",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp?ver=14.1.2.1"
                    },
                    "description": "none",
                    "idleTimeout": "60",
                    "ipDfMode": "pmtu",
                    "ipTosToClient": "0",
                    "ipTtlMode": "decrement",
                    "ipTtlV4": 255,
                    "ipTtlV6": 64,
                    "linkQosToClient": "0",
                    "noChecksum": "disabled",
                    "proxyMss": "disabled",
                    "sendBufferSize": 655350,
                },
                {
                    "kind": "tm:ltm:profile:udp:udpstate",
                    "name": "udp_gtm_dns",
                    "partition": "Common",
                    "fullPath": "/Common/udp_gtm_dns",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp_gtm_dns?ver=14.1.2.1",
                    "allowNoPayload": "disabled",
                    "appService": "none",
                    "bufferMaxBytes": 655350,
                    "bufferMaxPackets": 0,
                    "datagramLoadBalancing": "enabled",
                    "defaultsFrom": "/Common/udp",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp?ver=14.1.2.1"
                    },
                    "description": "none",
                    "idleTimeout": "5",
                    "ipDfMode": "pmtu",
                    "ipTosToClient": "0",
                    "ipTtlMode": "proxy",
                    "ipTtlV4": 255,
                    "ipTtlV6": 64,
                    "linkQosToClient": "0",
                    "noChecksum": "disabled",
                    "proxyMss": "disabled",
                    "sendBufferSize": 655350,
                },
                {
                    "kind": "tm:ltm:profile:udp:udpstate",
                    "name": "udp_preserve_ttl",
                    "partition": "Common",
                    "fullPath": "/Common/udp_preserve_ttl",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp_preserve_ttl?ver=14.1.2.1",
                    "allowNoPayload": "disabled",
                    "appService": "none",
                    "bufferMaxBytes": 655350,
                    "bufferMaxPackets": 0,
                    "datagramLoadBalancing": "disabled",
                    "defaultsFrom": "/Common/udp",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp?ver=14.1.2.1"
                    },
                    "description": "none",
                    "idleTimeout": "60",
                    "ipDfMode": "pmtu",
                    "ipTosToClient": "0",
                    "ipTtlMode": "preserve",
                    "ipTtlV4": 255,
                    "ipTtlV6": 64,
                    "linkQosToClient": "0",
                    "noChecksum": "disabled",
                    "proxyMss": "disabled",
                    "sendBufferSize": 655350,
                },
            ],
        }


class test_get_ltm_profileudp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "allowNoPayload": "disabled",
                "appService": "none",
                "bufferMaxBytes": 655350,
                "bufferMaxPackets": 0,
                "datagramLoadBalancing": "disabled",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/udp",
                "generation": 1,
                "idleTimeout": "60",
                "ipDfMode": "pmtu",
                "ipTosToClient": "0",
                "ipTtlMode": "proxy",
                "ipTtlV4": 255,
                "ipTtlV6": 64,
                "kind": "tm:ltm:profile:udp:udpstate",
                "linkQosToClient": "0",
                "name": "udp",
                "noChecksum": "disabled",
                "partition": "Common",
                "proxyMss": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp?ver=14.1.2.1",
                "sendBufferSize": 655350,
            },
            {
                "allowNoPayload": "disabled",
                "appService": "none",
                "bufferMaxBytes": 655350,
                "bufferMaxPackets": 0,
                "datagramLoadBalancing": "disabled",
                "defaultsFrom": "/Common/udp",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp?ver=14.1.2.1"
                },
                "description": "none",
                "fullPath": "/Common/udp_decrement_ttl",
                "generation": 1,
                "idleTimeout": "60",
                "ipDfMode": "pmtu",
                "ipTosToClient": "0",
                "ipTtlMode": "decrement",
                "ipTtlV4": 255,
                "ipTtlV6": 64,
                "kind": "tm:ltm:profile:udp:udpstate",
                "linkQosToClient": "0",
                "name": "udp_decrement_ttl",
                "noChecksum": "disabled",
                "partition": "Common",
                "proxyMss": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp_decrement_ttl?ver=14.1.2.1",
                "sendBufferSize": 655350,
            },
            {
                "allowNoPayload": "disabled",
                "appService": "none",
                "bufferMaxBytes": 655350,
                "bufferMaxPackets": 0,
                "datagramLoadBalancing": "enabled",
                "defaultsFrom": "/Common/udp",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp?ver=14.1.2.1"
                },
                "description": "none",
                "fullPath": "/Common/udp_gtm_dns",
                "generation": 1,
                "idleTimeout": "5",
                "ipDfMode": "pmtu",
                "ipTosToClient": "0",
                "ipTtlMode": "proxy",
                "ipTtlV4": 255,
                "ipTtlV6": 64,
                "kind": "tm:ltm:profile:udp:udpstate",
                "linkQosToClient": "0",
                "name": "udp_gtm_dns",
                "noChecksum": "disabled",
                "partition": "Common",
                "proxyMss": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp_gtm_dns?ver=14.1.2.1",
                "sendBufferSize": 655350,
            },
            {
                "allowNoPayload": "disabled",
                "appService": "none",
                "bufferMaxBytes": 655350,
                "bufferMaxPackets": 0,
                "datagramLoadBalancing": "disabled",
                "defaultsFrom": "/Common/udp",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp?ver=14.1.2.1"
                },
                "description": "none",
                "fullPath": "/Common/udp_preserve_ttl",
                "generation": 1,
                "idleTimeout": "60",
                "ipDfMode": "pmtu",
                "ipTosToClient": "0",
                "ipTtlMode": "preserve",
                "ipTtlV4": 255,
                "ipTtlV6": 64,
                "kind": "tm:ltm:profile:udp:udpstate",
                "linkQosToClient": "0",
                "name": "udp_preserve_ttl",
                "noChecksum": "disabled",
                "partition": "Common",
                "proxyMss": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/udp/~Common~udp_preserve_ttl?ver=14.1.2.1",
                "sendBufferSize": 655350,
            },
        ],
        "kind": "tm:ltm:profile:udp:udpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/udp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileUdp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileUdp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
