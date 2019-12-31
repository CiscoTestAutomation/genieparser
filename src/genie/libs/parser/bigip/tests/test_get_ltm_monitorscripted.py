# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorscripted
from genie.libs.parser.bigip.get_ltm_monitorscripted import LtmMonitorScripted

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/scripted'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:scripted:scriptedcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/scripted?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:scripted:scriptedstate",
                    "name": "scripted",
                    "partition": "Common",
                    "fullPath": "/Common/scripted",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/scripted/~Common~scripted?ver=14.1.2.1",
                    "debug": "no",
                    "destination": "*:*",
                    "interval": 10,
                    "manualResume": "disabled",
                    "timeUntilUp": 0,
                    "timeout": 31,
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitorscripted(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/scripted",
                "generation": 0,
                "interval": 10,
                "kind": "tm:ltm:monitor:scripted:scriptedstate",
                "manualResume": "disabled",
                "name": "scripted",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/scripted/~Common~scripted?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 31,
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:scripted:scriptedcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/scripted?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorScripted(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorScripted(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
