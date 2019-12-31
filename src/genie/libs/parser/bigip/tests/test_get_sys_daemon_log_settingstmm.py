# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_daemon_log_settingstmm
from genie.libs.parser.bigip.get_sys_daemon_log_settingstmm import (
    SysDaemonlogsettingsTmm,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/daemon-log-settings/tmm'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:daemon-log-settings:tmm:tmmstate",
            "selfLink": "https://localhost/mgmt/tm/sys/daemon-log-settings/tmm?ver=14.1.2.1",
            "arpLogLevel": "warning",
            "httpCompressionLogLevel": "error",
            "httpLogLevel": "error",
            "ipLogLevel": "warning",
            "iruleLogLevel": "informational",
            "layer4LogLevel": "notice",
            "netLogLevel": "warning",
            "osLogLevel": "notice",
            "pvaLogLevel": "informational",
            "sslLogLevel": "warning",
        }


class test_get_sys_daemon_log_settingstmm(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "arpLogLevel": "warning",
        "httpCompressionLogLevel": "error",
        "httpLogLevel": "error",
        "ipLogLevel": "warning",
        "iruleLogLevel": "informational",
        "kind": "tm:sys:daemon-log-settings:tmm:tmmstate",
        "layer4LogLevel": "notice",
        "netLogLevel": "warning",
        "osLogLevel": "notice",
        "pvaLogLevel": "informational",
        "selfLink": "https://localhost/mgmt/tm/sys/daemon-log-settings/tmm?ver=14.1.2.1",
        "sslLogLevel": "warning",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysDaemonlogsettingsTmm(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysDaemonlogsettingsTmm(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
