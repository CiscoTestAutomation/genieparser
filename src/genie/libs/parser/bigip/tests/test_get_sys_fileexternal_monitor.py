# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_fileexternal_monitor
from genie.libs.parser.bigip.get_sys_fileexternal_monitor import (
    SysFileExternalmonitor,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/file/external-monitor'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:file:external-monitor:external-monitorcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/file/external-monitor?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:file:external-monitor:external-monitorstate",
                    "name": "arg_example",
                    "partition": "Common",
                    "fullPath": "/Common/arg_example",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/file/external-monitor/~Common~arg_example?ver=14.1.2.1",
                    "checksum": "SHA1:3159:0c78e6641632e47d11802b29cfd119d2233cb80a",
                    "createTime": "2019-09-17T22:26:44Z",
                    "createdBy": "root",
                    "lastUpdateTime": "2019-09-17T22:26:44Z",
                    "mode": 33261,
                    "revision": 1,
                    "size": 3159,
                    "systemPath": "/config/monitors/arg_example",
                    "updatedBy": "root",
                },
                {
                    "kind": "tm:sys:file:external-monitor:external-monitorstate",
                    "name": "paap_version_monitor",
                    "partition": "Common",
                    "fullPath": "/Common/paap_version_monitor",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/file/external-monitor/~Common~paap_version_monitor?ver=14.1.2.1",
                    "checksum": "SHA1:3721:7a6e27d67c8af0e90c3245d4ac80c49df0c73286",
                    "createTime": "2019-09-17T22:26:44Z",
                    "createdBy": "root",
                    "lastUpdateTime": "2019-09-17T22:26:44Z",
                    "mode": 33261,
                    "revision": 1,
                    "size": 3721,
                    "systemPath": "/config/monitors/paap_version_sample",
                    "updatedBy": "root",
                },
                {
                    "kind": "tm:sys:file:external-monitor:external-monitorstate",
                    "name": "sample_monitor",
                    "partition": "Common",
                    "fullPath": "/Common/sample_monitor",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/file/external-monitor/~Common~sample_monitor?ver=14.1.2.1",
                    "checksum": "SHA1:1984:71c41d1bdb5de92179861095e5ffa80c021cbebd",
                    "createTime": "2019-09-17T22:26:44Z",
                    "createdBy": "root",
                    "lastUpdateTime": "2019-09-17T22:26:44Z",
                    "mode": 33261,
                    "revision": 1,
                    "size": 1984,
                    "systemPath": "/config/monitors/sample_monitor",
                    "updatedBy": "root",
                },
            ],
        }


class test_get_sys_fileexternal_monitor(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "checksum": "SHA1:3159:0c78e6641632e47d11802b29cfd119d2233cb80a",
                "createTime": "2019-09-17T22:26:44Z",
                "createdBy": "root",
                "fullPath": "/Common/arg_example",
                "generation": 1,
                "kind": "tm:sys:file:external-monitor:external-monitorstate",
                "lastUpdateTime": "2019-09-17T22:26:44Z",
                "mode": 33261,
                "name": "arg_example",
                "partition": "Common",
                "revision": 1,
                "selfLink": "https://localhost/mgmt/tm/sys/file/external-monitor/~Common~arg_example?ver=14.1.2.1",
                "size": 3159,
                "systemPath": "/config/monitors/arg_example",
                "updatedBy": "root",
            },
            {
                "checksum": "SHA1:3721:7a6e27d67c8af0e90c3245d4ac80c49df0c73286",
                "createTime": "2019-09-17T22:26:44Z",
                "createdBy": "root",
                "fullPath": "/Common/paap_version_monitor",
                "generation": 1,
                "kind": "tm:sys:file:external-monitor:external-monitorstate",
                "lastUpdateTime": "2019-09-17T22:26:44Z",
                "mode": 33261,
                "name": "paap_version_monitor",
                "partition": "Common",
                "revision": 1,
                "selfLink": "https://localhost/mgmt/tm/sys/file/external-monitor/~Common~paap_version_monitor?ver=14.1.2.1",
                "size": 3721,
                "systemPath": "/config/monitors/paap_version_sample",
                "updatedBy": "root",
            },
            {
                "checksum": "SHA1:1984:71c41d1bdb5de92179861095e5ffa80c021cbebd",
                "createTime": "2019-09-17T22:26:44Z",
                "createdBy": "root",
                "fullPath": "/Common/sample_monitor",
                "generation": 1,
                "kind": "tm:sys:file:external-monitor:external-monitorstate",
                "lastUpdateTime": "2019-09-17T22:26:44Z",
                "mode": 33261,
                "name": "sample_monitor",
                "partition": "Common",
                "revision": 1,
                "selfLink": "https://localhost/mgmt/tm/sys/file/external-monitor/~Common~sample_monitor?ver=14.1.2.1",
                "size": 1984,
                "systemPath": "/config/monitors/sample_monitor",
                "updatedBy": "root",
            },
        ],
        "kind": "tm:sys:file:external-monitor:external-monitorcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/file/external-monitor?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysFileExternalmonitor(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysFileExternalmonitor(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
