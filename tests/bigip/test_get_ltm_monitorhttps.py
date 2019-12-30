# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorhttps
from genie.libs.parser.bigip.get_ltm_monitorhttps import LtmMonitorHttps

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/https'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:https:httpscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/https?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:https:httpsstate",
                    "name": "https",
                    "partition": "Common",
                    "fullPath": "/Common/https",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/https/~Common~https?ver=14.1.2.1",
                    "adaptive": "disabled",
                    "adaptiveDivergenceType": "relative",
                    "adaptiveDivergenceValue": 25,
                    "adaptiveLimit": 200,
                    "adaptiveSamplingTimespan": 300,
                    "destination": "*:*",
                    "interval": 5,
                    "ipDscp": 0,
                    "manualResume": "disabled",
                    "reverse": "disabled",
                    "send": "GET /\\r\\n",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "transparent": "disabled",
                    "upInterval": 0,
                },
                {
                    "kind": "tm:ltm:monitor:https:httpsstate",
                    "name": "https_443",
                    "partition": "Common",
                    "fullPath": "/Common/https_443",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/https/~Common~https_443?ver=14.1.2.1",
                    "adaptive": "disabled",
                    "adaptiveDivergenceType": "relative",
                    "adaptiveDivergenceValue": 25,
                    "adaptiveLimit": 200,
                    "adaptiveSamplingTimespan": 300,
                    "defaultsFrom": "/Common/https",
                    "destination": "*:443",
                    "interval": 5,
                    "ipDscp": 0,
                    "manualResume": "disabled",
                    "reverse": "disabled",
                    "send": "GET /\\r\\n",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "transparent": "disabled",
                    "upInterval": 0,
                },
                {
                    "kind": "tm:ltm:monitor:https:httpsstate",
                    "name": "https_head_f5",
                    "partition": "Common",
                    "fullPath": "/Common/https_head_f5",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/https/~Common~https_head_f5?ver=14.1.2.1",
                    "adaptive": "disabled",
                    "adaptiveDivergenceType": "relative",
                    "adaptiveDivergenceValue": 25,
                    "adaptiveLimit": 200,
                    "adaptiveSamplingTimespan": 300,
                    "defaultsFrom": "/Common/https",
                    "destination": "*:*",
                    "interval": 5,
                    "ipDscp": 0,
                    "manualResume": "disabled",
                    "recv": "Server\\:",
                    "reverse": "disabled",
                    "send": "HEAD / HTTP/1.0\\r\\n\\r\\n",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "transparent": "disabled",
                    "upInterval": 0,
                },
            ],
        }


class test_get_ltm_monitorhttps(unittest.TestCase):

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
                "destination": "*:*",
                "fullPath": "/Common/https",
                "generation": 0,
                "interval": 5,
                "ipDscp": 0,
                "kind": "tm:ltm:monitor:https:httpsstate",
                "manualResume": "disabled",
                "name": "https",
                "partition": "Common",
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/https/~Common~https?ver=14.1.2.1",
                "send": "GET /\\r\\n",
                "timeUntilUp": 0,
                "timeout": 16,
                "transparent": "disabled",
                "upInterval": 0,
            },
            {
                "adaptive": "disabled",
                "adaptiveDivergenceType": "relative",
                "adaptiveDivergenceValue": 25,
                "adaptiveLimit": 200,
                "adaptiveSamplingTimespan": 300,
                "defaultsFrom": "/Common/https",
                "destination": "*:443",
                "fullPath": "/Common/https_443",
                "generation": 0,
                "interval": 5,
                "ipDscp": 0,
                "kind": "tm:ltm:monitor:https:httpsstate",
                "manualResume": "disabled",
                "name": "https_443",
                "partition": "Common",
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/https/~Common~https_443?ver=14.1.2.1",
                "send": "GET /\\r\\n",
                "timeUntilUp": 0,
                "timeout": 16,
                "transparent": "disabled",
                "upInterval": 0,
            },
            {
                "adaptive": "disabled",
                "adaptiveDivergenceType": "relative",
                "adaptiveDivergenceValue": 25,
                "adaptiveLimit": 200,
                "adaptiveSamplingTimespan": 300,
                "defaultsFrom": "/Common/https",
                "destination": "*:*",
                "fullPath": "/Common/https_head_f5",
                "generation": 0,
                "interval": 5,
                "ipDscp": 0,
                "kind": "tm:ltm:monitor:https:httpsstate",
                "manualResume": "disabled",
                "name": "https_head_f5",
                "partition": "Common",
                "recv": "Server\\:",
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/https/~Common~https_head_f5?ver=14.1.2.1",
                "send": "HEAD / HTTP/1.0\\r\\n\\r\\n",
                "timeUntilUp": 0,
                "timeout": 16,
                "transparent": "disabled",
                "upInterval": 0,
            },
        ],
        "kind": "tm:ltm:monitor:https:httpscollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/https?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorHttps(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorHttps(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
