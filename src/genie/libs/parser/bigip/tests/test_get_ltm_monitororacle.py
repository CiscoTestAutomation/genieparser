# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitororacle
from genie.libs.parser.bigip.get_ltm_monitororacle import LtmMonitorOracle

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/oracle'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:oracle:oraclecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/oracle?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:oracle:oraclestate",
                    "name": "oracle",
                    "partition": "Common",
                    "fullPath": "/Common/oracle",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/oracle/~Common~oracle?ver=14.1.2.1",
                    "count": "0",
                    "database": "%node_ip%:%node_port%:",
                    "debug": "no",
                    "destination": "*:*",
                    "interval": 30,
                    "manualResume": "disabled",
                    "timeUntilUp": 0,
                    "timeout": 91,
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitororacle(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "count": "0",
                "database": "%node_ip%:%node_port%:",
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/oracle",
                "generation": 0,
                "interval": 30,
                "kind": "tm:ltm:monitor:oracle:oraclestate",
                "manualResume": "disabled",
                "name": "oracle",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/oracle/~Common~oracle?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 91,
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:oracle:oraclecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/oracle?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorOracle(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorOracle(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
