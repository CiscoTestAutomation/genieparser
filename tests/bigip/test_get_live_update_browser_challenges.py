# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_live_update_browser_challenges
from genie.libs.parser.bigip.get_live_update_browser_challenges import (
    Live_updateBrowserchallenges,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/live-update/browser-challenges'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "installScheduleReference": {
                "link": "https://localhost/mgmt/tm/live-update/browser-challenges/install-schedule"
            },
            "updateFilesReference": {
                "link": "https://localhost/mgmt/tm/live-update/browser-challenges/update-files"
            },
            "installationsReference": {
                "link": "https://localhost/mgmt/tm/live-update/browser-challenges/installations"
            },
            "availabilityReference": {
                "link": "https://localhost/mgmt/tm/live-update/browser-challenges/availability"
            },
        }


class test_get_live_update_browser_challenges(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "availabilityReference": {
            "link": "https://localhost/mgmt/tm/live-update/browser-challenges/availability"
        },
        "installScheduleReference": {
            "link": "https://localhost/mgmt/tm/live-update/browser-challenges/install-schedule"
        },
        "installationsReference": {
            "link": "https://localhost/mgmt/tm/live-update/browser-challenges/installations"
        },
        "updateFilesReference": {
            "link": "https://localhost/mgmt/tm/live-update/browser-challenges/update-files"
        },
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = Live_updateBrowserchallenges(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Live_updateBrowserchallenges(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
