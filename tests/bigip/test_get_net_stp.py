# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_stp
from genie.libs.parser.bigip.get_net_stp import NetStp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/stp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:stp:stpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/stp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:stp:stpstate",
                    "name": "cist",
                    "partition": "Common",
                    "fullPath": "/Common/cist",
                    "generation": 2153,
                    "selfLink": "https://localhost/mgmt/tm/net/stp/~Common~cist?ver=14.1.2.1",
                    "instanceId": 0,
                    "priority": 61440,
                    "vlans": [
                        "/Common/External",
                        "/Common/HA",
                        "/Common/Internal",
                        "/Common/Services",
                    ],
                    "vlansReference": [
                        {
                            "link": "https://localhost/mgmt/tm/net/vlan/~Common~External?ver=14.1.2.1"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/net/vlan/~Common~HA?ver=14.1.2.1"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/net/vlan/~Common~Services?ver=14.1.2.1"
                        },
                    ],
                    "interfaces": [
                        {
                            "name": "1.1",
                            "externalPathCost": 200000,
                            "internalPathCost": 200000,
                            "priority": 128,
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/net/interface/1.1?ver=14.1.2.1"
                            },
                        },
                        {
                            "name": "1.2",
                            "externalPathCost": 200000,
                            "internalPathCost": 200000,
                            "priority": 128,
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/net/interface/1.2?ver=14.1.2.1"
                            },
                        },
                        {
                            "name": "1.3",
                            "externalPathCost": 200000,
                            "internalPathCost": 200000,
                            "priority": 128,
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/net/interface/1.3?ver=14.1.2.1"
                            },
                        },
                    ],
                }
            ],
        }


class test_get_net_stp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/cist",
                "generation": 2153,
                "instanceId": 0,
                "interfaces": [
                    {
                        "externalPathCost": 200000,
                        "internalPathCost": 200000,
                        "name": "1.1",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/net/interface/1.1?ver=14.1.2.1"
                        },
                        "priority": 128,
                    },
                    {
                        "externalPathCost": 200000,
                        "internalPathCost": 200000,
                        "name": "1.2",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/net/interface/1.2?ver=14.1.2.1"
                        },
                        "priority": 128,
                    },
                    {
                        "externalPathCost": 200000,
                        "internalPathCost": 200000,
                        "name": "1.3",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/net/interface/1.3?ver=14.1.2.1"
                        },
                        "priority": 128,
                    },
                ],
                "kind": "tm:net:stp:stpstate",
                "name": "cist",
                "partition": "Common",
                "priority": 61440,
                "selfLink": "https://localhost/mgmt/tm/net/stp/~Common~cist?ver=14.1.2.1",
                "vlans": [
                    "/Common/External",
                    "/Common/HA",
                    "/Common/Internal",
                    "/Common/Services",
                ],
                "vlansReference": [
                    {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~External?ver=14.1.2.1"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~HA?ver=14.1.2.1"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~Services?ver=14.1.2.1"
                    },
                ],
            }
        ],
        "kind": "tm:net:stp:stpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/stp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetStp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetStp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
