# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_filessl_cert
from genie.libs.parser.bigip.get_sys_filessl_cert import SysFileSslcert

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/file/ssl-cert'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:file:ssl-cert:ssl-certcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-cert?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:file:ssl-cert:ssl-certstate",
                    "name": "ca-bundle.crt",
                    "partition": "Common",
                    "fullPath": "/Common/ca-bundle.crt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt?ver=14.1.2.1",
                    "certificateKeyCurveName": "none",
                    "certificateKeySize": 2048,
                    "checksum": "SHA1:4735518:f474e6b474ec07cbb8910550a00e1593e6eaca8f",
                    "createTime": "2019-09-17T22:41:04Z",
                    "createdBy": "root",
                    "expirationDate": 1893455999,
                    "expirationString": "Dec 31 23:59:59 2029 GMT",
                    "fingerprint": "SHA256/B5:BD:2C:B7:9C:BD:19:07:29:8D:6B:DF:48:42:E5:16:D8:C7:8F:A6:FC:96:D2:5F:71:AF:81:4E:16:CC:24:5E",
                    "isBundle": "true",
                    "issuer": "CN=Starfield Services Root Certificate Authority,OU=http://certificates.starfieldtech.com/repository/,O=Starfield Technologies, Inc.,L=Scottsdale,ST=Arizona,C=US",
                    "keyType": "rsa-public",
                    "lastUpdateTime": "2019-09-17T22:41:04Z",
                    "mode": 33188,
                    "revision": 1,
                    "size": 4735518,
                    "subject": "CN=Starfield Services Root Certificate Authority,OU=http://certificates.starfieldtech.com/repository/,O=Starfield Technologies, Inc.,L=Scottsdale,ST=Arizona,C=US",
                    "systemPath": "/config/ssl/ssl.crt/ca-bundle.crt",
                    "updatedBy": "root",
                    "version": 3,
                    "bundleCertificatesReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt/bundle-certificates?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                    "certValidatorsReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt/cert-validators?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:file:ssl-cert:ssl-certstate",
                    "name": "default.crt",
                    "partition": "Common",
                    "fullPath": "/Common/default.crt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt?ver=14.1.2.1",
                    "certificateKeyCurveName": "none",
                    "certificateKeySize": 2048,
                    "checksum": "SHA1:1338:87de153e5d0307e7b5d9e58831302ea4e6789ef4",
                    "createTime": "2019-10-10T14:15:29Z",
                    "createdBy": "root",
                    "email": "root@localhost.localdomain",
                    "expirationDate": 1886076929,
                    "expirationString": "Oct  7 14:15:29 2029 GMT",
                    "fingerprint": "SHA256/3A:F7:3E:DF:9C:A2:FF:9A:62:4D:44:85:29:5D:2E:53:98:E1:8D:66:34:B4:8B:90:F5:B4:D8:E3:D3:7C:EE:DE",
                    "isBundle": "false",
                    "issuer": "emailAddress=root@localhost.localdomain,CN=localhost.localdomain,OU=IT,O=MyCompany,L=Seattle,ST=WA,C=US",
                    "keyType": "rsa-public",
                    "lastUpdateTime": "2019-10-10T14:15:29Z",
                    "mode": 33188,
                    "revision": 1,
                    "serialNumber": "308384129",
                    "size": 1338,
                    "subject": "emailAddress=root@localhost.localdomain,CN=localhost.localdomain,OU=IT,O=MyCompany,L=Seattle,ST=WA,C=US",
                    "systemPath": "/config/ssl/ssl.crt/default.crt",
                    "updatedBy": "root",
                    "version": 3,
                    "bundleCertificatesReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt/bundle-certificates?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                    "certValidatorsReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt/cert-validators?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:file:ssl-cert:ssl-certstate",
                    "name": "f5-ca-bundle.crt",
                    "partition": "Common",
                    "fullPath": "/Common/f5-ca-bundle.crt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-ca-bundle.crt?ver=14.1.2.1",
                    "certificateKeyCurveName": "none",
                    "certificateKeySize": 2048,
                    "checksum": "SHA1:2151:0b3091b2d597dfb584d18b92d3f0b082d5913b34",
                    "createTime": "2019-09-17T21:07:53Z",
                    "createdBy": "root",
                    "expirationDate": 1922896554,
                    "expirationString": "Dec  7 17:55:54 2030 GMT",
                    "fingerprint": "SHA256/43:DF:57:74:B0:3E:7F:EF:5F:E4:0D:93:1A:7B:ED:F1:BB:2E:6B:42:73:8C:4E:6D:38:41:10:3D:3A:A7:F3:39",
                    "isBundle": "false",
                    "issuer": "CN=Entrust Root Certification Authority - G2,OU=(c) 2009 Entrust, Inc. - for authorized use only,OU=See www.entrust.net/legal-terms,O=Entrust, Inc.,C=US",
                    "keyType": "rsa-public",
                    "lastUpdateTime": "2019-09-17T21:07:53Z",
                    "mode": 33188,
                    "revision": 1,
                    "serialNumber": "1246989352",
                    "size": 2151,
                    "subject": "CN=Entrust Root Certification Authority - G2,OU=(c) 2009 Entrust, Inc. - for authorized use only,OU=See www.entrust.net/legal-terms,O=Entrust, Inc.,C=US",
                    "systemPath": "/config/ssl/ssl.crt/f5-ca-bundle.crt",
                    "updatedBy": "root",
                    "version": 3,
                    "bundleCertificatesReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-ca-bundle.crt/bundle-certificates?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                    "certValidatorsReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-ca-bundle.crt/cert-validators?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:file:ssl-cert:ssl-certstate",
                    "name": "f5-irule.crt",
                    "partition": "Common",
                    "fullPath": "/Common/f5-irule.crt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-irule.crt?ver=14.1.2.1",
                    "certificateKeyCurveName": "none",
                    "certificateKeySize": 2048,
                    "checksum": "SHA1:1728:0e41ec7bddceae530c3c2c8ffa5e7262947e3a0e",
                    "createTime": "2019-09-17T21:07:53Z",
                    "createdBy": "root",
                    "email": "support@f5.com",
                    "expirationDate": 1815944413,
                    "expirationString": "Jul 18 21:00:13 2027 GMT",
                    "fingerprint": "SHA256/AC:08:EA:3F:0E:AC:C8:DD:A2:2A:7D:AA:73:02:86:1E:1F:38:51:4A:80:D3:E6:AE:4E:6B:01:0C:68:FF:18:D2",
                    "isBundle": "false",
                    "issuer": "emailAddress=support@f5.com,CN=support.f5.com,OU=Product Development,O=F5 Networks,L=Seattle,ST=Washington,C=US",
                    "keyType": "rsa-public",
                    "lastUpdateTime": "2019-09-17T21:07:53Z",
                    "mode": 33188,
                    "revision": 1,
                    "serialNumber": "87:ae:02:f9:18:f9:4a:11",
                    "size": 1728,
                    "subject": "emailAddress=support@f5.com,CN=support.f5.com,OU=Product Development,O=F5 Networks,L=Seattle,ST=Washington,C=US",
                    "systemPath": "/config/ssl/ssl.crt/f5-irule.crt",
                    "updatedBy": "root",
                    "version": 3,
                    "bundleCertificatesReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-irule.crt/bundle-certificates?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                    "certValidatorsReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-irule.crt/cert-validators?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
            ],
        }


