# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_persistencesource_addr
from genie.libs.parser.bigip.get_ltm_persistencesource_addr import (
    LtmPersistenceSourceaddr,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/persistence/source-addr'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:persistence:source-addr:source-addrcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/persistence/source-addr?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:persistence:source-addr:source-addrstate",
                    "name": "source_addr",
                    "partition": "Common",
                    "fullPath": "/Common/source_addr",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/persistence/source-addr/~Common~source_addr?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "hashAlgorithm": "default",
                    "mapProxies": "enabled",
                    "mapProxyAddress": "none",
                    "mapProxyClass": "none",
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


class test_get_ltm_persistencesource_addr(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/source_addr",
                "generation": 1,
                "hashAlgorithm": "default",
                "kind": "tm:ltm:persistence:source-addr:source-addrstate",
                "mapProxies": "enabled",
                "mapProxyAddress": "none",
                "mapProxyClass": "none",
                "mask": "none",
                "matchAcrossPools": "disabled",
                "matchAcrossServices": "disabled",
                "matchAcrossVirtuals": "disabled",
                "mirror": "disabled",
                "name": "source_addr",
                "overrideConnectionLimit": "disabled",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/persistence/source-addr/~Common~source_addr?ver=14.1.2.1",
                "timeout": "180",
            }
        ],
        "kind": "tm:ltm:persistence:source-addr:source-addrcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/persistence/source-addr?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmPersistenceSourceaddr(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmPersistenceSourceaddr(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
