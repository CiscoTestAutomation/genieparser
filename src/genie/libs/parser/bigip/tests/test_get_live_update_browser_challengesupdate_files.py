# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_live_update_browser_challengesupdate_files
from genie.libs.parser.bigip.get_live_update_browser_challengesupdate_files import (
    Live_updateBrowserchallengesUpdatefiles,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/live-update/browser-challenges/update-files'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:live-update:browser-challenges:update-files-collectionstate",
            "totalItems": 1,
            "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/update-files",
            "items": [
                {
                    "id": "ff8080816db607de016db607df4e000c",
                    "filename": "BrowserChallenges_20180825_225328.im",
                    "md5": "17AA91F6A83E5BF55D2B8622ACB8E9FC",
                    "fileLocationReference": {
                        "link": "https://localhost/mgmt/tm/live-update/file-transfer/downloads/BrowserChallenges_20180825_225328.im"
                    },
                    "createDateTime": "2018-08-25T22:53:28Z",
                    "isFileAvailable": True,
                    "isFileManuallyUploaded": False,
                    "isGenesis": True,
                    "kind": "tm:live-update:browser-challenges:update-filesstate",
                    "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/update-files/ff8080816db607de016db607df4e000c",
                }
            ],
        }


class test_get_live_update_browser_challengesupdate_files(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "createDateTime": "2018-08-25T22:53:28Z",
                "fileLocationReference": {
                    "link": "https://localhost/mgmt/tm/live-update/file-transfer/downloads/BrowserChallenges_20180825_225328.im"
                },
                "filename": "BrowserChallenges_20180825_225328.im",
                "id": "ff8080816db607de016db607df4e000c",
                "isFileAvailable": True,
                "isFileManuallyUploaded": False,
                "isGenesis": True,
                "kind": "tm:live-update:browser-challenges:update-filesstate",
                "md5": "17AA91F6A83E5BF55D2B8622ACB8E9FC",
                "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/update-files/ff8080816db607de016db607df4e000c",
            }
        ],
        "kind": "tm:live-update:browser-challenges:update-files-collectionstate",
        "selfLink": "https://localhost/mgmt/tm/live-update/browser-challenges/update-files",
        "totalItems": 1,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = Live_updateBrowserchallengesUpdatefiles(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Live_updateBrowserchallengesUpdatefiles(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
