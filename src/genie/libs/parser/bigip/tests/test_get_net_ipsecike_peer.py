# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_ipsecike_peer
from genie.libs.parser.bigip.get_net_ipsecike_peer import NetIpsecIkepeer

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/ipsec/ike-peer'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:ipsec:ike-peer:ike-peercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/ipsec/ike-peer?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:ipsec:ike-peer:ike-peerstate",
                    "name": "anonymous",
                    "partition": "Common",
                    "fullPath": "/Common/anonymous",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/ipsec/ike-peer/~Common~anonymous?ver=14.1.2.1",
                    "dpdDelay": 30,
                    "generatePolicy": "off",
                    "lifetime": 1440,
                    "mode": "main",
                    "myCertFile": "/Common/default.crt",
                    "myCertFileReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt?ver=14.1.2.1"
                    },
                    "myCertKeyFile": "/Common/default.key",
                    "myCertKeyFileReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key?ver=14.1.2.1"
                    },
                    "myIdType": "asn1dn",
                    "natTraversal": "off",
                    "passive": "false",
                    "peersCertType": "none",
                    "peersIdType": "asn1dn",
                    "phase1AuthMethod": "rsa-signature",
                    "phase1EncryptAlgorithm": "3des",
                    "phase1HashAlgorithm": "sha256",
                    "phase1PerfectForwardSecrecy": "modp1024",
                    "prf": "sha256",
                    "proxySupport": "enabled",
                    "remoteAddress": "any6",
                    "replayWindowSize": 64,
                    "state": "disabled",
                    "verifyCert": "false",
                    "version": ["v1"],
                }
            ],
        }


class test_get_net_ipsecike_peer(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "dpdDelay": 30,
                "fullPath": "/Common/anonymous",
                "generatePolicy": "off",
                "generation": 1,
                "kind": "tm:net:ipsec:ike-peer:ike-peerstate",
                "lifetime": 1440,
                "mode": "main",
                "myCertFile": "/Common/default.crt",
                "myCertFileReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt?ver=14.1.2.1"
                },
                "myCertKeyFile": "/Common/default.key",
                "myCertKeyFileReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key?ver=14.1.2.1"
                },
                "myIdType": "asn1dn",
                "name": "anonymous",
                "natTraversal": "off",
                "partition": "Common",
                "passive": "false",
                "peersCertType": "none",
                "peersIdType": "asn1dn",
                "phase1AuthMethod": "rsa-signature",
                "phase1EncryptAlgorithm": "3des",
                "phase1HashAlgorithm": "sha256",
                "phase1PerfectForwardSecrecy": "modp1024",
                "prf": "sha256",
                "proxySupport": "enabled",
                "remoteAddress": "any6",
                "replayWindowSize": 64,
                "selfLink": "https://localhost/mgmt/tm/net/ipsec/ike-peer/~Common~anonymous?ver=14.1.2.1",
                "state": "disabled",
                "verifyCert": "false",
                "version": ["v1"],
            }
        ],
        "kind": "tm:net:ipsec:ike-peer:ike-peercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/ipsec/ike-peer?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetIpsecIkepeer(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetIpsecIkepeer(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
