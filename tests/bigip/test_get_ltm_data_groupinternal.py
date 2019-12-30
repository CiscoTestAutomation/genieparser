# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_data_groupinternal
from genie.libs.parser.bigip.get_ltm_data_groupinternal import (
    LtmDatagroupInternal,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/data-group/internal'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:data-group:internal:internalcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:data-group:internal:internalstate",
                    "name": "aol",
                    "partition": "Common",
                    "fullPath": "/Common/aol",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal/~Common~aol?ver=14.1.2.1",
                    "type": "ip",
                    "records": [
                        {"name": "64.12.96.0/19", "data": ""},
                        {"name": "195.93.16.0/20", "data": ""},
                        {"name": "195.93.48.0/22", "data": ""},
                        {"name": "195.93.64.0/19", "data": ""},
                        {"name": "195.93.96.0/19", "data": ""},
                        {"name": "198.81.0.0/22", "data": ""},
                        {"name": "198.81.8.0/23", "data": ""},
                        {"name": "198.81.16.0/20", "data": ""},
                        {"name": "202.67.65.128/25", "data": ""},
                        {"name": "205.188.112.0/20", "data": ""},
                        {"name": "205.188.146.144/30", "data": ""},
                        {"name": "205.188.192.0/20", "data": ""},
                        {"name": "205.188.208.0/23", "data": ""},
                        {"name": "207.200.112.0/21", "data": ""},
                    ],
                },
                {
                    "kind": "tm:ltm:data-group:internal:internalstate",
                    "name": "images",
                    "partition": "Common",
                    "fullPath": "/Common/images",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal/~Common~images?ver=14.1.2.1",
                    "type": "string",
                    "records": [
                        {"name": ".bmp", "data": ""},
                        {"name": ".gif", "data": ""},
                        {"name": ".jpg", "data": ""},
                    ],
                },
                {
                    "kind": "tm:ltm:data-group:internal:internalstate",
                    "name": "private_net",
                    "partition": "Common",
                    "fullPath": "/Common/private_net",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal/~Common~private_net?ver=14.1.2.1",
                    "type": "ip",
                    "records": [
                        {"name": "10.0.0.0/8", "data": ""},
                        {"name": "172.16.0.0/12", "data": ""},
                        {"name": "192.168.0.0/16", "data": ""},
                    ],
                },
                {
                    "kind": "tm:ltm:data-group:internal:internalstate",
                    "name": "sys_APM_MS_Office_OFBA_DG",
                    "partition": "Common",
                    "fullPath": "/Common/sys_APM_MS_Office_OFBA_DG",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal/~Common~sys_APM_MS_Office_OFBA_DG?ver=14.1.2.1",
                    "description": "This internal data-group is used in _sys_APM_MS_Office_OFBA_Support irule",
                    "type": "string",
                    "records": [
                        {"name": "ie_sp_session_sharing_enabled", "data": "0"},
                        {
                            "name": "ie_sp_session_sharing_inactivity_timeout",
                            "data": "60",
                        },
                        {"name": "ofba_auth_dialog_size", "data": "800x600"},
                        {
                            "name": "useragent1",
                            "data": "microsoft data access internet publishing provider",
                        },
                        {
                            "name": "useragent2",
                            "data": "office protocol discovery",
                        },
                        {"name": "useragent3", "data": "microsoft office"},
                        {"name": "useragent4", "data": "non-browser"},
                        {"name": "useragent5", "data": "msoffice 12"},
                        {
                            "name": "useragent6",
                            "data": "microsoft-webdav-miniredir",
                        },
                        {"name": "useragent7", "data": "webdav-miniredir"},
                        {
                            "name": "useragent9",
                            "data": "ms frontpage 1[23456789]",
                        },
                        {"name": "useragent10", "data": "onenote"},
                    ],
                },
            ],
        }


class test_get_ltm_data_groupinternal(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/aol",
                "generation": 1,
                "kind": "tm:ltm:data-group:internal:internalstate",
                "name": "aol",
                "partition": "Common",
                "records": [
                    {"data": "", "name": "64.12.96.0/19"},
                    {"data": "", "name": "195.93.16.0/20"},
                    {"data": "", "name": "195.93.48.0/22"},
                    {"data": "", "name": "195.93.64.0/19"},
                    {"data": "", "name": "195.93.96.0/19"},
                    {"data": "", "name": "198.81.0.0/22"},
                    {"data": "", "name": "198.81.8.0/23"},
                    {"data": "", "name": "198.81.16.0/20"},
                    {"data": "", "name": "202.67.65.128/25"},
                    {"data": "", "name": "205.188.112.0/20"},
                    {"data": "", "name": "205.188.146.144/30"},
                    {"data": "", "name": "205.188.192.0/20"},
                    {"data": "", "name": "205.188.208.0/23"},
                    {"data": "", "name": "207.200.112.0/21"},
                ],
                "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal/~Common~aol?ver=14.1.2.1",
                "type": "ip",
            },
            {
                "fullPath": "/Common/images",
                "generation": 1,
                "kind": "tm:ltm:data-group:internal:internalstate",
                "name": "images",
                "partition": "Common",
                "records": [
                    {"data": "", "name": ".bmp"},
                    {"data": "", "name": ".gif"},
                    {"data": "", "name": ".jpg"},
                ],
                "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal/~Common~images?ver=14.1.2.1",
                "type": "string",
            },
            {
                "fullPath": "/Common/private_net",
                "generation": 1,
                "kind": "tm:ltm:data-group:internal:internalstate",
                "name": "private_net",
                "partition": "Common",
                "records": [
                    {"data": "", "name": "10.0.0.0/8"},
                    {"data": "", "name": "172.16.0.0/12"},
                    {"data": "", "name": "192.168.0.0/16"},
                ],
                "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal/~Common~private_net?ver=14.1.2.1",
                "type": "ip",
            },
            {
                "description": "This internal data-group is used in "
                "_sys_APM_MS_Office_OFBA_Support irule",
                "fullPath": "/Common/sys_APM_MS_Office_OFBA_DG",
                "generation": 1,
                "kind": "tm:ltm:data-group:internal:internalstate",
                "name": "sys_APM_MS_Office_OFBA_DG",
                "partition": "Common",
                "records": [
                    {"data": "0", "name": "ie_sp_session_sharing_enabled"},
                    {
                        "data": "60",
                        "name": "ie_sp_session_sharing_inactivity_timeout",
                    },
                    {"data": "800x600", "name": "ofba_auth_dialog_size"},
                    {
                        "data": "microsoft data access internet publishing "
                        "provider",
                        "name": "useragent1",
                    },
                    {
                        "data": "office protocol discovery",
                        "name": "useragent2",
                    },
                    {"data": "microsoft office", "name": "useragent3"},
                    {"data": "non-browser", "name": "useragent4"},
                    {"data": "msoffice 12", "name": "useragent5"},
                    {
                        "data": "microsoft-webdav-miniredir",
                        "name": "useragent6",
                    },
                    {"data": "webdav-miniredir", "name": "useragent7"},
                    {"data": "ms frontpage 1[23456789]", "name": "useragent9"},
                    {"data": "onenote", "name": "useragent10"},
                ],
                "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal/~Common~sys_APM_MS_Office_OFBA_DG?ver=14.1.2.1",
                "type": "string",
            },
        ],
        "kind": "tm:ltm:data-group:internal:internalcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/data-group/internal?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmDatagroupInternal(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmDatagroupInternal(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
