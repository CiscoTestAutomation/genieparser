# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_port_list
from genie.libs.parser.bigip.get_net_port_list import NetPortlist

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/port-list'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:port-list:port-listcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/port-list?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:port-list:port-liststate",
                    "name": "_sys_self_allow_tcp_defaults",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_self_allow_tcp_defaults",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/port-list/~Common~_sys_self_allow_tcp_defaults?ver=14.1.2.1",
                    "ports": [
                        {"name": "22"},
                        {"name": "53"},
                        {"name": "161"},
                        {"name": "443"},
                        {"name": "1029-1043"},
                        {"name": "4353"},
                    ],
                },
                {
                    "kind": "tm:net:port-list:port-liststate",
                    "name": "_sys_self_allow_udp_defaults",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_self_allow_udp_defaults",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/port-list/~Common~_sys_self_allow_udp_defaults?ver=14.1.2.1",
                    "ports": [
                        {"name": "53"},
                        {"name": "161"},
                        {"name": "520"},
                        {"name": "1026"},
                        {"name": "4353"},
                    ],
                },
            ],
        }


class test_get_net_port_list(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/_sys_self_allow_tcp_defaults",
                "generation": 1,
                "kind": "tm:net:port-list:port-liststate",
                "name": "_sys_self_allow_tcp_defaults",
                "partition": "Common",
                "ports": [
                    {"name": "22"},
                    {"name": "53"},
                    {"name": "161"},
                    {"name": "443"},
                    {"name": "1029-1043"},
                    {"name": "4353"},
                ],
                "selfLink": "https://localhost/mgmt/tm/net/port-list/~Common~_sys_self_allow_tcp_defaults?ver=14.1.2.1",
            },
            {
                "fullPath": "/Common/_sys_self_allow_udp_defaults",
                "generation": 1,
                "kind": "tm:net:port-list:port-liststate",
                "name": "_sys_self_allow_udp_defaults",
                "partition": "Common",
                "ports": [
                    {"name": "53"},
                    {"name": "161"},
                    {"name": "520"},
                    {"name": "1026"},
                    {"name": "4353"},
                ],
                "selfLink": "https://localhost/mgmt/tm/net/port-list/~Common~_sys_self_allow_udp_defaults?ver=14.1.2.1",
            },
        ],
        "kind": "tm:net:port-list:port-listcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/port-list?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetPortlist(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetPortlist(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
