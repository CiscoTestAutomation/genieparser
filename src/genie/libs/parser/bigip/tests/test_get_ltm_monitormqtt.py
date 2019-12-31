# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitormqtt
from genie.libs.parser.bigip.get_ltm_monitormqtt import LtmMonitorMqtt

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/mqtt'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:mqtt:mqttcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/mqtt?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:mqtt:mqttstate",
                    "name": "mqtt",
                    "partition": "Common",
                    "fullPath": "/Common/mqtt",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/mqtt/~Common~mqtt?ver=14.1.2.1",
                    "debug": "no",
                    "destination": "*:*",
                    "interval": 5,
                    "manualResume": "disabled",
                    "mqttVersion": "3.1.1",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitormqtt(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/mqtt",
                "generation": 0,
                "interval": 5,
                "kind": "tm:ltm:monitor:mqtt:mqttstate",
                "manualResume": "disabled",
                "mqttVersion": "3.1.1",
                "name": "mqtt",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/mqtt/~Common~mqtt?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 16,
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:mqtt:mqttcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/mqtt?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorMqtt(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorMqtt(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
