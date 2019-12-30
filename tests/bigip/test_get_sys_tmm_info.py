# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_tmm_info
from genie.libs.parser.bigip.get_sys_tmm_info import SysTmminfo

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/tmm-info'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:tmm-info:tmm-infostats",
            "selfLink": "https://localhost/mgmt/tm/sys/tmm-info?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/tmm-info/0.0": {
                    "nestedStats": {
                        "entries": {
                            "cpu": {"value": 0},
                            "fiveMinAvgUsageRatio": {"value": 1},
                            "fiveSecAvgUsageRatio": {"value": 1},
                            "memoryTotal": {"value": 2155872256},
                            "memoryUsed": {"value": 235604408},
                            "npus": {"value": 1},
                            "oneMinAvgUsageRatio": {"value": 1},
                            "tmid": {"value": 0},
                            "tmmId": {"description": "0.0"},
                            "tmmPid": {"value": 9762},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/tmm-info/0.1": {
                    "nestedStats": {
                        "entries": {
                            "cpu": {"value": 1},
                            "fiveMinAvgUsageRatio": {"value": 1},
                            "fiveSecAvgUsageRatio": {"value": 1},
                            "memoryTotal": {"value": 0},
                            "memoryUsed": {"value": 0},
                            "npus": {"value": 1},
                            "oneMinAvgUsageRatio": {"value": 1},
                            "tmid": {"value": 1},
                            "tmmId": {"description": "0.1"},
                            "tmmPid": {"value": 9762},
                        }
                    }
                },
            },
        }


class test_get_sys_tmm_info(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:tmm-info:tmm-infostats",
            "selfLink": "https://localhost/mgmt/tm/sys/tmm-info?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/tmm-info/0.0": {
                    "nestedStats": {
                        "entries": {
                            "cpu": {"value": 0},
                            "fiveMinAvgUsageRatio": {"value": 1},
                            "fiveSecAvgUsageRatio": {"value": 1},
                            "memoryTotal": {"value": 2155872256},
                            "memoryUsed": {"value": 235604408},
                            "npus": {"value": 1},
                            "oneMinAvgUsageRatio": {"value": 1},
                            "tmid": {"value": 0},
                            "tmmId": {"description": "0.0"},
                            "tmmPid": {"value": 9762},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/tmm-info/0.1": {
                    "nestedStats": {
                        "entries": {
                            "cpu": {"value": 1},
                            "fiveMinAvgUsageRatio": {"value": 1},
                            "fiveSecAvgUsageRatio": {"value": 1},
                            "memoryTotal": {"value": 0},
                            "memoryUsed": {"value": 0},
                            "npus": {"value": 1},
                            "oneMinAvgUsageRatio": {"value": 1},
                            "tmid": {"value": 1},
                            "tmmId": {"description": "0.1"},
                            "tmmPid": {"value": 9762},
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysTmminfo(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysTmminfo(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
