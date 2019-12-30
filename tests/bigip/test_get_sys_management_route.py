# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_management_route
from genie.libs.parser.bigip.get_sys_management_route import SysManagementroute

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/management-route'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:management-route:management-routecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/management-route?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:management-route:management-routestate",
                    "name": "default",
                    "partition": "Common",
                    "fullPath": "/Common/default",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/management-route/~Common~default?ver=14.1.2.1",
                    "gateway": "192.168.189.254",
                    "mtu": 0,
                    "network": "default",
                },
                {
                    "kind": "tm:sys:management-route:management-routestate",
                    "name": "MGMT_ROUTE_1",
                    "partition": "Common",
                    "fullPath": "/Common/MGMT_ROUTE_1",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/management-route/~Common~MGMT_ROUTE_1?ver=14.1.2.1",
                    "gateway": "192.168.0.1",
                    "mtu": 0,
                    "network": "172.24.2.0/24",
                },
            ],
        }


class test_get_sys_management_route(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/default",
                "gateway": "192.168.189.254",
                "generation": 1,
                "kind": "tm:sys:management-route:management-routestate",
                "mtu": 0,
                "name": "default",
                "network": "default",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/management-route/~Common~default?ver=14.1.2.1",
            },
            {
                "fullPath": "/Common/MGMT_ROUTE_1",
                "gateway": "192.168.0.1",
                "generation": 1,
                "kind": "tm:sys:management-route:management-routestate",
                "mtu": 0,
                "name": "MGMT_ROUTE_1",
                "network": "172.24.2.0/24",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/sys/management-route/~Common~MGMT_ROUTE_1?ver=14.1.2.1",
            },
        ],
        "kind": "tm:sys:management-route:management-routecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/management-route?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysManagementroute(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysManagementroute(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
