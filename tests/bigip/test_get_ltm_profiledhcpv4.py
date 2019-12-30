# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profiledhcpv4
from genie.libs.parser.bigip.get_ltm_profiledhcpv4 import LtmProfileDhcpv4

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/dhcpv4'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:dhcpv4:dhcpv4collectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv4?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:dhcpv4:dhcpv4state",
                    "name": "dhcpv4",
                    "partition": "Common",
                    "fullPath": "/Common/dhcpv4",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv4/~Common~dhcpv4?ver=14.1.2.1",
                    "appService": "none",
                    "authentication": {
                        "enabled": "false",
                        "userName": {
                            "format": "mac-address",
                            "separator1": "@",
                            "separator2": "@",
                            "suboptionId1": 1,
                            "suboptionId2": 2,
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
                    "maxHops": 4,
                    "mode": "relay",
                    "relayAgentId": {
                        "add": "false",
                        "remove": "false",
                        "suboptions": {
                            "id1": 1,
                            "id2": 0,
                            "value1": "2",
                            "value2": "none",
                        },
                    },
                    "subscriberDiscovery": {
                        "enabled": "false",
                        "subscriberId": {
                            "format": "mac-address",
                            "separator1": "@",
                            "separator2": "@",
                            "suboptionId1": 1,
                            "suboptionId2": 2,
                            "tcl": "none",
                        },
                    },
                    "transactionTimeout": 30,
                    "ttlDecValue": "by-1",
                    "ttlValue": 0,
                },
                {
                    "kind": "tm:ltm:profile:dhcpv4:dhcpv4state",
                    "name": "dhcpv4_fwd",
                    "partition": "Common",
                    "fullPath": "/Common/dhcpv4_fwd",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv4/~Common~dhcpv4_fwd?ver=14.1.2.1",
                    "appService": "none",
                    "authentication": {
                        "enabled": "false",
                        "userName": {
                            "format": "mac-address",
                            "separator1": "@",
                            "separator2": "@",
                            "suboptionId1": 1,
                            "suboptionId2": 2,
                            "tcl": "none",
                        },
                        "virtual": "none",
                    },
                    "defaultLeaseTime": 86400,
                    "defaultsFrom": "/Common/dhcpv4",
                    "defaultsFromReference": {
                        "link": "https://localhost/mgmt/tm/ltm/profile/dhcpv4/~Common~dhcpv4?ver=14.1.2.1"
                    },
                    "description": "none",
                    "idleTimeout": "60",
                    "leaseQueryMaxRetry": 3,
                    "leaseQueryOnly": "false",
                    "maxHops": 4,
                    "mode": "forwarding",
                    "relayAgentId": {
                        "add": "false",
                        "remove": "false",
                        "suboptions": {
                            "id1": 1,
                            "id2": 0,
                            "value1": "2",
                            "value2": "none",
                        },
                    },
                    "subscriberDiscovery": {
                        "enabled": "false",
                        "subscriberId": {
                            "format": "mac-address",
                            "separator1": "@",
                            "separator2": "@",
                            "suboptionId1": 1,
                            "suboptionId2": 2,
                            "tcl": "none",
                        },
                    },
                    "transactionTimeout": 30,
                    "ttlDecValue": "by-1",
                    "ttlValue": 0,
                },
            ],
        }


class test_get_ltm_profiledhcpv4(unittest.TestCase):

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
                        "suboptionId1": 1,
                        "suboptionId2": 2,
                        "tcl": "none",
                    },
                    "virtual": "none",
                },
                "defaultLeaseTime": 86400,
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/dhcpv4",
                "generation": 1,
                "idleTimeout": "60",
                "kind": "tm:ltm:profile:dhcpv4:dhcpv4state",
                "leaseQueryMaxRetry": 3,
                "leaseQueryOnly": "false",
                "maxHops": 4,
                "mode": "relay",
                "name": "dhcpv4",
                "partition": "Common",
                "relayAgentId": {
                    "add": "false",
                    "remove": "false",
                    "suboptions": {
                        "id1": 1,
                        "id2": 0,
                        "value1": "2",
                        "value2": "none",
                    },
                },
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv4/~Common~dhcpv4?ver=14.1.2.1",
                "subscriberDiscovery": {
                    "enabled": "false",
                    "subscriberId": {
                        "format": "mac-address",
                        "separator1": "@",
                        "separator2": "@",
                        "suboptionId1": 1,
                        "suboptionId2": 2,
                        "tcl": "none",
                    },
                },
                "transactionTimeout": 30,
                "ttlDecValue": "by-1",
                "ttlValue": 0,
            },
            {
                "appService": "none",
                "authentication": {
                    "enabled": "false",
                    "userName": {
                        "format": "mac-address",
                        "separator1": "@",
                        "separator2": "@",
                        "suboptionId1": 1,
                        "suboptionId2": 2,
                        "tcl": "none",
                    },
                    "virtual": "none",
                },
                "defaultLeaseTime": 86400,
                "defaultsFrom": "/Common/dhcpv4",
                "defaultsFromReference": {
                    "link": "https://localhost/mgmt/tm/ltm/profile/dhcpv4/~Common~dhcpv4?ver=14.1.2.1"
                },
                "description": "none",
                "fullPath": "/Common/dhcpv4_fwd",
                "generation": 1,
                "idleTimeout": "60",
                "kind": "tm:ltm:profile:dhcpv4:dhcpv4state",
                "leaseQueryMaxRetry": 3,
                "leaseQueryOnly": "false",
                "maxHops": 4,
                "mode": "forwarding",
                "name": "dhcpv4_fwd",
                "partition": "Common",
                "relayAgentId": {
                    "add": "false",
                    "remove": "false",
                    "suboptions": {
                        "id1": 1,
                        "id2": 0,
                        "value1": "2",
                        "value2": "none",
                    },
                },
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv4/~Common~dhcpv4_fwd?ver=14.1.2.1",
                "subscriberDiscovery": {
                    "enabled": "false",
                    "subscriberId": {
                        "format": "mac-address",
                        "separator1": "@",
                        "separator2": "@",
                        "suboptionId1": 1,
                        "suboptionId2": 2,
                        "tcl": "none",
                    },
                },
                "transactionTimeout": 30,
                "ttlDecValue": "by-1",
                "ttlValue": 0,
            },
        ],
        "kind": "tm:ltm:profile:dhcpv4:dhcpv4collectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/dhcpv4?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileDhcpv4(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileDhcpv4(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
