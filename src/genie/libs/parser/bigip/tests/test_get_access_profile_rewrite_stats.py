# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_access_profile_rewrite_stats
from genie.libs.parser.bigip.get_access_profile_rewrite_stats import (
    AccessProfilerewritestats,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/access/profile-rewrite-stats'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [
                {
                    "clientRequestBytes": 0,
                    "clientResponseBytes": 0,
                    "serverRequestBytes": 0,
                    "serverResponseBytes": 0,
                    "clientRequests": 0,
                    "clientResponses": 0,
                    "serverResponses": 0,
                    "serverRequests": 0,
                    "cacheHits": 0,
                    "cacheMisses": 0,
                    "name": "/Common/rewrite",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                },
                {
                    "clientRequestBytes": 0,
                    "clientResponseBytes": 0,
                    "serverRequestBytes": 0,
                    "serverResponseBytes": 0,
                    "clientRequests": 0,
                    "clientResponses": 0,
                    "serverResponses": 0,
                    "serverRequests": 0,
                    "cacheHits": 0,
                    "cacheMisses": 0,
                    "name": "/Common/rewrite-portal",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                },
                {
                    "clientRequestBytes": 0,
                    "clientResponseBytes": 0,
                    "serverRequestBytes": 0,
                    "serverResponseBytes": 0,
                    "clientRequests": 0,
                    "clientResponses": 0,
                    "serverResponses": 0,
                    "serverRequests": 0,
                    "cacheHits": 0,
                    "cacheMisses": 0,
                    "name": "/Common/rewrite-uri-translation",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                },
            ],
            "generation": 0,
            "lastUpdateMicros": 0,
            "kind": "tm:access:profile-rewrite:stats:profilerewritestatcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/access/profile-rewrite/stats",
        }


class test_get_access_profile_rewrite_stats(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [
            {
                "cacheHits": 0,
                "cacheMisses": 0,
                "clientRequestBytes": 0,
                "clientRequests": 0,
                "clientResponseBytes": 0,
                "clientResponses": 0,
                "generation": 0,
                "lastUpdateMicros": 0,
                "name": "/Common/rewrite",
                "serverRequestBytes": 0,
                "serverRequests": 0,
                "serverResponseBytes": 0,
                "serverResponses": 0,
            },
            {
                "cacheHits": 0,
                "cacheMisses": 0,
                "clientRequestBytes": 0,
                "clientRequests": 0,
                "clientResponseBytes": 0,
                "clientResponses": 0,
                "generation": 0,
                "lastUpdateMicros": 0,
                "name": "/Common/rewrite-portal",
                "serverRequestBytes": 0,
                "serverRequests": 0,
                "serverResponseBytes": 0,
                "serverResponses": 0,
            },
            {
                "cacheHits": 0,
                "cacheMisses": 0,
                "clientRequestBytes": 0,
                "clientRequests": 0,
                "clientResponseBytes": 0,
                "clientResponses": 0,
                "generation": 0,
                "lastUpdateMicros": 0,
                "name": "/Common/rewrite-uri-translation",
                "serverRequestBytes": 0,
                "serverRequests": 0,
                "serverResponseBytes": 0,
                "serverResponses": 0,
            },
        ],
        "kind": "tm:access:profile-rewrite:stats:profilerewritestatcollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/access/profile-rewrite/stats",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AccessProfilerewritestats(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AccessProfilerewritestats(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
