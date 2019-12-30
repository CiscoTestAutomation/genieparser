# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_ciphergroup
from genie.libs.parser.bigip.get_ltm_ciphergroup import LtmCipherGroup

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/cipher/group'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:cipher:group:groupcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:cipher:group:groupstate",
                    "name": "f5-aes",
                    "partition": "Common",
                    "fullPath": "/Common/f5-aes",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group/~Common~f5-aes?ver=14.1.2.1",
                    "ordering": "default",
                    "allow": [
                        {
                            "name": "f5-aes",
                            "partition": "Common",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-aes?ver=14.1.2.1"
                            },
                        }
                    ],
                },
                {
                    "kind": "tm:ltm:cipher:group:groupstate",
                    "name": "f5-default",
                    "partition": "Common",
                    "fullPath": "/Common/f5-default",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group/~Common~f5-default?ver=14.1.2.1",
                    "ordering": "default",
                    "allow": [
                        {
                            "name": "f5-default",
                            "partition": "Common",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-default?ver=14.1.2.1"
                            },
                        }
                    ],
                },
                {
                    "kind": "tm:ltm:cipher:group:groupstate",
                    "name": "f5-ecc",
                    "partition": "Common",
                    "fullPath": "/Common/f5-ecc",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group/~Common~f5-ecc?ver=14.1.2.1",
                    "ordering": "default",
                    "allow": [
                        {
                            "name": "f5-ecc",
                            "partition": "Common",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-ecc?ver=14.1.2.1"
                            },
                        }
                    ],
                },
                {
                    "kind": "tm:ltm:cipher:group:groupstate",
                    "name": "f5-hw_keys",
                    "partition": "Common",
                    "fullPath": "/Common/f5-hw_keys",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group/~Common~f5-hw_keys?ver=14.1.2.1",
                    "ordering": "default",
                    "allow": [
                        {
                            "name": "f5-hw_keys",
                            "partition": "Common",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-hw_keys?ver=14.1.2.1"
                            },
                        }
                    ],
                },
                {
                    "kind": "tm:ltm:cipher:group:groupstate",
                    "name": "f5-secure",
                    "partition": "Common",
                    "fullPath": "/Common/f5-secure",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group/~Common~f5-secure?ver=14.1.2.1",
                    "ordering": "default",
                    "allow": [
                        {
                            "name": "f5-secure",
                            "partition": "Common",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-secure?ver=14.1.2.1"
                            },
                        }
                    ],
                },
            ],
        }


class test_get_ltm_ciphergroup(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "allow": [
                    {
                        "name": "f5-aes",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-aes?ver=14.1.2.1"
                        },
                        "partition": "Common",
                    }
                ],
                "fullPath": "/Common/f5-aes",
                "generation": 1,
                "kind": "tm:ltm:cipher:group:groupstate",
                "name": "f5-aes",
                "ordering": "default",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group/~Common~f5-aes?ver=14.1.2.1",
            },
            {
                "allow": [
                    {
                        "name": "f5-default",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-default?ver=14.1.2.1"
                        },
                        "partition": "Common",
                    }
                ],
                "fullPath": "/Common/f5-default",
                "generation": 1,
                "kind": "tm:ltm:cipher:group:groupstate",
                "name": "f5-default",
                "ordering": "default",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group/~Common~f5-default?ver=14.1.2.1",
            },
            {
                "allow": [
                    {
                        "name": "f5-ecc",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-ecc?ver=14.1.2.1"
                        },
                        "partition": "Common",
                    }
                ],
                "fullPath": "/Common/f5-ecc",
                "generation": 1,
                "kind": "tm:ltm:cipher:group:groupstate",
                "name": "f5-ecc",
                "ordering": "default",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group/~Common~f5-ecc?ver=14.1.2.1",
            },
            {
                "allow": [
                    {
                        "name": "f5-hw_keys",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-hw_keys?ver=14.1.2.1"
                        },
                        "partition": "Common",
                    }
                ],
                "fullPath": "/Common/f5-hw_keys",
                "generation": 1,
                "kind": "tm:ltm:cipher:group:groupstate",
                "name": "f5-hw_keys",
                "ordering": "default",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group/~Common~f5-hw_keys?ver=14.1.2.1",
            },
            {
                "allow": [
                    {
                        "name": "f5-secure",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/ltm/cipher/rule/~Common~f5-secure?ver=14.1.2.1"
                        },
                        "partition": "Common",
                    }
                ],
                "fullPath": "/Common/f5-secure",
                "generation": 1,
                "kind": "tm:ltm:cipher:group:groupstate",
                "name": "f5-secure",
                "ordering": "default",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group/~Common~f5-secure?ver=14.1.2.1",
            },
        ],
        "kind": "tm:ltm:cipher:group:groupcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/cipher/group?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmCipherGroup(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmCipherGroup(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
