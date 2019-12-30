# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cloud_ltmnode_addresses
from genie.libs.parser.bigip.get_cloud_ltmnode_addresses import (
    CloudLtmNodeaddresses,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cloud/ltm/node-addresses'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [
                {
                    "address": "1.1.1.1",
                    "session": "user-enabled",
                    "objectId": 91291,
                    "description": "",
                    "statsContext": {
                        "stats": [
                            {
                                "name": "health",
                                "value": 0.0,
                                "description": "unknown",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.cur-conns",
                                "value": 0.0,
                                "description": "Server side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.max-conns",
                                "value": 0.0,
                                "description": "Server side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.tot-conns",
                                "value": 0.0,
                                "description": "Server side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                        ]
                    },
                    "name": "node1",
                    "fullPath": "/Common/node1",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91291",
                },
                {
                    "address": "172.16.231.161",
                    "session": "monitor-enabled",
                    "objectId": 91468,
                    "description": "172.16.231.161",
                    "statsContext": {
                        "stats": [
                            {
                                "name": "health",
                                "value": 0.0,
                                "description": "offline",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.cur-conns",
                                "value": 0.0,
                                "description": "Server side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.max-conns",
                                "value": 0.0,
                                "description": "Server side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.tot-conns",
                                "value": 0.0,
                                "description": "Server side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                        ]
                    },
                    "name": "172.16.231.161",
                    "fullPath": "/Common/172.16.231.161",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91468",
                },
                {
                    "address": "172.16.221.161",
                    "session": "monitor-enabled",
                    "objectId": 91497,
                    "description": "172.16.221.161",
                    "statsContext": {
                        "stats": [
                            {
                                "name": "health",
                                "value": 0.0,
                                "description": "offline",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.cur-conns",
                                "value": 0.0,
                                "description": "Server side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.max-conns",
                                "value": 0.0,
                                "description": "Server side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.tot-conns",
                                "value": 0.0,
                                "description": "Server side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                        ]
                    },
                    "name": "172.16.221.161",
                    "fullPath": "/Common/172.16.221.161",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91497",
                },
                {
                    "address": "172.16.101.161",
                    "session": "monitor-enabled",
                    "objectId": 91550,
                    "description": "172.16.101.161",
                    "statsContext": {
                        "stats": [
                            {
                                "name": "health",
                                "value": 0.0,
                                "description": "offline",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.cur-conns",
                                "value": 0.0,
                                "description": "Server side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.max-conns",
                                "value": 0.0,
                                "description": "Server side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.tot-conns",
                                "value": 0.0,
                                "description": "Server side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                        ]
                    },
                    "name": "172.16.101.161",
                    "fullPath": "/Common/172.16.101.161",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91550",
                },
                {
                    "address": "172.16.201.161",
                    "session": "monitor-enabled",
                    "objectId": 91555,
                    "description": "172.16.201.161",
                    "statsContext": {
                        "stats": [
                            {
                                "name": "health",
                                "value": 0.0,
                                "description": "offline",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.cur-conns",
                                "value": 0.0,
                                "description": "Server side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.max-conns",
                                "value": 0.0,
                                "description": "Server side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.tot-conns",
                                "value": 0.0,
                                "description": "Server side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                        ]
                    },
                    "name": "172.16.201.161",
                    "fullPath": "/Common/172.16.201.161",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91555",
                },
                {
                    "address": "101.168.11.139",
                    "session": "user-enabled",
                    "objectId": 91634,
                    "description": "",
                    "statsContext": {
                        "stats": [
                            {
                                "name": "health",
                                "value": 0.0,
                                "description": "unknown",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.cur-conns",
                                "value": 0.0,
                                "description": "Server side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.max-conns",
                                "value": 0.0,
                                "description": "Server side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.tot-conns",
                                "value": 0.0,
                                "description": "Server side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                        ]
                    },
                    "name": "101.168.11.139",
                    "fullPath": "/Common/101.168.11.139",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91634",
                },
                {
                    "address": "101.168.12.139",
                    "session": "user-enabled",
                    "objectId": 91637,
                    "description": "",
                    "statsContext": {
                        "stats": [
                            {
                                "name": "health",
                                "value": 0.0,
                                "description": "unknown",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.cur-conns",
                                "value": 0.0,
                                "description": "Server side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.max-conns",
                                "value": 0.0,
                                "description": "Server side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.tot-conns",
                                "value": 0.0,
                                "description": "Server side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                        ]
                    },
                    "name": "101.168.12.139",
                    "fullPath": "/Common/101.168.12.139",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91637",
                },
                {
                    "address": "100.192.149.176",
                    "session": "user-enabled",
                    "objectId": 91670,
                    "description": "",
                    "statsContext": {
                        "stats": [
                            {
                                "name": "health",
                                "value": 0.0,
                                "description": "unknown",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.cur-conns",
                                "value": 0.0,
                                "description": "Server side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.max-conns",
                                "value": 0.0,
                                "description": "Server side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.tot-conns",
                                "value": 0.0,
                                "description": "Server side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                        ]
                    },
                    "name": "lbsrvcmainupfdpw05",
                    "fullPath": "/Common/lbsrvcmainupfdpw05",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91670",
                },
                {
                    "address": "100.192.149.177",
                    "session": "user-enabled",
                    "objectId": 91673,
                    "description": "",
                    "statsContext": {
                        "stats": [
                            {
                                "name": "health",
                                "value": 0.0,
                                "description": "unknown",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.cur-conns",
                                "value": 0.0,
                                "description": "Server side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.max-conns",
                                "value": 0.0,
                                "description": "Server side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.tot-conns",
                                "value": 0.0,
                                "description": "Server side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                        ]
                    },
                    "name": "lbsrvcmainupfdpw06",
                    "fullPath": "/Common/lbsrvcmainupfdpw06",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91673",
                },
                {
                    "address": "10.2.1.9",
                    "session": "user-disabled",
                    "objectId": 91736,
                    "description": "",
                    "statsContext": {
                        "stats": [
                            {
                                "name": "health",
                                "value": 0.0,
                                "description": "unknown",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.pkts-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-in",
                                "value": 0.0,
                                "description": "Server side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.bits-out",
                                "value": 0.0,
                                "description": "Server side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.cur-conns",
                                "value": 0.0,
                                "description": "Server side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.max-conns",
                                "value": 0.0,
                                "description": "Server side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "serverside.tot-conns",
                                "value": 0.0,
                                "description": "Server side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                        ]
                    },
                    "name": "Project7-Node1",
                    "fullPath": "/Common/Project7-Node1",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91736",
                },
            ],
            "generation": 0,
            "lastUpdateMicros": 0,
            "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddresscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses",
        }


class test_get_cloud_ltmnode_addresses(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [
            {
                "address": "1.1.1.1",
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/node1",
                "generation": 0,
                "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                "lastUpdateMicros": 1577719472,
                "name": "node1",
                "objectId": 91291,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91291",
                "session": "user-enabled",
                "statsContext": {
                    "stats": [
                        {
                            "description": "unknown",
                            "lastUpdateMicros": 0,
                            "name": "health",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                    ]
                },
            },
            {
                "address": "172.16.231.161",
                "authPartition": "Common",
                "description": "172.16.231.161",
                "fullPath": "/Common/172.16.231.161",
                "generation": 0,
                "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                "lastUpdateMicros": 1577719472,
                "name": "172.16.231.161",
                "objectId": 91468,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91468",
                "session": "monitor-enabled",
                "statsContext": {
                    "stats": [
                        {
                            "description": "offline",
                            "lastUpdateMicros": 0,
                            "name": "health",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                    ]
                },
            },
            {
                "address": "172.16.221.161",
                "authPartition": "Common",
                "description": "172.16.221.161",
                "fullPath": "/Common/172.16.221.161",
                "generation": 0,
                "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                "lastUpdateMicros": 1577719472,
                "name": "172.16.221.161",
                "objectId": 91497,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91497",
                "session": "monitor-enabled",
                "statsContext": {
                    "stats": [
                        {
                            "description": "offline",
                            "lastUpdateMicros": 0,
                            "name": "health",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                    ]
                },
            },
            {
                "address": "172.16.101.161",
                "authPartition": "Common",
                "description": "172.16.101.161",
                "fullPath": "/Common/172.16.101.161",
                "generation": 0,
                "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                "lastUpdateMicros": 1577719472,
                "name": "172.16.101.161",
                "objectId": 91550,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91550",
                "session": "monitor-enabled",
                "statsContext": {
                    "stats": [
                        {
                            "description": "offline",
                            "lastUpdateMicros": 0,
                            "name": "health",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                    ]
                },
            },
            {
                "address": "172.16.201.161",
                "authPartition": "Common",
                "description": "172.16.201.161",
                "fullPath": "/Common/172.16.201.161",
                "generation": 0,
                "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                "lastUpdateMicros": 1577719472,
                "name": "172.16.201.161",
                "objectId": 91555,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91555",
                "session": "monitor-enabled",
                "statsContext": {
                    "stats": [
                        {
                            "description": "offline",
                            "lastUpdateMicros": 0,
                            "name": "health",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                    ]
                },
            },
            {
                "address": "101.168.11.139",
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/101.168.11.139",
                "generation": 0,
                "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                "lastUpdateMicros": 1577719472,
                "name": "101.168.11.139",
                "objectId": 91634,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91634",
                "session": "user-enabled",
                "statsContext": {
                    "stats": [
                        {
                            "description": "unknown",
                            "lastUpdateMicros": 0,
                            "name": "health",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                    ]
                },
            },
            {
                "address": "101.168.12.139",
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/101.168.12.139",
                "generation": 0,
                "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                "lastUpdateMicros": 1577719472,
                "name": "101.168.12.139",
                "objectId": 91637,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91637",
                "session": "user-enabled",
                "statsContext": {
                    "stats": [
                        {
                            "description": "unknown",
                            "lastUpdateMicros": 0,
                            "name": "health",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                    ]
                },
            },
            {
                "address": "100.192.149.176",
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/lbsrvcmainupfdpw05",
                "generation": 0,
                "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                "lastUpdateMicros": 1577719472,
                "name": "lbsrvcmainupfdpw05",
                "objectId": 91670,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91670",
                "session": "user-enabled",
                "statsContext": {
                    "stats": [
                        {
                            "description": "unknown",
                            "lastUpdateMicros": 0,
                            "name": "health",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                    ]
                },
            },
            {
                "address": "100.192.149.177",
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/lbsrvcmainupfdpw06",
                "generation": 0,
                "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                "lastUpdateMicros": 1577719472,
                "name": "lbsrvcmainupfdpw06",
                "objectId": 91673,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91673",
                "session": "user-enabled",
                "statsContext": {
                    "stats": [
                        {
                            "description": "unknown",
                            "lastUpdateMicros": 0,
                            "name": "health",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                    ]
                },
            },
            {
                "address": "10.2.1.9",
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/Project7-Node1",
                "generation": 0,
                "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddressstate",
                "lastUpdateMicros": 1577719472,
                "name": "Project7-Node1",
                "objectId": 91736,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses/91736",
                "session": "user-disabled",
                "statsContext": {
                    "stats": [
                        {
                            "description": "unknown",
                            "lastUpdateMicros": 0,
                            "name": "health",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Server side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "serverside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                    ]
                },
            },
        ],
        "kind": "tm:cloud:ltm:node-addresses:ltmnodeaddresscollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/cloud/ltm/node-addresses",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CloudLtmNodeaddresses(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CloudLtmNodeaddresses(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
