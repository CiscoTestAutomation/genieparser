# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_file_apmcustomization_template_file
from genie.libs.parser.bigip.get_file_apmcustomization_template_file import (
    FileApmCustomizationtemplatefile,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/file/apm/policy/customization-template-file'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [],
            "generation": 0,
            "lastUpdateMicros": 0,
            "kind": "tm:file:apm:policy:customization-template-file:fileobjectcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/file/apm/policy/customization-template-file",
        }


class test_get_file_apmcustomization_template_file(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [],
        "kind": "tm:file:apm:policy:customization-template-file:fileobjectcollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/file/apm/policy/customization-template-file",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = FileApmCustomizationtemplatefile(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = FileApmCustomizationtemplatefile(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
