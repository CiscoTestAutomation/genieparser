# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilesplitsessionclient
from genie.libs.parser.bigip.get_ltm_profilesplitsessionclient import (
    LtmProfileSplitsessionclient,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/splitsessionclient'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:splitsessionclient:splitsessionclientcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/splitsessionclient?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:splitsessionclient:splitsessionclientstate",
                    "name": "splitsessionclient",
                    "partition": "Common",
                    "fullPath": "/Common/splitsessionclient",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/splitsessionclient/~Common~splitsessionclient?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "httpHeader": "none",
                    "localPeer": "false",
                    "peerIp": "any6",
                    "peerPort": 0,
                    "sessionLookupType": "flow",
                }
            ],
        }


class test_get_ltm_profilesplitsessionclient(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/splitsessionclient",
                "generation": 1,
                "httpHeader": "none",
                "kind": "tm:ltm:profile:splitsessionclient:splitsessionclientstate",
                "localPeer": "false",
                "name": "splitsessionclient",
                "partition": "Common",
                "peerIp": "any6",
                "peerPort": 0,
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/splitsessionclient/~Common~splitsessionclient?ver=14.1.2.1",
                "sessionLookupType": "flow",
            }
        ],
        "kind": "tm:ltm:profile:splitsessionclient:splitsessionclientcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/splitsessionclient?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileSplitsessionclient(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileSplitsessionclient(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
