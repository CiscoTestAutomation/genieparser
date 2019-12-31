# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_live_update_browser_challengesinstallations
from genie.libs.parser.bigip.get_live_update_browser_challengesinstallations import (
    Live_updateBrowserchallengesInstallations,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/live-update/browser-challenges/installations'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:live-update:browser-challenges:installations-collectionstate",
            "totalItems": 1,
            "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/installations",
            "items": [
                {
                    "id": "ff8080816db607de016db607dfb20010",
                    "lastUpdateMicros": 1570717032369000,
                    "updateFileReference": {
                        "link": "https://localhost/mgmt/tm/live-update/browser-challenges/update-files/ff8080816db607de016db607df4e000c"
                    },
                    "status": "install-complete",
                    "kind": "tm:live-update:browser-challenges:installationsstate",
                    "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/installations/ff8080816db607de016db607dfb20010",
                }
            ],
        }


class test_get_live_update_browser_challengesinstallations(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "id": "ff8080816db607de016db607dfb20010",
                "kind": "tm:live-update:browser-challenges:installationsstate",
                "lastUpdateMicros": 1570717032369000,
                "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/installations/ff8080816db607de016db607dfb20010",
                "status": "install-complete",
                "updateFileReference": {
                    "link": "https://localhost/mgmt/tm/live-update/browser-challenges/update-files/ff8080816db607de016db607df4e000c"
                },
            }
        ],
        "kind": "tm:live-update:browser-challenges:installations-collectionstate",
        "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/installations",
        "totalItems": 1,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = Live_updateBrowserchallengesInstallations(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Live_updateBrowserchallengesInstallations(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
