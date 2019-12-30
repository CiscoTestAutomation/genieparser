# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_live_update_bot_signaturesinstallations
from genie.libs.parser.bigip.get_live_update_bot_signaturesinstallations import (
    Live_updateBotsignaturesInstallations,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/live-update/bot-signatures/installations'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:live-update:bot-signatures:installations-collectionstate",
            "totalItems": 1,
            "selfLink": "https://localhost/mgmt/tm/live-update/bot-signatures/installations",
            "items": [
                {
                    "id": "ff8080816db607de016db607dfb0000f",
                    "lastUpdateMicros": 1570717032367000,
                    "updateFileReference": {
                        "link": "https://localhost/mgmt/tm/live-update/bot-signatures/update-files/ff8080816db607de016db607df23000b"
                    },
                    "status": "install-complete",
                    "kind": "tm:live-update:bot-signatures:installationsstate",
                    "selfLink": "https://localhost/mgmt/tm/live-update/bot-signatures/installations/ff8080816db607de016db607dfb0000f",
                }
            ],
        }


class test_get_live_update_bot_signaturesinstallations(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "id": "ff8080816db607de016db607dfb0000f",
                "kind": "tm:live-update:bot-signatures:installationsstate",
                "lastUpdateMicros": 1570717032367000,
                "selfLink": "https://localhost/mgmt/tm/live-update/bot-signatures/installations/ff8080816db607de016db607dfb0000f",
                "status": "install-complete",
                "updateFileReference": {
                    "link": "https://localhost/mgmt/tm/live-update/bot-signatures/update-files/ff8080816db607de016db607df23000b"
                },
            }
        ],
        "kind": "tm:live-update:bot-signatures:installations-collectionstate",
        "selfLink": "https://localhost/mgmt/tm/live-update/bot-signatures/installations",
        "totalItems": 1,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = Live_updateBotsignaturesInstallations(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Live_updateBotsignaturesInstallations(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
