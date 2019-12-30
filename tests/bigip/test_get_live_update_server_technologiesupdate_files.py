# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_live_update_server_technologiesupdate_files
from genie.libs.parser.bigip.get_live_update_server_technologiesupdate_files import (
    Live_updateServertechnologiesUpdatefiles,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/live-update/server-technologies/update-files'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:live-update:server-technologies:update-files-collectionstate",
            "totalItems": 1,
            "selfLink": "https://localhost/mgmt/tm/live-update/server-technologies/update-files",
            "items": [
                {
                    "id": "ff8080816db607de016db607df57000d",
                    "filename": "ServerTechnologies_20180214_141357.im",
                    "md5": "1A66C0B41A50DC606A72ABC2CE5E855D",
                    "fileLocationReference": {
                        "link": "https://localhost/mgmt/tm/live-update/file-transfer/downloads/ServerTechnologies_20180214_141357.im"
                    },
                    "createDateTime": "2018-02-14T14:13:57Z",
                    "isFileAvailable": True,
                    "isFileManuallyUploaded": False,
                    "isGenesis": True,
                    "kind": "tm:live-update:server-technologies:update-filesstate",
                    "selfLink": "https://localhost/mgmt/tm/live-update/server-technologies/update-files/ff8080816db607de016db607df57000d",
                }
            ],
        }


class test_get_live_update_server_technologiesupdate_files(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "createDateTime": "2018-02-14T14:13:57Z",
                "fileLocationReference": {
                    "link": "https://localhost/mgmt/tm/live-update/file-transfer/downloads/ServerTechnologies_20180214_141357.im"
                },
                "filename": "ServerTechnologies_20180214_141357.im",
                "id": "ff8080816db607de016db607df57000d",
                "isFileAvailable": True,
                "isFileManuallyUploaded": False,
                "isGenesis": True,
                "kind": "tm:live-update:server-technologies:update-filesstate",
                "md5": "1A66C0B41A50DC606A72ABC2CE5E855D",
                "selfLink": "https://localhost/mgmt/tm/live-update/server-technologies/update-files/ff8080816db607de016db607df57000d",
            }
        ],
        "kind": "tm:live-update:server-technologies:update-files-collectionstate",
        "selfLink": "https://localhost/mgmt/tm/live-update/server-technologies/update-files",
        "totalItems": 1,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = Live_updateServertechnologiesUpdatefiles(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Live_updateServertechnologiesUpdatefiles(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
