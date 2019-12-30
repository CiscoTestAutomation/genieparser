# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorldap
from genie.libs.parser.bigip.get_ltm_monitorldap import LtmMonitorLdap

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/ldap'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:ldap:ldapcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/ldap?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:ldap:ldapstate",
                    "name": "ldap",
                    "partition": "Common",
                    "fullPath": "/Common/ldap",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/ldap/~Common~ldap?ver=14.1.2.1",
                    "chaseReferrals": "yes",
                    "debug": "no",
                    "destination": "*:*",
                    "interval": 10,
                    "manualResume": "disabled",
                    "timeUntilUp": 0,
                    "timeout": 31,
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitorldap(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "chaseReferrals": "yes",
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/ldap",
                "generation": 0,
                "interval": 10,
                "kind": "tm:ltm:monitor:ldap:ldapstate",
                "manualResume": "disabled",
                "name": "ldap",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/ldap/~Common~ldap?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 31,
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:ldap:ldapcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/ldap?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorLdap(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorLdap(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
