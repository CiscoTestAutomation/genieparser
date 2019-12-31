# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cm_cert
from genie.libs.parser.bigip.get_cm_cert import CmCert

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cm/cert'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:cm:cert:certcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/cm/cert?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:cm:cert:certstate",
                    "name": "dtca-bundle.crt",
                    "partition": "Common",
                    "fullPath": "/Common/dtca-bundle.crt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/cm/cert/~Common~dtca-bundle.crt?ver=14.1.2.1",
                    "certificateKeySize": 2048,
                    "checksum": "SHA1:1289:b7a62f6a7b114163e252c9097b51accd24fd3fa4",
                    "createTime": "2019-10-10T14:16:21Z",
                    "createdBy": "root",
                    "expirationDate": 1886076981,
                    "expirationString": "Oct  7 14:16:21 2029 GMT",
                    "isBundle": "false",
                    "issuer": "CN=21d56e4b-1d05-4764-8d9f000c29350dbd",
                    "keyType": "rsa-public",
                    "lastUpdateTime": "2019-10-10T14:16:21Z",
                    "mode": 33188,
                    "revision": 1,
                    "serialNumber": "630505",
                    "size": 1289,
                    "subject": "CN=21d56e4b-1d05-4764-8d9f000c29350dbd",
                    "updatedBy": "root",
                    "version": 3,
                },
                {
                    "kind": "tm:cm:cert:certstate",
                    "name": "dtca.crt",
                    "partition": "Common",
                    "fullPath": "/Common/dtca.crt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/cm/cert/~Common~dtca.crt?ver=14.1.2.1",
                    "certificateKeySize": 2048,
                    "checksum": "SHA1:1289:b7a62f6a7b114163e252c9097b51accd24fd3fa4",
                    "createTime": "2019-10-10T14:16:21Z",
                    "createdBy": "root",
                    "expirationDate": 1886076981,
                    "expirationString": "Oct  7 14:16:21 2029 GMT",
                    "isBundle": "false",
                    "issuer": "CN=21d56e4b-1d05-4764-8d9f000c29350dbd",
                    "keyType": "rsa-public",
                    "lastUpdateTime": "2019-10-10T14:16:21Z",
                    "mode": 33188,
                    "revision": 1,
                    "serialNumber": "630505",
                    "size": 1289,
                    "subject": "CN=21d56e4b-1d05-4764-8d9f000c29350dbd",
                    "updatedBy": "root",
                    "version": 3,
                },
                {
                    "kind": "tm:cm:cert:certstate",
                    "name": "dtdi.crt",
                    "partition": "Common",
                    "fullPath": "/Common/dtdi.crt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/cm/cert/~Common~dtdi.crt?ver=14.1.2.1",
                    "certificateKeySize": 2048,
                    "checksum": "SHA1:1220:2216148fef3f572e55bd98f4b20d051a310c5092",
                    "createTime": "2019-10-10T14:16:21Z",
                    "createdBy": "root",
                    "expirationDate": 1886076981,
                    "expirationString": "Oct  7 14:16:21 2029 GMT",
                    "isBundle": "false",
                    "issuer": "CN=21d56e4b-1d05-4764-8d9f000c29350dbd",
                    "keyType": "rsa-public",
                    "lastUpdateTime": "2019-10-10T14:16:21Z",
                    "mode": 33188,
                    "revision": 1,
                    "serialNumber": "709406",
                    "size": 1220,
                    "subject": "CN=bigip1",
                    "updatedBy": "root",
                    "version": 3,
                },
            ],
        }


class test_get_cm_cert(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "certificateKeySize": 2048,
                "checksum": "SHA1:1289:b7a62f6a7b114163e252c9097b51accd24fd3fa4",
                "createTime": "2019-10-10T14:16:21Z",
                "createdBy": "root",
                "expirationDate": 1886076981,
                "expirationString": "Oct  7 14:16:21 2029 GMT",
                "fullPath": "/Common/dtca-bundle.crt",
                "generation": 1,
                "isBundle": "false",
                "issuer": "CN=21d56e4b-1d05-4764-8d9f000c29350dbd",
                "keyType": "rsa-public",
                "kind": "tm:cm:cert:certstate",
                "lastUpdateTime": "2019-10-10T14:16:21Z",
                "mode": 33188,
                "name": "dtca-bundle.crt",
                "partition": "Common",
                "revision": 1,
                "selfLink": "https://localhost/mgmt/tm/cm/cert/~Common~dtca-bundle.crt?ver=14.1.2.1",
                "serialNumber": "630505",
                "size": 1289,
                "subject": "CN=21d56e4b-1d05-4764-8d9f000c29350dbd",
                "updatedBy": "root",
                "version": 3,
            },
            {
                "certificateKeySize": 2048,
                "checksum": "SHA1:1289:b7a62f6a7b114163e252c9097b51accd24fd3fa4",
                "createTime": "2019-10-10T14:16:21Z",
                "createdBy": "root",
                "expirationDate": 1886076981,
                "expirationString": "Oct  7 14:16:21 2029 GMT",
                "fullPath": "/Common/dtca.crt",
                "generation": 1,
                "isBundle": "false",
                "issuer": "CN=21d56e4b-1d05-4764-8d9f000c29350dbd",
                "keyType": "rsa-public",
                "kind": "tm:cm:cert:certstate",
                "lastUpdateTime": "2019-10-10T14:16:21Z",
                "mode": 33188,
                "name": "dtca.crt",
                "partition": "Common",
                "revision": 1,
                "selfLink": "https://localhost/mgmt/tm/cm/cert/~Common~dtca.crt?ver=14.1.2.1",
                "serialNumber": "630505",
                "size": 1289,
                "subject": "CN=21d56e4b-1d05-4764-8d9f000c29350dbd",
                "updatedBy": "root",
                "version": 3,
            },
            {
                "certificateKeySize": 2048,
                "checksum": "SHA1:1220:2216148fef3f572e55bd98f4b20d051a310c5092",
                "createTime": "2019-10-10T14:16:21Z",
                "createdBy": "root",
                "expirationDate": 1886076981,
                "expirationString": "Oct  7 14:16:21 2029 GMT",
                "fullPath": "/Common/dtdi.crt",
                "generation": 1,
                "isBundle": "false",
                "issuer": "CN=21d56e4b-1d05-4764-8d9f000c29350dbd",
                "keyType": "rsa-public",
                "kind": "tm:cm:cert:certstate",
                "lastUpdateTime": "2019-10-10T14:16:21Z",
                "mode": 33188,
                "name": "dtdi.crt",
                "partition": "Common",
                "revision": 1,
                "selfLink": "https://localhost/mgmt/tm/cm/cert/~Common~dtdi.crt?ver=14.1.2.1",
                "serialNumber": "709406",
                "size": 1220,
                "subject": "CN=bigip1",
                "updatedBy": "root",
                "version": 3,
            },
        ],
        "kind": "tm:cm:cert:certcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/cm/cert?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CmCert(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CmCert(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
