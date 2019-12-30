# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorudp
from genie.libs.parser.bigip.get_ltm_monitorudp import LtmMonitorUdp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/udp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:udp:udpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/udp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:udp:udpstate",
                    "name": "udp",
                    "partition": "Common",
                    "fullPath": "/Common/udp",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/udp/~Common~udp?ver=14.1.2.1",
                    "adaptive": "disabled",
                    "adaptiveDivergenceType": "relative",
                    "adaptiveDivergenceValue": 25,
                    "adaptiveLimit": 200,
                    "adaptiveSamplingTimespan": 300,
                    "debug": "no",
                    "destination": "*:*",
                    "interval": 5,
                    "manualResume": "disabled",
                    "reverse": "disabled",
                    "send": "default send string",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "transparent": "disabled",
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitorudp(unittest.TestCase):

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
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/udp",
                "generation": 0,
                "interval": 5,
                "kind": "tm:ltm:monitor:udp:udpstate",
                "manualResume": "disabled",
                "name": "udp",
                "partition": "Common",
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/udp/~Common~udp?ver=14.1.2.1",
                "send": "default send string",
                "timeUntilUp": 0,
                "timeout": 16,
                "transparent": "disabled",
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:udp:udpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/udp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorUdp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorUdp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
