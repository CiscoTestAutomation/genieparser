# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_route_domain
from genie.libs.parser.bigip.get_net_route_domain import NetRoutedomain

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/route-domain'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:route-domain:route-domaincollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/route-domain?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:route-domain:route-domainstate",
                    "name": "0",
                    "partition": "Common",
                    "fullPath": "/Common/0",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/route-domain/~Common~0?ver=14.1.2.1",
                    "connectionLimit": 0,
                    "id": 0,
                    "strict": "enabled",
                    "throughputCapacity": "infinite",
                    "vlans": [
                        "/Common/External",
                        "/Common/http-tunnel",
                        "/Common/socks-tunnel",
                        "/Common/Internal",
                        "/Common/Services",
                        "/Common/HA",
                    ],
                    "vlansReference": [
                        {
                            "link": "https://localhost/mgmt/tm/net/vlan/~Common~External?ver=14.1.2.1"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/net/tunnels/tunnel/~Common~http-tunnel?ver=14.1.2.1"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/net/tunnels/tunnel/~Common~socks-tunnel?ver=14.1.2.1"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/net/vlan/~Common~Services?ver=14.1.2.1"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/net/vlan/~Common~HA?ver=14.1.2.1"
                        },
                    ],
                }
            ],
        }


class test_get_net_route_domain(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "connectionLimit": 0,
                "fullPath": "/Common/0",
                "generation": 1,
                "id": 0,
                "kind": "tm:net:route-domain:route-domainstate",
                "name": "0",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/route-domain/~Common~0?ver=14.1.2.1",
                "strict": "enabled",
                "throughputCapacity": "infinite",
                "vlans": [
                    "/Common/External",
                    "/Common/http-tunnel",
                    "/Common/socks-tunnel",
                    "/Common/Internal",
                    "/Common/Services",
                    "/Common/HA",
                ],
                "vlansReference": [
                    {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~External?ver=14.1.2.1"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/net/tunnels/tunnel/~Common~http-tunnel?ver=14.1.2.1"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/net/tunnels/tunnel/~Common~socks-tunnel?ver=14.1.2.1"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~Services?ver=14.1.2.1"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~HA?ver=14.1.2.1"
                    },
                ],
            }
        ],
        "kind": "tm:net:route-domain:route-domaincollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/route-domain?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetRoutedomain(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetRoutedomain(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
