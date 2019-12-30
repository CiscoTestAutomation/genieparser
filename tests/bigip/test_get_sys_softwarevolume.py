# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_softwarevolume
from genie.libs.parser.bigip.get_sys_softwarevolume import SysSoftwareVolume

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/software/volume'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:software:volume:volumecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/software/volume?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:software:volume:volumestate",
                    "name": "HD1.1",
                    "fullPath": "HD1.1",
                    "generation": 2118,
                    "selfLink": "https://localhost/mgmt/tm/sys/software/volume/HD1.1?ver=14.1.2.1",
                    "active": True,
                    "apiRawValues": {},
                    "basebuild": "0.0.4",
                    "build": "0.0.4",
                    "product": "BIG-IP",
                    "status": "complete",
                    "version": "14.1.2.1",
                    "media": [
                        {
                            "name": "HD1.1",
                            "defaultBootLocation": True,
                            "media": "hd",
                            "size": "default",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/sys/software/volume/HD1.1?ver=14.1.2.1"
                            },
                        }
                    ],
                }
            ],
        }


class test_get_sys_softwarevolume(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "active": True,
                "apiRawValues": {},
                "basebuild": "0.0.4",
                "build": "0.0.4",
                "fullPath": "HD1.1",
                "generation": 2118,
                "kind": "tm:sys:software:volume:volumestate",
                "media": [
                    {
                        "defaultBootLocation": True,
                        "media": "hd",
                        "name": "HD1.1",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/sys/software/volume/HD1.1?ver=14.1.2.1"
                        },
                        "size": "default",
                    }
                ],
                "name": "HD1.1",
                "product": "BIG-IP",
                "selfLink": "https://localhost/mgmt/tm/sys/software/volume/HD1.1?ver=14.1.2.1",
                "status": "complete",
                "version": "14.1.2.1",
            }
        ],
        "kind": "tm:sys:software:volume:volumecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/software/volume?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysSoftwareVolume(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysSoftwareVolume(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
