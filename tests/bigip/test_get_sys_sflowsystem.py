# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_sflowsystem
from genie.libs.parser.bigip.get_sys_sflowsystem import SysSflowSystem

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/sflow/data-source/system'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:sflow:data-source:system:systemstats",
            "selfLink": "https://localhost/mgmt/tm/sys/sflow/data-source/system?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/sflow/data-source/system/system": {
                    "nestedStats": {
                        "entries": {
                            "isActive": {"description": "no"},
                            "tmName": {"description": "system"},
                            "pollInterval": {"value": 10},
                        }
                    }
                }
            },
        }


class test_get_sys_sflowsystem(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/sflow/data-source/system/system": {
                "nestedStats": {
                    "entries": {
                        "isActive": {"description": "no"},
                        "pollInterval": {"value": 10},
                        "tmName": {"description": "system"},
                    }
                }
            }
        },
        "kind": "tm:sys:sflow:data-source:system:systemstats",
        "selfLink": "https://localhost/mgmt/tm/sys/sflow/data-source/system?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysSflowSystem(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysSflowSystem(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
