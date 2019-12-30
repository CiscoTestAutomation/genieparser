# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilestatistics
from genie.libs.parser.bigip.get_ltm_profilestatistics import (
    LtmProfileStatistics,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/statistics'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:statistics:statisticscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/statistics?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:statistics:statisticsstate",
                    "name": "stats",
                    "partition": "Common",
                    "fullPath": "/Common/stats",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/statistics/~Common~stats?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "field1": "none",
                    "field10": "none",
                    "field11": "none",
                    "field12": "none",
                    "field13": "none",
                    "field14": "none",
                    "field15": "none",
                    "field16": "none",
                    "field17": "none",
                    "field18": "none",
                    "field19": "none",
                    "field2": "none",
                    "field20": "none",
                    "field21": "none",
                    "field22": "none",
                    "field23": "none",
                    "field24": "none",
                    "field25": "none",
                    "field26": "none",
                    "field27": "none",
                    "field28": "none",
                    "field29": "none",
                    "field3": "none",
                    "field30": "none",
                    "field31": "none",
                    "field32": "none",
                    "field4": "none",
                    "field5": "none",
                    "field6": "none",
                    "field7": "none",
                    "field8": "none",
                    "field9": "none",
                }
            ],
        }


class test_get_ltm_profilestatistics(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "field1": "none",
                "field10": "none",
                "field11": "none",
                "field12": "none",
                "field13": "none",
                "field14": "none",
                "field15": "none",
                "field16": "none",
                "field17": "none",
                "field18": "none",
                "field19": "none",
                "field2": "none",
                "field20": "none",
                "field21": "none",
                "field22": "none",
                "field23": "none",
                "field24": "none",
                "field25": "none",
                "field26": "none",
                "field27": "none",
                "field28": "none",
                "field29": "none",
                "field3": "none",
                "field30": "none",
                "field31": "none",
                "field32": "none",
                "field4": "none",
                "field5": "none",
                "field6": "none",
                "field7": "none",
                "field8": "none",
                "field9": "none",
                "fullPath": "/Common/stats",
                "generation": 1,
                "kind": "tm:ltm:profile:statistics:statisticsstate",
                "name": "stats",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/statistics/~Common~stats?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:statistics:statisticscollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/statistics?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileStatistics(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileStatistics(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
