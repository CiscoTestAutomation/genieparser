# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilehttp2
from genie.libs.parser.bigip.get_ltm_profilehttp2 import LtmProfileHttp2

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/http2'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:http2:http2collectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/http2?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:http2:http2state",
                    "name": "http2",
                    "partition": "Common",
                    "fullPath": "/Common/http2",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/http2/~Common~http2?ver=14.1.2.1",
                    "activationModes": ["alpn"],
                    "appService": "none",
                    "concurrentStreamsPerConnection": 10,
                    "connectionIdleTimeout": 300,
                    "defaultsFrom": "none",
                    "description": "none",
                    "enforceTlsRequirements": "enabled",
                    "frameSize": 2048,
                    "headerTableSize": 4096,
                    "includeContentLength": "disabled",
                    "insertHeader": "disabled",
                    "insertHeaderName": "X-HTTP2",
                    "receiveWindow": 32,
                    "writeSize": 16384,
                }
            ],
        }


class test_get_ltm_profilehttp2(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "activationModes": ["alpn"],
                "appService": "none",
                "concurrentStreamsPerConnection": 10,
                "connectionIdleTimeout": 300,
                "defaultsFrom": "none",
                "description": "none",
                "enforceTlsRequirements": "enabled",
                "frameSize": 2048,
                "fullPath": "/Common/http2",
                "generation": 1,
                "headerTableSize": 4096,
                "includeContentLength": "disabled",
                "insertHeader": "disabled",
                "insertHeaderName": "X-HTTP2",
                "kind": "tm:ltm:profile:http2:http2state",
                "name": "http2",
                "partition": "Common",
                "receiveWindow": 32,
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/http2/~Common~http2?ver=14.1.2.1",
                "writeSize": 16384,
            }
        ],
        "kind": "tm:ltm:profile:http2:http2collectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/http2?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileHttp2(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileHttp2(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
