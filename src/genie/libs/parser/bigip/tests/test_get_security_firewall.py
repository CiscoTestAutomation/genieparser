# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_security_firewall
from genie.libs.parser.bigip.get_security_firewall import SecurityFirewall

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/security/firewall'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:security:firewall:firewallcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/security/firewall?ver=14.1.2.1",
            "items": [
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/security/firewall/management-ip-rules?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/security/firewall/uuid-default-autogenerate?ver=14.1.2.1"
                    }
                },
            ],
        }


class test_get_security_firewall(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/security/firewall/management-ip-rules?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/security/firewall/uuid-default-autogenerate?ver=14.1.2.1"
                }
            },
        ],
        "kind": "tm:security:firewall:firewallcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/security/firewall?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SecurityFirewall(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SecurityFirewall(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
