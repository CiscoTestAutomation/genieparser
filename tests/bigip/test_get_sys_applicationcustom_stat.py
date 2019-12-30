# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_applicationcustom_stat
from genie.libs.parser.bigip.get_sys_applicationcustom_stat import (
    SysApplicationCustomstat,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/application/custom-stat'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:application:custom-stat:custom-statcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/application/custom-stat?ver=14.1.2.1",
            "items": [],
        }


class test_get_sys_applicationcustom_stat(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [],
        "kind": "tm:sys:application:custom-stat:custom-statcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/application/custom-stat?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysApplicationCustomstat(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysApplicationCustomstat(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
