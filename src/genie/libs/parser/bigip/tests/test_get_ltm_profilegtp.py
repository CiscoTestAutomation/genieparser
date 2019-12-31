# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilegtp
from genie.libs.parser.bigip.get_ltm_profilegtp import LtmProfileGtp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/gtp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:gtp:gtpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/gtp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:gtp:gtpstate",
                    "name": "gtp",
                    "partition": "Common",
                    "fullPath": "/Common/gtp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/gtp/~Common~gtp?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "ingressMax": 0,
                }
            ],
        }


class test_get_ltm_profilegtp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/gtp",
                "generation": 1,
                "ingressMax": 0,
                "kind": "tm:ltm:profile:gtp:gtpstate",
                "name": "gtp",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/gtp/~Common~gtp?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:gtp:gtpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/gtp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileGtp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileGtp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
