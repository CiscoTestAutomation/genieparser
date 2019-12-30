# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_ipsecipsec_policy
from genie.libs.parser.bigip.get_net_ipsecipsec_policy import (
    NetIpsecIpsecpolicy,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/ipsec/ipsec-policy'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:ipsec:ipsec-policy:ipsec-policycollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/ipsec/ipsec-policy?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:ipsec:ipsec-policy:ipsec-policystate",
                    "name": "default-ipsec-policy",
                    "partition": "Common",
                    "fullPath": "/Common/default-ipsec-policy",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/ipsec/ipsec-policy/~Common~default-ipsec-policy?ver=14.1.2.1",
                    "ikePhase2AuthAlgorithm": "aes-gcm128",
                    "ikePhase2EncryptAlgorithm": "aes-gcm128",
                    "ikePhase2Lifetime": 1440,
                    "ikePhase2LifetimeKilobytes": 0,
                    "ikePhase2PerfectForwardSecrecy": "none",
                    "ipcomp": "none",
                    "mode": "transport",
                    "protocol": "esp",
                    "tunnelLocalAddress": "any6",
                    "tunnelRemoteAddress": "any6",
                },
                {
                    "kind": "tm:net:ipsec:ipsec-policy:ipsec-policystate",
                    "name": "default-ipsec-policy-interface",
                    "partition": "Common",
                    "fullPath": "/Common/default-ipsec-policy-interface",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/ipsec/ipsec-policy/~Common~default-ipsec-policy-interface?ver=14.1.2.1",
                    "ikePhase2AuthAlgorithm": "aes-gcm128",
                    "ikePhase2EncryptAlgorithm": "aes-gcm128",
                    "ikePhase2Lifetime": 1440,
                    "ikePhase2LifetimeKilobytes": 0,
                    "ikePhase2PerfectForwardSecrecy": "none",
                    "ipcomp": "none",
                    "mode": "interface",
                    "protocol": "esp",
                    "tunnelLocalAddress": "any6",
                    "tunnelRemoteAddress": "any6",
                },
                {
                    "kind": "tm:net:ipsec:ipsec-policy:ipsec-policystate",
                    "name": "default-ipsec-policy-isession",
                    "partition": "Common",
                    "fullPath": "/Common/default-ipsec-policy-isession",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/ipsec/ipsec-policy/~Common~default-ipsec-policy-isession?ver=14.1.2.1",
                    "ikePhase2AuthAlgorithm": "aes-gcm128",
                    "ikePhase2EncryptAlgorithm": "aes-gcm128",
                    "ikePhase2Lifetime": 1440,
                    "ikePhase2LifetimeKilobytes": 0,
                    "ikePhase2PerfectForwardSecrecy": "none",
                    "ipcomp": "none",
                    "mode": "isession",
                    "protocol": "esp",
                    "tunnelLocalAddress": "any6",
                    "tunnelRemoteAddress": "any6",
                },
            ],
        }


class test_get_net_ipsecipsec_policy(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/default-ipsec-policy",
                "generation": 1,
                "ikePhase2AuthAlgorithm": "aes-gcm128",
                "ikePhase2EncryptAlgorithm": "aes-gcm128",
                "ikePhase2Lifetime": 1440,
                "ikePhase2LifetimeKilobytes": 0,
                "ikePhase2PerfectForwardSecrecy": "none",
                "ipcomp": "none",
                "kind": "tm:net:ipsec:ipsec-policy:ipsec-policystate",
                "mode": "transport",
                "name": "default-ipsec-policy",
                "partition": "Common",
                "protocol": "esp",
                "selfLink": "https://localhost/mgmt/tm/net/ipsec/ipsec-policy/~Common~default-ipsec-policy?ver=14.1.2.1",
                "tunnelLocalAddress": "any6",
                "tunnelRemoteAddress": "any6",
            },
            {
                "fullPath": "/Common/default-ipsec-policy-interface",
                "generation": 1,
                "ikePhase2AuthAlgorithm": "aes-gcm128",
                "ikePhase2EncryptAlgorithm": "aes-gcm128",
                "ikePhase2Lifetime": 1440,
                "ikePhase2LifetimeKilobytes": 0,
                "ikePhase2PerfectForwardSecrecy": "none",
                "ipcomp": "none",
                "kind": "tm:net:ipsec:ipsec-policy:ipsec-policystate",
                "mode": "interface",
                "name": "default-ipsec-policy-interface",
                "partition": "Common",
                "protocol": "esp",
                "selfLink": "https://localhost/mgmt/tm/net/ipsec/ipsec-policy/~Common~default-ipsec-policy-interface?ver=14.1.2.1",
                "tunnelLocalAddress": "any6",
                "tunnelRemoteAddress": "any6",
            },
            {
                "fullPath": "/Common/default-ipsec-policy-isession",
                "generation": 1,
                "ikePhase2AuthAlgorithm": "aes-gcm128",
                "ikePhase2EncryptAlgorithm": "aes-gcm128",
                "ikePhase2Lifetime": 1440,
                "ikePhase2LifetimeKilobytes": 0,
                "ikePhase2PerfectForwardSecrecy": "none",
                "ipcomp": "none",
                "kind": "tm:net:ipsec:ipsec-policy:ipsec-policystate",
                "mode": "isession",
                "name": "default-ipsec-policy-isession",
                "partition": "Common",
                "protocol": "esp",
                "selfLink": "https://localhost/mgmt/tm/net/ipsec/ipsec-policy/~Common~default-ipsec-policy-isession?ver=14.1.2.1",
                "tunnelLocalAddress": "any6",
                "tunnelRemoteAddress": "any6",
            },
        ],
        "kind": "tm:net:ipsec:ipsec-policy:ipsec-policycollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/ipsec/ipsec-policy?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetIpsecIpsecpolicy(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetIpsecIpsecpolicy(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
