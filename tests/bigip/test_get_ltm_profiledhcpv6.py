# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profiledhcpv6
from genie.libs.parser.bigip.get_ltm_profiledhcpv6 import LtmProfileDhcpv6

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/dhcpv6'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:dhcpv6:dhcpv6collectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv6?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:dhcpv6:dhcpv6state",
                    "name": "dhcpv6",
                    "partition": "Common",
                    "fullPath": "/Common/dhcpv6",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv6/~Common~dhcpv6?ver=14.1.2.1",
                    "appService": "none",
                    "authentication": {
                        "enabled": "false",
                        "userName": {
                            "format": "mac-address",
                            "separator1": "@",
                            "separator2": "@",
                            "tcl": "none",
                        },
                        "virtual": "none",
                    },
                    "defaultLeaseTime": 86400,
                    "defaultsFrom": "none",
                    "description": "none",
                    "idleTimeout": "60",
                    "leaseQueryMaxRetry": 3,
                    "leaseQueryOnly": "false",
                    "mode": "relay",
                    "remoteIdOption": {
                        "add": "false",
                        "enterpriseNumber": 0,
                        "remove": "false",
                        "value": "none",
                    },
                    "subscriberDiscovery": {
                        "enabled": "false",
                        "subscriberId": {
                            "format": "mac-address",
                            "separator1": "@",
                            "separator2": "@",
                            "tcl": "none",
                        },
                    },
                    "subscriberIdOption": {
                        "add": "false",
                        "remove": "false",
                        "value": "none",
                    },
                    "transactionTimeout": 30,
                },
                {
                    "kind": "tm:ltm:profile:dhcpv6:dhcpv6state",
                    "name": "dhcpv6_fwd",
                    "partition": "Common",
                    "fullPath": "/Common/dhcpv6_fwd",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv6/~Common~dhcpv6_fwd?ver=14.1.2.1",
                    "appService": "none",
                    "authentication": {
                        "enabled": "false",
                        "userName": {
                            "format": "mac-address",
                            "separator1": "@",
                            "separator2": "@",
                            "tcl": "none",
                        },
                        "virtual": "none",
                    },
                    "defaultLeaseTime": 86400,
                    "defaultsFrom": "/Common/dhcpv6",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/dhcpv6/~Common~dhcpv6?ver=14.1.2.1"
                    },
                    "description": "none",
                    "idleTimeout": "60",
                    "leaseQueryMaxRetry": 3,
                    "leaseQueryOnly": "false",
                    "mode": "forwarding",
                    "remoteIdOption": {
                        "add": "false",
                        "enterpriseNumber": 0,
                        "remove": "false",
                        "value": "none",
                    },
                    "subscriberDiscovery": {
                        "enabled": "false",
                        "subscriberId": {
                            "format": "mac-address",
                            "separator1": "@",
                            "separator2": "@",
                            "tcl": "none",
                        },
                    },
                    "subscriberIdOption": {
                        "add": "false",
                        "remove": "false",
                        "value": "none",
                    },
                    "transactionTimeout": 30,
                },
            ],
        }


class test_get_ltm_profiledhcpv6(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "authentication": {
                    "enabled": "false",
                    "userName": {
                        "format": "mac-address",
                        "separator1": "@",
                        "separator2": "@",
                        "tcl": "none",
                    },
                    "virtual": "none",
                },
                "defaultLeaseTime": 86400,
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/dhcpv6",
                "generation": 1,
                "idleTimeout": "60",
                "kind": "tm:ltm:profile:dhcpv6:dhcpv6state",
                "leaseQueryMaxRetry": 3,
                "leaseQueryOnly": "false",
                "mode": "relay",
                "name": "dhcpv6",
                "partition": "Common",
                "remoteIdOption": {
                    "add": "false",
                    "enterpriseNumber": 0,
                    "remove": "false",
                    "value": "none",
                },
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv6/~Common~dhcpv6?ver=14.1.2.1",
                "subscriberDiscovery": {
                    "enabled": "false",
                    "subscriberId": {
                        "format": "mac-address",
                        "separator1": "@",
                        "separator2": "@",
                        "tcl": "none",
                    },
                },
                "subscriberIdOption": {
                    "add": "false",
                    "remove": "false",
                    "value": "none",
                },
                "transactionTimeout": 30,
            },
            {
                "appService": "none",
                "authentication": {
                    "enabled": "false",
                    "userName": {
                        "format": "mac-address",
                        "separator1": "@",
                        "separator2": "@",
                        "tcl": "none",
                    },
                    "virtual": "none",
                },
                "defaultLeaseTime": 86400,
                "defaultsFrom": "/Common/dhcpv6",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/dhcpv6/~Common~dhcpv6?ver=14.1.2.1"
                },
                "description": "none",
                "fullPath": "/Common/dhcpv6_fwd",
                "generation": 1,
                "idleTimeout": "60",
                "kind": "tm:ltm:profile:dhcpv6:dhcpv6state",
                "leaseQueryMaxRetry": 3,
                "leaseQueryOnly": "false",
                "mode": "forwarding",
                "name": "dhcpv6_fwd",
                "partition": "Common",
                "remoteIdOption": {
                    "add": "false",
                    "enterpriseNumber": 0,
                    "remove": "false",
                    "value": "none",
                },
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv6/~Common~dhcpv6_fwd?ver=14.1.2.1",
                "subscriberDiscovery": {
                    "enabled": "false",
                    "subscriberId": {
                        "format": "mac-address",
                        "separator1": "@",
                        "separator2": "@",
                        "tcl": "none",
                    },
                },
                "subscriberIdOption": {
                    "add": "false",
                    "remove": "false",
                    "value": "none",
                },
                "transactionTimeout": 30,
            },
        ],
        "kind": "tm:ltm:profile:dhcpv6:dhcpv6collectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv6?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileDhcpv6(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileDhcpv6(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
