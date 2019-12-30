# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_persistencehash
from genie.libs.parser.bigip.get_ltm_persistencehash import LtmPersistenceHash

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/persistence/hash'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:persistence:hash:hashcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/persistence/hash?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:persistence:hash:hashstate",
                    "name": "hash",
                    "partition": "Common",
                    "fullPath": "/Common/hash",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/persistence/hash/~Common~hash?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "hashAlgorithm": "default",
                    "hashBufferLimit": 0,
                    "hashEndPattern": "none",
                    "hashLength": 0,
                    "hashOffset": 0,
                    "hashStartPattern": "none",
                    "matchAcrossPools": "disabled",
                    "matchAcrossServices": "disabled",
                    "matchAcrossVirtuals": "disabled",
                    "mirror": "disabled",
                    "overrideConnectionLimit": "disabled",
                    "rule": "none",
                    "timeout": "180",
                }
            ],
        }


class test_get_ltm_persistencehash(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/hash",
                "generation": 1,
                "hashAlgorithm": "default",
                "hashBufferLimit": 0,
                "hashEndPattern": "none",
                "hashLength": 0,
                "hashOffset": 0,
                "hashStartPattern": "none",
                "kind": "tm:ltm:persistence:hash:hashstate",
                "matchAcrossPools": "disabled",
                "matchAcrossServices": "disabled",
                "matchAcrossVirtuals": "disabled",
                "mirror": "disabled",
                "name": "hash",
                "overrideConnectionLimit": "disabled",
                "partition": "Common",
                "rule": "none",
                "selfLink": "https://localhost/mgmt/tm/ltm/persistence/hash/~Common~hash?ver=14.1.2.1",
                "timeout": "180",
            }
        ],
        "kind": "tm:ltm:persistence:hash:hashcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/persistence/hash?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmPersistenceHash(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmPersistenceHash(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
