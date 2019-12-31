# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_cryptoca_bundle_manager
from genie.libs.parser.bigip.get_sys_cryptoca_bundle_manager import (
    SysCryptoCabundlemanager,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/crypto/ca-bundle-manager'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:crypto:ca-bundle-manager:ca-bundle-managercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/crypto/ca-bundle-manager?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:crypto:ca-bundle-manager:ca-bundle-managerstate",
                    "name": "ca-bundle",
                    "partition": "Common",
                    "fullPath": "/Common/ca-bundle",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/crypto/ca-bundle-manager/~Common~ca-bundle?ver=14.1.2.1",
                    "proxyPort": 3128,
                    "timeOut": 8,
                    "trustedCaBundle": "/Common/f5-ca-bundle.crt",
                    "trustedCaBundleReference": {
                        "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-ca-bundle.crt?ver=14.1.2.1"
                    },
                    "updateInterval": 0,
                    "includeUrl": [
                        "https://cdn.f5.com/product/ca-bundle/blended-bundle.crt"
                    ],
                }
            ],
        }


class test_get_sys_cryptoca_bundle_manager(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/ca-bundle",
                "generation": 1,
                "includeUrl": [
                    "https://cdn.f5.com/product/ca-bundle/blended-bundle.crt"
                ],
                "kind": "tm:sys:crypto:ca-bundle-manager:ca-bundle-managerstate",
                "name": "ca-bundle",
                "partition": "Common",
                "proxyPort": 3128,
                "selfLink": "https://localhost/mgmt/tm/sys/crypto/ca-bundle-manager/~Common~ca-bundle?ver=14.1.2.1",
                "timeOut": 8,
                "trustedCaBundle": "/Common/f5-ca-bundle.crt",
                "trustedCaBundleReference": {
                    "link": "https://localhost/mgmt/tm/sys/file/ssl-cert/~Common~f5-ca-bundle.crt?ver=14.1.2.1"
                },
                "updateInterval": 0,
            }
        ],
        "kind": "tm:sys:crypto:ca-bundle-manager:ca-bundle-managercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/crypto/ca-bundle-manager?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysCryptoCabundlemanager(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysCryptoCabundlemanager(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
