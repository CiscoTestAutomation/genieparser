# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileqoe
from genie.libs.parser.bigip.get_ltm_profileqoe import LtmProfileQoe

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/qoe'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:qoe:qoecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/qoe?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:qoe:qoestate",
                    "name": "qoe",
                    "partition": "Common",
                    "fullPath": "/Common/qoe",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/qoe/~Common~qoe?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "video": "false",
                }
            ],
        }


class test_get_ltm_profileqoe(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/qoe",
                "generation": 1,
                "kind": "tm:ltm:profile:qoe:qoestate",
                "name": "qoe",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/qoe/~Common~qoe?ver=14.1.2.1",
                "video": "false",
            }
        ],
        "kind": "tm:ltm:profile:qoe:qoecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/qoe?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileQoe(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileQoe(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
