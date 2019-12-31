# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitordiameter
from genie.libs.parser.bigip.get_ltm_monitordiameter import LtmMonitorDiameter

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/diameter'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:diameter:diametercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/diameter?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:diameter:diameterstate",
                    "name": "diameter",
                    "partition": "Common",
                    "fullPath": "/Common/diameter",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/diameter/~Common~diameter?ver=14.1.2.1",
                    "interval": 10,
                    "manualResume": "disabled",
                    "originRealm": "f5.com",
                    "productName": "F5 BIGIP Diameter Health Monitoring",
                    "timeUntilUp": 0,
                    "timeout": 31,
                    "upInterval": 0,
                    "vendorId": "3375",
                }
            ],
        }


class test_get_ltm_monitordiameter(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/diameter",
                "generation": 0,
                "interval": 10,
                "kind": "tm:ltm:monitor:diameter:diameterstate",
                "manualResume": "disabled",
                "name": "diameter",
                "originRealm": "f5.com",
                "partition": "Common",
                "productName": "F5 BIGIP Diameter Health Monitoring",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/diameter/~Common~diameter?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 31,
                "upInterval": 0,
                "vendorId": "3375",
            }
        ],
        "kind": "tm:ltm:monitor:diameter:diametercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/diameter?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorDiameter(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorDiameter(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
