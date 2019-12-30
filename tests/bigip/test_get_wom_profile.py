# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_wom_profile
from genie.libs.parser.bigip.get_wom_profile import WomProfile

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/wom/profile'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:wom:profile:profilecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/wom/profile?ver=14.1.2.1",
            "items": [
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/wom/profile/isession?ver=14.1.2.1"
                    }
                }
            ],
        }


class test_get_wom_profile(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/wom/profile/isession?ver=14.1.2.1"
                }
            }
        ],
        "kind": "tm:wom:profile:profilecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/wom/profile?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = WomProfile(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = WomProfile(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
