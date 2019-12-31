# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_cryptocert
from genie.libs.parser.bigip.get_sys_cryptocert import SysCryptoCert

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/crypto/cert'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:crypto:cert:certcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/crypto/cert?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:crypto:cert:certstate",
                    "name": "/Common/ca-bundle.crt",
                    "fullPath": "/Common/ca-bundle.crt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~ca-bundle.crt?ver=14.1.2.1",
                    "apiRawValues": {
                        "certificateKeySize": "2048",
                        "expiration": "Dec 31 23:59:59 2029 GMT",
                        "issuer": "CN=Starfield Services Root Certificate Authority,OU=http://certificates.starfieldtech.com/repository/,O=Starfield Technologies, Inc.,L=Scottsdale,ST=Arizona,C=US",
                        "publicKeyType": "RSA",
                    },
                    "city": "Scottsdale",
                    "commonName": "Starfield Services Root Certificate Authority",
                    "country": "US",
                    "fingerprint": "SHA256/B5:BD:2C:B7:9C:BD:19:07:29:8D:6B:DF:48:42:E5:16:D8:C7:8F:A6:FC:96:D2:5F:71:AF:81:4E:16:CC:24:5E",
                    "organization": "Starfield Technologies, Inc.",
                    "ou": "http://certificates.starfieldtech.com/repository/",
                    "state": "Arizona",
                    "certValidatorsReference": {
                        "link": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~ca-bundle.crt/cert-validators?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:crypto:cert:certstate",
                    "name": "/Common/default.crt",
                    "fullPath": "/Common/default.crt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~default.crt?ver=14.1.2.1",
                    "apiRawValues": {
                        "certificateKeySize": "2048",
                        "expiration": "Oct  7 14:15:29 2029 GMT",
                        "issuer": "emailAddress=root@localhost.localdomain,CN=localhost.localdomain,OU=IT,O=MyCompany,L=Seattle,ST=WA,C=US",
                        "publicKeyType": "RSA",
                    },
                    "city": "Seattle",
                    "commonName": "localhost.localdomain",
                    "country": "US",
                    "emailAddress": "root@localhost.localdomain",
                    "fingerprint": "SHA256/3A:F7:3E:DF:9C:A2:FF:9A:62:4D:44:85:29:5D:2E:53:98:E1:8D:66:34:B4:8B:90:F5:B4:D8:E3:D3:7C:EE:DE",
                    "organization": "MyCompany",
                    "ou": "IT",
                    "state": "WA",
                    "certValidatorsReference": {
                        "link": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~default.crt/cert-validators?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:crypto:cert:certstate",
                    "name": "/Common/f5-ca-bundle.crt",
                    "fullPath": "/Common/f5-ca-bundle.crt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~f5-ca-bundle.crt?ver=14.1.2.1",
                    "apiRawValues": {
                        "certificateKeySize": "2048",
                        "expiration": "Dec  7 17:55:54 2030 GMT",
                        "issuer": "CN=Entrust Root Certification Authority - G2,OU=(c) 2009 Entrust, Inc. - for authorized use only,OU=See www.entrust.net/legal-terms,O=Entrust, Inc.,C=US",
                        "publicKeyType": "RSA",
                    },
                    "commonName": "Entrust Root Certification Authority - G2",
                    "country": "US",
                    "fingerprint": "SHA256/43:DF:57:74:B0:3E:7F:EF:5F:E4:0D:93:1A:7B:ED:F1:BB:2E:6B:42:73:8C:4E:6D:38:41:10:3D:3A:A7:F3:39",
                    "organization": "Entrust, Inc.",
                    "ou": "See www.entrust.net/legal-terms",
                    "certValidatorsReference": {
                        "link": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~f5-ca-bundle.crt/cert-validators?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:sys:crypto:cert:certstate",
                    "name": "/Common/f5-irule.crt",
                    "fullPath": "/Common/f5-irule.crt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~f5-irule.crt?ver=14.1.2.1",
                    "apiRawValues": {
                        "certificateKeySize": "2048",
                        "expiration": "Jul 18 21:00:13 2027 GMT",
                        "issuer": "emailAddress=support@f5.com,CN=support.f5.com,OU=Product Development,O=F5 Networks,L=Seattle,ST=Washington,C=US",
                        "publicKeyType": "RSA",
                    },
                    "city": "Seattle",
                    "commonName": "support.f5.com",
                    "country": "US",
                    "emailAddress": "support@f5.com",
                    "fingerprint": "SHA256/AC:08:EA:3F:0E:AC:C8:DD:A2:2A:7D:AA:73:02:86:1E:1F:38:51:4A:80:D3:E6:AE:4E:6B:01:0C:68:FF:18:D2",
                    "organization": "F5 Networks",
                    "ou": "Product Development",
                    "state": "Washington",
                    "certValidatorsReference": {
                        "link": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~f5-irule.crt/cert-validators?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
            ],
        }


class test_get_sys_cryptocert(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "apiRawValues": {
                    "certificateKeySize": "2048",
                    "expiration": "Dec 31 23:59:59 2029 GMT",
                    "issuer": "CN=Starfield Services Root Certificate "
                    "Authority,OU=http://certificates.starfieldtech.com/repository/,O=Starfield "
                    "Technologies, "
                    "Inc.,L=Scottsdale,ST=Arizona,C=US",
                    "publicKeyType": "RSA",
                },
                "certValidatorsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~ca-bundle.crt/cert-validators?ver=14.1.2.1",
                },
                "city": "Scottsdale",
                "commonName": "Starfield Services Root Certificate Authority",
                "country": "US",
                "fingerprint": "SHA256/B5:BD:2C:B7:9C:BD:19:07:29:8D:6B:DF:48:42:E5:16:D8:C7:8F:A6:FC:96:D2:5F:71:AF:81:4E:16:CC:24:5E",
                "fullPath": "/Common/ca-bundle.crt",
                "generation": 1,
                "kind": "tm:sys:crypto:cert:certstate",
                "name": "/Common/ca-bundle.crt",
                "organization": "Starfield Technologies, Inc.",
                "ou": "http://certificates.starfieldtech.com/repository/",
                "selfLink": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~ca-bundle.crt?ver=14.1.2.1",
                "state": "Arizona",
            },
            {
                "apiRawValues": {
                    "certificateKeySize": "2048",
                    "expiration": "Oct  7 14:15:29 2029 GMT",
                    "issuer": "emailAddress=root@localhost.localdomain,CN=localhost.localdomain,OU=IT,O=MyCompany,L=Seattle,ST=WA,C=US",
                    "publicKeyType": "RSA",
                },
                "certValidatorsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~default.crt/cert-validators?ver=14.1.2.1",
                },
                "city": "Seattle",
                "commonName": "localhost.localdomain",
                "country": "US",
                "emailAddress": "root@localhost.localdomain",
                "fingerprint": "SHA256/3A:F7:3E:DF:9C:A2:FF:9A:62:4D:44:85:29:5D:2E:53:98:E1:8D:66:34:B4:8B:90:F5:B4:D8:E3:D3:7C:EE:DE",
                "fullPath": "/Common/default.crt",
                "generation": 1,
                "kind": "tm:sys:crypto:cert:certstate",
                "name": "/Common/default.crt",
                "organization": "MyCompany",
                "ou": "IT",
                "selfLink": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~default.crt?ver=14.1.2.1",
                "state": "WA",
            },
            {
                "apiRawValues": {
                    "certificateKeySize": "2048",
                    "expiration": "Dec  7 17:55:54 2030 GMT",
                    "issuer": "CN=Entrust Root Certification "
                    "Authority - G2,OU=(c) 2009 Entrust, "
                    "Inc. - for authorized use only,OU=See "
                    "www.entrust.net/legal-terms,O=Entrust, "
                    "Inc.,C=US",
                    "publicKeyType": "RSA",
                },
                "certValidatorsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~f5-ca-bundle.crt/cert-validators?ver=14.1.2.1",
                },
                "commonName": "Entrust Root Certification Authority - G2",
                "country": "US",
                "fingerprint": "SHA256/43:DF:57:74:B0:3E:7F:EF:5F:E4:0D:93:1A:7B:ED:F1:BB:2E:6B:42:73:8C:4E:6D:38:41:10:3D:3A:A7:F3:39",
                "fullPath": "/Common/f5-ca-bundle.crt",
                "generation": 1,
                "kind": "tm:sys:crypto:cert:certstate",
                "name": "/Common/f5-ca-bundle.crt",
                "organization": "Entrust, Inc.",
                "ou": "See www.entrust.net/legal-terms",
                "selfLink": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~f5-ca-bundle.crt?ver=14.1.2.1",
            },
            {
                "apiRawValues": {
                    "certificateKeySize": "2048",
                    "expiration": "Jul 18 21:00:13 2027 GMT",
                    "issuer": "emailAddress=support@f5.com,CN=support.f5.com,OU=Product "
                    "Development,O=F5 "
                    "Networks,L=Seattle,ST=Washington,C=US",
                    "publicKeyType": "RSA",
                },
                "certValidatorsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~f5-irule.crt/cert-validators?ver=14.1.2.1",
                },
                "city": "Seattle",
                "commonName": "support.f5.com",
                "country": "US",
                "emailAddress": "support@f5.com",
                "fingerprint": "SHA256/AC:08:EA:3F:0E:AC:C8:DD:A2:2A:7D:AA:73:02:86:1E:1F:38:51:4A:80:D3:E6:AE:4E:6B:01:0C:68:FF:18:D2",
                "fullPath": "/Common/f5-irule.crt",
                "generation": 1,
                "kind": "tm:sys:crypto:cert:certstate",
                "name": "/Common/f5-irule.crt",
                "organization": "F5 Networks",
                "ou": "Product Development",
                "selfLink": "https://localhost/mgmt/tm/sys/crypto/cert/~Common~f5-irule.crt?ver=14.1.2.1",
                "state": "Washington",
            },
        ],
        "kind": "tm:sys:crypto:cert:certcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/crypto/cert?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysCryptoCert(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysCryptoCert(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
