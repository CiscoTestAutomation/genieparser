# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileconnector
from genie.libs.parser.bigip.get_ltm_profileconnector import (
    LtmProfileConnector,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/connector'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:connector:connectorcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/connector?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:connector:connectorstate",
                    "name": "access-logonpage-protection-connector",
                    "partition": "Common",
                    "fullPath": "/Common/access-logonpage-protection-connector",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/connector/~Common~access-logonpage-protection-connector?ver=14.1.2.1",
                    "appService": "none",
                    "connectionTimeout": 0,
                    "entryVirtualServer": "none",
                    "serviceDownAction": "ignore",
                },
                {
                    "kind": "tm:ltm:profile:connector:connectorstate",
                    "name": "connector",
                    "partition": "Common",
                    "fullPath": "/Common/connector",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/connector/~Common~connector?ver=14.1.2.1",
                    "appService": "none",
                    "connectionTimeout": 0,
                    "entryVirtualServer": "none",
                    "serviceDownAction": "ignore",
                },
            ],
        }


class test_get_ltm_profileconnector(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "connectionTimeout": 0,
                "entryVirtualServer": "none",
                "fullPath": "/Common/access-logonpage-protection-connector",
                "generation": 1,
                "kind": "tm:ltm:profile:connector:connectorstate",
                "name": "access-logonpage-protection-connector",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/connector/~Common~access-logonpage-protection-connector?ver=14.1.2.1",
                "serviceDownAction": "ignore",
            },
            {
                "appService": "none",
                "connectionTimeout": 0,
                "entryVirtualServer": "none",
                "fullPath": "/Common/connector",
                "generation": 1,
                "kind": "tm:ltm:profile:connector:connectorstate",
                "name": "connector",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/connector/~Common~connector?ver=14.1.2.1",
                "serviceDownAction": "ignore",
            },
        ],
        "kind": "tm:ltm:profile:connector:connectorcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/connector?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileConnector(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileConnector(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
