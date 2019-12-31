# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_live_update_threat_campaignsupdate_files
from genie.libs.parser.bigip.get_live_update_threat_campaignsupdate_files import (
    Live_updateThreatcampaignsUpdatefiles,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/live-update/threat-campaigns/update-files'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:live-update:threat-campaigns:update-files-collectionstate",
            "totalItems": 0,
            "selfLink": "https://localhost/mgmt/tm/live-update/threat-campaigns/update-files",
            "items": [],
        }


class test_get_live_update_threat_campaignsupdate_files(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [],
        "kind": "tm:live-update:threat-campaigns:update-files-collectionstate",
        "selfLink": "https://localhost/mgmt/tm/live-update/threat-campaigns/update-files",
        "totalItems": 0,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = Live_updateThreatcampaignsUpdatefiles(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Live_updateThreatcampaignsUpdatefiles(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
