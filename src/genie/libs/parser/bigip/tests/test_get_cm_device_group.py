# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cm_device_group
from genie.libs.parser.bigip.get_cm_device_group import CmDevicegroup

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cm/device-group'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:cm:device-group:device-groupcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/cm/device-group?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:cm:device-group:device-groupstate",
                    "name": "device_trust_group",
                    "partition": "Common",
                    "fullPath": "/Common/device_trust_group",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/cm/device-group/~Common~device_trust_group?ver=14.1.2.1",
                    "asmSync": "disabled",
                    "autoSync": "enabled",
                    "fullLoadOnSync": "false",
                    "incrementalConfigSyncSizeMax": 1024,
                    "networkFailover": "disabled",
                    "saveOnAutoSync": "false",
                    "type": "sync-only",
                    "devicesReference": {
                        "link": "https://localhost/mgmt/tm/cm/device-group/~Common~device_trust_group/devices?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:cm:device-group:device-groupstate",
                    "name": "gtm",
                    "partition": "Common",
                    "fullPath": "/Common/gtm",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/cm/device-group/~Common~gtm?ver=14.1.2.1",
                    "asmSync": "disabled",
                    "autoSync": "disabled",
                    "fullLoadOnSync": "false",
                    "incrementalConfigSyncSizeMax": 1024,
                    "networkFailover": "disabled",
                    "saveOnAutoSync": "false",
                    "type": "sync-only",
                    "devicesReference": {
                        "link": "https://localhost/mgmt/tm/cm/device-group/~Common~gtm/devices?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
            ],
        }


class test_get_cm_device_group(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "asmSync": "disabled",
                "autoSync": "enabled",
                "devicesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/cm/device-group/~Common~device_trust_group/devices?ver=14.1.2.1",
                },
                "fullLoadOnSync": "false",
                "fullPath": "/Common/device_trust_group",
                "generation": 1,
                "incrementalConfigSyncSizeMax": 1024,
                "kind": "tm:cm:device-group:device-groupstate",
                "name": "device_trust_group",
                "networkFailover": "disabled",
                "partition": "Common",
                "saveOnAutoSync": "false",
                "selfLink": "https://localhost/mgmt/tm/cm/device-group/~Common~device_trust_group?ver=14.1.2.1",
                "type": "sync-only",
            },
            {
                "asmSync": "disabled",
                "autoSync": "disabled",
                "devicesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/cm/device-group/~Common~gtm/devices?ver=14.1.2.1",
                },
                "fullLoadOnSync": "false",
                "fullPath": "/Common/gtm",
                "generation": 1,
                "incrementalConfigSyncSizeMax": 1024,
                "kind": "tm:cm:device-group:device-groupstate",
                "name": "gtm",
                "networkFailover": "disabled",
                "partition": "Common",
                "saveOnAutoSync": "false",
                "selfLink": "https://localhost/mgmt/tm/cm/device-group/~Common~gtm?ver=14.1.2.1",
                "type": "sync-only",
            },
        ],
        "kind": "tm:cm:device-group:device-groupcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/cm/device-group?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CmDevicegroup(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CmDevicegroup(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
