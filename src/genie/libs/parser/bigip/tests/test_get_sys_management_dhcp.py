# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_management_dhcp
from genie.libs.parser.bigip.get_sys_management_dhcp import SysManagementdhcp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/management-dhcp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:management-dhcp:management-dhcpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/management-dhcp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:management-dhcp:management-dhcpstate",
                    "name": "sys-mgmt-dhcp-config",
                    "partition": "Common",
                    "fullPath": "/Common/sys-mgmt-dhcp-config",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/management-dhcp/~Common~sys-mgmt-dhcp-config?ver=14.1.2.1",
                    "requestOptions": [
                        "subnet-mask",
                        "broadcast-address",
                        "routers",
                        "domain-name",
                        "domain-name-servers",
                        "host-name",
                        "ntp-servers",
                        "interface-mtu",
                    ],
                }
            ],
        }


class test_get_sys_management_dhcp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/sys-mgmt-dhcp-config",
                "generation": 1,
                "kind": "tm:sys:management-dhcp:management-dhcpstate",
                "name": "sys-mgmt-dhcp-config",
                "partition": "Common",
                "requestOptions": [
                    "subnet-mask",
                    "broadcast-address",
                    "routers",
                    "domain-name",
                    "domain-name-servers",
                    "host-name",
                    "ntp-servers",
                    "interface-mtu",
                ],
                "selfLink": "https://localhost/mgmt/tm/sys/management-dhcp/~Common~sys-mgmt-dhcp-config?ver=14.1.2.1",
            }
        ],
        "kind": "tm:sys:management-dhcp:management-dhcpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/management-dhcp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysManagementdhcp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysManagementdhcp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
