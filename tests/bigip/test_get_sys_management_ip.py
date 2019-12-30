# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_management_ip
from genie.libs.parser.bigip.get_sys_management_ip import SysManagementip

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/management-ip'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:management-ip:management-ipcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/management-ip?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:management-ip:management-ipstate",
                    "name": "192.168.189.233/24",
                    "fullPath": "192.168.189.233/24",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/management-ip/192.168.189.233~24?ver=14.1.2.1",
                }
            ],
        }


class test_get_sys_management_ip(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "192.168.189.233/24",
                "generation": 1,
                "kind": "tm:sys:management-ip:management-ipstate",
                "name": "192.168.189.233/24",
                "selfLink": "https://localhost/mgmt/tm/sys/management-ip/192.168.189.233~24?ver=14.1.2.1",
            }
        ],
        "kind": "tm:sys:management-ip:management-ipcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/management-ip?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysManagementip(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysManagementip(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
