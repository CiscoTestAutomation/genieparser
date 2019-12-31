# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_url_dburl_category
from genie.libs.parser.bigip.get_sys_url_dburl_category import (
    SysUrldbUrlcategory,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/url-db/url-category'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:url-db:url-category:url-categorycollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/url-db/url-category?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:url-db:url-category:url-categorystate",
                    "name": "Uncategorized",
                    "partition": "Common",
                    "fullPath": "/Common/Uncategorized",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/url-db/url-category/~Common~Uncategorized?ver=14.1.2.1",
                    "catId": 25573,
                    "catNumber": 153,
                    "defaultAction": "block",
                    "description": "Sites not categorized in the Master Database.",
                    "displayName": "Uncategorized",
                    "f5Id": 16449,
                    "isCustom": "false",
                    "isRecategory": "false",
                    "parentCatNumber": 146,
                    "severityLevel": 0,
                },
                {
                    "kind": "tm:sys:url-db:url-category:url-categorystate",
                    "name": "User-Defined",
                    "partition": "Common",
                    "fullPath": "/Common/User-Defined",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/url-db/url-category/~Common~User-Defined?ver=14.1.2.1",
                    "catId": 0,
                    "catNumber": 64,
                    "defaultAction": "allow",
                    "description": "User-defined category",
                    "displayName": "User-Defined",
                    "f5Id": 16513,
                    "isCustom": "false",
                    "isRecategory": "false",
                    "parentCatNumber": 0,
                    "severityLevel": 0,
                },
            ],
        }


class test_get_sys_url_dburl_category(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "catId": 25573,
                "catNumber": 153,
                "defaultAction": "block",
                "description": "Sites not categorized in the Master Database.",
                "displayName": "Uncategorized",
                "f5Id": 16449,
                "fullPath": "/Common/Uncategorized",
                "generation": 1,
                "isCustom": "false",
                "isRecategory": "false",
                "kind": "tm:sys:url-db:url-category:url-categorystate",
                "name": "Uncategorized",
                "parentCatNumber": 146,
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/url-db/url-category/~Common~Uncategorized?ver=14.1.2.1",
                "severityLevel": 0,
            },
            {
                "catId": 0,
                "catNumber": 64,
                "defaultAction": "allow",
                "description": "User-defined category",
                "displayName": "User-Defined",
                "f5Id": 16513,
                "fullPath": "/Common/User-Defined",
                "generation": 1,
                "isCustom": "false",
                "isRecategory": "false",
                "kind": "tm:sys:url-db:url-category:url-categorystate",
                "name": "User-Defined",
                "parentCatNumber": 0,
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/url-db/url-category/~Common~User-Defined?ver=14.1.2.1",
                "severityLevel": 0,
            },
        ],
        "kind": "tm:sys:url-db:url-category:url-categorycollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/url-db/url-category?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysUrldbUrlcategory(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysUrldbUrlcategory(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
