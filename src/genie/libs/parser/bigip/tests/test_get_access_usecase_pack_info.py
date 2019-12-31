# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_access_usecase_pack_info
from genie.libs.parser.bigip.get_access_usecase_pack_info import (
    AccessUsecasepackinfo,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/access/usecase-pack-info'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "message": "UsecasePackInfo is not yet created.",
            "generation": 0,
            "lastUpdateMicros": 0,
        }


class test_get_access_usecase_pack_info(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "lastUpdateMicros": 0,
        "message": "UsecasePackInfo is not yet created.",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AccessUsecasepackinfo(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AccessUsecasepackinfo(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
