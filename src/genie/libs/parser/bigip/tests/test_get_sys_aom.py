# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_aom
from genie.libs.parser.bigip.get_sys_aom import SysAom

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/aom'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:aom:aomstate",
            "selfLink": "https://localhost/mgmt/tm/sys/aom?ver=14.1.2.1",
            "ipmi": "disabled",
            "mediaRedirection": "disabled",
            "readonly": "disabled",
            "vkvm": "disabled",
            "webui": "disabled",
        }


class test_get_sys_aom(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "ipmi": "disabled",
        "kind": "tm:sys:aom:aomstate",
        "mediaRedirection": "disabled",
        "readonly": "disabled",
        "selfLink": "https://localhost/mgmt/tm/sys/aom?ver=14.1.2.1",
        "vkvm": "disabled",
        "webui": "disabled",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysAom(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysAom(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
