# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitormodule_score
from genie.libs.parser.bigip.get_ltm_monitormodule_score import (
    LtmMonitorModulescore,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/module-score'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:module-score:module-scorecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/module-score?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:module-score:module-scorestate",
                    "name": "module_score",
                    "partition": "Common",
                    "fullPath": "/Common/module_score",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/module-score/~Common~module_score?ver=14.1.2.1",
                    "debug": "no",
                    "interval": 10,
                    "snmpCommunity": "public",
                    "snmpPort": 161,
                    "snmpVersion": "v2c",
                    "timeUntilUp": 0,
                    "timeout": 30,
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitormodule_score(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "debug": "no",
                "fullPath": "/Common/module_score",
                "generation": 0,
                "interval": 10,
                "kind": "tm:ltm:monitor:module-score:module-scorestate",
                "name": "module_score",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/module-score/~Common~module_score?ver=14.1.2.1",
                "snmpCommunity": "public",
                "snmpPort": 161,
                "snmpVersion": "v2c",
                "timeUntilUp": 0,
                "timeout": 30,
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:module-score:module-scorecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/module-score?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorModulescore(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorModulescore(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
