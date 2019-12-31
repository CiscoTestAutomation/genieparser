# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitorsip
from genie.libs.parser.bigip.get_gtm_monitorsip import GtmMonitorSip

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/sip'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:sip:sipcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/sip?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:sip:sipstate",
                    "name": "sip",
                    "partition": "Common",
                    "fullPath": "/Common/sip",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/sip/~Common~sip?ver=14.1.2.1",
                    "compatibility": "enabled",
                    "debug": "no",
                    "destination": "*:*",
                    "ignoreDownResponse": "disabled",
                    "interval": 30,
                    "mode": "udp",
                    "probeTimeout": 5,
                    "timeout": 120,
                }
            ],
        }


class test_get_gtm_monitorsip(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "compatibility": "enabled",
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/sip",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 30,
                "kind": "tm:gtm:monitor:sip:sipstate",
                "mode": "udp",
                "name": "sip",
                "partition": "Common",
                "probeTimeout": 5,
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/sip/~Common~sip?ver=14.1.2.1",
                "timeout": 120,
            }
        ],
        "kind": "tm:gtm:monitor:sip:sipcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/sip?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorSip(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorSip(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
