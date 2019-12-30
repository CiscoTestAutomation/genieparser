# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorsip
from genie.libs.parser.bigip.get_ltm_monitorsip import LtmMonitorSip

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/sip'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:sip:sipcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/sip?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:sip:sipstate",
                    "name": "sip",
                    "partition": "Common",
                    "fullPath": "/Common/sip",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/sip/~Common~sip?ver=14.1.2.1",
                    "cipherlist": "DEFAULT:+SHA:+3DES:+kEDH",
                    "compatibility": "enabled",
                    "debug": "no",
                    "destination": "*:*",
                    "interval": 5,
                    "manualResume": "disabled",
                    "mode": "udp",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitorsip(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "cipherlist": "DEFAULT:+SHA:+3DES:+kEDH",
                "compatibility": "enabled",
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/sip",
                "generation": 0,
                "interval": 5,
                "kind": "tm:ltm:monitor:sip:sipstate",
                "manualResume": "disabled",
                "mode": "udp",
                "name": "sip",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/sip/~Common~sip?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 16,
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:sip:sipcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/sip?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorSip(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorSip(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
