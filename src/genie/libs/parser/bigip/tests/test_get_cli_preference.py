# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cli_preference
from genie.libs.parser.bigip.get_cli_preference import CliPreference

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cli/preference'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:cli:preference:preferencestate",
            "selfLink": "https://localhost/mgmt/tm/cli/preference?ver=14.1.2.1",
            "aliasPath": ["/Common"],
            "aliasPathReference": [
                {
                    "link": "https://localhost/mgmt/tm/sys/folder/~Common?ver=14.1.2.1"
                }
            ],
            "confirmEdit": "enabled",
            "displayThreshold": 100,
            "editor": "vi",
            "historyDateTime": "disabled",
            "historyFileSize": 10000,
            "historySize": 500,
            "keymap": "default",
            "listAllProperties": "disabled",
            "pager": "disabled",
            "prompt": [
                "host",
                "user",
                "status",
                "current-folder",
                "config-sync-status",
            ],
            "showAliases": "enabled",
            "showImportedVersions": "disabled",
            "statUnits": "default",
            "tableIndentWidth": 2,
            "tclSyntaxHighlighting": "disabled",
            "video": "enabled",
            "warn": "bell",
        }


class test_get_cli_preference(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "aliasPath": ["/Common"],
        "aliasPathReference": [
            {
                "link": "https://localhost/mgmt/tm/sys/folder/~Common?ver=14.1.2.1"
            }
        ],
        "confirmEdit": "enabled",
        "displayThreshold": 100,
        "editor": "vi",
        "historyDateTime": "disabled",
        "historyFileSize": 10000,
        "historySize": 500,
        "keymap": "default",
        "kind": "tm:cli:preference:preferencestate",
        "listAllProperties": "disabled",
        "pager": "disabled",
        "prompt": [
            "host",
            "user",
            "status",
            "current-folder",
            "config-sync-status",
        ],
        "selfLink": "https://localhost/mgmt/tm/cli/preference?ver=14.1.2.1",
        "showAliases": "enabled",
        "showImportedVersions": "disabled",
        "statUnits": "default",
        "tableIndentWidth": 2,
        "tclSyntaxHighlighting": "disabled",
        "video": "enabled",
        "warn": "bell",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CliPreference(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CliPreference(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
