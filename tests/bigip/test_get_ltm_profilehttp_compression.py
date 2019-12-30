# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilehttp_compression
from genie.libs.parser.bigip.get_ltm_profilehttp_compression import (
    LtmProfileHttpcompression,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/http-compression'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:http-compression:http-compressioncollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/http-compression?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:http-compression:http-compressionstate",
                    "name": "httpcompression",
                    "partition": "Common",
                    "fullPath": "/Common/httpcompression",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/http-compression/~Common~httpcompression?ver=14.1.2.1",
                    "allowHttp_10": "disabled",
                    "appService": "none",
                    "browserWorkarounds": "disabled",
                    "bufferSize": 4096,
                    "contentTypeExclude": [],
                    "contentTypeInclude": [
                        "text/",
                        "application/(xml|x-javascript)",
                    ],
                    "cpuSaver": "enabled",
                    "cpuSaverHigh": 90,
                    "cpuSaverLow": 75,
                    "defaultsFrom": "none",
                    "description": "none",
                    "gzipLevel": 1,
                    "gzipMemoryLevel": 8192,
                    "gzipWindowSize": 16384,
                    "keepAcceptEncoding": "disabled",
                    "methodPrefer": "gzip",
                    "minSize": 1024,
                    "selective": "disabled",
                    "uriExclude": [],
                    "uriInclude": [".*"],
                    "varyHeader": "enabled",
                },
                {
                    "kind": "tm:ltm:profile:http-compression:http-compressionstate",
                    "name": "wan-optimized-compression",
                    "partition": "Common",
                    "fullPath": "/Common/wan-optimized-compression",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/http-compression/~Common~wan-optimized-compression?ver=14.1.2.1",
                    "allowHttp_10": "enabled",
                    "appService": "none",
                    "browserWorkarounds": "disabled",
                    "bufferSize": 131072,
                    "contentTypeExclude": [],
                    "contentTypeInclude": [
                        "text/",
                        "application/(xml|x-javascript)",
                    ],
                    "cpuSaver": "enabled",
                    "cpuSaverHigh": 90,
                    "cpuSaverLow": 75,
                    "defaultsFrom": "/Common/httpcompression",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/http-compression/~Common~httpcompression?ver=14.1.2.1"
                    },
                    "description": "none",
                    "gzipLevel": 1,
                    "gzipMemoryLevel": 16384,
                    "gzipWindowSize": 65536,
                    "keepAcceptEncoding": "disabled",
                    "methodPrefer": "gzip",
                    "minSize": 1024,
                    "selective": "disabled",
                    "uriExclude": [],
                    "uriInclude": [".*"],
                    "varyHeader": "enabled",
                },
            ],
        }


class test_get_ltm_profilehttp_compression(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "allowHttp_10": "disabled",
                "appService": "none",
                "browserWorkarounds": "disabled",
                "bufferSize": 4096,
                "contentTypeExclude": [],
                "contentTypeInclude": [
                    "text/",
                    "application/(xml|x-javascript)",
                ],
                "cpuSaver": "enabled",
                "cpuSaverHigh": 90,
                "cpuSaverLow": 75,
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/httpcompression",
                "generation": 1,
                "gzipLevel": 1,
                "gzipMemoryLevel": 8192,
                "gzipWindowSize": 16384,
                "keepAcceptEncoding": "disabled",
                "kind": "tm:ltm:profile:http-compression:http-compressionstate",
                "methodPrefer": "gzip",
                "minSize": 1024,
                "name": "httpcompression",
                "partition": "Common",
                "selective": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/http-compression/~Common~httpcompression?ver=14.1.2.1",
                "uriExclude": [],
                "uriInclude": [".*"],
                "varyHeader": "enabled",
            },
            {
                "allowHttp_10": "enabled",
                "appService": "none",
                "browserWorkarounds": "disabled",
                "bufferSize": 131072,
                "contentTypeExclude": [],
                "contentTypeInclude": [
                    "text/",
                    "application/(xml|x-javascript)",
                ],
                "cpuSaver": "enabled",
                "cpuSaverHigh": 90,
                "cpuSaverLow": 75,
                "defaultsFrom": "/Common/httpcompression",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/http-compression/~Common~httpcompression?ver=14.1.2.1"
                },
                "description": "none",
                "fullPath": "/Common/wan-optimized-compression",
                "generation": 1,
                "gzipLevel": 1,
                "gzipMemoryLevel": 16384,
                "gzipWindowSize": 65536,
                "keepAcceptEncoding": "disabled",
                "kind": "tm:ltm:profile:http-compression:http-compressionstate",
                "methodPrefer": "gzip",
                "minSize": 1024,
                "name": "wan-optimized-compression",
                "partition": "Common",
                "selective": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/http-compression/~Common~wan-optimized-compression?ver=14.1.2.1",
                "uriExclude": [],
                "uriInclude": [".*"],
                "varyHeader": "enabled",
            },
        ],
        "kind": "tm:ltm:profile:http-compression:http-compressioncollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/http-compression?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileHttpcompression(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileHttpcompression(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
