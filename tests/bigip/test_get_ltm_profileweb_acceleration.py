# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileweb_acceleration
from genie.libs.parser.bigip.get_ltm_profileweb_acceleration import (
    LtmProfileWebacceleration,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/web-acceleration'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:web-acceleration:web-accelerationcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/web-acceleration?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:web-acceleration:web-accelerationstate",
                    "name": "apm-enduser-if-cache",
                    "partition": "Common",
                    "fullPath": "/Common/apm-enduser-if-cache",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~apm-enduser-if-cache?ver=14.1.2.1",
                    "appService": "none",
                    "applications": [],
                    "applicationsReference": [],
                    "cacheAgingRate": 9,
                    "cacheClientCacheControlMode": "all",
                    "cacheInsertAgeHeader": "enabled",
                    "cacheMaxAge": 36000,
                    "cacheMaxEntries": 1000,
                    "cacheObjectMaxSize": 12000000,
                    "cacheObjectMinSize": 5,
                    "cacheSize": 50,
                    "cacheUriExclude": [],
                    "cacheUriInclude": [".*"],
                    "cacheUriIncludeOverride": [],
                    "cacheUriPinned": [],
                    "defaultsFrom": "/Common/webacceleration",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~webacceleration?ver=14.1.2.1"
                    },
                    "metadataCacheMaxSize": 25,
                },
                {
                    "kind": "tm:ltm:profile:web-acceleration:web-accelerationstate",
                    "name": "optimized-acceleration",
                    "partition": "Common",
                    "fullPath": "/Common/optimized-acceleration",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~optimized-acceleration?ver=14.1.2.1",
                    "appService": "none",
                    "applications": [],
                    "applicationsReference": [],
                    "cacheAgingRate": 9,
                    "cacheClientCacheControlMode": "all",
                    "cacheInsertAgeHeader": "enabled",
                    "cacheMaxAge": 3600,
                    "cacheMaxEntries": 10000,
                    "cacheObjectMaxSize": 67108864,
                    "cacheObjectMinSize": 0,
                    "cacheSize": 6144,
                    "cacheUriExclude": [],
                    "cacheUriInclude": [".*"],
                    "cacheUriIncludeOverride": [],
                    "cacheUriPinned": [],
                    "defaultsFrom": "/Common/webacceleration",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~webacceleration?ver=14.1.2.1"
                    },
                    "metadataCacheMaxSize": 25,
                },
                {
                    "kind": "tm:ltm:profile:web-acceleration:web-accelerationstate",
                    "name": "optimized-caching",
                    "partition": "Common",
                    "fullPath": "/Common/optimized-caching",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~optimized-caching?ver=14.1.2.1",
                    "appService": "none",
                    "applications": [],
                    "applicationsReference": [],
                    "cacheAgingRate": 9,
                    "cacheClientCacheControlMode": "all",
                    "cacheInsertAgeHeader": "enabled",
                    "cacheMaxAge": 86400,
                    "cacheMaxEntries": 10000,
                    "cacheObjectMaxSize": 2000000,
                    "cacheObjectMinSize": 0,
                    "cacheSize": 10,
                    "cacheUriExclude": [],
                    "cacheUriInclude": [".*"],
                    "cacheUriIncludeOverride": [],
                    "cacheUriPinned": [],
                    "defaultsFrom": "/Common/webacceleration",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~webacceleration?ver=14.1.2.1"
                    },
                    "metadataCacheMaxSize": 25,
                },
                {
                    "kind": "tm:ltm:profile:web-acceleration:web-accelerationstate",
                    "name": "webacceleration",
                    "partition": "Common",
                    "fullPath": "/Common/webacceleration",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~webacceleration?ver=14.1.2.1",
                    "appService": "none",
                    "applications": [],
                    "applicationsReference": [],
                    "cacheAgingRate": 9,
                    "cacheClientCacheControlMode": "all",
                    "cacheInsertAgeHeader": "enabled",
                    "cacheMaxAge": 3600,
                    "cacheMaxEntries": 10000,
                    "cacheObjectMaxSize": 50000,
                    "cacheObjectMinSize": 500,
                    "cacheSize": 100,
                    "cacheUriExclude": [],
                    "cacheUriInclude": [".*"],
                    "cacheUriIncludeOverride": [],
                    "cacheUriPinned": [],
                    "defaultsFrom": "none",
                    "metadataCacheMaxSize": 25,
                },
            ],
        }


