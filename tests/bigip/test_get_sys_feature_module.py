# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_feature_module
from genie.libs.parser.bigip.get_sys_feature_module import SysFeaturemodule

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/feature-module'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:feature-module:feature-modulecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/feature-module?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:feature-module:feature-modulestate",
                    "name": "cgnat",
                    "fullPath": "cgnat",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/feature-module/cgnat?ver=14.1.2.1",
                    "disabled": True,
                }
            ],
        }


class test_get_sys_feature_module(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "disabled": True,
                "fullPath": "cgnat",
                "generation": 1,
                "kind": "tm:sys:feature-module:feature-modulestate",
                "name": "cgnat",
                "selfLink": "https://localhost/mgmt/tm/sys/feature-module/cgnat?ver=14.1.2.1",
            }
        ],
        "kind": "tm:sys:feature-module:feature-modulecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/feature-module?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysFeaturemodule(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysFeaturemodule(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
