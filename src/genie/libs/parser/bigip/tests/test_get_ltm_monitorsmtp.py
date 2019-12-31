# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorsmtp
from genie.libs.parser.bigip.get_ltm_monitorsmtp import LtmMonitorSmtp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/smtp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:smtp:smtpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/smtp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:smtp:smtpstate",
                    "name": "smtp",
                    "partition": "Common",
                    "fullPath": "/Common/smtp",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/smtp/~Common~smtp?ver=14.1.2.1",
                    "debug": "no",
                    "destination": "*:*",
                    "interval": 5,
                    "manualResume": "disabled",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitorsmtp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/smtp",
                "generation": 0,
                "interval": 5,
                "kind": "tm:ltm:monitor:smtp:smtpstate",
                "manualResume": "disabled",
                "name": "smtp",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/smtp/~Common~smtp?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 16,
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:smtp:smtpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/smtp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorSmtp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorSmtp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
