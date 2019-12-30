# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilemblb
from genie.libs.parser.bigip.get_ltm_profilemblb import LtmProfileMblb

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/mblb'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:mblb:mblbcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/mblb?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:mblb:mblbstate",
                    "name": "mblb",
                    "partition": "Common",
                    "fullPath": "/Common/mblb",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/mblb/~Common~mblb?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "egressHigh": 50,
                    "egressLow": 5,
                    "ingressHigh": 50,
                    "ingressLow": 5,
                    "isolateAbort": "enabled",
                    "isolateClient": "disabled",
                    "isolateExpire": "enabled",
                    "isolateServer": "enabled",
                    "minConn": 0,
                    "shutdownTimeout": 5,
                    "tagTtl": 60,
                }
            ],
        }


class test_get_ltm_profilemblb(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "egressHigh": 50,
                "egressLow": 5,
                "fullPath": "/Common/mblb",
                "generation": 0,
                "ingressHigh": 50,
                "ingressLow": 5,
                "isolateAbort": "enabled",
                "isolateClient": "disabled",
                "isolateExpire": "enabled",
                "isolateServer": "enabled",
                "kind": "tm:ltm:profile:mblb:mblbstate",
                "minConn": 0,
                "name": "mblb",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/mblb/~Common~mblb?ver=14.1.2.1",
                "shutdownTimeout": 5,
                "tagTtl": 60,
            }
        ],
        "kind": "tm:ltm:profile:mblb:mblbcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/mblb?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileMblb(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileMblb(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
