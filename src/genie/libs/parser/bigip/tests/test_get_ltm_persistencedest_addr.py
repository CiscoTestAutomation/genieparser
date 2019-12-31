# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_persistencedest_addr
from genie.libs.parser.bigip.get_ltm_persistencedest_addr import (
    LtmPersistenceDestaddr,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/persistence/dest-addr'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:persistence:dest-addr:dest-addrcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/persistence/dest-addr?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:persistence:dest-addr:dest-addrstate",
                    "name": "dest_addr",
                    "partition": "Common",
                    "fullPath": "/Common/dest_addr",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/persistence/dest-addr/~Common~dest_addr?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "hashAlgorithm": "default",
                    "mask": "none",
                    "matchAcrossPools": "disabled",
                    "matchAcrossServices": "disabled",
                    "matchAcrossVirtuals": "disabled",
                    "mirror": "disabled",
                    "overrideConnectionLimit": "disabled",
                    "timeout": "180",
                }
            ],
        }


class test_get_ltm_persistencedest_addr(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/dest_addr",
                "generation": 1,
                "hashAlgorithm": "default",
                "kind": "tm:ltm:persistence:dest-addr:dest-addrstate",
                "mask": "none",
                "matchAcrossPools": "disabled",
                "matchAcrossServices": "disabled",
                "matchAcrossVirtuals": "disabled",
                "mirror": "disabled",
                "name": "dest_addr",
                "overrideConnectionLimit": "disabled",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/persistence/dest-addr/~Common~dest_addr?ver=14.1.2.1",
                "timeout": "180",
            }
        ],
        "kind": "tm:ltm:persistence:dest-addr:dest-addrcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/persistence/dest-addr?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmPersistenceDestaddr(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmPersistenceDestaddr(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
