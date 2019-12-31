# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilehttp_proxy_connect
from genie.libs.parser.bigip.get_ltm_profilehttp_proxy_connect import (
    LtmProfileHttpproxyconnect,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/http-proxy-connect'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:http-proxy-connect:http-proxy-connectcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/http-proxy-connect?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:http-proxy-connect:http-proxy-connectstate",
                    "name": "http-proxy-connect",
                    "partition": "Common",
                    "fullPath": "/Common/http-proxy-connect",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/http-proxy-connect/~Common~http-proxy-connect?ver=14.1.2.1",
                    "appService": "none",
                    "defaultState": "enabled",
                    "defaultsFrom": "none",
                    "description": "none",
                }
            ],
        }


class test_get_ltm_profilehttp_proxy_connect(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultState": "enabled",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/http-proxy-connect",
                "generation": 1,
                "kind": "tm:ltm:profile:http-proxy-connect:http-proxy-connectstate",
                "name": "http-proxy-connect",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/http-proxy-connect/~Common~http-proxy-connect?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:http-proxy-connect:http-proxy-connectcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/http-proxy-connect?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileHttpproxyconnect(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileHttpproxyconnect(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
