# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_auth_password_policy
from genie.libs.parser.bigip.get_auth_password_policy import AuthPasswordpolicy

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/auth/password-policy'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:auth:password-policy:password-policystate",
            "selfLink": "https://localhost/mgmt/tm/auth/password-policy?ver=14.1.2.1",
            "expirationWarning": 7,
            "maxDuration": 99999,
            "maxLoginFailures": 0,
            "minDuration": 0,
            "minimumLength": 6,
            "passwordMemory": 0,
            "policyEnforcement": "enabled",
            "requiredLowercase": 0,
            "requiredNumeric": 0,
            "requiredSpecial": 0,
            "requiredUppercase": 0,
        }


class test_get_auth_password_policy(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "expirationWarning": 7,
        "kind": "tm:auth:password-policy:password-policystate",
        "maxDuration": 99999,
        "maxLoginFailures": 0,
        "minDuration": 0,
        "minimumLength": 6,
        "passwordMemory": 0,
        "policyEnforcement": "enabled",
        "requiredLowercase": 0,
        "requiredNumeric": 0,
        "requiredSpecial": 0,
        "requiredUppercase": 0,
        "selfLink": "https://localhost/mgmt/tm/auth/password-policy?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AuthPasswordpolicy(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AuthPasswordpolicy(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
