# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_cryptokey
from genie.libs.parser.bigip.get_sys_cryptokey import SysCryptoKey

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/crypto/key'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:crypto:key:keycollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/crypto/key?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:crypto:key:keystate",
                    "name": "/Common/default.key",
                    "fullPath": "/Common/default.key",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/crypto/key/~Common~default.key?ver=14.1.2.1",
                    "keySize": "2048",
                    "keyType": "rsa-private",
                    "securityType": "normal",
                },
                {
                    "kind": "tm:sys:crypto:key:keystate",
                    "name": "/Common/f5_api_com.key",
                    "fullPath": "/Common/f5_api_com.key",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/crypto/key/~Common~f5_api_com.key?ver=14.1.2.1",
                    "keySize": "4096",
                    "keyType": "rsa-private",
                    "securityType": "password",
                },
            ],
        }


class test_get_sys_cryptokey(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/default.key",
                "generation": 1,
                "keySize": "2048",
                "keyType": "rsa-private",
                "kind": "tm:sys:crypto:key:keystate",
                "name": "/Common/default.key",
                "securityType": "normal",
                "selfLink": "https://localhost/mgmt/tm/sys/crypto/key/~Common~default.key?ver=14.1.2.1",
            },
            {
                "fullPath": "/Common/f5_api_com.key",
                "generation": 1,
                "keySize": "4096",
                "keyType": "rsa-private",
                "kind": "tm:sys:crypto:key:keystate",
                "name": "/Common/f5_api_com.key",
                "securityType": "password",
                "selfLink": "https://localhost/mgmt/tm/sys/crypto/key/~Common~f5_api_com.key?ver=14.1.2.1",
            },
        ],
        "kind": "tm:sys:crypto:key:keycollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/crypto/key?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysCryptoKey(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysCryptoKey(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
