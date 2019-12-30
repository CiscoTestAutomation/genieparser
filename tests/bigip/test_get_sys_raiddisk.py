# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_raiddisk
from genie.libs.parser.bigip.get_sys_raiddisk import SysRaidDisk

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/raid/disk'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:raid:disk:diskcollectionstats",
            "selfLink": "https://localhost/mgmt/tm/sys/raid/disk?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/raid/disk/HD1": {
                    "nestedStats": {
                        "kind": "tm:sys:raid:disk:diskstats",
                        "selfLink": "https://localhost/mgmt/tm/sys/raid/disk/HD1?ver=14.1.2.1",
                        "entries": {
                            "arrayStatus": {"description": "undefined"},
                            "isArrayMember": {"description": "no"},
                            "model": {
                                "description": "VMware, VMware Virtual S"
                            },
                            "tmName": {"description": "HD1"},
                            "serialNumber": {"description": "VMware-sda"},
                        },
                    }
                }
            },
        }


class test_get_sys_raiddisk(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/raid/disk/HD1": {
                "nestedStats": {
                    "entries": {
                        "arrayStatus": {"description": "undefined"},
                        "isArrayMember": {"description": "no"},
                        "model": {
                            "description": "VMware, " "VMware " "Virtual " "S"
                        },
                        "serialNumber": {"description": "VMware-sda"},
                        "tmName": {"description": "HD1"},
                    },
                    "kind": "tm:sys:raid:disk:diskstats",
                    "selfLink": "https://localhost/mgmt/tm/sys/raid/disk/HD1?ver=14.1.2.1",
                }
            }
        },
        "kind": "tm:sys:raid:disk:diskcollectionstats",
        "selfLink": "https://localhost/mgmt/tm/sys/raid/disk?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysRaidDisk(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysRaidDisk(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
