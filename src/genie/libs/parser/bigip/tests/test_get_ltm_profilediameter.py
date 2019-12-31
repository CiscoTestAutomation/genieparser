# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilediameter
from genie.libs.parser.bigip.get_ltm_profilediameter import LtmProfileDiameter

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/diameter'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:diameter:diametercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/diameter?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:diameter:diameterstate",
                    "name": "diameter",
                    "partition": "Common",
                    "fullPath": "/Common/diameter",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/diameter/~Common~diameter?ver=14.1.2.1",
                    "appService": "none",
                    "connectionPrime": "disabled",
                    "defaultsFrom": "none",
                    "description": "none",
                    "destinationRealm": "none",
                    "handshakeTimeout": 10,
                    "hostIpRewrite": "enabled",
                    "maxRetransmitAttempts": 1,
                    "maxWatchdogFailure": 10,
                    "originHostToClient": "none",
                    "originHostToServer": "none",
                    "originRealmToClient": "none",
                    "originRealmToServer": "none",
                    "parentAvp": "none",
                    "persistAvp": "Session-Id",
                    "resetOnTimeout": "enabled",
                    "retransmitTimeout": 10,
                    "watchdogTimeout": 0,
                }
            ],
        }


class test_get_ltm_profilediameter(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "connectionPrime": "disabled",
                "defaultsFrom": "none",
                "description": "none",
                "destinationRealm": "none",
                "fullPath": "/Common/diameter",
                "generation": 1,
                "handshakeTimeout": 10,
                "hostIpRewrite": "enabled",
                "kind": "tm:ltm:profile:diameter:diameterstate",
                "maxRetransmitAttempts": 1,
                "maxWatchdogFailure": 10,
                "name": "diameter",
                "originHostToClient": "none",
                "originHostToServer": "none",
                "originRealmToClient": "none",
                "originRealmToServer": "none",
                "parentAvp": "none",
                "partition": "Common",
                "persistAvp": "Session-Id",
                "resetOnTimeout": "enabled",
                "retransmitTimeout": 10,
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/diameter/~Common~diameter?ver=14.1.2.1",
                "watchdogTimeout": 0,
            }
        ],
        "kind": "tm:ltm:profile:diameter:diametercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/diameter?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileDiameter(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileDiameter(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
