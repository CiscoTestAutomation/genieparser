# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profiledns
from genie.libs.parser.bigip.get_ltm_profiledns import LtmProfileDns

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/dns'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:dns:dnscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/dns?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:dns:dnsstate",
                    "name": "dns",
                    "partition": "Common",
                    "fullPath": "/Common/dns",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/dns/~Common~dns?ver=14.1.2.1",
                    "appService": "none",
                    "avrDnsstatSampleRate": 0,
                    "cache": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "dnsSecurity": "none",
                    "dns64": "disabled",
                    "dns64AdditionalSectionRewrite": "disabled",
                    "dns64Prefix": "any6",
                    "edns0ClientSubnetInsert": "disabled",
                    "enableCache": "no",
                    "enableDnsExpress": "yes",
                    "enableDnsFirewall": "no",
                    "enableDnssec": "yes",
                    "enableGtm": "yes",
                    "enableHardwareQueryValidation": "no",
                    "enableHardwareResponseCache": "no",
                    "enableLogging": "no",
                    "enableRapidResponse": "no",
                    "logProfile": "none",
                    "processRd": "yes",
                    "processXfr": "no",
                    "rapidResponseLastAction": "drop",
                    "unhandledQueryAction": "allow",
                    "useLocalBind": "yes",
                }
            ],
        }


class test_get_ltm_profiledns(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "avrDnsstatSampleRate": 0,
                "cache": "none",
                "defaultsFrom": "none",
                "description": "none",
                "dns64": "disabled",
                "dns64AdditionalSectionRewrite": "disabled",
                "dns64Prefix": "any6",
                "dnsSecurity": "none",
                "edns0ClientSubnetInsert": "disabled",
                "enableCache": "no",
                "enableDnsExpress": "yes",
                "enableDnsFirewall": "no",
                "enableDnssec": "yes",
                "enableGtm": "yes",
                "enableHardwareQueryValidation": "no",
                "enableHardwareResponseCache": "no",
                "enableLogging": "no",
                "enableRapidResponse": "no",
                "fullPath": "/Common/dns",
                "generation": 1,
                "kind": "tm:ltm:profile:dns:dnsstate",
                "logProfile": "none",
                "name": "dns",
                "partition": "Common",
                "processRd": "yes",
                "processXfr": "no",
                "rapidResponseLastAction": "drop",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/dns/~Common~dns?ver=14.1.2.1",
                "unhandledQueryAction": "allow",
                "useLocalBind": "yes",
            }
        ],
        "kind": "tm:ltm:profile:dns:dnscollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/dns?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileDns(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileDns(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
