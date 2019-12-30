# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileipsecalg
from genie.libs.parser.bigip.get_ltm_profileipsecalg import LtmProfileIpsecalg

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/ipsecalg'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:ipsecalg:ipsecalgcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/ipsecalg?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:ipsecalg:ipsecalgstate",
                    "name": "ipsecalg",
                    "partition": "Common",
                    "fullPath": "/Common/ipsecalg",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/ipsecalg/~Common~ipsecalg?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "idleTimeout": "3600",
                    "initialConnectionTimeout": 3,
                    "logProfile": "none",
                    "logPublisher": "none",
                    "pendingIkeConnectionLimit": 5,
                }
            ],
        }


class test_get_ltm_profileipsecalg(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/ipsecalg",
                "generation": 1,
                "idleTimeout": "3600",
                "initialConnectionTimeout": 3,
                "kind": "tm:ltm:profile:ipsecalg:ipsecalgstate",
                "logProfile": "none",
                "logPublisher": "none",
                "name": "ipsecalg",
                "partition": "Common",
                "pendingIkeConnectionLimit": 5,
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/ipsecalg/~Common~ipsecalg?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:ipsecalg:ipsecalgcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/ipsecalg?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileIpsecalg(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileIpsecalg(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
