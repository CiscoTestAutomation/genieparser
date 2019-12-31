# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitoricmp
from genie.libs.parser.bigip.get_ltm_monitoricmp import LtmMonitorIcmp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/icmp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:icmp:icmpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/icmp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:icmp:icmpstate",
                    "name": "icmp",
                    "partition": "Common",
                    "fullPath": "/Common/icmp",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/icmp/~Common~icmp?ver=14.1.2.1",
                    "adaptive": "disabled",
                    "adaptiveDivergenceType": "relative",
                    "adaptiveDivergenceValue": 25,
                    "adaptiveLimit": 200,
                    "adaptiveSamplingTimespan": 300,
                    "destination": "*",
                    "interval": 5,
                    "manualResume": "disabled",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "transparent": "disabled",
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitoricmp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "adaptive": "disabled",
                "adaptiveDivergenceType": "relative",
                "adaptiveDivergenceValue": 25,
                "adaptiveLimit": 200,
                "adaptiveSamplingTimespan": 300,
                "destination": "*",
                "fullPath": "/Common/icmp",
                "generation": 0,
                "interval": 5,
                "kind": "tm:ltm:monitor:icmp:icmpstate",
                "manualResume": "disabled",
                "name": "icmp",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/icmp/~Common~icmp?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 16,
                "transparent": "disabled",
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:icmp:icmpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/icmp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorIcmp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorIcmp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
