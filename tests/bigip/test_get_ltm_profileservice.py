# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileservice
from genie.libs.parser.bigip.get_ltm_profileservice import LtmProfileService

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/service'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:service:servicecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/service?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:service:servicestate",
                    "name": "access-logonpage-protection-service",
                    "partition": "Common",
                    "fullPath": "/Common/access-logonpage-protection-service",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/service/~Common~access-logonpage-protection-service?ver=14.1.2.1",
                    "appService": "none",
                    "type": "f5-module",
                },
                {
                    "kind": "tm:ltm:profile:service:servicestate",
                    "name": "service",
                    "partition": "Common",
                    "fullPath": "/Common/service",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/service/~Common~service?ver=14.1.2.1",
                    "appService": "none",
                    "type": "inline",
                },
            ],
        }


class test_get_ltm_profileservice(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "fullPath": "/Common/access-logonpage-protection-service",
                "generation": 1,
                "kind": "tm:ltm:profile:service:servicestate",
                "name": "access-logonpage-protection-service",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/service/~Common~access-logonpage-protection-service?ver=14.1.2.1",
                "type": "f5-module",
            },
            {
                "appService": "none",
                "fullPath": "/Common/service",
                "generation": 1,
                "kind": "tm:ltm:profile:service:servicestate",
                "name": "service",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/service/~Common~service?ver=14.1.2.1",
                "type": "inline",
            },
        ],
        "kind": "tm:ltm:profile:service:servicecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/service?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileService(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileService(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
