# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_live_update_browser_challengesinstall_schedule
from genie.libs.parser.bigip.get_live_update_browser_challengesinstall_schedule import (
    Live_updateBrowserchallengesInstallschedule,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/live-update/browser-challenges/install-schedule'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "frequency": "never",
            "startTime": "00:00",
            "endTime": "23:59",
            "applyAtAllTimes": True,
            "applyOnAllDays": True,
            "applyOnSundays": False,
            "applyOnMondays": False,
            "applyOnTuesdays": False,
            "applyOnWednesdays": False,
            "applyOnThursdays": False,
            "applyOnFridays": False,
            "applyOnSaturdays": False,
            "kind": "tm:live-update:browser-challenges:install-schedulestate",
            "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/install-schedule",
        }


class test_get_live_update_browser_challengesinstall_schedule(
    unittest.TestCase
):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "applyAtAllTimes": True,
        "applyOnAllDays": True,
        "applyOnFridays": False,
        "applyOnMondays": False,
        "applyOnSaturdays": False,
        "applyOnSundays": False,
        "applyOnThursdays": False,
        "applyOnTuesdays": False,
        "applyOnWednesdays": False,
        "endTime": "23:59",
        "frequency": "never",
        "kind": "tm:live-update:browser-challenges:install-schedulestate",
        "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/install-schedule",
        "startTime": "00:00",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = Live_updateBrowserchallengesInstallschedule(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Live_updateBrowserchallengesInstallschedule(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
