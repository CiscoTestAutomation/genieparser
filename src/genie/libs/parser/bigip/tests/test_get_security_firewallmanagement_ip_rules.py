# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_security_firewallmanagement_ip_rules
from genie.libs.parser.bigip.get_security_firewallmanagement_ip_rules import (
    SecurityFirewallManagementiprules,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/security/firewall/management-ip-rules'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:security:firewall:management-ip-rules:management-ip-rulesstate",
            "selfLink": "https://localhost/mgmt/tm/security/firewall/management-ip-rules?ver=14.1.2.1",
            "rulesReference": {
                "link": "https://localhost/mgmt/tm/security/firewall/management-ip-rules/rules?ver=14.1.2.1",
                "isSubcollection": True,
            },
        }


class test_get_security_firewallmanagement_ip_rules(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "kind": "tm:security:firewall:management-ip-rules:management-ip-rulesstate",
        "rulesReference": {
            "isSubcollection": True,
            "link": "https://localhost/mgmt/tm/security/firewall/management-ip-rules/rules?ver=14.1.2.1",
        },
        "selfLink": "https://localhost/mgmt/tm/security/firewall/management-ip-rules?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SecurityFirewallManagementiprules(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SecurityFirewallManagementiprules(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
