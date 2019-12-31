# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilefasthttp
from genie.libs.parser.bigip.get_ltm_profilefasthttp import LtmProfileFasthttp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/fasthttp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:fasthttp:fasthttpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/fasthttp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:fasthttp:fasthttpstate",
                    "name": "fasthttp",
                    "partition": "Common",
                    "fullPath": "/Common/fasthttp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/fasthttp/~Common~fasthttp?ver=14.1.2.1",
                    "appService": "none",
                    "clientCloseTimeout": 5,
                    "connpoolIdleTimeoutOverride": 0,
                    "connpoolMaxReuse": 0,
                    "connpoolMaxSize": 2048,
                    "connpoolMinSize": 0,
                    "connpoolReplenish": "enabled",
                    "connpoolStep": 4,
                    "defaultsFrom": "none",
                    "description": "none",
                    "forceHttp_10Response": "disabled",
                    "hardwareSynCookie": "disabled",
                    "headerInsert": "none",
                    "http_11CloseWorkarounds": "disabled",
                    "idleTimeout": 300,
                    "insertXforwardedFor": "disabled",
                    "layer_7": "enabled",
                    "maxHeaderSize": 32768,
                    "maxRequests": 0,
                    "mssOverride": 0,
                    "receiveWindowSize": 0,
                    "resetOnTimeout": "enabled",
                    "serverCloseTimeout": 5,
                    "serverSack": "disabled",
                    "serverTimestamp": "disabled",
                    "uncleanShutdown": "disabled",
                }
            ],
        }


class test_get_ltm_profilefasthttp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "clientCloseTimeout": 5,
                "connpoolIdleTimeoutOverride": 0,
                "connpoolMaxReuse": 0,
                "connpoolMaxSize": 2048,
                "connpoolMinSize": 0,
                "connpoolReplenish": "enabled",
                "connpoolStep": 4,
                "defaultsFrom": "none",
                "description": "none",
                "forceHttp_10Response": "disabled",
                "fullPath": "/Common/fasthttp",
                "generation": 1,
                "hardwareSynCookie": "disabled",
                "headerInsert": "none",
                "http_11CloseWorkarounds": "disabled",
                "idleTimeout": 300,
                "insertXforwardedFor": "disabled",
                "kind": "tm:ltm:profile:fasthttp:fasthttpstate",
                "layer_7": "enabled",
                "maxHeaderSize": 32768,
                "maxRequests": 0,
                "mssOverride": 0,
                "name": "fasthttp",
                "partition": "Common",
                "receiveWindowSize": 0,
                "resetOnTimeout": "enabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/fasthttp/~Common~fasthttp?ver=14.1.2.1",
                "serverCloseTimeout": 5,
                "serverSack": "disabled",
                "serverTimestamp": "disabled",
                "uncleanShutdown": "disabled",
            }
        ],
        "kind": "tm:ltm:profile:fasthttp:fasthttpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/fasthttp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileFasthttp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileFasthttp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
