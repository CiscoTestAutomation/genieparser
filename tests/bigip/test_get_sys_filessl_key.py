# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_filessl_key
from genie.libs.parser.bigip.get_sys_filessl_key import SysFileSslkey

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/file/ssl-key'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:file:ssl-key:ssl-keycollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-key?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:file:ssl-key:ssl-keystate",
                    "name": "default.key",
                    "partition": "Common",
                    "fullPath": "/Common/default.key",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key?ver=14.1.2.1",
                    "checksum": "SHA1:1704:962754799ae957f6fd37341f86d50e42af0c6bd2",
                    "createTime": "2019-10-10T14:15:28Z",
                    "createdBy": "root",
                    "curveName": "none",
                    "keySize": 2048,
                    "keyType": "rsa-private",
                    "lastUpdateTime": "2019-10-10T14:15:28Z",
                    "mode": 33184,
                    "revision": 1,
                    "securityType": "normal",
                    "size": 1704,
                    "systemPath": "/config/ssl/ssl.key/default.key",
                    "updatedBy": "root",
                    "certOrderManagerReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key/cert-order-manager?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:file:ssl-key:ssl-keystate",
                    "name": "f5_api_com.key",
                    "partition": "Common",
                    "fullPath": "/Common/f5_api_com.key",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5_api_com.key?ver=14.1.2.1",
                    "checksum": "SHA1:3306:2ed85f77768f0b80e1c2a3b34cb69db26c4d0c2e",
                    "createTime": "2019-10-10T14:26:18Z",
                    "createdBy": "root",
                    "curveName": "none",
                    "keySize": 4096,
                    "keyType": "rsa-private",
                    "lastUpdateTime": "2019-10-10T14:26:18Z",
                    "mode": 33184,
                    "passphrase": "$M$Sq$WDufoLJX0gFBR2gQY5mLgBcDQmu5qnxG02puqLps1OjbKMhjZ9E6mh5P3mA09EOLHUIyUAfPV9dl+iv5kF05lCEBc3qUTrIiG4rKiJPWgIw=",
                    "revision": 1,
                    "securityType": "password",
                    "size": 3306,
                    "sourcePath": "file:///config/ssl/ssl.key/f5_api_com.key",
                    "updatedBy": "root",
                    "certOrderManagerReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5_api_com.key/cert-order-manager?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
            ],
        }


class test_get_sys_filessl_key(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "certOrderManagerReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key/cert-order-manager?ver=14.1.2.1",
                },
                "checksum": "SHA1:1704:962754799ae957f6fd37341f86d50e42af0c6bd2",
                "createTime": "2019-10-10T14:15:28Z",
                "createdBy": "root",
                "curveName": "none",
                "fullPath": "/Common/default.key",
                "generation": 1,
                "keySize": 2048,
                "keyType": "rsa-private",
                "kind": "tm:sys:file:ssl-key:ssl-keystate",
                "lastUpdateTime": "2019-10-10T14:15:28Z",
                "mode": 33184,
                "name": "default.key",
                "partition": "Common",
                "revision": 1,
                "securityType": "normal",
                "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key?ver=14.1.2.1",
                "size": 1704,
                "systemPath": "/config/ssl/ssl.key/default.key",
                "updatedBy": "root",
            },
            {
                "certOrderManagerReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5_api_com.key/cert-order-manager?ver=14.1.2.1",
                },
                "checksum": "SHA1:3306:2ed85f77768f0b80e1c2a3b34cb69db26c4d0c2e",
                "createTime": "2019-10-10T14:26:18Z",
                "createdBy": "root",
                "curveName": "none",
                "fullPath": "/Common/f5_api_com.key",
                "generation": 1,
                "keySize": 4096,
                "keyType": "rsa-private",
                "kind": "tm:sys:file:ssl-key:ssl-keystate",
                "lastUpdateTime": "2019-10-10T14:26:18Z",
                "mode": 33184,
                "name": "f5_api_com.key",
                "partition": "Common",
                "passphrase": "$M$Sq$WDufoLJX0gFBR2gQY5mLgBcDQmu5qnxG02puqLps1OjbKMhjZ9E6mh5P3mA09EOLHUIyUAfPV9dl+iv5kF05lCEBc3qUTrIiG4rKiJPWgIw=",
                "revision": 1,
                "securityType": "password",
                "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~f5_api_com.key?ver=14.1.2.1",
                "size": 3306,
                "sourcePath": "file:///config/ssl/ssl.key/f5_api_com.key",
                "updatedBy": "root",
            },
        ],
        "kind": "tm:sys:file:ssl-key:ssl-keycollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-key?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysFileSslkey(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysFileSslkey(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
