# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_rate_shapingqueue
from genie.libs.parser.bigip.get_net_rate_shapingqueue import (
    NetRateshapingQueue,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/rate-shaping/queue'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:rate-shaping:queue:queuecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/queue?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:rate-shaping:queue:queuestate",
                    "name": "pfifo",
                    "partition": "Common",
                    "fullPath": "/Common/pfifo",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/queue/~Common~pfifo?ver=14.1.2.1",
                    "pfifoMaxSize": 4194304,
                    "pfifoMinSize": 65536,
                    "sfqBucketCount": 0,
                    "sfqBucketSize": 0,
                    "sfqPerturbation": 10,
                    "type": "pfifo",
                },
                {
                    "kind": "tm:net:rate-shaping:queue:queuestate",
                    "name": "sfq",
                    "partition": "Common",
                    "fullPath": "/Common/sfq",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/queue/~Common~sfq?ver=14.1.2.1",
                    "pfifoMaxSize": 0,
                    "pfifoMinSize": 0,
                    "sfqBucketCount": 256,
                    "sfqBucketSize": 0,
                    "sfqPerturbation": 10,
                    "type": "sfq",
                },
            ],
        }


class test_get_net_rate_shapingqueue(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/pfifo",
                "generation": 1,
                "kind": "tm:net:rate-shaping:queue:queuestate",
                "name": "pfifo",
                "partition": "Common",
                "pfifoMaxSize": 4194304,
                "pfifoMinSize": 65536,
                "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/queue/~Common~pfifo?ver=14.1.2.1",
                "sfqBucketCount": 0,
                "sfqBucketSize": 0,
                "sfqPerturbation": 10,
                "type": "pfifo",
            },
            {
                "fullPath": "/Common/sfq",
                "generation": 1,
                "kind": "tm:net:rate-shaping:queue:queuestate",
                "name": "sfq",
                "partition": "Common",
                "pfifoMaxSize": 0,
                "pfifoMinSize": 0,
                "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/queue/~Common~sfq?ver=14.1.2.1",
                "sfqBucketCount": 256,
                "sfqBucketSize": 0,
                "sfqPerturbation": 10,
                "type": "sfq",
            },
        ],
        "kind": "tm:net:rate-shaping:queue:queuecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/rate-shaping/queue?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetRateshapingQueue(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetRateshapingQueue(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