class test_get_sys_filessl_cert(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "bundleCertificatesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt/bundle-certificates?ver=14.1.2.1",
                },
                "certValidatorsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt/cert-validators?ver=14.1.2.1",
                },
                "certificateKeyCurveName": "none",
                "certificateKeySize": 2048,
                "checksum": "SHA1:4735518:f474e6b474ec07cbb8910550a00e1593e6eaca8f",
                "createTime": "2019-09-17T22:41:04Z",
                "createdBy": "root",
                "expirationDate": 1893455999,
                "expirationString": "Dec 31 23:59:59 2029 GMT",
                "fingerprint": "SHA256/B5:BD:2C:B7:9C:BD:19:07:29:8D:6B:DF:48:42:E5:16:D8:C7:8F:A6:FC:96:D2:5F:71:AF:81:4E:16:CC:24:5E",
                "fullPath": "/Common/ca-bundle.crt",
                "generation": 1,
                "isBundle": "true",
                "issuer": "CN=Starfield Services Root Certificate "
                "Authority,OU=http://certificates.starfieldtech.com/repository/,O=Starfield "
                "Technologies, Inc.,L=Scottsdale,ST=Arizona,C=US",
                "keyType": "rsa-public",
                "kind": "tm:sys:file:ssl-cert:ssl-certstate",
                "lastUpdateTime": "2019-09-17T22:41:04Z",
                "mode": 33188,
                "name": "ca-bundle.crt",
                "partition": "Common",
                "revision": 1,
                "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt?ver=14.1.2.1",
                "size": 4735518,
                "subject": "CN=Starfield Services Root Certificate "
                "Authority,OU=http://certificates.starfieldtech.com/repository/,O=Starfield "
                "Technologies, Inc.,L=Scottsdale,ST=Arizona,C=US",
                "systemPath": "/config/ssl/ssl.crt/ca-bundle.crt",
                "updatedBy": "root",
                "version": 3,
            },
            {
                "bundleCertificatesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt/bundle-certificates?ver=14.1.2.1",
                },
                "certValidatorsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt/cert-validators?ver=14.1.2.1",
                },
                "certificateKeyCurveName": "none",
                "certificateKeySize": 2048,
                "checksum": "SHA1:1338:87de153e5d0307e7b5d9e58831302ea4e6789ef4",
                "createTime": "2019-10-10T14:15:29Z",
                "createdBy": "root",
                "email": "root@localhost.localdomain",
                "expirationDate": 1886076929,
                "expirationString": "Oct  7 14:15:29 2029 GMT",
                "fingerprint": "SHA256/3A:F7:3E:DF:9C:A2:FF:9A:62:4D:44:85:29:5D:2E:53:98:E1:8D:66:34:B4:8B:90:F5:B4:D8:E3:D3:7C:EE:DE",
                "fullPath": "/Common/default.crt",
                "generation": 1,
                "isBundle": "false",
                "issuer": "emailAddress=root@localhost.localdomain,CN=localhost.localdomain,OU=IT,O=MyCompany,L=Seattle,ST=WA,C=US",
                "keyType": "rsa-public",
                "kind": "tm:sys:file:ssl-cert:ssl-certstate",
                "lastUpdateTime": "2019-10-10T14:15:29Z",
                "mode": 33188,
                "name": "default.crt",
                "partition": "Common",
                "revision": 1,
                "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt?ver=14.1.2.1",
                "serialNumber": "308384129",
                "size": 1338,
                "subject": "emailAddress=root@localhost.localdomain,CN=localhost.localdomain,OU=IT,O=MyCompany,L=Seattle,ST=WA,C=US",
                "systemPath": "/config/ssl/ssl.crt/default.crt",
                "updatedBy": "root",
                "version": 3,
            },
            {
                "bundleCertificatesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-ca-bundle.crt/bundle-certificates?ver=14.1.2.1",
                },
                "certValidatorsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-ca-bundle.crt/cert-validators?ver=14.1.2.1",
                },
                "certificateKeyCurveName": "none",
                "certificateKeySize": 2048,
                "checksum": "SHA1:2151:0b3091b2d597dfb584d18b92d3f0b082d5913b34",
                "createTime": "2019-09-17T21:07:53Z",
                "createdBy": "root",
                "expirationDate": 1922896554,
                "expirationString": "Dec  7 17:55:54 2030 GMT",
                "fingerprint": "SHA256/43:DF:57:74:B0:3E:7F:EF:5F:E4:0D:93:1A:7B:ED:F1:BB:2E:6B:42:73:8C:4E:6D:38:41:10:3D:3A:A7:F3:39",
                "fullPath": "/Common/f5-ca-bundle.crt",
                "generation": 1,
                "isBundle": "false",
                "issuer": "CN=Entrust Root Certification Authority - G2,OU=(c) "
                "2009 Entrust, Inc. - for authorized use only,OU=See "
                "www.entrust.net/legal-terms,O=Entrust, Inc.,C=US",
                "keyType": "rsa-public",
                "kind": "tm:sys:file:ssl-cert:ssl-certstate",
                "lastUpdateTime": "2019-09-17T21:07:53Z",
                "mode": 33188,
                "name": "f5-ca-bundle.crt",
                "partition": "Common",
                "revision": 1,
                "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-ca-bundle.crt?ver=14.1.2.1",
                "serialNumber": "1246989352",
                "size": 2151,
                "subject": "CN=Entrust Root Certification Authority - G2,OU=(c) "
                "2009 Entrust, Inc. - for authorized use only,OU=See "
                "www.entrust.net/legal-terms,O=Entrust, Inc.,C=US",
                "systemPath": "/config/ssl/ssl.crt/f5-ca-bundle.crt",
                "updatedBy": "root",
                "version": 3,
            },
            {
                "bundleCertificatesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-irule.crt/bundle-certificates?ver=14.1.2.1",
                },
                "certValidatorsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-irule.crt/cert-validators?ver=14.1.2.1",
                },
                "certificateKeyCurveName": "none",
                "certificateKeySize": 2048,
                "checksum": "SHA1:1728:0e41ec7bddceae530c3c2c8ffa5e7262947e3a0e",
                "createTime": "2019-09-17T21:07:53Z",
                "createdBy": "root",
                "email": "support@f5.com",
                "expirationDate": 1815944413,
                "expirationString": "Jul 18 21:00:13 2027 GMT",
                "fingerprint": "SHA256/AC:08:EA:3F:0E:AC:C8:DD:A2:2A:7D:AA:73:02:86:1E:1F:38:51:4A:80:D3:E6:AE:4E:6B:01:0C:68:FF:18:D2",
                "fullPath": "/Common/f5-irule.crt",
                "generation": 1,
                "isBundle": "false",
                "issuer": "emailAddress=support@f5.com,CN=support.f5.com,OU=Product "
                "Development,O=F5 Networks,L=Seattle,ST=Washington,C=US",
                "keyType": "rsa-public",
                "kind": "tm:sys:file:ssl-cert:ssl-certstate",
                "lastUpdateTime": "2019-09-17T21:07:53Z",
                "mode": 33188,
                "name": "f5-irule.crt",
                "partition": "Common",
                "revision": 1,
                "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-irule.crt?ver=14.1.2.1",
                "serialNumber": "87:ae:02:f9:18:f9:4a:11",
                "size": 1728,
                "subject": "emailAddress=support@f5.com,CN=support.f5.com,OU=Product "
                "Development,O=F5 Networks,L=Seattle,ST=Washington,C=US",
                "systemPath": "/config/ssl/ssl.crt/f5-irule.crt",
                "updatedBy": "root",
                "version": 3,
            },
        ],
        "kind": "tm:sys:file:ssl-cert:ssl-certcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-cert?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysFileSslcert(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysFileSslcert(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
