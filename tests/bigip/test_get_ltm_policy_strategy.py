# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_policy_strategy
from genie.libs.parser.bigip.get_ltm_policy_strategy import LtmPolicystrategy

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/policy-strategy'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:policy-strategy:policy-strategycollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/policy-strategy?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:policy-strategy:policy-strategystate",
                    "name": "all-match",
                    "partition": "Common",
                    "fullPath": "/Common/all-match",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~all-match?ver=14.1.2.1",
                    "strategy": "all-match",
                    "operandsReference": {
                        "link": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~all-match/operands?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:ltm:policy-strategy:policy-strategystate",
                    "name": "best-match",
                    "partition": "Common",
                    "fullPath": "/Common/best-match",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~best-match?ver=14.1.2.1",
                    "strategy": "best-match",
                    "operandsReference": {
                        "link": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~best-match/operands?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:ltm:policy-strategy:policy-strategystate",
                    "name": "first-match",
                    "partition": "Common",
                    "fullPath": "/Common/first-match",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~first-match?ver=14.1.2.1",
                    "strategy": "first-match",
                    "operandsReference": {
                        "link": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~first-match/operands?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
            ],
        }


class test_get_ltm_policy_strategy(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/all-match",
                "generation": 1,
                "kind": "tm:ltm:policy-strategy:policy-strategystate",
                "name": "all-match",
                "operandsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~all-match/operands?ver=14.1.2.1",
                },
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~all-match?ver=14.1.2.1",
                "strategy": "all-match",
            },
            {
                "fullPath": "/Common/best-match",
                "generation": 1,
                "kind": "tm:ltm:policy-strategy:policy-strategystate",
                "name": "best-match",
                "operandsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~best-match/operands?ver=14.1.2.1",
                },
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~best-match?ver=14.1.2.1",
                "strategy": "best-match",
            },
            {
                "fullPath": "/Common/first-match",
                "generation": 1,
                "kind": "tm:ltm:policy-strategy:policy-strategystate",
                "name": "first-match",
                "operandsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~first-match/operands?ver=14.1.2.1",
                },
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/policy-strategy/~Common~first-match?ver=14.1.2.1",
                "strategy": "first-match",
            },
        ],
        "kind": "tm:ltm:policy-strategy:policy-strategycollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/policy-strategy?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmPolicystrategy(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmPolicystrategy(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
