# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorinband
from genie.libs.parser.bigip.get_ltm_monitorinband import LtmMonitorInband

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/inband'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:inband:inbandcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/inband?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:inband:inbandstate",
                    "name": "inband",
                    "partition": "Common",
                    "fullPath": "/Common/inband",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/inband/~Common~inband?ver=14.1.2.1",
                    "failureInterval": 30,
                    "failures": 3,
                    "responseTime": 10,
                    "retryTime": 300,
                }
            ],
        }


class test_get_ltm_monitorinband(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "failureInterval": 30,
                "failures": 3,
                "fullPath": "/Common/inband",
                "generation": 0,
                "kind": "tm:ltm:monitor:inband:inbandstate",
                "name": "inband",
                "partition": "Common",
                "responseTime": 10,
                "retryTime": 300,
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/inband/~Common~inband?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:monitor:inband:inbandcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/inband?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorInband(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorInband(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
