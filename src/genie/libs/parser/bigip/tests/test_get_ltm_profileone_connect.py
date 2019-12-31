# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileone_connect
from genie.libs.parser.bigip.get_ltm_profileone_connect import (
    LtmProfileOneconnect,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/one-connect'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:one-connect:one-connectcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/one-connect?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:one-connect:one-connectstate",
                    "name": "oneconnect",
                    "partition": "Common",
                    "fullPath": "/Common/oneconnect",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/one-connect/~Common~oneconnect?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "idleTimeoutOverride": "disabled",
                    "limitType": "none",
                    "maxAge": 86400,
                    "maxReuse": 1000,
                    "maxSize": 10000,
                    "sharePools": "disabled",
                    "sourceMask": "any",
                }
            ],
        }


class test_get_ltm_profileone_connect(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/oneconnect",
                "generation": 1,
                "idleTimeoutOverride": "disabled",
                "kind": "tm:ltm:profile:one-connect:one-connectstate",
                "limitType": "none",
                "maxAge": 86400,
                "maxReuse": 1000,
                "maxSize": 10000,
                "name": "oneconnect",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/one-connect/~Common~oneconnect?ver=14.1.2.1",
                "sharePools": "disabled",
                "sourceMask": "any",
            }
        ],
        "kind": "tm:ltm:profile:one-connect:one-connectcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/one-connect?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileOneconnect(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileOneconnect(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
