# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_auth_partition
from genie.libs.parser.bigip.get_auth_partition import AuthPartition

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/auth/partition'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:auth:partition:partitioncollectionstate",
            "selfLink": "https://localhost/mgmt/tm/auth/partition?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:auth:partition:partitionstate",
                    "name": "Common",
                    "fullPath": "Common",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/auth/partition/Common?ver=14.1.2.1",
                    "defaultRouteDomain": 0,
                    "description": "Repository for system objects and shared objects.",
                }
            ],
        }


class test_get_auth_partition(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "defaultRouteDomain": 0,
                "description": "Repository for system objects and shared objects.",
                "fullPath": "Common",
                "generation": 0,
                "kind": "tm:auth:partition:partitionstate",
                "name": "Common",
                "selfLink": "https://localhost/mgmt/tm/auth/partition/Common?ver=14.1.2.1",
            }
        ],
        "kind": "tm:auth:partition:partitioncollectionstate",
        "selfLink": "https://localhost/mgmt/tm/auth/partition?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AuthPartition(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AuthPartition(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
