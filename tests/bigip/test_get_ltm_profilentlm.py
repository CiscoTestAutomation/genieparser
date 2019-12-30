# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilentlm
from genie.libs.parser.bigip.get_ltm_profilentlm import LtmProfileNtlm

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/ntlm'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:ntlm:ntlmcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/ntlm?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:ntlm:ntlmstate",
                    "name": "ntlm",
                    "partition": "Common",
                    "fullPath": "/Common/ntlm",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/ntlm/~Common~ntlm?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "insertCookieDomain": "none",
                    "insertCookieName": "NTLMconnpool",
                    "insertCookiePassphrase": "mypassphrase",
                    "keyByCookie": "disabled",
                    "keyByCookieName": "mycookie",
                    "keyByDomain": "disabled",
                    "keyByIpAddress": "disabled",
                    "keyByTarget": "disabled",
                    "keyByUser": "enabled",
                    "keyByWorkstation": "disabled",
                }
            ],
        }


class test_get_ltm_profilentlm(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/ntlm",
                "generation": 0,
                "insertCookieDomain": "none",
                "insertCookieName": "NTLMconnpool",
                "insertCookiePassphrase": "mypassphrase",
                "keyByCookie": "disabled",
                "keyByCookieName": "mycookie",
                "keyByDomain": "disabled",
                "keyByIpAddress": "disabled",
                "keyByTarget": "disabled",
                "keyByUser": "enabled",
                "keyByWorkstation": "disabled",
                "kind": "tm:ltm:profile:ntlm:ntlmstate",
                "name": "ntlm",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/ntlm/~Common~ntlm?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:ntlm:ntlmcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/ntlm?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileNtlm(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileNtlm(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
