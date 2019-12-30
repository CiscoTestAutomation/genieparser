# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitorfirepass
from genie.libs.parser.bigip.get_gtm_monitorfirepass import GtmMonitorFirepass

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/firepass'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:firepass:firepasscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/firepass?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:firepass:firepassstate",
                    "name": "firepass_gtm",
                    "partition": "Common",
                    "fullPath": "/Common/firepass_gtm",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/firepass/~Common~firepass_gtm?ver=14.1.2.1",
                    "cipherlist": "HIGH:!ADH",
                    "concurrencyLimit": 95,
                    "destination": "*:*",
                    "ignoreDownResponse": "disabled",
                    "interval": 30,
                    "maxLoadAverage": 12,
                    "probeTimeout": 5,
                    "timeout": 90,
                    "username": "gtmuser",
                }
            ],
        }


class test_get_gtm_monitorfirepass(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "cipherlist": "HIGH:!ADH",
                "concurrencyLimit": 95,
                "destination": "*:*",
                "fullPath": "/Common/firepass_gtm",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 30,
                "kind": "tm:gtm:monitor:firepass:firepassstate",
                "maxLoadAverage": 12,
                "name": "firepass_gtm",
                "partition": "Common",
                "probeTimeout": 5,
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/firepass/~Common~firepass_gtm?ver=14.1.2.1",
                "timeout": 90,
                "username": "gtmuser",
            }
        ],
        "kind": "tm:gtm:monitor:firepass:firepasscollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/firepass?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorFirepass(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorFirepass(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
