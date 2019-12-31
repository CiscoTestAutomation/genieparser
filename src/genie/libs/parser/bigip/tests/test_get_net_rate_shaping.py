# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_rate_shaping
from genie.libs.parser.bigip.get_net_rate_shaping import NetRateshaping

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/rate-shaping'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:rate-shaping:rate-shapingcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/rate-shaping?ver=14.1.2.1",
            "items": [
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/net/rate-shaping/class?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/net/rate-shaping/color-policer?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/net/rate-shaping/drop-policy?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/net/rate-shaping/queue?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/net/rate-shaping/shaping-policy?ver=14.1.2.1"
                    }
                },
            ],
        }


class test_get_net_rate_shaping(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/net/rate-shaping/class?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/net/rate-shaping/color-policer?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/net/rate-shaping/drop-policy?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/net/rate-shaping/queue?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/net/rate-shaping/shaping-policy?ver=14.1.2.1"
                }
            },
        ],
        "kind": "tm:net:rate-shaping:rate-shapingcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/rate-shaping?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetRateshaping(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetRateshaping(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
