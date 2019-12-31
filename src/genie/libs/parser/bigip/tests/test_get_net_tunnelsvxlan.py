# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelsvxlan
from genie.libs.parser.bigip.get_net_tunnelsvxlan import NetTunnelsVxlan

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/vxlan'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:vxlan:vxlancollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:vxlan:vxlanstate",
                    "name": "vxlan",
                    "partition": "Common",
                    "fullPath": "/Common/vxlan",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1",
                    "encapsulationType": "vxlan",
                    "floodingType": "multicast",
                    "port": 4789,
                },
                {
                    "kind": "tm:net:tunnels:vxlan:vxlanstate",
                    "name": "vxlan-gpe",
                    "partition": "Common",
                    "fullPath": "/Common/vxlan-gpe",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan-gpe?ver=14.1.2.1",
                    "defaultsFrom": "/Common/vxlan",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1"
                    },
                    "encapsulationType": "vxlan-gpe",
                    "floodingType": "multipoint",
                    "port": 4790,
                },
                {
                    "kind": "tm:net:tunnels:vxlan:vxlanstate",
                    "name": "vxlan-multipoint",
                    "partition": "Common",
                    "fullPath": "/Common/vxlan-multipoint",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan-multipoint?ver=14.1.2.1",
                    "defaultsFrom": "/Common/vxlan",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1"
                    },
                    "encapsulationType": "vxlan",
                    "floodingType": "multipoint",
                    "port": 4789,
                },
                {
                    "kind": "tm:net:tunnels:vxlan:vxlanstate",
                    "name": "vxlan-ovsdb",
                    "partition": "Common",
                    "fullPath": "/Common/vxlan-ovsdb",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan-ovsdb?ver=14.1.2.1",
                    "defaultsFrom": "/Common/vxlan",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1"
                    },
                    "encapsulationType": "vxlan",
                    "floodingType": "replicator",
                    "port": 4789,
                },
                {
                    "kind": "tm:net:tunnels:vxlan:vxlanstate",
                    "name": "vxlan-ovsdb-multipoint",
                    "partition": "Common",
                    "fullPath": "/Common/vxlan-ovsdb-multipoint",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan-ovsdb-multipoint?ver=14.1.2.1",
                    "defaultsFrom": "/Common/vxlan",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1"
                    },
                    "encapsulationType": "vxlan",
                    "floodingType": "multipoint",
                    "port": 4789,
                },
                {
                    "kind": "tm:net:tunnels:vxlan:vxlanstate",
                    "name": "vxlan-ovsdb-no-flooding",
                    "partition": "Common",
                    "fullPath": "/Common/vxlan-ovsdb-no-flooding",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan-ovsdb-no-flooding?ver=14.1.2.1",
                    "defaultsFrom": "/Common/vxlan",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1"
                    },
                    "encapsulationType": "vxlan",
                    "floodingType": "none",
                    "port": 4789,
                },
            ],
        }


class test_get_net_tunnelsvxlan(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "encapsulationType": "vxlan",
                "floodingType": "multicast",
                "fullPath": "/Common/vxlan",
                "generation": 1,
                "kind": "tm:net:tunnels:vxlan:vxlanstate",
                "name": "vxlan",
                "partition": "Common",
                "port": 4789,
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1",
            },
            {
                "defaultsFrom": "/Common/vxlan",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1"
                },
                "encapsulationType": "vxlan-gpe",
                "floodingType": "multipoint",
                "fullPath": "/Common/vxlan-gpe",
                "generation": 1,
                "kind": "tm:net:tunnels:vxlan:vxlanstate",
                "name": "vxlan-gpe",
                "partition": "Common",
                "port": 4790,
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan-gpe?ver=14.1.2.1",
            },
            {
                "defaultsFrom": "/Common/vxlan",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1"
                },
                "encapsulationType": "vxlan",
                "floodingType": "multipoint",
                "fullPath": "/Common/vxlan-multipoint",
                "generation": 1,
                "kind": "tm:net:tunnels:vxlan:vxlanstate",
                "name": "vxlan-multipoint",
                "partition": "Common",
                "port": 4789,
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan-multipoint?ver=14.1.2.1",
            },
            {
                "defaultsFrom": "/Common/vxlan",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1"
                },
                "encapsulationType": "vxlan",
                "floodingType": "replicator",
                "fullPath": "/Common/vxlan-ovsdb",
                "generation": 1,
                "kind": "tm:net:tunnels:vxlan:vxlanstate",
                "name": "vxlan-ovsdb",
                "partition": "Common",
                "port": 4789,
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan-ovsdb?ver=14.1.2.1",
            },
            {
                "defaultsFrom": "/Common/vxlan",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1"
                },
                "encapsulationType": "vxlan",
                "floodingType": "multipoint",
                "fullPath": "/Common/vxlan-ovsdb-multipoint",
                "generation": 1,
                "kind": "tm:net:tunnels:vxlan:vxlanstate",
                "name": "vxlan-ovsdb-multipoint",
                "partition": "Common",
                "port": 4789,
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan-ovsdb-multipoint?ver=14.1.2.1",
            },
            {
                "defaultsFrom": "/Common/vxlan",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan?ver=14.1.2.1"
                },
                "encapsulationType": "vxlan",
                "floodingType": "none",
                "fullPath": "/Common/vxlan-ovsdb-no-flooding",
                "generation": 1,
                "kind": "tm:net:tunnels:vxlan:vxlanstate",
                "name": "vxlan-ovsdb-no-flooding",
                "partition": "Common",
                "port": 4789,
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan/~Common~vxlan-ovsdb-no-flooding?ver=14.1.2.1",
            },
        ],
        "kind": "tm:net:tunnels:vxlan:vxlancollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/vxlan?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsVxlan(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsVxlan(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
