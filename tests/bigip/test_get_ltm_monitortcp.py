# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitortcp
from genie.libs.parser.bigip.get_ltm_monitortcp import LtmMonitorTcp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/tcp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:tcp:tcpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:tcp:tcpstate",
                    "name": "monitor-8888-10.10.34.249",
                    "partition": "Common",
                    "fullPath": "/Common/monitor-8888-10.10.34.249",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp/~Common~monitor-8888-10.10.34.249?ver=14.1.2.1",
                    "adaptive": "disabled",
                    "adaptiveDivergenceType": "relative",
                    "adaptiveDivergenceValue": 25,
                    "adaptiveLimit": 200,
                    "adaptiveSamplingTimespan": 300,
                    "defaultsFrom": "/Common/tcp",
                    "description": "monitor-8888-10.10.34.249",
                    "destination": "*:*",
                    "interval": 5,
                    "ipDscp": 0,
                    "manualResume": "disabled",
                    "reverse": "disabled",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "transparent": "disabled",
                    "upInterval": 0,
                },
                {
                    "kind": "tm:ltm:monitor:tcp:tcpstate",
                    "name": "monitor-8888-10.10.34.250",
                    "partition": "Common",
                    "fullPath": "/Common/monitor-8888-10.10.34.250",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp/~Common~monitor-8888-10.10.34.250?ver=14.1.2.1",
                    "adaptive": "disabled",
                    "adaptiveDivergenceType": "relative",
                    "adaptiveDivergenceValue": 25,
                    "adaptiveLimit": 200,
                    "adaptiveSamplingTimespan": 300,
                    "defaultsFrom": "/Common/tcp",
                    "description": "monitor-8888-10.10.34.250",
                    "destination": "*:*",
                    "interval": 5,
                    "ipDscp": 0,
                    "manualResume": "disabled",
                    "reverse": "disabled",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "transparent": "disabled",
                    "upInterval": 0,
                },
                {
                    "kind": "tm:ltm:monitor:tcp:tcpstate",
                    "name": "monitor-8888-10.10.34.251_2",
                    "partition": "Common",
                    "fullPath": "/Common/monitor-8888-10.10.34.251_2",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp/~Common~monitor-8888-10.10.34.251_2?ver=14.1.2.1",
                    "adaptive": "disabled",
                    "adaptiveDivergenceType": "relative",
                    "adaptiveDivergenceValue": 25,
                    "adaptiveLimit": 200,
                    "adaptiveSamplingTimespan": 300,
                    "defaultsFrom": "/Common/tcp",
                    "description": "monitor-8888-10.10.34.251_2",
                    "destination": "*:*",
                    "interval": 5,
                    "ipDscp": 0,
                    "manualResume": "disabled",
                    "reverse": "disabled",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "transparent": "disabled",
                    "upInterval": 0,
                },
                {
                    "kind": "tm:ltm:monitor:tcp:tcpstate",
                    "name": "monitor-until-up-300",
                    "partition": "Common",
                    "fullPath": "/Common/monitor-until-up-300",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp/~Common~monitor-until-up-300?ver=14.1.2.1",
                    "adaptive": "disabled",
                    "adaptiveDivergenceType": "relative",
                    "adaptiveDivergenceValue": 25,
                    "adaptiveLimit": 200,
                    "adaptiveSamplingTimespan": 300,
                    "defaultsFrom": "/Common/tcp",
                    "description": "monitor-until-up-300",
                    "destination": "*:*",
                    "interval": 5,
                    "ipDscp": 0,
                    "manualResume": "disabled",
                    "reverse": "disabled",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "transparent": "disabled",
                    "upInterval": 0,
                },
                {
                    "kind": "tm:ltm:monitor:tcp:tcpstate",
                    "name": "tcp",
                    "partition": "Common",
                    "fullPath": "/Common/tcp",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp/~Common~tcp?ver=14.1.2.1",
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
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "transparent": "disabled",
                    "upInterval": 0,
                },
            ],
        }


class test_get_ltm_monitortcp(unittest.TestCase):

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
                "defaultsFrom": "/Common/tcp",
                "description": "monitor-8888-10.10.34.249",
                "destination": "*:*",
                "fullPath": "/Common/monitor-8888-10.10.34.249",
                "generation": 0,
                "interval": 5,
                "ipDscp": 0,
                "kind": "tm:ltm:monitor:tcp:tcpstate",
                "manualResume": "disabled",
                "name": "monitor-8888-10.10.34.249",
                "partition": "Common",
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp/~Common~monitor-8888-10.10.34.249?ver=14.1.2.1",
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
                "defaultsFrom": "/Common/tcp",
                "description": "monitor-8888-10.10.34.250",
                "destination": "*:*",
                "fullPath": "/Common/monitor-8888-10.10.34.250",
                "generation": 0,
                "interval": 5,
                "ipDscp": 0,
                "kind": "tm:ltm:monitor:tcp:tcpstate",
                "manualResume": "disabled",
                "name": "monitor-8888-10.10.34.250",
                "partition": "Common",
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp/~Common~monitor-8888-10.10.34.250?ver=14.1.2.1",
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
                "defaultsFrom": "/Common/tcp",
                "description": "monitor-8888-10.10.34.251_2",
                "destination": "*:*",
                "fullPath": "/Common/monitor-8888-10.10.34.251_2",
                "generation": 0,
                "interval": 5,
                "ipDscp": 0,
                "kind": "tm:ltm:monitor:tcp:tcpstate",
                "manualResume": "disabled",
                "name": "monitor-8888-10.10.34.251_2",
                "partition": "Common",
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp/~Common~monitor-8888-10.10.34.251_2?ver=14.1.2.1",
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
                "defaultsFrom": "/Common/tcp",
                "description": "monitor-until-up-300",
                "destination": "*:*",
                "fullPath": "/Common/monitor-until-up-300",
                "generation": 0,
                "interval": 5,
                "ipDscp": 0,
                "kind": "tm:ltm:monitor:tcp:tcpstate",
                "manualResume": "disabled",
                "name": "monitor-until-up-300",
                "partition": "Common",
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp/~Common~monitor-until-up-300?ver=14.1.2.1",
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
                "destination": "*:*",
                "fullPath": "/Common/tcp",
                "generation": 0,
                "interval": 5,
                "ipDscp": 0,
                "kind": "tm:ltm:monitor:tcp:tcpstate",
                "manualResume": "disabled",
                "name": "tcp",
                "partition": "Common",
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp/~Common~tcp?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 16,
                "transparent": "disabled",
                "upInterval": 0,
            },
        ],
        "kind": "tm:ltm:monitor:tcp:tcpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorTcp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorTcp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
