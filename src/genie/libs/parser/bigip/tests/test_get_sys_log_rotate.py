# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_log_rotate
from genie.libs.parser.bigip.get_sys_log_rotate import SysLogrotate

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/log-rotate'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:log-rotate:log-rotatestate",
            "selfLink": "https://localhost/mgmt/tm/sys/log-rotate?ver=14.1.2.1",
            "commonBacklogs": 24,
            "ilxRotations": "10",
            "ilxSchedule": "daily",
            "ilxSize": "10240",
            "maxFileSize": 1024000,
        }


class test_get_sys_log_rotate(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "commonBacklogs": 24,
        "ilxRotations": "10",
        "ilxSchedule": "daily",
        "ilxSize": "10240",
        "kind": "tm:sys:log-rotate:log-rotatestate",
        "maxFileSize": 1024000,
        "selfLink": "https://localhost/mgmt/tm/sys/log-rotate?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysLogrotate(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysLogrotate(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
