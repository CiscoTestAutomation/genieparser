# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_security_firewalluuid_default_autogenerate
from genie.libs.parser.bigip.get_security_firewalluuid_default_autogenerate import (
    SecurityFirewallUuiddefaultautogenerate,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/security/firewall/uuid-default-autogenerate'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:security:firewall:uuid-default-autogenerate:uuid-default-autogeneratestate",
            "selfLink": "https://localhost/mgmt/tm/security/firewall/uuid-default-autogenerate?ver=14.1.2.1",
            "mode": "disabled",
        }


class test_get_security_firewalluuid_default_autogenerate(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "kind": "tm:security:firewall:uuid-default-autogenerate:uuid-default-autogeneratestate",
        "mode": "disabled",
        "selfLink": "https://localhost/mgmt/tm/security/firewall/uuid-default-autogenerate?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SecurityFirewallUuiddefaultautogenerate(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SecurityFirewallUuiddefaultautogenerate(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
