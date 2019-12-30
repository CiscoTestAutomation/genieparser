# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cloud_cmdevice_group
from genie.libs.parser.bigip.get_cloud_cmdevice_group import CloudCmDevicegroup

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cloud/cm/device-group'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [
                {
                    "type": "sync-only",
                    "syncState": "group_disconnected",
                    "autoSync": "enabled",
                    "networkFailover": "disabled",
                    "devices": [
                        {
                            "managementIp": "192.168.189.233",
                            "hostname": "bigip01.lab.local",
                            "memberSyncState": "Unknown",
                            "generation": 0,
                            "lastUpdateMicros": 0,
                        }
                    ],
                    "objectId": 12429,
                    "description": "",
                    "name": "device_trust_group",
                    "fullPath": "/Common/device_trust_group",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:cm:device-group:cmdevicegroupstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/cm/device-group/~Common~device_trust_group",
                },
                {
                    "type": "sync-only",
                    "syncState": "group_disconnected",
                    "autoSync": "disabled",
                    "networkFailover": "disabled",
                    "devices": [
                        {
                            "managementIp": "192.168.189.233",
                            "hostname": "bigip01.lab.local",
                            "memberSyncState": "Unknown",
                            "generation": 0,
                            "lastUpdateMicros": 0,
                        }
                    ],
                    "objectId": 12431,
                    "description": "",
                    "name": "gtm",
                    "fullPath": "/Common/gtm",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:cm:device-group:cmdevicegroupstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/cm/device-group/~Common~gtm",
                },
            ],
            "generation": 0,
            "lastUpdateMicros": 0,
            "kind": "tm:cloud:cm:device-group:cmdevicegroupcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/cloud/cm/device-group",
        }


class test_get_cloud_cmdevice_group(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [
            {
                "authPartition": "Common",
                "autoSync": "enabled",
                "description": "",
                "devices": [
                    {
                        "generation": 0,
                        "hostname": "bigip01.lab.local",
                        "lastUpdateMicros": 0,
                        "managementIp": "192.168.189.233",
                        "memberSyncState": "Unknown",
                    }
                ],
                "fullPath": "/Common/device_trust_group",
                "generation": 0,
                "kind": "tm:cloud:cm:device-group:cmdevicegroupstate",
                "lastUpdateMicros": 0,
                "name": "device_trust_group",
                "networkFailover": "disabled",
                "objectId": 12429,
                "selfLink": "https://localhost/mgmt/tm/cloud/cm/device-group/~Common~device_trust_group",
                "syncState": "group_disconnected",
                "type": "sync-only",
            },
            {
                "authPartition": "Common",
                "autoSync": "disabled",
                "description": "",
                "devices": [
                    {
                        "generation": 0,
                        "hostname": "bigip01.lab.local",
                        "lastUpdateMicros": 0,
                        "managementIp": "192.168.189.233",
                        "memberSyncState": "Unknown",
                    }
                ],
                "fullPath": "/Common/gtm",
                "generation": 0,
                "kind": "tm:cloud:cm:device-group:cmdevicegroupstate",
                "lastUpdateMicros": 0,
                "name": "gtm",
                "networkFailover": "disabled",
                "objectId": 12431,
                "selfLink": "https://localhost/mgmt/tm/cloud/cm/device-group/~Common~gtm",
                "syncState": "group_disconnected",
                "type": "sync-only",
            },
        ],
        "kind": "tm:cloud:cm:device-group:cmdevicegroupcollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/cloud/cm/device-group",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CloudCmDevicegroup(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CloudCmDevicegroup(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
