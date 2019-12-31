# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitornone
from genie.libs.parser.bigip.get_ltm_monitornone import LtmMonitorNone

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/none'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:none:nonecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/none?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:none:nonestate",
                    "name": "none",
                    "partition": "Common",
                    "fullPath": "/Common/none",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/none/~Common~none?ver=14.1.2.1",
                    "destination": "*:6666",
                    "ignoreDownResponse": "disabled",
                    "interval": 0,
                    "probeTimeout": 0,
                    "timeUntilUp": 86500,
                    "timeout": 0,
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitornone(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "destination": "*:6666",
                "fullPath": "/Common/none",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 0,
                "kind": "tm:ltm:monitor:none:nonestate",
                "name": "none",
                "partition": "Common",
                "probeTimeout": 0,
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/none/~Common~none?ver=14.1.2.1",
                "timeUntilUp": 86500,
                "timeout": 0,
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:none:nonecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/none?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorNone(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorNone(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
