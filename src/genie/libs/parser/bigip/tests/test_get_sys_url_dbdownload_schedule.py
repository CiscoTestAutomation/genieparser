# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_url_dbdownload_schedule
from genie.libs.parser.bigip.get_sys_url_dbdownload_schedule import (
    SysUrldbDownloadschedule,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/url-db/download-schedule'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:url-db:download-schedule:download-schedulecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/url-db/download-schedule?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:url-db:download-schedule:download-schedulestate",
                    "name": "urldb",
                    "partition": "Common",
                    "fullPath": "/Common/urldb",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/url-db/download-schedule/~Common~urldb?ver=14.1.2.1",
                    "downloadNow": "false",
                    "endTime": "3:00",
                    "startTime": "1:00",
                    "status": "true",
                    "useProxy": "false",
                }
            ],
        }


class test_get_sys_url_dbdownload_schedule(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "downloadNow": "false",
                "endTime": "3:00",
                "fullPath": "/Common/urldb",
                "generation": 1,
                "kind": "tm:sys:url-db:download-schedule:download-schedulestate",
                "name": "urldb",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/url-db/download-schedule/~Common~urldb?ver=14.1.2.1",
                "startTime": "1:00",
                "status": "true",
                "useProxy": "false",
            }
        ],
        "kind": "tm:sys:url-db:download-schedule:download-schedulecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/url-db/download-schedule?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysUrldbDownloadschedule(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysUrldbDownloadschedule(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
