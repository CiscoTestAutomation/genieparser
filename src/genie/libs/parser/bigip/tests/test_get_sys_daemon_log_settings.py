# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_daemon_log_settings
from genie.libs.parser.bigip.get_sys_daemon_log_settings import (
    SysDaemonlogsettings,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/daemon-log-settings'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:daemon-log-settings:daemon-log-settingscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/daemon-log-settings?ver=14.1.2.1",
            "items": [
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/clusterd?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/csyncd?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/icr-eventd?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/icrd?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/lind?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/mcpd?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/tmm?ver=14.1.2.1"
                    }
                },
            ],
        }


class test_get_sys_daemon_log_settings(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/clusterd?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/csyncd?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/icr-eventd?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/icrd?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/lind?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/mcpd?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/sys/daemon-log-settings/tmm?ver=14.1.2.1"
                }
            },
        ],
        "kind": "tm:sys:daemon-log-settings:daemon-log-settingscollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/daemon-log-settings?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysDaemonlogsettings(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysDaemonlogsettings(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
