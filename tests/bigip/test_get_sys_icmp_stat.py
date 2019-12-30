# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_icmp_stat
from genie.libs.parser.bigip.get_sys_icmp_stat import SysIcmpstat

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/icmp-stat'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:icmp-stat:icmp-statstats",
            "selfLink": "https://localhost/mgmt/tm/sys/icmp-stat?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/icmp-stat/0": {
                    "nestedStats": {
                        "entries": {
                            "drop": {"value": 0},
                            "err": {"value": 0},
                            "errCksum": {"value": 0},
                            "errLen": {"value": 0},
                            "errMem": {"value": 0},
                            "errOpt": {"value": 0},
                            "errProto": {"value": 0},
                            "errRtx": {"value": 0},
                            "forward": {"value": 0},
                            "ipType": {"description": "IPv4"},
                            "rtx": {"value": 0},
                            "rx": {"value": 3853},
                            "tx": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/icmp-stat/1": {
                    "nestedStats": {
                        "entries": {
                            "drop": {"value": 0},
                            "err": {"value": 0},
                            "errCksum": {"value": 0},
                            "errLen": {"value": 0},
                            "errMem": {"value": 0},
                            "errOpt": {"value": 0},
                            "errProto": {"value": 35},
                            "errRtx": {"value": 0},
                            "forward": {"value": 0},
                            "ipType": {"description": "IPv6"},
                            "rtx": {"value": 0},
                            "rx": {"value": 25},
                            "tx": {"value": 75},
                        }
                    }
                },
            },
        }


class test_get_sys_icmp_stat(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:icmp-stat:icmp-statstats",
            "selfLink": "https://localhost/mgmt/tm/sys/icmp-stat?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/icmp-stat/0": {
                    "nestedStats": {
                        "entries": {
                            "drop": {"value": 0},
                            "err": {"value": 0},
                            "errCksum": {"value": 0},
                            "errLen": {"value": 0},
                            "errMem": {"value": 0},
                            "errOpt": {"value": 0},
                            "errProto": {"value": 0},
                            "errRtx": {"value": 0},
                            "forward": {"value": 0},
                            "ipType": {"description": "IPv4"},
                            "rtx": {"value": 0},
                            "rx": {"value": 3853},
                            "tx": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/icmp-stat/1": {
                    "nestedStats": {
                        "entries": {
                            "drop": {"value": 0},
                            "err": {"value": 0},
                            "errCksum": {"value": 0},
                            "errLen": {"value": 0},
                            "errMem": {"value": 0},
                            "errOpt": {"value": 0},
                            "errProto": {"value": 35},
                            "errRtx": {"value": 0},
                            "forward": {"value": 0},
                            "ipType": {"description": "IPv6"},
                            "rtx": {"value": 0},
                            "rx": {"value": 25},
                            "tx": {"value": 75},
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysIcmpstat(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysIcmpstat(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
