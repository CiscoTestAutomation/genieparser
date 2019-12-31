# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorsasp
from genie.libs.parser.bigip.get_ltm_monitorsasp import LtmMonitorSasp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/sasp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:sasp:saspcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/sasp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:sasp:saspstate",
                    "name": "sasp",
                    "partition": "Common",
                    "fullPath": "/Common/sasp",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/sasp/~Common~sasp?ver=14.1.2.1",
                    "interval": "auto",
                    "mode": "push",
                    "protocol": "tcp",
                    "service": "3860",
                    "timeUntilUp": 0,
                }
            ],
        }


class test_get_ltm_monitorsasp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/sasp",
                "generation": 0,
                "interval": "auto",
                "kind": "tm:ltm:monitor:sasp:saspstate",
                "mode": "push",
                "name": "sasp",
                "partition": "Common",
                "protocol": "tcp",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/sasp/~Common~sasp?ver=14.1.2.1",
                "service": "3860",
                "timeUntilUp": 0,
            }
        ],
        "kind": "tm:ltm:monitor:sasp:saspcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/sasp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorSasp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorSasp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
