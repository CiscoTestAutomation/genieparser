# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_daemon_log_settingsmcpd
from genie.libs.parser.bigip.get_sys_daemon_log_settingsmcpd import (
    SysDaemonlogsettingsMcpd,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/daemon-log-settings/mcpd'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:daemon-log-settings:mcpd:mcpdstate",
            "selfLink": "https://localhost/mgmt/tm/sys/daemon-log-settings/mcpd?ver=14.1.2.1",
            "audit": "enabled",
            "logLevel": "notice",
        }


class test_get_sys_daemon_log_settingsmcpd(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "audit": "enabled",
        "kind": "tm:sys:daemon-log-settings:mcpd:mcpdstate",
        "logLevel": "notice",
        "selfLink": "https://localhost/mgmt/tm/sys/daemon-log-settings/mcpd?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysDaemonlogsettingsMcpd(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysDaemonlogsettingsMcpd(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
