# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilepptp
from genie.libs.parser.bigip.get_ltm_profilepptp import LtmProfilePptp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/pptp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:pptp:pptpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/pptp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:pptp:pptpstate",
                    "name": "pptp",
                    "partition": "Common",
                    "fullPath": "/Common/pptp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/pptp/~Common~pptp?ver=14.1.2.1",
                    "appService": "none",
                    "csvFormat": "disabled",
                    "defaultsFrom": "none",
                    "description": "none",
                    "includeDestinationIp": "disabled",
                    "publisherName": "none",
                }
            ],
        }


class test_get_ltm_profilepptp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "csvFormat": "disabled",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/pptp",
                "generation": 1,
                "includeDestinationIp": "disabled",
                "kind": "tm:ltm:profile:pptp:pptpstate",
                "name": "pptp",
                "partition": "Common",
                "publisherName": "none",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/pptp/~Common~pptp?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:pptp:pptpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/pptp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfilePptp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfilePptp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
