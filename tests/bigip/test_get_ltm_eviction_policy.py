# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_eviction_policy
from genie.libs.parser.bigip.get_ltm_eviction_policy import LtmEvictionpolicy

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/eviction-policy'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:eviction-policy:eviction-policycollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/eviction-policy?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:eviction-policy:eviction-policystate",
                    "name": "default-eviction-policy",
                    "partition": "Common",
                    "fullPath": "/Common/default-eviction-policy",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/eviction-policy/~Common~default-eviction-policy?ver=14.1.2.1",
                    "highWater": 95,
                    "lowWater": 85,
                    "slowFlow": {
                        "enabled": "false",
                        "evictionType": "percent",
                        "gracePeriod": 10,
                        "maximum": 100,
                        "thresholdBps": 32,
                        "throttling": "disabled",
                    },
                    "strategies": {
                        "biasBytes": {"delay": 0, "enabled": "false"},
                        "biasFast": {"delay": 0, "enabled": "false"},
                        "biasIdle": {"enabled": "true"},
                        "biasOldest": {"enabled": "true"},
                        "biasSlow": {"delay": 0, "enabled": "false"},
                        "lowPriorityGeographies": {"enabled": "false"},
                        "lowPriorityPort": {"enabled": "false"},
                        "lowPriorityRouteDomain": {"enabled": "false"},
                        "lowPriorityVirtualServer": {"enabled": "false"},
                    },
                }
            ],
        }


class test_get_ltm_eviction_policy(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/default-eviction-policy",
                "generation": 1,
                "highWater": 95,
                "kind": "tm:ltm:eviction-policy:eviction-policystate",
                "lowWater": 85,
                "name": "default-eviction-policy",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/eviction-policy/~Common~default-eviction-policy?ver=14.1.2.1",
                "slowFlow": {
                    "enabled": "false",
                    "evictionType": "percent",
                    "gracePeriod": 10,
                    "maximum": 100,
                    "thresholdBps": 32,
                    "throttling": "disabled",
                },
                "strategies": {
                    "biasBytes": {"delay": 0, "enabled": "false"},
                    "biasFast": {"delay": 0, "enabled": "false"},
                    "biasIdle": {"enabled": "true"},
                    "biasOldest": {"enabled": "true"},
                    "biasSlow": {"delay": 0, "enabled": "false"},
                    "lowPriorityGeographies": {"enabled": "false"},
                    "lowPriorityPort": {"enabled": "false"},
                    "lowPriorityRouteDomain": {"enabled": "false"},
                    "lowPriorityVirtualServer": {"enabled": "false"},
                },
            }
        ],
        "kind": "tm:ltm:eviction-policy:eviction-policycollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/eviction-policy?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmEvictionpolicy(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmEvictionpolicy(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
