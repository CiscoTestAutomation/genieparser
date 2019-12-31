# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilerewrite
from genie.libs.parser.bigip.get_ltm_profilerewrite import LtmProfileRewrite

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/rewrite'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:rewrite:rewritecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/rewrite?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:rewrite:rewritestate",
                    "name": "rewrite",
                    "partition": "Common",
                    "fullPath": "/Common/rewrite",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite?ver=14.1.2.1",
                    "appService": "none",
                    "bypassList": [],
                    "clientCachingType": "cache-css-js",
                    "defaultsFrom": "none",
                    "javaCaFile": "/Common/ca-bundle.crt",
                    "javaCaFileReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt?ver=14.1.2.1"
                    },
                    "javaCrl": "none",
                    "javaSignKey": "/Common/default.key",
                    "javaSignKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key?ver=14.1.2.1"
                    },
                    "javaSigner": "/Common/default.crt",
                    "javaSignerReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt?ver=14.1.2.1"
                    },
                    "locationSpecific": "false",
                    "request": {
                        "insertXforwardedFor": "enabled",
                        "insertXforwardedHost": "disabled",
                        "insertXforwardedProto": "disabled",
                        "rewriteHeaders": "enabled",
                    },
                    "response": {
                        "rewriteContent": "enabled",
                        "rewriteHeaders": "enabled",
                    },
                    "rewriteList": [],
                    "rewriteMode": "portal",
                    "splitTunneling": "false",
                    "uriRulesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite/uri-rules?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:ltm:profile:rewrite:rewritestate",
                    "name": "rewrite-portal",
                    "partition": "Common",
                    "fullPath": "/Common/rewrite-portal",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite-portal?ver=14.1.2.1",
                    "appService": "none",
                    "bypassList": [],
                    "clientCachingType": "cache-css-js",
                    "defaultsFrom": "/Common/rewrite",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite?ver=14.1.2.1"
                    },
                    "javaCaFile": "/Common/ca-bundle.crt",
                    "javaCaFileReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt?ver=14.1.2.1"
                    },
                    "javaCrl": "none",
                    "javaSignKey": "/Common/default.key",
                    "javaSignKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key?ver=14.1.2.1"
                    },
                    "javaSigner": "/Common/default.crt",
                    "javaSignerReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt?ver=14.1.2.1"
                    },
                    "locationSpecific": "false",
                    "request": {
                        "insertXforwardedFor": "enabled",
                        "insertXforwardedHost": "disabled",
                        "insertXforwardedProto": "disabled",
                        "rewriteHeaders": "enabled",
                    },
                    "response": {
                        "rewriteContent": "enabled",
                        "rewriteHeaders": "enabled",
                    },
                    "rewriteList": [],
                    "rewriteMode": "portal",
                    "splitTunneling": "false",
                    "uriRulesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite-portal/uri-rules?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:ltm:profile:rewrite:rewritestate",
                    "name": "rewrite-uri-translation",
                    "partition": "Common",
                    "fullPath": "/Common/rewrite-uri-translation",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite-uri-translation?ver=14.1.2.1",
                    "appService": "none",
                    "bypassList": [],
                    "clientCachingType": "cache-css-js",
                    "defaultsFrom": "/Common/rewrite",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite?ver=14.1.2.1"
                    },
                    "javaCaFile": "/Common/ca-bundle.crt",
                    "javaCaFileReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt?ver=14.1.2.1"
                    },
                    "javaCrl": "none",
                    "javaSignKey": "/Common/default.key",
                    "javaSignKeyReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key?ver=14.1.2.1"
                    },
                    "javaSigner": "/Common/default.crt",
                    "javaSignerReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt?ver=14.1.2.1"
                    },
                    "locationSpecific": "false",
                    "request": {
                        "insertXforwardedFor": "enabled",
                        "insertXforwardedHost": "disabled",
                        "insertXforwardedProto": "disabled",
                        "rewriteHeaders": "enabled",
                    },
                    "response": {
                        "rewriteContent": "enabled",
                        "rewriteHeaders": "enabled",
                    },
                    "rewriteList": [],
                    "rewriteMode": "uri-translation",
                    "splitTunneling": "false",
                    "uriRulesReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite-uri-translation/uri-rules?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
            ],
        }


