# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_live_update_server_technologiesinstallations
from genie.libs.parser.bigip.get_live_update_server_technologiesinstallations import (
    Live_updateServertechnologiesInstallations,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/live-update/server-technologies/installations'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:live-update:server-technologies:installations-collectionstate",
            "totalItems": 1,
            "selfLink": "https://localhost/mgmt/tm/live-update/server-technologies/installations",
            "items": [
                {
                    "id": "ff8080816db607de016db607dfb40011",
                    "lastUpdateMicros": 1570717032371000,
                    "updateFileReference": {
                        "link": "https://localhost/mgmt/tm/live-update/server-technologies/update-files/ff8080816db607de016db607df57000d"
                    },
                    "status": "install-complete",
                    "kind": "tm:live-update:server-technologies:installationsstate",
                    "selfLink": "https://localhost/mgmt/tm/live-update/server-technologies/installations/ff8080816db607de016db607dfb40011",
                }
            ],
        }


class test_get_live_update_server_technologiesinstallations(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "id": "ff8080816db607de016db607dfb40011",
                "kind": "tm:live-update:server-technologies:installationsstate",
                "lastUpdateMicros": 1570717032371000,
                "selfLink": "https://localhost/mgmt/tm/live-update/server-technologies/installations/ff8080816db607de016db607dfb40011",
                "status": "install-complete",
                "updateFileReference": {
                    "link": "https://localhost/mgmt/tm/live-update/server-technologies/update-files/ff8080816db607de016db607df57000d"
                },
            }
        ],
        "kind": "tm:live-update:server-technologies:installations-collectionstate",
        "selfLink": "https://localhost/mgmt/tm/live-update/server-technologies/installations",
        "totalItems": 1,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = Live_updateServertechnologiesInstallations(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Live_updateServertechnologiesInstallations(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
