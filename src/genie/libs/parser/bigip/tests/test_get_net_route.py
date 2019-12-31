# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_route
from genie.libs.parser.bigip.get_net_route import NetRoute

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/route'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:route:routecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/route?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:route:routestate",
                    "name": "Defaul_Route",
                    "partition": "Common",
                    "fullPath": "/Common/Defaul_Route",
                    "generation": 1017,
                    "selfLink": "https://localhost/mgmt/tm/net/route/~Common~Defaul_Route?ver=14.1.2.1",
                    "description": "Default",
                    "gw": "192.168.40.2",
                    "mtu": 0,
                    "network": "default",
                },
                {
                    "kind": "tm:net:route:routestate",
                    "name": "One_route",
                    "partition": "Common",
                    "fullPath": "/Common/One_route",
                    "generation": 1374,
                    "selfLink": "https://localhost/mgmt/tm/net/route/~Common~One_route?ver=14.1.2.1",
                    "description": "Default",
                    "gw": "192.168.40.2",
                    "mtu": 0,
                    "network": "1.1.1.0/24",
                },
                {
                    "kind": "tm:net:route:routestate",
                    "name": "Three_Route",
                    "partition": "Common",
                    "fullPath": "/Common/Three_Route",
                    "generation": 1376,
                    "selfLink": "https://localhost/mgmt/tm/net/route/~Common~Three_Route?ver=14.1.2.1",
                    "description": "Default",
                    "gw": "192.168.40.2",
                    "mtu": 0,
                    "network": "3.3.3.0/24",
                },
                {
                    "kind": "tm:net:route:routestate",
                    "name": "Two_Route",
                    "partition": "Common",
                    "fullPath": "/Common/Two_Route",
                    "generation": 1375,
                    "selfLink": "https://localhost/mgmt/tm/net/route/~Common~Two_Route?ver=14.1.2.1",
                    "description": "Default",
                    "gw": "192.168.40.2",
                    "mtu": 0,
                    "network": "2.2.2.0/24",
                },
            ],
        }


class test_get_net_route(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "description": "Default",
                "fullPath": "/Common/Defaul_Route",
                "generation": 1017,
                "gw": "192.168.40.2",
                "kind": "tm:net:route:routestate",
                "mtu": 0,
                "name": "Defaul_Route",
                "network": "default",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/route/~Common~Defaul_Route?ver=14.1.2.1",
            },
            {
                "description": "Default",
                "fullPath": "/Common/One_route",
                "generation": 1374,
                "gw": "192.168.40.2",
                "kind": "tm:net:route:routestate",
                "mtu": 0,
                "name": "One_route",
                "network": "1.1.1.0/24",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/route/~Common~One_route?ver=14.1.2.1",
            },
            {
                "description": "Default",
                "fullPath": "/Common/Three_Route",
                "generation": 1376,
                "gw": "192.168.40.2",
                "kind": "tm:net:route:routestate",
                "mtu": 0,
                "name": "Three_Route",
                "network": "3.3.3.0/24",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/route/~Common~Three_Route?ver=14.1.2.1",
            },
            {
                "description": "Default",
                "fullPath": "/Common/Two_Route",
                "generation": 1375,
                "gw": "192.168.40.2",
                "kind": "tm:net:route:routestate",
                "mtu": 0,
                "name": "Two_Route",
                "network": "2.2.2.0/24",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/route/~Common~Two_Route?ver=14.1.2.1",
            },
        ],
        "kind": "tm:net:route:routecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/route?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetRoute(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetRoute(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
