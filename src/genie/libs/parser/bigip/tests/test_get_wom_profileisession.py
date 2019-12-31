# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_wom_profileisession
from genie.libs.parser.bigip.get_wom_profileisession import WomProfileIsession

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/wom/profile/isession'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:wom:profile:isession:isessioncollectionstate",
            "selfLink": "https://localhost/mgmt/tm/wom/profile/isession?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:wom:profile:isession:isessionstate",
                    "name": "isession",
                    "partition": "Common",
                    "fullPath": "/Common/isession",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession?ver=14.1.2.1",
                    "adaptiveCompression": "enabled",
                    "compression": "enabled",
                    "compressionCodecs": ["deflate", "lzo", "bzip2"],
                    "dataEncryption": "disabled",
                    "deduplication": "enabled",
                    "deflateCompressionLevel": 1,
                    "mode": "enabled",
                    "portTransparency": "enabled",
                    "reuseConnection": "enabled",
                    "targetVirtual": "virtual-match-all",
                },
                {
                    "kind": "tm:wom:profile:isession:isessionstate",
                    "name": "isession-encrypt",
                    "partition": "Common",
                    "fullPath": "/Common/isession-encrypt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession-encrypt?ver=14.1.2.1",
                    "adaptiveCompression": "enabled",
                    "compression": "enabled",
                    "compressionCodecs": ["deflate", "lzo", "bzip2"],
                    "dataEncryption": "enabled",
                    "deduplication": "enabled",
                    "defaultsFrom": "/Common/isession",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession?ver=14.1.2.1"
                    },
                    "deflateCompressionLevel": 1,
                    "mode": "enabled",
                    "portTransparency": "enabled",
                    "reuseConnection": "enabled",
                    "targetVirtual": "virtual-match-all",
                },
                {
                    "kind": "tm:wom:profile:isession:isessionstate",
                    "name": "isession-mapi",
                    "partition": "Common",
                    "fullPath": "/Common/isession-mapi",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession-mapi?ver=14.1.2.1",
                    "adaptiveCompression": "enabled",
                    "compression": "enabled",
                    "compressionCodecs": ["deflate", "lzo", "bzip2"],
                    "dataEncryption": "disabled",
                    "deduplication": "enabled",
                    "defaultsFrom": "/Common/isession",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession?ver=14.1.2.1"
                    },
                    "deflateCompressionLevel": 1,
                    "mode": "enabled",
                    "portTransparency": "enabled",
                    "reuseConnection": "enabled",
                    "targetVirtual": "virtual-match-all",
                },
                {
                    "kind": "tm:wom:profile:isession:isessionstate",
                    "name": "isession-softwoc",
                    "partition": "Common",
                    "fullPath": "/Common/isession-softwoc",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession-softwoc?ver=14.1.2.1",
                    "adaptiveCompression": "enabled",
                    "compression": "enabled",
                    "compressionCodecs": ["deflate", "lzo", "bzip2"],
                    "dataEncryption": "disabled",
                    "deduplication": "disabled",
                    "defaultsFrom": "/Common/isession",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession?ver=14.1.2.1"
                    },
                    "deflateCompressionLevel": 1,
                    "mode": "enabled",
                    "portTransparency": "enabled",
                    "reuseConnection": "enabled",
                    "targetVirtual": "virtual-match-all",
                },
            ],
        }


class test_get_wom_profileisession(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "adaptiveCompression": "enabled",
                "compression": "enabled",
                "compressionCodecs": ["deflate", "lzo", "bzip2"],
                "dataEncryption": "disabled",
                "deduplication": "enabled",
                "deflateCompressionLevel": 1,
                "fullPath": "/Common/isession",
                "generation": 1,
                "kind": "tm:wom:profile:isession:isessionstate",
                "mode": "enabled",
                "name": "isession",
                "partition": "Common",
                "portTransparency": "enabled",
                "reuseConnection": "enabled",
                "selfLink": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession?ver=14.1.2.1",
                "targetVirtual": "virtual-match-all",
            },
            {
                "adaptiveCompression": "enabled",
                "compression": "enabled",
                "compressionCodecs": ["deflate", "lzo", "bzip2"],
                "dataEncryption": "enabled",
                "deduplication": "enabled",
                "defaultsFrom": "/Common/isession",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession?ver=14.1.2.1"
                },
                "deflateCompressionLevel": 1,
                "fullPath": "/Common/isession-encrypt",
                "generation": 1,
                "kind": "tm:wom:profile:isession:isessionstate",
                "mode": "enabled",
                "name": "isession-encrypt",
                "partition": "Common",
                "portTransparency": "enabled",
                "reuseConnection": "enabled",
                "selfLink": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession-encrypt?ver=14.1.2.1",
                "targetVirtual": "virtual-match-all",
            },
            {
                "adaptiveCompression": "enabled",
                "compression": "enabled",
                "compressionCodecs": ["deflate", "lzo", "bzip2"],
                "dataEncryption": "disabled",
                "deduplication": "enabled",
                "defaultsFrom": "/Common/isession",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession?ver=14.1.2.1"
                },
                "deflateCompressionLevel": 1,
                "fullPath": "/Common/isession-mapi",
                "generation": 1,
                "kind": "tm:wom:profile:isession:isessionstate",
                "mode": "enabled",
                "name": "isession-mapi",
                "partition": "Common",
                "portTransparency": "enabled",
                "reuseConnection": "enabled",
                "selfLink": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession-mapi?ver=14.1.2.1",
                "targetVirtual": "virtual-match-all",
            },
            {
                "adaptiveCompression": "enabled",
                "compression": "enabled",
                "compressionCodecs": ["deflate", "lzo", "bzip2"],
                "dataEncryption": "disabled",
                "deduplication": "disabled",
                "defaultsFrom": "/Common/isession",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession?ver=14.1.2.1"
                },
                "deflateCompressionLevel": 1,
                "fullPath": "/Common/isession-softwoc",
                "generation": 1,
                "kind": "tm:wom:profile:isession:isessionstate",
                "mode": "enabled",
                "name": "isession-softwoc",
                "partition": "Common",
                "portTransparency": "enabled",
                "reuseConnection": "enabled",
                "selfLink": "https://localhost/mgmt/tm/wom/profile/isession/~Common~isession-softwoc?ver=14.1.2.1",
                "targetVirtual": "virtual-match-all",
            },
        ],
        "kind": "tm:wom:profile:isession:isessioncollectionstate",
        "selfLink": "https://localhost/mgmt/tm/wom/profile/isession?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = WomProfileIsession(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = WomProfileIsession(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
