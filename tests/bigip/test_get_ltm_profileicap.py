# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileicap
from genie.libs.parser.bigip.get_ltm_profileicap import LtmProfileIcap

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/icap'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:icap:icapcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/icap?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:icap:icapstate",
                    "name": "icap",
                    "partition": "Common",
                    "fullPath": "/Common/icap",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/icap/~Common~icap?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "headerFrom": "none",
                    "host": "none",
                    "previewLength": 0,
                    "referer": "none",
                    "uri": "none",
                    "userAgent": "none",
                }
            ],
        }


class test_get_ltm_profileicap(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "fullPath": "/Common/icap",
                "generation": 1,
                "headerFrom": "none",
                "host": "none",
                "kind": "tm:ltm:profile:icap:icapstate",
                "name": "icap",
                "partition": "Common",
                "previewLength": 0,
                "referer": "none",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/icap/~Common~icap?ver=14.1.2.1",
                "uri": "none",
                "userAgent": "none",
            }
        ],
        "kind": "tm:ltm:profile:icap:icapcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/icap?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileIcap(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileIcap(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