class test_get_ltm_profilerewrite(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "bypassList": [],
                "clientCachingType": "cache-css-js",
                "defaultsFrom": "none",
                "fullPath": "/Common/rewrite",
                "generation": 1,
                "javaCaFile": "/Common/ca-bundle.crt",
                "javaCaFileReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt?ver=14.1.2.1"
                },
                "javaCrl": "none",
                "javaSignKey": "/Common/default.key",
                "javaSignKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key?ver=14.1.2.1"
                },
                "javaSigner": "/Common/default.crt",
                "javaSignerReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt?ver=14.1.2.1"
                },
                "kind": "tm:ltm:profile:rewrite:rewritestate",
                "locationSpecific": "false",
                "name": "rewrite",
                "partition": "Common",
                "request": {
                    "insertXforwardedFor": "enabled",
                    "insertXforwardedHost": "disabled",
                    "insertXforwardedProto": "disabled",
                    "rewriteHeaders": "enabled",
                },
                "response": {
                    "rewriteContent": "enabled",
                    "rewriteHeaders": "enabled",
                },
                "rewriteList": [],
                "rewriteMode": "portal",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite?ver=14.1.2.1",
                "splitTunneling": "false",
                "uriRulesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite/uri-rules?ver=14.1.2.1",
                },
            },
            {
                "appService": "none",
                "bypassList": [],
                "clientCachingType": "cache-css-js",
                "defaultsFrom": "/Common/rewrite",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite?ver=14.1.2.1"
                },
                "fullPath": "/Common/rewrite-portal",
                "generation": 1,
                "javaCaFile": "/Common/ca-bundle.crt",
                "javaCaFileReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt?ver=14.1.2.1"
                },
                "javaCrl": "none",
                "javaSignKey": "/Common/default.key",
                "javaSignKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key?ver=14.1.2.1"
                },
                "javaSigner": "/Common/default.crt",
                "javaSignerReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt?ver=14.1.2.1"
                },
                "kind": "tm:ltm:profile:rewrite:rewritestate",
                "locationSpecific": "false",
                "name": "rewrite-portal",
                "partition": "Common",
                "request": {
                    "insertXforwardedFor": "enabled",
                    "insertXforwardedHost": "disabled",
                    "insertXforwardedProto": "disabled",
                    "rewriteHeaders": "enabled",
                },
                "response": {
                    "rewriteContent": "enabled",
                    "rewriteHeaders": "enabled",
                },
                "rewriteList": [],
                "rewriteMode": "portal",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite-portal?ver=14.1.2.1",
                "splitTunneling": "false",
                "uriRulesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite-portal/uri-rules?ver=14.1.2.1",
                },
            },
            {
                "appService": "none",
                "bypassList": [],
                "clientCachingType": "cache-css-js",
                "defaultsFrom": "/Common/rewrite",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite?ver=14.1.2.1"
                },
                "fullPath": "/Common/rewrite-uri-translation",
                "generation": 1,
                "javaCaFile": "/Common/ca-bundle.crt",
                "javaCaFileReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~ca-bundle.crt?ver=14.1.2.1"
                },
                "javaCrl": "none",
                "javaSignKey": "/Common/default.key",
                "javaSignKeyReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-key/~Common~default.key?ver=14.1.2.1"
                },
                "javaSigner": "/Common/default.crt",
                "javaSignerReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~default.crt?ver=14.1.2.1"
                },
                "kind": "tm:ltm:profile:rewrite:rewritestate",
                "locationSpecific": "false",
                "name": "rewrite-uri-translation",
                "partition": "Common",
                "request": {
                    "insertXforwardedFor": "enabled",
                    "insertXforwardedHost": "disabled",
                    "insertXforwardedProto": "disabled",
                    "rewriteHeaders": "enabled",
                },
                "response": {
                    "rewriteContent": "enabled",
                    "rewriteHeaders": "enabled",
                },
                "rewriteList": [],
                "rewriteMode": "uri-translation",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite-uri-translation?ver=14.1.2.1",
                "splitTunneling": "false",
                "uriRulesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/ltm/profile/rewrite/~Common~rewrite-uri-translation/uri-rules?ver=14.1.2.1",
                },
            },
        ],
        "kind": "tm:ltm:profile:rewrite:rewritecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/rewrite?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileRewrite(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileRewrite(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
