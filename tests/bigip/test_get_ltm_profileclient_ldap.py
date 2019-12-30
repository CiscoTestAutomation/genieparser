# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileclient_ldap
from genie.libs.parser.bigip.get_ltm_profileclient_ldap import (
    LtmProfileClientldap,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/client-ldap'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:client-ldap:client-ldapcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/client-ldap?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:client-ldap:client-ldapstate",
                    "name": "clientldap",
                    "partition": "Common",
                    "fullPath": "/Common/clientldap",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/client-ldap/~Common~clientldap?ver=14.1.2.1",
                    "activationMode": "require",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                }
            ],
        }


class test_get_ltm_profileclient_ldap(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "activationMode": "require",
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/clientldap",
                "generation": 1,
                "kind": "tm:ltm:profile:client-ldap:client-ldapstate",
                "name": "clientldap",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/client-ldap/~Common~clientldap?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:client-ldap:client-ldapcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/client-ldap?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileClientldap(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileClientldap(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
