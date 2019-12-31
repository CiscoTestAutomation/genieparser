# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_live_update_bot_signaturesupdate_files
from genie.libs.parser.bigip.get_live_update_bot_signaturesupdate_files import (
    Live_updateBotsignaturesUpdatefiles,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/live-update/bot-signatures/update-files'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:live-update:bot-signatures:update-files-collectionstate",
            "totalItems": 1,
            "selfLink": "https://localhost/mgmt/tm/live-update/bot-signatures/update-files",
            "items": [
                {
                    "id": "ff8080816db607de016db607df23000b",
                    "filename": "BotSignatures_20180515_150859.im",
                    "md5": "8146165C2AADCBCF0174D08AF35CD358",
                    "fileLocationReference": {
                        "link": "https://localhost/mgmt/tm/live-update/file-transfer/downloads/BotSignatures_20180515_150859.im"
                    },
                    "createDateTime": "2018-05-15T15:08:59Z",
                    "isFileAvailable": True,
                    "isFileManuallyUploaded": False,
                    "isGenesis": True,
                    "kind": "tm:live-update:bot-signatures:update-filesstate",
                    "selfLink": "https://localhost/mgmt/tm/live-update/bot-signatures/update-files/ff8080816db607de016db607df23000b",
                }
            ],
        }


class test_get_live_update_bot_signaturesupdate_files(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "createDateTime": "2018-05-15T15:08:59Z",
                "fileLocationReference": {
                    "link": "https://localhost/mgmt/tm/live-update/file-transfer/downloads/BotSignatures_20180515_150859.im"
                },
                "filename": "BotSignatures_20180515_150859.im",
                "id": "ff8080816db607de016db607df23000b",
                "isFileAvailable": True,
                "isFileManuallyUploaded": False,
                "isGenesis": True,
                "kind": "tm:live-update:bot-signatures:update-filesstate",
                "md5": "8146165C2AADCBCF0174D08AF35CD358",
                "selfLink": "https://localhost/mgmt/tm/live-update/bot-signatures/update-files/ff8080816db607de016db607df23000b",
            }
        ],
        "kind": "tm:live-update:bot-signatures:update-files-collectionstate",
        "selfLink": "https://localhost/mgmt/tm/live-update/bot-signatures/update-files",
        "totalItems": 1,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = Live_updateBotsignaturesUpdatefiles(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Live_updateBotsignaturesUpdatefiles(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
