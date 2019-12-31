# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_rate_shapingdrop_policy
from genie.libs.parser.bigip.get_net_rate_shapingdrop_policy import (
    NetRateshapingDroppolicy,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/rate-shaping/drop-policy'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:rate-shaping:drop-policy:drop-policycollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/drop-policy?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:rate-shaping:drop-policy:drop-policystate",
                    "name": "fred",
                    "partition": "Common",
                    "fullPath": "/Common/fred",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/drop-policy/~Common~fred?ver=14.1.2.1",
                    "averagePacketSize": 1024,
                    "fredMaxActive": 0,
                    "fredMaxDrop": 100,
                    "fredMinDrop": 0,
                    "inverseWeight": 128,
                    "maxProbability": 100,
                    "maxThreshold": 9216,
                    "minThreshold": 3072,
                    "redHardLimit": 0,
                    "type": "fred",
                },
                {
                    "kind": "tm:net:rate-shaping:drop-policy:drop-policystate",
                    "name": "red",
                    "partition": "Common",
                    "fullPath": "/Common/red",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/drop-policy/~Common~red?ver=14.1.2.1",
                    "averagePacketSize": 1024,
                    "fredMaxActive": 100,
                    "fredMaxDrop": 0,
                    "fredMinDrop": 0,
                    "inverseWeight": 512,
                    "maxProbability": 10,
                    "maxThreshold": 15,
                    "minThreshold": 5,
                    "redHardLimit": 60,
                    "type": "red",
                },
                {
                    "kind": "tm:net:rate-shaping:drop-policy:drop-policystate",
                    "name": "tail",
                    "partition": "Common",
                    "fullPath": "/Common/tail",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/drop-policy/~Common~tail?ver=14.1.2.1",
                    "averagePacketSize": 0,
                    "fredMaxActive": 0,
                    "fredMaxDrop": 0,
                    "fredMinDrop": 0,
                    "inverseWeight": 0,
                    "maxProbability": 0,
                    "maxThreshold": 0,
                    "minThreshold": 0,
                    "redHardLimit": 0,
                    "type": "tail",
                },
            ],
        }


class test_get_net_rate_shapingdrop_policy(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "averagePacketSize": 1024,
                "fredMaxActive": 0,
                "fredMaxDrop": 100,
                "fredMinDrop": 0,
                "fullPath": "/Common/fred",
                "generation": 1,
                "inverseWeight": 128,
                "kind": "tm:net:rate-shaping:drop-policy:drop-policystate",
                "maxProbability": 100,
                "maxThreshold": 9216,
                "minThreshold": 3072,
                "name": "fred",
                "partition": "Common",
                "redHardLimit": 0,
                "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/drop-policy/~Common~fred?ver=14.1.2.1",
                "type": "fred",
            },
            {
                "averagePacketSize": 1024,
                "fredMaxActive": 100,
                "fredMaxDrop": 0,
                "fredMinDrop": 0,
                "fullPath": "/Common/red",
                "generation": 1,
                "inverseWeight": 512,
                "kind": "tm:net:rate-shaping:drop-policy:drop-policystate",
                "maxProbability": 10,
                "maxThreshold": 15,
                "minThreshold": 5,
                "name": "red",
                "partition": "Common",
                "redHardLimit": 60,
                "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/drop-policy/~Common~red?ver=14.1.2.1",
                "type": "red",
            },
            {
                "averagePacketSize": 0,
                "fredMaxActive": 0,
                "fredMaxDrop": 0,
                "fredMinDrop": 0,
                "fullPath": "/Common/tail",
                "generation": 1,
                "inverseWeight": 0,
                "kind": "tm:net:rate-shaping:drop-policy:drop-policystate",
                "maxProbability": 0,
                "maxThreshold": 0,
                "minThreshold": 0,
                "name": "tail",
                "partition": "Common",
                "redHardLimit": 0,
                "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/drop-policy/~Common~tail?ver=14.1.2.1",
                "type": "tail",
            },
        ],
        "kind": "tm:net:rate-shaping:drop-policy:drop-policycollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/drop-policy?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetRateshapingDroppolicy(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetRateshapingDroppolicy(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
