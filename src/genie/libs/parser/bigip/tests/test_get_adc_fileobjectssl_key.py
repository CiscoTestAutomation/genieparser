# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_adc_fileobjectssl_key
from genie.libs.parser.bigip.get_adc_fileobjectssl_key import (
    AdcFileobjectSslkey,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/adc/fileobject/ssl-key'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [
                {
                    "cachePath": "/config/filestore/files_d/Common_d/certificate_key_d/:Common:default.key_29297_1",
                    "systemPath": "/config/ssl/ssl.key/default.key",
                    "checksum": "SHA1:1704:962754799ae957f6fd37341f86d50e42af0c6bd2",
                    "size": 1704,
                    "objectId": 29297,
                    "name": "default.key",
                    "fullPath": "/Common/default.key",
                    "authPartition": "/Common",
                    "generation": 1,
                    "lastUpdateMicros": 0,
                    "kind": "tm:adc:fileobject:ssl-key:fileobjectitemstate",
                    "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-key/~Common~default.key",
                },
                {
                    "cachePath": "/config/filestore/files_d/Common_d/certificate_key_d/:Common:f5_api_com.key_110432_1",
                    "systemPath": "",
                    "checksum": "SHA1:3306:2ed85f77768f0b80e1c2a3b34cb69db26c4d0c2e",
                    "size": 3306,
                    "objectId": 30570,
                    "name": "f5_api_com.key",
                    "fullPath": "/Common/f5_api_com.key",
                    "authPartition": "/Common",
                    "generation": 1,
                    "lastUpdateMicros": 0,
                    "kind": "tm:adc:fileobject:ssl-key:fileobjectitemstate",
                    "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-key/~Common~f5_api_com.key",
                },
            ],
            "generation": 2,
            "lastUpdateMicros": 0,
            "kind": "tm:adc:fileobject:ssl-key:fileobjectcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-key",
        }


class test_get_adc_fileobjectssl_key(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 2,
        "items": [
            {
                "authPartition": "/Common",
                "cachePath": "/config/filestore/files_d/Common_d/certificate_key_d/:Common:default.key_29297_1",
                "checksum": "SHA1:1704:962754799ae957f6fd37341f86d50e42af0c6bd2",
                "fullPath": "/Common/default.key",
                "generation": 1,
                "kind": "tm:adc:fileobject:ssl-key:fileobjectitemstate",
                "lastUpdateMicros": 0,
                "name": "default.key",
                "objectId": 29297,
                "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-key/~Common~default.key",
                "size": 1704,
                "systemPath": "/config/ssl/ssl.key/default.key",
            },
            {
                "authPartition": "/Common",
                "cachePath": "/config/filestore/files_d/Common_d/certificate_key_d/:Common:f5_api_com.key_110432_1",
                "checksum": "SHA1:3306:2ed85f77768f0b80e1c2a3b34cb69db26c4d0c2e",
                "fullPath": "/Common/f5_api_com.key",
                "generation": 1,
                "kind": "tm:adc:fileobject:ssl-key:fileobjectitemstate",
                "lastUpdateMicros": 0,
                "name": "f5_api_com.key",
                "objectId": 30570,
                "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-key/~Common~f5_api_com.key",
                "size": 3306,
                "systemPath": "",
            },
        ],
        "kind": "tm:adc:fileobject:ssl-key:fileobjectcollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/adc/fileobject/ssl-key",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AdcFileobjectSslkey(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AdcFileobjectSslkey(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
