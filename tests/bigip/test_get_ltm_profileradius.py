# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileradius
from genie.libs.parser.bigip.get_ltm_profileradius import LtmProfileRadius

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/radius'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:radius:radiuscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/radius?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:radius:radiusstate",
                    "name": "radiusLB",
                    "partition": "Common",
                    "fullPath": "/Common/radiusLB",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/radius/~Common~radiusLB?ver=14.1.2.1",
                    "appService": "none",
                    "clients": [],
                    "defaultsFrom": "none",
                    "description": "none",
                    "persistAvp": "none",
                },
                {
                    "kind": "tm:ltm:profile:radius:radiusstate",
                    "name": "radiusLB-subscriber-aware",
                    "partition": "Common",
                    "fullPath": "/Common/radiusLB-subscriber-aware",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/radius/~Common~radiusLB-subscriber-aware?ver=14.1.2.1",
                    "appService": "none",
                    "clients": [],
                    "defaultsFrom": "/Common/radiusLB",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/radius/~Common~radiusLB?ver=14.1.2.1"
                    },
                    "description": "none",
                    "persistAvp": "none",
                },
            ],
        }


class test_get_ltm_profileradius(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "clients": [],
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/radiusLB",
                "generation": 1,
                "kind": "tm:ltm:profile:radius:radiusstate",
                "name": "radiusLB",
                "partition": "Common",
                "persistAvp": "none",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/radius/~Common~radiusLB?ver=14.1.2.1",
            },
            {
                "appService": "none",
                "clients": [],
                "defaultsFrom": "/Common/radiusLB",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/radius/~Common~radiusLB?ver=14.1.2.1"
                },
                "description": "none",
                "fullPath": "/Common/radiusLB-subscriber-aware",
                "generation": 1,
                "kind": "tm:ltm:profile:radius:radiusstate",
                "name": "radiusLB-subscriber-aware",
                "partition": "Common",
                "persistAvp": "none",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/radius/~Common~radiusLB-subscriber-aware?ver=14.1.2.1",
            },
        ],
        "kind": "tm:ltm:profile:radius:radiuscollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/radius?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileRadius(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileRadius(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
