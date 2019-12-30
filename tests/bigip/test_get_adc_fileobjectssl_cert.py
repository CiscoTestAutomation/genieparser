# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_adc_fileobjectssl_cert
from genie.libs.parser.bigip.get_adc_fileobjectssl_cert import (
    AdcFileobjectSslcert,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/adc/fileobject/ssl-cert'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [
                {
                    "cachePath": "/config/filestore/files_d/Common_d/certificate_d/:Common:f5-irule.crt_29289_1",
                    "systemPath": "/config/ssl/ssl.crt/f5-irule.crt",
                    "checksum": "SHA1:1728:0e41ec7bddceae530c3c2c8ffa5e7262947e3a0e",
                    "size": 1728,
                    "objectId": 29289,
                    "name": "f5-irule.crt",
                    "fullPath": "/Common/f5-irule.crt",
                    "authPartition": "/Common",
                    "generation": 1,
                    "lastUpdateMicros": 0,
                    "kind": "tm:adc:fileobject:ssl-cert:fileobjectitemstate",
                    "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-cert/~Common~f5-irule.crt",
                },
                {
                    "cachePath": "/config/filestore/files_d/Common_d/certificate_d/:Common:f5-ca-bundle.crt_29291_1",
                    "systemPath": "/config/ssl/ssl.crt/f5-ca-bundle.crt",
                    "checksum": "SHA1:2151:0b3091b2d597dfb584d18b92d3f0b082d5913b34",
                    "size": 2151,
                    "objectId": 29291,
                    "name": "f5-ca-bundle.crt",
                    "fullPath": "/Common/f5-ca-bundle.crt",
                    "authPartition": "/Common",
                    "generation": 1,
                    "lastUpdateMicros": 0,
                    "kind": "tm:adc:fileobject:ssl-cert:fileobjectitemstate",
                    "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-cert/~Common~f5-ca-bundle.crt",
                },
                {
                    "cachePath": "/config/filestore/files_d/Common_d/certificate_d/:Common:default.crt_29293_1",
                    "systemPath": "/config/ssl/ssl.crt/default.crt",
                    "checksum": "SHA1:1338:87de153e5d0307e7b5d9e58831302ea4e6789ef4",
                    "size": 1338,
                    "objectId": 29293,
                    "name": "default.crt",
                    "fullPath": "/Common/default.crt",
                    "authPartition": "/Common",
                    "generation": 1,
                    "lastUpdateMicros": 0,
                    "kind": "tm:adc:fileobject:ssl-cert:fileobjectitemstate",
                    "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-cert/~Common~default.crt",
                },
                {
                    "cachePath": "/config/filestore/files_d/Common_d/certificate_d/:Common:ca-bundle.crt_29295_1",
                    "systemPath": "/config/ssl/ssl.crt/ca-bundle.crt",
                    "checksum": "SHA1:4735518:f474e6b474ec07cbb8910550a00e1593e6eaca8f",
                    "size": 4735518,
                    "objectId": 29295,
                    "name": "ca-bundle.crt",
                    "fullPath": "/Common/ca-bundle.crt",
                    "authPartition": "/Common",
                    "generation": 1,
                    "lastUpdateMicros": 0,
                    "kind": "tm:adc:fileobject:ssl-cert:fileobjectitemstate",
                    "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-cert/~Common~ca-bundle.crt",
                },
            ],
            "generation": 4,
            "lastUpdateMicros": 0,
            "kind": "tm:adc:fileobject:ssl-cert:fileobjectcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-cert",
        }


class test_get_adc_fileobjectssl_cert(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 4,
        "items": [
            {
                "authPartition": "/Common",
                "cachePath": "/config/filestore/files_d/Common_d/certificate_d/:Common:f5-irule.crt_29289_1",
                "checksum": "SHA1:1728:0e41ec7bddceae530c3c2c8ffa5e7262947e3a0e",
                "fullPath": "/Common/f5-irule.crt",
                "generation": 1,
                "kind": "tm:adc:fileobject:ssl-cert:fileobjectitemstate",
                "lastUpdateMicros": 0,
                "name": "f5-irule.crt",
                "objectId": 29289,
                "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-cert/~Common~f5-irule.crt",
                "size": 1728,
                "systemPath": "/config/ssl/ssl.crt/f5-irule.crt",
            },
            {
                "authPartition": "/Common",
                "cachePath": "/config/filestore/files_d/Common_d/certificate_d/:Common:f5-ca-bundle.crt_29291_1",
                "checksum": "SHA1:2151:0b3091b2d597dfb584d18b92d3f0b082d5913b34",
                "fullPath": "/Common/f5-ca-bundle.crt",
                "generation": 1,
                "kind": "tm:adc:fileobject:ssl-cert:fileobjectitemstate",
                "lastUpdateMicros": 0,
                "name": "f5-ca-bundle.crt",
                "objectId": 29291,
                "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-cert/~Common~f5-ca-bundle.crt",
                "size": 2151,
                "systemPath": "/config/ssl/ssl.crt/f5-ca-bundle.crt",
            },
            {
                "authPartition": "/Common",
                "cachePath": "/config/filestore/files_d/Common_d/certificate_d/:Common:default.crt_29293_1",
                "checksum": "SHA1:1338:87de153e5d0307e7b5d9e58831302ea4e6789ef4",
                "fullPath": "/Common/default.crt",
                "generation": 1,
                "kind": "tm:adc:fileobject:ssl-cert:fileobjectitemstate",
                "lastUpdateMicros": 0,
                "name": "default.crt",
                "objectId": 29293,
                "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-cert/~Common~default.crt",
                "size": 1338,
                "systemPath": "/config/ssl/ssl.crt/default.crt",
            },
            {
                "authPartition": "/Common",
                "cachePath": "/config/filestore/files_d/Common_d/certificate_d/:Common:ca-bundle.crt_29295_1",
                "checksum": "SHA1:4735518:f474e6b474ec07cbb8910550a00e1593e6eaca8f",
                "fullPath": "/Common/ca-bundle.crt",
                "generation": 1,
                "kind": "tm:adc:fileobject:ssl-cert:fileobjectitemstate",
                "lastUpdateMicros": 0,
                "name": "ca-bundle.crt",
                "objectId": 29295,
                "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-cert/~Common~ca-bundle.crt",
                "size": 4735518,
                "systemPath": "/config/ssl/ssl.crt/ca-bundle.crt",
            },
        ],
        "kind": "tm:adc:fileobject:ssl-cert:fileobjectcollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-cert",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AdcFileobjectSslcert(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AdcFileobjectSslcert(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
