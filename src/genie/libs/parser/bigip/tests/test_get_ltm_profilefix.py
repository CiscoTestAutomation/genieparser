# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilefix
from genie.libs.parser.bigip.get_ltm_profilefix import LtmProfileFix

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/fix'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:fix:fixcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/fix?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:fix:fixstate",
                    "name": "fix",
                    "partition": "Common",
                    "fullPath": "/Common/fix",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/fix/~Common~fix?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "errorAction": "dont-forward",
                    "fullLogonParsing": "true",
                    "messageLogPublisher": "none",
                    "quickParsing": "false",
                    "reportLogPublisher": "none",
                    "responseParsing": "false",
                    "senderTagClass": [],
                    "statisticsSampleInterval": 20,
                }
            ],
        }


class test_get_ltm_profilefix(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "errorAction": "dont-forward",
                "fullLogonParsing": "true",
                "fullPath": "/Common/fix",
                "generation": 1,
                "kind": "tm:ltm:profile:fix:fixstate",
                "messageLogPublisher": "none",
                "name": "fix",
                "partition": "Common",
                "quickParsing": "false",
                "reportLogPublisher": "none",
                "responseParsing": "false",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/fix/~Common~fix?ver=14.1.2.1",
                "senderTagClass": [],
                "statisticsSampleInterval": 20,
            }
        ],
        "kind": "tm:ltm:profile:fix:fixcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/fix?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileFix(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileFix(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
