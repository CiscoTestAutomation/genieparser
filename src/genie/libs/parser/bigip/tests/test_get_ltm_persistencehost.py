# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_persistencehost
from genie.libs.parser.bigip.get_ltm_persistencehost import LtmPersistenceHost

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/persistence/host'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:persistence:host:hostcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/persistence/host?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:persistence:host:hoststate",
                    "name": "host",
                    "partition": "Common",
                    "fullPath": "/Common/host",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/persistence/host/~Common~host?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "matchAcrossPools": "disabled",
                    "matchAcrossServices": "disabled",
                    "matchAcrossVirtuals": "disabled",
                    "mirror": "disabled",
                    "overrideConnectionLimit": "disabled",
                    "timeout": "180",
                }
            ],
        }


class test_get_ltm_persistencehost(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/host",
                "generation": 1,
                "kind": "tm:ltm:persistence:host:hoststate",
                "matchAcrossPools": "disabled",
                "matchAcrossServices": "disabled",
                "matchAcrossVirtuals": "disabled",
                "mirror": "disabled",
                "name": "host",
                "overrideConnectionLimit": "disabled",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/persistence/host/~Common~host?ver=14.1.2.1",
                "timeout": "180",
            }
        ],
        "kind": "tm:ltm:persistence:host:hostcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/persistence/host?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmPersistenceHost(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmPersistenceHost(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
