# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_disklogical_disk
from genie.libs.parser.bigip.get_sys_disklogical_disk import SysDiskLogicaldisk

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/disk/logical-disk'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:disk:logical-disk:logical-diskcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/disk/logical-disk?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:disk:logical-disk:logical-diskstate",
                    "name": "HD1",
                    "fullPath": "HD1",
                    "generation": 2083,
                    "selfLink": "https://localhost/mgmt/tm/sys/disk/logical-disk/HD1?ver=14.1.2.1",
                    "mode": "mixed",
                    "size": 77824,
                    "vgFree": 21420,
                    "vgInUse": 56184,
                    "vgReserved": 0,
                }
            ],
        }


class test_get_sys_disklogical_disk(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "HD1",
                "generation": 2083,
                "kind": "tm:sys:disk:logical-disk:logical-diskstate",
                "mode": "mixed",
                "name": "HD1",
                "selfLink": "https://localhost/mgmt/tm/sys/disk/logical-disk/HD1?ver=14.1.2.1",
                "size": 77824,
                "vgFree": 21420,
                "vgInUse": 56184,
                "vgReserved": 0,
            }
        ],
        "kind": "tm:sys:disk:logical-disk:logical-diskcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/disk/logical-disk?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysDiskLogicaldisk(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysDiskLogicaldisk(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
