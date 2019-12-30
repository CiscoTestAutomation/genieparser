# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_persistencecookie
from genie.libs.parser.bigip.get_ltm_persistencecookie import (
    LtmPersistenceCookie,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/persistence/cookie'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:persistence:cookie:cookiecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/persistence/cookie?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:persistence:cookie:cookiestate",
                    "name": "cookie",
                    "partition": "Common",
                    "fullPath": "/Common/cookie",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/persistence/cookie/~Common~cookie?ver=14.1.2.1",
                    "alwaysSend": "disabled",
                    "appService": "none",
                    "cookieEncryption": "disabled",
                    "cookieName": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "encryptCookiePoolname": "disabled",
                    "expiration": "0",
                    "hashLength": 0,
                    "hashOffset": 0,
                    "httponly": "enabled",
                    "matchAcrossPools": "disabled",
                    "matchAcrossServices": "disabled",
                    "matchAcrossVirtuals": "disabled",
                    "method": "insert",
                    "mirror": "disabled",
                    "overrideConnectionLimit": "disabled",
                    "secure": "enabled",
                    "timeout": "180",
                }
            ],
        }


class test_get_ltm_persistencecookie(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "alwaysSend": "disabled",
                "appService": "none",
                "cookieEncryption": "disabled",
                "cookieName": "none",
                "defaultsFrom": "none",
                "description": "none",
                "encryptCookiePoolname": "disabled",
                "expiration": "0",
                "fullPath": "/Common/cookie",
                "generation": 1,
                "hashLength": 0,
                "hashOffset": 0,
                "httponly": "enabled",
                "kind": "tm:ltm:persistence:cookie:cookiestate",
                "matchAcrossPools": "disabled",
                "matchAcrossServices": "disabled",
                "matchAcrossVirtuals": "disabled",
                "method": "insert",
                "mirror": "disabled",
                "name": "cookie",
                "overrideConnectionLimit": "disabled",
                "partition": "Common",
                "secure": "enabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/persistence/cookie/~Common~cookie?ver=14.1.2.1",
                "timeout": "180",
            }
        ],
        "kind": "tm:ltm:persistence:cookie:cookiecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/persistence/cookie?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmPersistenceCookie(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmPersistenceCookie(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
