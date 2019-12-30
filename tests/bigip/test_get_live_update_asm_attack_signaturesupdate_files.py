# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_live_update_asm_attack_signaturesupdate_files
from genie.libs.parser.bigip.get_live_update_asm_attack_signaturesupdate_files import (
    Live_updateAsmattacksignaturesUpdatefiles,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/live-update/asm-attack-signatures/update-files'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:live-update:asm-attack-signatures:update-files-collectionstate",
            "totalItems": 1,
            "selfLink": "https://localhost/mgmt/tm/live-update/asm-attack-signatures/update-files",
            "items": [
                {
                    "id": "ff8080816db607de016db607df1e000a",
                    "filename": "ASM-AttackSignatures_20180508_142725.im",
                    "md5": "79022EC76D8A4FB347B407CC86285B27",
                    "fileLocationReference": {
                        "link": "https://localhost/mgmt/tm/live-update/file-transfer/downloads/ASM-AttackSignatures_20180508_142725.im"
                    },
                    "createDateTime": "2018-05-08T14:27:25Z",
                    "isFileAvailable": True,
                    "isFileManuallyUploaded": False,
                    "isGenesis": True,
                    "kind": "tm:live-update:asm-attack-signatures:update-filesstate",
                    "selfLink": "https://localhost/mgmt/tm/live-update/asm-attack-signatures/update-files/ff8080816db607de016db607df1e000a",
                }
            ],
        }


class test_get_live_update_asm_attack_signaturesupdate_files(
    unittest.TestCase
):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "createDateTime": "2018-05-08T14:27:25Z",
                "fileLocationReference": {
                    "link": "https://localhost/mgmt/tm/live-update/file-transfer/downloads/ASM-AttackSignatures_20180508_142725.im"
                },
                "filename": "ASM-AttackSignatures_20180508_142725.im",
                "id": "ff8080816db607de016db607df1e000a",
                "isFileAvailable": True,
                "isFileManuallyUploaded": False,
                "isGenesis": True,
                "kind": "tm:live-update:asm-attack-signatures:update-filesstate",
                "md5": "79022EC76D8A4FB347B407CC86285B27",
                "selfLink": "https://localhost/mgmt/tm/live-update/asm-attack-signatures/update-files/ff8080816db607de016db607df1e000a",
            }
        ],
        "kind": "tm:live-update:asm-attack-signatures:update-files-collectionstate",
        "selfLink": "https://localhost/mgmt/tm/live-update/asm-attack-signatures/update-files",
        "totalItems": 1,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = Live_updateAsmattacksignaturesUpdatefiles(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Live_updateAsmattacksignaturesUpdatefiles(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
