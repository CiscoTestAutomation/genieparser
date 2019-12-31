# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_authprofile
from genie.libs.parser.bigip.get_ltm_authprofile import LtmAuthProfile

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/auth/profile'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:auth:profile:profilecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:auth:profile:profilestate",
                    "name": "krbdelegate",
                    "partition": "Common",
                    "fullPath": "/Common/krbdelegate",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~krbdelegate?ver=14.1.2.1",
                    "cookieKey": "abc123",
                    "cookieName": "f5auth",
                    "credentialSource": "http-basic-auth",
                    "enabled": "yes",
                    "fileName": "tmm_commonkrbdelegate1",
                    "idleTimeout": 300,
                    "type": "krbdelegate",
                },
                {
                    "kind": "tm:ltm:auth:profile:profilestate",
                    "name": "ldap",
                    "partition": "Common",
                    "fullPath": "/Common/ldap",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~ldap?ver=14.1.2.1",
                    "cookieKey": "abc123",
                    "cookieName": "f5auth",
                    "credentialSource": "http-basic-auth",
                    "enabled": "yes",
                    "fileName": "tmm_commonldap1",
                    "idleTimeout": 300,
                    "rule": "/Common/_sys_auth_ldap",
                    "ruleReference": {
                        "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ldap?ver=14.1.2.1"
                    },
                    "type": "ldap",
                },
                {
                    "kind": "tm:ltm:auth:profile:profilestate",
                    "name": "radius",
                    "partition": "Common",
                    "fullPath": "/Common/radius",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~radius?ver=14.1.2.1",
                    "cookieKey": "abc123",
                    "cookieName": "f5auth",
                    "credentialSource": "http-basic-auth",
                    "enabled": "yes",
                    "fileName": "tmm_commonradius1",
                    "idleTimeout": 300,
                    "rule": "/Common/_sys_auth_radius",
                    "ruleReference": {
                        "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_radius?ver=14.1.2.1"
                    },
                    "type": "radius",
                },
                {
                    "kind": "tm:ltm:auth:profile:profilestate",
                    "name": "ssl_cc_ldap",
                    "partition": "Common",
                    "fullPath": "/Common/ssl_cc_ldap",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~ssl_cc_ldap?ver=14.1.2.1",
                    "cookieKey": "abc123",
                    "cookieName": "f5auth",
                    "credentialSource": "http-basic-auth",
                    "enabled": "yes",
                    "fileName": "tmm_commonsslccldap1",
                    "idleTimeout": 300,
                    "rule": "/Common/_sys_auth_ssl_cc_ldap",
                    "ruleReference": {
                        "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_cc_ldap?ver=14.1.2.1"
                    },
                    "type": "ssl-cc-ldap",
                },
                {
                    "kind": "tm:ltm:auth:profile:profilestate",
                    "name": "ssl_crldp",
                    "partition": "Common",
                    "fullPath": "/Common/ssl_crldp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~ssl_crldp?ver=14.1.2.1",
                    "cookieKey": "abc123",
                    "cookieName": "f5auth",
                    "credentialSource": "http-basic-auth",
                    "enabled": "yes",
                    "fileName": "tmm_commonsslcrldp1",
                    "idleTimeout": 300,
                    "rule": "/Common/_sys_auth_ssl_crldp",
                    "ruleReference": {
                        "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_crldp?ver=14.1.2.1"
                    },
                    "type": "ssl-crldp",
                },
                {
                    "kind": "tm:ltm:auth:profile:profilestate",
                    "name": "ssl_ocsp",
                    "partition": "Common",
                    "fullPath": "/Common/ssl_ocsp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~ssl_ocsp?ver=14.1.2.1",
                    "cookieKey": "abc123",
                    "cookieName": "f5auth",
                    "credentialSource": "http-basic-auth",
                    "enabled": "yes",
                    "fileName": "tmm_commonsslocsp1",
                    "idleTimeout": 300,
                    "rule": "/Common/_sys_auth_ssl_ocsp",
                    "ruleReference": {
                        "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_ocsp?ver=14.1.2.1"
                    },
                    "type": "ssl-ocsp",
                },
                {
                    "kind": "tm:ltm:auth:profile:profilestate",
                    "name": "tacacs",
                    "partition": "Common",
                    "fullPath": "/Common/tacacs",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~tacacs?ver=14.1.2.1",
                    "cookieKey": "abc123",
                    "cookieName": "f5auth",
                    "credentialSource": "http-basic-auth",
                    "enabled": "yes",
                    "fileName": "tmm_commontacacs1",
                    "idleTimeout": 300,
                    "rule": "/Common/_sys_auth_tacacs",
                    "ruleReference": {
                        "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_tacacs?ver=14.1.2.1"
                    },
                    "type": "tacacs",
                },
            ],
        }


