# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileresponse_adapt
from genie.libs.parser.bigip.get_ltm_profileresponse_adapt import (
    LtmProfileResponseadapt,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/response-adapt'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:response-adapt:response-adaptcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/response-adapt?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:response-adapt:response-adaptstate",
                    "name": "responseadapt",
                    "partition": "Common",
                    "fullPath": "/Common/responseadapt",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/response-adapt/~Common~responseadapt?ver=14.1.2.1",
                    "allowHttp_10": "no",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "enabled": "yes",
                    "internalVirtual": "none",
                    "previewSize": 1024,
                    "serviceDownAction": "ignore",
                    "timeout": 0,
                }
            ],
        }


class test_get_ltm_profileresponse_adapt(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "allowHttp_10": "no",
                "appService": "none",
                "defaultsFrom": "none",
                "enabled": "yes",
                "fullPath": "/Common/responseadapt",
                "generation": 1,
                "internalVirtual": "none",
                "kind": "tm:ltm:profile:response-adapt:response-adaptstate",
                "name": "responseadapt",
                "partition": "Common",
                "previewSize": 1024,
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/response-adapt/~Common~responseadapt?ver=14.1.2.1",
                "serviceDownAction": "ignore",
                "timeout": 0,
            }
        ],
        "kind": "tm:ltm:profile:response-adapt:response-adaptcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/response-adapt?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileResponseadapt(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileResponseadapt(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
