# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cm_key
from genie.libs.parser.bigip.get_cm_key import CmKey

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cm/key'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:cm:key:keycollectionstate",
            "selfLink": "https://localhost/mgmt/tm/cm/key?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:cm:key:keystate",
                    "name": "dtca.key",
                    "partition": "Common",
                    "fullPath": "/Common/dtca.key",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/cm/key/~Common~dtca.key?ver=14.1.2.1",
                    "checksum": "SHA1:1704:96c4de44ab994bbe7ee270d7def01fd1a4563f80",
                    "createTime": "2019-10-10T14:16:21Z",
                    "createdBy": "root",
                    "keySize": 2048,
                    "keyType": "rsa-private",
                    "lastUpdateTime": "2019-10-10T14:16:21Z",
                    "mode": 33184,
                    "revision": 1,
                    "securityType": "normal",
                    "size": 1704,
                    "updatedBy": "root",
                },
                {
                    "kind": "tm:cm:key:keystate",
                    "name": "dtdi.key",
                    "partition": "Common",
                    "fullPath": "/Common/dtdi.key",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/cm/key/~Common~dtdi.key?ver=14.1.2.1",
                    "checksum": "SHA1:1708:9f2a99dc20e2c3e26dd67457e0d3d3253dc387be",
                    "createTime": "2019-10-10T14:16:21Z",
                    "createdBy": "root",
                    "keySize": 2048,
                    "keyType": "rsa-private",
                    "lastUpdateTime": "2019-10-10T14:16:21Z",
                    "mode": 33184,
                    "revision": 1,
                    "securityType": "normal",
                    "size": 1708,
                    "updatedBy": "root",
                },
            ],
        }


class test_get_cm_key(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "checksum": "SHA1:1704:96c4de44ab994bbe7ee270d7def01fd1a4563f80",
                "createTime": "2019-10-10T14:16:21Z",
                "createdBy": "root",
                "fullPath": "/Common/dtca.key",
                "generation": 1,
                "keySize": 2048,
                "keyType": "rsa-private",
                "kind": "tm:cm:key:keystate",
                "lastUpdateTime": "2019-10-10T14:16:21Z",
                "mode": 33184,
                "name": "dtca.key",
                "partition": "Common",
                "revision": 1,
                "securityType": "normal",
                "selfLink": "https://localhost/mgmt/tm/cm/key/~Common~dtca.key?ver=14.1.2.1",
                "size": 1704,
                "updatedBy": "root",
            },
            {
                "checksum": "SHA1:1708:9f2a99dc20e2c3e26dd67457e0d3d3253dc387be",
                "createTime": "2019-10-10T14:16:21Z",
                "createdBy": "root",
                "fullPath": "/Common/dtdi.key",
                "generation": 1,
                "keySize": 2048,
                "keyType": "rsa-private",
                "kind": "tm:cm:key:keystate",
                "lastUpdateTime": "2019-10-10T14:16:21Z",
                "mode": 33184,
                "name": "dtdi.key",
                "partition": "Common",
                "revision": 1,
                "securityType": "normal",
                "selfLink": "https://localhost/mgmt/tm/cm/key/~Common~dtdi.key?ver=14.1.2.1",
                "size": 1708,
                "updatedBy": "root",
            },
        ],
        "kind": "tm:cm:key:keycollectionstate",
        "selfLink": "https://localhost/mgmt/tm/cm/key?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CmKey(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CmKey(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
