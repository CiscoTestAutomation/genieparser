# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitorwap
from genie.libs.parser.bigip.get_gtm_monitorwap import GtmMonitorWap

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/wap'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:wap:wapcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/wap?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:wap:wapstate",
                    "name": "wap",
                    "partition": "Common",
                    "fullPath": "/Common/wap",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/wap/~Common~wap?ver=14.1.2.1",
                    "debug": "no",
                    "destination": "*:*",
                    "ignoreDownResponse": "disabled",
                    "interval": 10,
                    "probeTimeout": 5,
                    "timeout": 31,
                }
            ],
        }


class test_get_gtm_monitorwap(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/wap",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 10,
                "kind": "tm:gtm:monitor:wap:wapstate",
                "name": "wap",
                "partition": "Common",
                "probeTimeout": 5,
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/wap/~Common~wap?ver=14.1.2.1",
                "timeout": 31,
            }
        ],
        "kind": "tm:gtm:monitor:wap:wapcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/wap?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorWap(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorWap(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
