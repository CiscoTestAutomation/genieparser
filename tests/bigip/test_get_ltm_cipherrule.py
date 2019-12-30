# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_cipherrule
from genie.libs.parser.bigip.get_ltm_cipherrule import LtmCipherRule

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/cipher/rule'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:cipher:rule:rulecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:cipher:rule:rulestate",
                    "name": "f5-aes",
                    "partition": "Common",
                    "fullPath": "/Common/f5-aes",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-aes?ver=14.1.2.1",
                    "cipher": "AES-GCM:AES",
                    "description": "Cipher suites that use the AES cipher.",
                    "dhGroups": "DEFAULT",
                    "signatureAlgorithms": "DEFAULT",
                },
                {
                    "kind": "tm:ltm:cipher:rule:rulestate",
                    "name": "f5-default",
                    "partition": "Common",
                    "fullPath": "/Common/f5-default",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-default?ver=14.1.2.1",
                    "cipher": "DEFAULT",
                    "description": "The recommended default cipher suites.",
                    "dhGroups": "DEFAULT",
                    "signatureAlgorithms": "DEFAULT",
                },
                {
                    "kind": "tm:ltm:cipher:rule:rulestate",
                    "name": "f5-ecc",
                    "partition": "Common",
                    "fullPath": "/Common/f5-ecc",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-ecc?ver=14.1.2.1",
                    "cipher": "ECDHE:ECDHE_ECDSA",
                    "description": "Cipher suites that utilize Elliptical Curve Ephemeral Diffie-Hellman key exchange.",
                    "dhGroups": "DEFAULT",
                    "signatureAlgorithms": "DEFAULT",
                },
                {
                    "kind": "tm:ltm:cipher:rule:rulestate",
                    "name": "f5-hw_keys",
                    "partition": "Common",
                    "fullPath": "/Common/f5-hw_keys",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-hw_keys?ver=14.1.2.1",
                    "cipher": "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-CBC-SHA:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:ECDH-RSA-AES256-GCM-SHA384:ECDH-RSA-AES256-SHA384:ECDH-RSA-AES256-SHA:AES256-GCM-SHA384:AES256-SHA256:AES256-SHA:ECDHE-RSA-DES-CBC3-SHA:DHE-RSA-DES-CBC3-SHA:ECDH-RSA-DES-CBC3-SHA:DES-CBC3-SHA:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES128-CBC-SHA:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:ECDH-RSA-AES128-GCM-SHA256:ECDH-RSA-AES128-SHA256:ECDH-RSA-AES128-SHA:AES128-GCM-SHA256:AES128-SHA256:AES128-SHA:RC4-SHA:RC4-MD5:DHE-RSA-DES-CBC-SHA:DHE-RSA-CAMELLIA256-SHA:CAMELLIA256-SHA:DHE-RSA-CAMELLIA128-SHA:!TLSv1:!TLSv1_1:!SSLv3:!DTLSv1",
                    "description": "Cipher suites eligible for use with a Hardware Security Module.",
                    "dhGroups": "DEFAULT",
                    "signatureAlgorithms": "DEFAULT",
                },
                {
                    "kind": "tm:ltm:cipher:rule:rulestate",
                    "name": "f5-secure",
                    "partition": "Common",
                    "fullPath": "/Common/f5-secure",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-secure?ver=14.1.2.1",
                    "cipher": "ECDHE:RSA:ECDHE_ECDSA:!SSLV3:!RC4:!EXP:!DES:!3DES",
                    "description": "Cipher suites that maximize regulatory compliance.",
                    "dhGroups": "DEFAULT",
                    "signatureAlgorithms": "DEFAULT",
                },
            ],
        }


class test_get_ltm_cipherrule(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "cipher": "AES-GCM:AES",
                "description": "Cipher suites that use the AES cipher.",
                "dhGroups": "DEFAULT",
                "fullPath": "/Common/f5-aes",
                "generation": 1,
                "kind": "tm:ltm:cipher:rule:rulestate",
                "name": "f5-aes",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-aes?ver=14.1.2.1",
                "signatureAlgorithms": "DEFAULT",
            },
            {
                "cipher": "DEFAULT",
                "description": "The recommended default cipher suites.",
                "dhGroups": "DEFAULT",
                "fullPath": "/Common/f5-default",
                "generation": 1,
                "kind": "tm:ltm:cipher:rule:rulestate",
                "name": "f5-default",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-default?ver=14.1.2.1",
                "signatureAlgorithms": "DEFAULT",
            },
            {
                "cipher": "ECDHE:ECDHE_ECDSA",
                "description": "Cipher suites that utilize Elliptical Curve "
                "Ephemeral Diffie-Hellman key exchange.",
                "dhGroups": "DEFAULT",
                "fullPath": "/Common/f5-ecc",
                "generation": 1,
                "kind": "tm:ltm:cipher:rule:rulestate",
                "name": "f5-ecc",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-ecc?ver=14.1.2.1",
                "signatureAlgorithms": "DEFAULT",
            },
            {
                "cipher": "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-CBC-SHA:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:ECDH-RSA-AES256-GCM-SHA384:ECDH-RSA-AES256-SHA384:ECDH-RSA-AES256-SHA:AES256-GCM-SHA384:AES256-SHA256:AES256-SHA:ECDHE-RSA-DES-CBC3-SHA:DHE-RSA-DES-CBC3-SHA:ECDH-RSA-DES-CBC3-SHA:DES-CBC3-SHA:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES128-CBC-SHA:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:ECDH-RSA-AES128-GCM-SHA256:ECDH-RSA-AES128-SHA256:ECDH-RSA-AES128-SHA:AES128-GCM-SHA256:AES128-SHA256:AES128-SHA:RC4-SHA:RC4-MD5:DHE-RSA-DES-CBC-SHA:DHE-RSA-CAMELLIA256-SHA:CAMELLIA256-SHA:DHE-RSA-CAMELLIA128-SHA:!TLSv1:!TLSv1_1:!SSLv3:!DTLSv1",
                "description": "Cipher suites eligible for use with a Hardware "
                "Security Module.",
                "dhGroups": "DEFAULT",
                "fullPath": "/Common/f5-hw_keys",
                "generation": 1,
                "kind": "tm:ltm:cipher:rule:rulestate",
                "name": "f5-hw_keys",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-hw_keys?ver=14.1.2.1",
                "signatureAlgorithms": "DEFAULT",
            },
            {
                "cipher": "ECDHE:RSA:ECDHE_ECDSA:!SSLV3:!RC4:!EXP:!DES:!3DES",
                "description": "Cipher suites that maximize regulatory compliance.",
                "dhGroups": "DEFAULT",
                "fullPath": "/Common/f5-secure",
                "generation": 1,
                "kind": "tm:ltm:cipher:rule:rulestate",
                "name": "f5-secure",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-secure?ver=14.1.2.1",
                "signatureAlgorithms": "DEFAULT",
            },
        ],
        "kind": "tm:ltm:cipher:rule:rulecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/cipher/rule?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmCipherRule(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmCipherRule(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