class test_get_ltm_profileweb_acceleration(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "applications": [],
                "applicationsReference": [],
                "cacheAgingRate": 9,
                "cacheClientCacheControlMode": "all",
                "cacheInsertAgeHeader": "enabled",
                "cacheMaxAge": 36000,
                "cacheMaxEntries": 1000,
                "cacheObjectMaxSize": 12000000,
                "cacheObjectMinSize": 5,
                "cacheSize": 50,
                "cacheUriExclude": [],
                "cacheUriInclude": [".*"],
                "cacheUriIncludeOverride": [],
                "cacheUriPinned": [],
                "defaultsFrom": "/Common/webacceleration",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~webacceleration?ver=14.1.2.1"
                },
                "fullPath": "/Common/apm-enduser-if-cache",
                "generation": 1,
                "kind": "tm:ltm:profile:web-acceleration:web-accelerationstate",
                "metadataCacheMaxSize": 25,
                "name": "apm-enduser-if-cache",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~apm-enduser-if-cache?ver=14.1.2.1",
            },
            {
                "appService": "none",
                "applications": [],
                "applicationsReference": [],
                "cacheAgingRate": 9,
                "cacheClientCacheControlMode": "all",
                "cacheInsertAgeHeader": "enabled",
                "cacheMaxAge": 3600,
                "cacheMaxEntries": 10000,
                "cacheObjectMaxSize": 67108864,
                "cacheObjectMinSize": 0,
                "cacheSize": 6144,
                "cacheUriExclude": [],
                "cacheUriInclude": [".*"],
                "cacheUriIncludeOverride": [],
                "cacheUriPinned": [],
                "defaultsFrom": "/Common/webacceleration",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~webacceleration?ver=14.1.2.1"
                },
                "fullPath": "/Common/optimized-acceleration",
                "generation": 1,
                "kind": "tm:ltm:profile:web-acceleration:web-accelerationstate",
                "metadataCacheMaxSize": 25,
                "name": "optimized-acceleration",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~optimized-acceleration?ver=14.1.2.1",
            },
            {
                "appService": "none",
                "applications": [],
                "applicationsReference": [],
                "cacheAgingRate": 9,
                "cacheClientCacheControlMode": "all",
                "cacheInsertAgeHeader": "enabled",
                "cacheMaxAge": 86400,
                "cacheMaxEntries": 10000,
                "cacheObjectMaxSize": 2000000,
                "cacheObjectMinSize": 0,
                "cacheSize": 10,
                "cacheUriExclude": [],
                "cacheUriInclude": [".*"],
                "cacheUriIncludeOverride": [],
                "cacheUriPinned": [],
                "defaultsFrom": "/Common/webacceleration",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~webacceleration?ver=14.1.2.1"
                },
                "fullPath": "/Common/optimized-caching",
                "generation": 1,
                "kind": "tm:ltm:profile:web-acceleration:web-accelerationstate",
                "metadataCacheMaxSize": 25,
                "name": "optimized-caching",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~optimized-caching?ver=14.1.2.1",
            },
            {
                "appService": "none",
                "applications": [],
                "applicationsReference": [],
                "cacheAgingRate": 9,
                "cacheClientCacheControlMode": "all",
                "cacheInsertAgeHeader": "enabled",
                "cacheMaxAge": 3600,
                "cacheMaxEntries": 10000,
                "cacheObjectMaxSize": 50000,
                "cacheObjectMinSize": 500,
                "cacheSize": 100,
                "cacheUriExclude": [],
                "cacheUriInclude": [".*"],
                "cacheUriIncludeOverride": [],
                "cacheUriPinned": [],
                "defaultsFrom": "none",
                "fullPath": "/Common/webacceleration",
                "generation": 1,
                "kind": "tm:ltm:profile:web-acceleration:web-accelerationstate",
                "metadataCacheMaxSize": 25,
                "name": "webacceleration",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/web-acceleration/~Common~webacceleration?ver=14.1.2.1",
            },
        ],
        "kind": "tm:ltm:profile:web-acceleration:web-accelerationcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/web-acceleration?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileWebacceleration(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileWebacceleration(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
