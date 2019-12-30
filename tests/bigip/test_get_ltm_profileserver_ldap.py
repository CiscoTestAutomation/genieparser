# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileserver_ldap
from genie.libs.parser.bigip.get_ltm_profileserver_ldap import (
    LtmProfileServerldap,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/server-ldap'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:server-ldap:server-ldapcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/server-ldap?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:server-ldap:server-ldapstate",
                    "name": "serverldap",
                    "partition": "Common",
                    "fullPath": "/Common/serverldap",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/server-ldap/~Common~serverldap?ver=14.1.2.1",
                    "activationMode": "none",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                }
            ],
        }


class test_get_ltm_profileserver_ldap(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "activationMode": "none",
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/serverldap",
                "generation": 1,
                "kind": "tm:ltm:profile:server-ldap:server-ldapstate",
                "name": "serverldap",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/server-ldap/~Common~serverldap?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:server-ldap:server-ldapcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/server-ldap?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileServerldap(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileServerldap(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
