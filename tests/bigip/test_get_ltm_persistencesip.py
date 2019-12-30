# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_persistencesip
from genie.libs.parser.bigip.get_ltm_persistencesip import LtmPersistenceSip

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/persistence/sip'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:persistence:sip:sipcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/persistence/sip?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:persistence:sip:sipstate",
                    "name": "sip_info",
                    "partition": "Common",
                    "fullPath": "/Common/sip_info",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/persistence/sip/~Common~sip_info?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "matchAcrossPools": "disabled",
                    "matchAcrossServices": "disabled",
                    "matchAcrossVirtuals": "disabled",
                    "mirror": "disabled",
                    "overrideConnectionLimit": "disabled",
                    "sipInfo": "none",
                    "timeout": "180",
                }
            ],
        }


class test_get_ltm_persistencesip(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/sip_info",
                "generation": 1,
                "kind": "tm:ltm:persistence:sip:sipstate",
                "matchAcrossPools": "disabled",
                "matchAcrossServices": "disabled",
                "matchAcrossVirtuals": "disabled",
                "mirror": "disabled",
                "name": "sip_info",
                "overrideConnectionLimit": "disabled",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/persistence/sip/~Common~sip_info?ver=14.1.2.1",
                "sipInfo": "none",
                "timeout": "180",
            }
        ],
        "kind": "tm:ltm:persistence:sip:sipcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/persistence/sip?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmPersistenceSip(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmPersistenceSip(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
