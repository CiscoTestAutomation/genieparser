# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_log_configlocal_syslog
from genie.libs.parser.bigip.get_sys_log_configlocal_syslog import (
    SysLogconfigLocalsyslog,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/log-config/destination/local-syslog'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:log-config:destination:local-syslog:local-syslogcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:log-config:destination:local-syslog:local-syslogstate",
                    "name": "local-syslog",
                    "partition": "Common",
                    "fullPath": "/Common/local-syslog",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog/~Common~local-syslog?ver=14.1.2.1",
                    "defaultFacility": "local0",
                    "defaultSeverity": "info",
                }
            ],
        }


class test_get_sys_log_configlocal_syslog(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "defaultFacility": "local0",
                "defaultSeverity": "info",
                "fullPath": "/Common/local-syslog",
                "generation": 1,
                "kind": "tm:sys:log-config:destination:local-syslog:local-syslogstate",
                "name": "local-syslog",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog/~Common~local-syslog?ver=14.1.2.1",
            }
        ],
        "kind": "tm:sys:log-config:destination:local-syslog:local-syslogcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/log-config/destination/local-syslog?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysLogconfigLocalsyslog(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysLogconfigLocalsyslog(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