class test_get_ltm_authprofile(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "cookieKey": "abc123",
                "cookieName": "f5auth",
                "credentialSource": "http-basic-auth",
                "enabled": "yes",
                "fileName": "tmm_commonkrbdelegate1",
                "fullPath": "/Common/krbdelegate",
                "generation": 1,
                "idleTimeout": 300,
                "kind": "tm:ltm:auth:profile:profilestate",
                "name": "krbdelegate",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~krbdelegate?ver=14.1.2.1",
                "type": "krbdelegate",
            },
            {
                "cookieKey": "abc123",
                "cookieName": "f5auth",
                "credentialSource": "http-basic-auth",
                "enabled": "yes",
                "fileName": "tmm_commonldap1",
                "fullPath": "/Common/ldap",
                "generation": 1,
                "idleTimeout": 300,
                "kind": "tm:ltm:auth:profile:profilestate",
                "name": "ldap",
                "partition": "Common",
                "rule": "/Common/_sys_auth_ldap",
                "ruleReference": {
                    "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ldap?ver=14.1.2.1"
                },
                "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~ldap?ver=14.1.2.1",
                "type": "ldap",
            },
            {
                "cookieKey": "abc123",
                "cookieName": "f5auth",
                "credentialSource": "http-basic-auth",
                "enabled": "yes",
                "fileName": "tmm_commonradius1",
                "fullPath": "/Common/radius",
                "generation": 1,
                "idleTimeout": 300,
                "kind": "tm:ltm:auth:profile:profilestate",
                "name": "radius",
                "partition": "Common",
                "rule": "/Common/_sys_auth_radius",
                "ruleReference": {
                    "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_radius?ver=14.1.2.1"
                },
                "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~radius?ver=14.1.2.1",
                "type": "radius",
            },
            {
                "cookieKey": "abc123",
                "cookieName": "f5auth",
                "credentialSource": "http-basic-auth",
                "enabled": "yes",
                "fileName": "tmm_commonsslccldap1",
                "fullPath": "/Common/ssl_cc_ldap",
                "generation": 1,
                "idleTimeout": 300,
                "kind": "tm:ltm:auth:profile:profilestate",
                "name": "ssl_cc_ldap",
                "partition": "Common",
                "rule": "/Common/_sys_auth_ssl_cc_ldap",
                "ruleReference": {
                    "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_cc_ldap?ver=14.1.2.1"
                },
                "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~ssl_cc_ldap?ver=14.1.2.1",
                "type": "ssl-cc-ldap",
            },
            {
                "cookieKey": "abc123",
                "cookieName": "f5auth",
                "credentialSource": "http-basic-auth",
                "enabled": "yes",
                "fileName": "tmm_commonsslcrldp1",
                "fullPath": "/Common/ssl_crldp",
                "generation": 1,
                "idleTimeout": 300,
                "kind": "tm:ltm:auth:profile:profilestate",
                "name": "ssl_crldp",
                "partition": "Common",
                "rule": "/Common/_sys_auth_ssl_crldp",
                "ruleReference": {
                    "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_crldp?ver=14.1.2.1"
                },
                "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~ssl_crldp?ver=14.1.2.1",
                "type": "ssl-crldp",
            },
            {
                "cookieKey": "abc123",
                "cookieName": "f5auth",
                "credentialSource": "http-basic-auth",
                "enabled": "yes",
                "fileName": "tmm_commonsslocsp1",
                "fullPath": "/Common/ssl_ocsp",
                "generation": 1,
                "idleTimeout": 300,
                "kind": "tm:ltm:auth:profile:profilestate",
                "name": "ssl_ocsp",
                "partition": "Common",
                "rule": "/Common/_sys_auth_ssl_ocsp",
                "ruleReference": {
                    "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_ocsp?ver=14.1.2.1"
                },
                "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~ssl_ocsp?ver=14.1.2.1",
                "type": "ssl-ocsp",
            },
            {
                "cookieKey": "abc123",
                "cookieName": "f5auth",
                "credentialSource": "http-basic-auth",
                "enabled": "yes",
                "fileName": "tmm_commontacacs1",
                "fullPath": "/Common/tacacs",
                "generation": 1,
                "idleTimeout": 300,
                "kind": "tm:ltm:auth:profile:profilestate",
                "name": "tacacs",
                "partition": "Common",
                "rule": "/Common/_sys_auth_tacacs",
                "ruleReference": {
                    "link": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_tacacs?ver=14.1.2.1"
                },
                "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile/~Common~tacacs?ver=14.1.2.1",
                "type": "tacacs",
            },
        ],
        "kind": "tm:ltm:auth:profile:profilecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/auth/profile?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmAuthProfile(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmAuthProfile(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
