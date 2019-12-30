# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorfirepass
from genie.libs.parser.bigip.get_ltm_monitorfirepass import LtmMonitorFirepass

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/firepass'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:firepass:firepasscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/firepass?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:firepass:firepassstate",
                    "name": "firepass",
                    "partition": "Common",
                    "fullPath": "/Common/firepass",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/firepass/~Common~firepass?ver=14.1.2.1",
                    "cipherlist": "HIGH:!ADH",
                    "concurrencyLimit": 95,
                    "destination": "*:*",
                    "interval": 5,
                    "maxLoadAverage": 12,
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "upInterval": 0,
                    "username": "gtmuser",
                }
            ],
        }


class test_get_ltm_monitorfirepass(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "cipherlist": "HIGH:!ADH",
                "concurrencyLimit": 95,
                "destination": "*:*",
                "fullPath": "/Common/firepass",
                "generation": 0,
                "interval": 5,
                "kind": "tm:ltm:monitor:firepass:firepassstate",
                "maxLoadAverage": 12,
                "name": "firepass",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/firepass/~Common~firepass?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 16,
                "upInterval": 0,
                "username": "gtmuser",
            }
        ],
        "kind": "tm:ltm:monitor:firepass:firepasscollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/firepass?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorFirepass(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorFirepass(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
