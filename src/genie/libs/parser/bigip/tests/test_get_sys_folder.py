# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_folder
from genie.libs.parser.bigip.get_sys_folder import SysFolder

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/folder'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:folder:foldercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/folder?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:folder:folderstate",
                    "name": "/",
                    "fullPath": "/",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/folder/~?ver=14.1.2.1",
                    "deviceGroup": "none",
                    "hidden": "false",
                    "inheritedDevicegroup": "false",
                    "inheritedTrafficGroup": "false",
                    "noRefCheck": "false",
                    "trafficGroup": "/Common/traffic-group-1",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                    },
                },
                {
                    "kind": "tm:sys:folder:folderstate",
                    "name": "Common",
                    "subPath": "/",
                    "fullPath": "/Common",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/folder/~Common?ver=14.1.2.1",
                    "deviceGroup": "none",
                    "hidden": "false",
                    "inheritedDevicegroup": "true",
                    "inheritedTrafficGroup": "true",
                    "noRefCheck": "false",
                    "trafficGroup": "/Common/traffic-group-1",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                    },
                },
                {
                    "kind": "tm:sys:folder:folderstate",
                    "name": "Drafts",
                    "partition": "Common",
                    "fullPath": "/Common/Drafts",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/folder/~Common~Drafts?ver=14.1.2.1",
                    "deviceGroup": "none",
                    "hidden": "false",
                    "inheritedDevicegroup": "true",
                    "inheritedTrafficGroup": "true",
                    "noRefCheck": "false",
                    "trafficGroup": "/Common/traffic-group-1",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                    },
                },
            ],
        }


class test_get_sys_folder(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "deviceGroup": "none",
                "fullPath": "/",
                "generation": 1,
                "hidden": "false",
                "inheritedDevicegroup": "false",
                "inheritedTrafficGroup": "false",
                "kind": "tm:sys:folder:folderstate",
                "name": "/",
                "noRefCheck": "false",
                "selfLink": "https://localhost/mgmt/tm/sys/folder/~?ver=14.1.2.1",
                "trafficGroup": "/Common/traffic-group-1",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                },
            },
            {
                "deviceGroup": "none",
                "fullPath": "/Common",
                "generation": 1,
                "hidden": "false",
                "inheritedDevicegroup": "true",
                "inheritedTrafficGroup": "true",
                "kind": "tm:sys:folder:folderstate",
                "name": "Common",
                "noRefCheck": "false",
                "selfLink": "https://localhost/mgmt/tm/sys/folder/~Common?ver=14.1.2.1",
                "subPath": "/",
                "trafficGroup": "/Common/traffic-group-1",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                },
            },
            {
                "deviceGroup": "none",
                "fullPath": "/Common/Drafts",
                "generation": 1,
                "hidden": "false",
                "inheritedDevicegroup": "true",
                "inheritedTrafficGroup": "true",
                "kind": "tm:sys:folder:folderstate",
                "name": "Drafts",
                "noRefCheck": "false",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/folder/~Common~Drafts?ver=14.1.2.1",
                "trafficGroup": "/Common/traffic-group-1",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                },
            },
        ],
        "kind": "tm:sys:folder:foldercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/folder?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysFolder(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysFolder(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
