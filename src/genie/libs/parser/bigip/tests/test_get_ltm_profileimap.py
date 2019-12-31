# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileimap
from genie.libs.parser.bigip.get_ltm_profileimap import LtmProfileImap

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/imap'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:imap:imapcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/imap?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:imap:imapstate",
                    "name": "imap",
                    "partition": "Common",
                    "fullPath": "/Common/imap",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/imap/~Common~imap?ver=14.1.2.1",
                    "activationMode": "require",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                }
            ],
        }


class test_get_ltm_profileimap(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "activationMode": "require",
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/imap",
                "generation": 1,
                "kind": "tm:ltm:profile:imap:imapstate",
                "name": "imap",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/imap/~Common~imap?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:imap:imapcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/imap?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileImap(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileImap(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
