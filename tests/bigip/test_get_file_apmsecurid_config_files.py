# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_file_apmsecurid_config_files
from genie.libs.parser.bigip.get_file_apmsecurid_config_files import (
    FileApmSecuridconfigfiles,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/file/apm/aaa/securid-config-files'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [],
            "generation": 0,
            "lastUpdateMicros": 0,
            "kind": "tm:file:apm:aaa:securid-config-files:fileobjectcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/file/apm/aaa/securid-config-files",
        }


class test_get_file_apmsecurid_config_files(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [],
        "kind": "tm:file:apm:aaa:securid-config-files:fileobjectcollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/file/apm/aaa/securid-config-files",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = FileApmSecuridconfigfiles(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = FileApmSecuridconfigfiles(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
