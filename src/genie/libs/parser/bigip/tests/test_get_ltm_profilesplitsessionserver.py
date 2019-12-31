# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilesplitsessionserver
from genie.libs.parser.bigip.get_ltm_profilesplitsessionserver import (
    LtmProfileSplitsessionserver,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/splitsessionserver'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:splitsessionserver:splitsessionservercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/splitsessionserver?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:splitsessionserver:splitsessionserverstate",
                    "name": "splitsessionserver",
                    "partition": "Common",
                    "fullPath": "/Common/splitsessionserver",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/splitsessionserver/~Common~splitsessionserver?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "httpHeader": "none",
                    "listenIp": "any6",
                    "listenPort": 0,
                    "localPeer": "false",
                    "sessionLookupType": "flow",
                    "splitsessionclient": "none",
                }
            ],
        }


class test_get_ltm_profilesplitsessionserver(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/splitsessionserver",
                "generation": 1,
                "httpHeader": "none",
                "kind": "tm:ltm:profile:splitsessionserver:splitsessionserverstate",
                "listenIp": "any6",
                "listenPort": 0,
                "localPeer": "false",
                "name": "splitsessionserver",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/splitsessionserver/~Common~splitsessionserver?ver=14.1.2.1",
                "sessionLookupType": "flow",
                "splitsessionclient": "none",
            }
        ],
        "kind": "tm:ltm:profile:splitsessionserver:splitsessionservercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/splitsessionserver?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileSplitsessionserver(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileSplitsessionserver(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
