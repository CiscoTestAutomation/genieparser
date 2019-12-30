# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_persistencemsrdp
from genie.libs.parser.bigip.get_ltm_persistencemsrdp import (
    LtmPersistenceMsrdp,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/persistence/msrdp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:persistence:msrdp:msrdpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/persistence/msrdp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:persistence:msrdp:msrdpstate",
                    "name": "msrdp",
                    "partition": "Common",
                    "fullPath": "/Common/msrdp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/persistence/msrdp/~Common~msrdp?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "hasSessionDir": "yes",
                    "matchAcrossPools": "disabled",
                    "matchAcrossServices": "disabled",
                    "matchAcrossVirtuals": "disabled",
                    "mirror": "disabled",
                    "overrideConnectionLimit": "disabled",
                    "timeout": "300",
                }
            ],
        }


class test_get_ltm_persistencemsrdp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/msrdp",
                "generation": 1,
                "hasSessionDir": "yes",
                "kind": "tm:ltm:persistence:msrdp:msrdpstate",
                "matchAcrossPools": "disabled",
                "matchAcrossServices": "disabled",
                "matchAcrossVirtuals": "disabled",
                "mirror": "disabled",
                "name": "msrdp",
                "overrideConnectionLimit": "disabled",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/persistence/msrdp/~Common~msrdp?ver=14.1.2.1",
                "timeout": "300",
            }
        ],
        "kind": "tm:ltm:persistence:msrdp:msrdpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/persistence/msrdp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmPersistenceMsrdp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmPersistenceMsrdp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
