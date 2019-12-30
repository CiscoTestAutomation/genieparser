# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_sync_status
from genie.libs.parser.bigip.get_gtm_sync_status import GtmSyncstatus

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/sync-status'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "syncing": False,
            "big3dDateTime": "2019-09-17T22:36:22.000Z",
            "generation": 0,
            "lastUpdateMicros": 0,
        }


class test_get_gtm_sync_status(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "big3dDateTime": "2019-09-17T22:36:22.000Z",
        "generation": 0,
        "lastUpdateMicros": 0,
        "syncing": False,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmSyncstatus(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmSyncstatus(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
