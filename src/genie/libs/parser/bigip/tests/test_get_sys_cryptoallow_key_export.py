# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_cryptoallow_key_export
from genie.libs.parser.bigip.get_sys_cryptoallow_key_export import (
    SysCryptoAllowkeyexport,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/crypto/allow-key-export'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:crypto:allow-key-export:allow-key-exportstate",
            "selfLink": "https://localhost/mgmt/tm/sys/crypto/allow-key-export?ver=14.1.2.1",
            "value": "enabled",
        }


class test_get_sys_cryptoallow_key_export(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "kind": "tm:sys:crypto:allow-key-export:allow-key-exportstate",
        "selfLink": "https://localhost/mgmt/tm/sys/crypto/allow-key-export?ver=14.1.2.1",
        "value": "enabled",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysCryptoAllowkeyexport(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysCryptoAllowkeyexport(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
