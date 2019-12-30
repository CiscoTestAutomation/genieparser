# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_ip_stat
from genie.libs.parser.bigip.get_sys_ip_stat import SysIpstat

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/ip-stat'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:ip-stat:ip-statstats",
            "selfLink": "https://localhost/mgmt/tm/sys/ip-stat?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/ip-stat/0": {
                    "nestedStats": {
                        "entries": {
                            "dropped": {"value": 0},
                            "errCksum": {"value": 0},
                            "errLen": {"value": 0},
                            "errMcastMaxPendingPackets": {"value": 0},
                            "errMcastMaxPendingRoutes": {"value": 0},
                            "errMcastNoRoute": {"value": 0},
                            "errMcastRouteLookupTimeout": {"value": 0},
                            "errMcastRpf": {"value": 0},
                            "errMcastWrongIf": {"value": 0},
                            "errMem": {"value": 0},
                            "errOpt": {"value": 0},
                            "errProto": {"value": 0},
                            "errReassembledTooLong": {"value": 0},
                            "errRtx": {"value": 0},
                            "ipType": {"description": "IPv4"},
                            "mcastRx": {"value": 45},
                            "mcastTx": {"value": 0},
                            "nbrPbqFullDropped": {"value": 0},
                            "nbrUnreachableDropped": {"value": 0},
                            "reassembled": {"value": 0},
                            "rx": {"value": 25363},
                            "rxFrag": {"value": 0},
                            "rxFragDropped": {"value": 0},
                            "tx": {"value": 20427},
                            "txFrag": {"value": 0},
                            "txFragDropped": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ip-stat/1": {
                    "nestedStats": {
                        "entries": {
                            "dropped": {"value": 0},
                            "errCksum": {"value": 0},
                            "errLen": {"value": 0},
                            "errMcastMaxPendingPackets": {"value": 0},
                            "errMcastMaxPendingRoutes": {"value": 0},
                            "errMcastNoRoute": {"value": 0},
                            "errMcastRouteLookupTimeout": {"value": 0},
                            "errMcastRpf": {"value": 0},
                            "errMcastWrongIf": {"value": 0},
                            "errMem": {"value": 0},
                            "errOpt": {"value": 0},
                            "errProto": {"value": 0},
                            "errReassembledTooLong": {"value": 0},
                            "errRtx": {"value": 0},
                            "ipType": {"description": "IPv6"},
                            "mcastRx": {"value": 35},
                            "mcastTx": {"value": 0},
                            "nbrPbqFullDropped": {"value": 0},
                            "nbrUnreachableDropped": {"value": 0},
                            "reassembled": {"value": 0},
                            "rx": {"value": 35},
                            "rxFrag": {"value": 0},
                            "rxFragDropped": {"value": 0},
                            "tx": {"value": 18},
                            "txFrag": {"value": 0},
                            "txFragDropped": {"value": 0},
                        }
                    }
                },
            },
        }


class test_get_sys_ip_stat(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:ip-stat:ip-statstats",
            "selfLink": "https://localhost/mgmt/tm/sys/ip-stat?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/ip-stat/0": {
                    "nestedStats": {
                        "entries": {
                            "dropped": {"value": 0},
                            "errCksum": {"value": 0},
                            "errLen": {"value": 0},
                            "errMcastMaxPendingPackets": {"value": 0},
                            "errMcastMaxPendingRoutes": {"value": 0},
                            "errMcastNoRoute": {"value": 0},
                            "errMcastRouteLookupTimeout": {"value": 0},
                            "errMcastRpf": {"value": 0},
                            "errMcastWrongIf": {"value": 0},
                            "errMem": {"value": 0},
                            "errOpt": {"value": 0},
                            "errProto": {"value": 0},
                            "errReassembledTooLong": {"value": 0},
                            "errRtx": {"value": 0},
                            "ipType": {"description": "IPv4"},
                            "mcastRx": {"value": 45},
                            "mcastTx": {"value": 0},
                            "nbrPbqFullDropped": {"value": 0},
                            "nbrUnreachableDropped": {"value": 0},
                            "reassembled": {"value": 0},
                            "rx": {"value": 25363},
                            "rxFrag": {"value": 0},
                            "rxFragDropped": {"value": 0},
                            "tx": {"value": 20427},
                            "txFrag": {"value": 0},
                            "txFragDropped": {"value": 0},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ip-stat/1": {
                    "nestedStats": {
                        "entries": {
                            "dropped": {"value": 0},
                            "errCksum": {"value": 0},
                            "errLen": {"value": 0},
                            "errMcastMaxPendingPackets": {"value": 0},
                            "errMcastMaxPendingRoutes": {"value": 0},
                            "errMcastNoRoute": {"value": 0},
                            "errMcastRouteLookupTimeout": {"value": 0},
                            "errMcastRpf": {"value": 0},
                            "errMcastWrongIf": {"value": 0},
                            "errMem": {"value": 0},
                            "errOpt": {"value": 0},
                            "errProto": {"value": 0},
                            "errReassembledTooLong": {"value": 0},
                            "errRtx": {"value": 0},
                            "ipType": {"description": "IPv6"},
                            "mcastRx": {"value": 35},
                            "mcastTx": {"value": 0},
                            "nbrPbqFullDropped": {"value": 0},
                            "nbrUnreachableDropped": {"value": 0},
                            "reassembled": {"value": 0},
                            "rx": {"value": 35},
                            "rxFrag": {"value": 0},
                            "rxFragDropped": {"value": 0},
                            "tx": {"value": 18},
                            "txFrag": {"value": 0},
                            "txFragDropped": {"value": 0},
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysIpstat(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysIpstat(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
