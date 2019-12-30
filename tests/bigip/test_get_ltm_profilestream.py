# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilestream
from genie.libs.parser.bigip.get_ltm_profilestream import LtmProfileStream

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/stream'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:stream:streamcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/stream?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:stream:streamstate",
                    "name": "stream",
                    "partition": "Common",
                    "fullPath": "/Common/stream",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/stream/~Common~stream?ver=14.1.2.1",
                    "appService": "none",
                    "chunkSize": 4096,
                    "chunking": "disabled",
                    "defaultsFrom": "none",
                    "description": "none",
                    "source": "none",
                    "tmTarget": "none",
                }
            ],
        }


class test_get_ltm_profilestream(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "chunkSize": 4096,
                "chunking": "disabled",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/stream",
                "generation": 1,
                "kind": "tm:ltm:profile:stream:streamstate",
                "name": "stream",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/stream/~Common~stream?ver=14.1.2.1",
                "source": "none",
                "tmTarget": "none",
            }
        ],
        "kind": "tm:ltm:profile:stream:streamcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/stream?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileStream(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileStream(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
