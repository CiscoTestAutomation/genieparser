# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitororacle
from genie.libs.parser.bigip.get_gtm_monitororacle import GtmMonitorOracle

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/oracle'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:oracle:oraclecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/oracle?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:oracle:oraclestate",
                    "name": "oracle",
                    "partition": "Common",
                    "fullPath": "/Common/oracle",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/oracle/~Common~oracle?ver=14.1.2.1",
                    "count": "0",
                    "debug": "no",
                    "destination": "*:*",
                    "ignoreDownResponse": "disabled",
                    "interval": 30,
                    "probeTimeout": 5,
                    "timeout": 91,
                }
            ],
        }


class test_get_gtm_monitororacle(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "count": "0",
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/oracle",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 30,
                "kind": "tm:gtm:monitor:oracle:oraclestate",
                "name": "oracle",
                "partition": "Common",
                "probeTimeout": 5,
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/oracle/~Common~oracle?ver=14.1.2.1",
                "timeout": 91,
            }
        ],
        "kind": "tm:gtm:monitor:oracle:oraclecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/oracle?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorOracle(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorOracle(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
