# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cloud_ltmpool_members
from genie.libs.parser.bigip.get_cloud_ltmpool_members import (
    CloudLtmPoolmembers,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cloud/ltm/pool-members'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [
                {
                    "address": "1.1.1.1",
                    "port": 80,
                    "nodeReference": {
                        "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/node1"
                    },
                    "objectId": 91297,
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
                    "name": "1.1.1.1:80",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91297",
                },
                {
                    "address": "172.16.231.161",
                    "port": 80,
                    "nodeReference": {
                        "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/172.16.231.161"
                    },
                    "objectId": 91568,
                    "description": "",
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
                    "name": "172.16.231.161:80",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577720534,
                    "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91568",
                },
                {
                    "address": "172.16.221.161",
                    "port": 80,
                    "nodeReference": {
                        "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/172.16.221.161"
                    },
                    "objectId": 91574,
                    "description": "",
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
                    "name": "172.16.221.161:80",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577720534,
                    "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91574",
                },
                {
                    "address": "172.16.201.161",
                    "port": 80,
                    "nodeReference": {
                        "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/172.16.201.161"
                    },
                    "objectId": 91578,
                    "description": "",
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
                    "name": "172.16.201.161:80",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577720534,
                    "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91578",
                },
                {
                    "address": "172.16.101.161",
                    "port": 80,
                    "nodeReference": {
                        "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/172.16.101.161"
                    },
                    "objectId": 91602,
                    "description": "",
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
                    "name": "172.16.101.161:80",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577720534,
                    "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91602",
                },
                {
                    "address": "101.168.11.139",
                    "port": 1129,
                    "nodeReference": {
                        "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/101.168.11.139"
                    },
                    "objectId": 91643,
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
                    "name": "101.168.11.139:1129",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91643",
                },
                {
                    "address": "101.168.12.139",
                    "port": 1129,
                    "nodeReference": {
                        "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/101.168.12.139"
                    },
                    "objectId": 91646,
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
                    "name": "101.168.12.139:1129",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91646",
                },
                {
                    "address": "100.192.149.176",
                    "port": 8191,
                    "nodeReference": {
                        "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/lbsrvcmainupfdpw05"
                    },
                    "objectId": 91679,
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
                    "name": "100.192.149.176:8191",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91679",
                },
                {
                    "address": "100.192.149.177",
                    "port": 8191,
                    "nodeReference": {
                        "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/lbsrvcmainupfdpw06"
                    },
                    "objectId": 91682,
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
                    "name": "100.192.149.177:8191",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91682",
                },
                {
                    "address": "10.2.1.9",
                    "port": 1007,
                    "nodeReference": {
                        "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/Project7-Node1"
                    },
                    "objectId": 91742,
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
                    "name": "10.2.1.9:1007",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719472,
                    "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91742",
                },
                {
                    "address": "172.16.101.161",
                    "port": 80,
                    "nodeReference": {
                        "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/172.16.101.161"
                    },
                    "objectId": 96255,
                    "description": "",
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
                    "name": "172.16.101.161:80",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 1577719551,
                    "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/96255",
                },
            ],
            "generation": 0,
            "lastUpdateMicros": 0,
            "kind": "tm:cloud:ltm:pool-members:ltmpoolmembercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members",
        }


class test_get_cloud_ltmpool_members(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [
            {
                "address": "1.1.1.1",
                "authPartition": "Common",
                "description": "",
                "generation": 0,
                "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                "lastUpdateMicros": 1577719472,
                "name": "1.1.1.1:80",
                "nodeReference": {
                    "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/node1"
                },
                "objectId": 91297,
                "port": 80,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91297",
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
                "description": "",
                "generation": 0,
                "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                "lastUpdateMicros": 1577720534,
                "name": "172.16.231.161:80",
                "nodeReference": {
                    "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/172.16.231.161"
                },
                "objectId": 91568,
                "port": 80,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91568",
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
                "description": "",
                "generation": 0,
                "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                "lastUpdateMicros": 1577720534,
                "name": "172.16.221.161:80",
                "nodeReference": {
                    "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/172.16.221.161"
                },
                "objectId": 91574,
                "port": 80,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91574",
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
                "description": "",
                "generation": 0,
                "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                "lastUpdateMicros": 1577720534,
                "name": "172.16.201.161:80",
                "nodeReference": {
                    "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/172.16.201.161"
                },
                "objectId": 91578,
                "port": 80,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91578",
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
                "description": "",
                "generation": 0,
                "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                "lastUpdateMicros": 1577720534,
                "name": "172.16.101.161:80",
                "nodeReference": {
                    "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/172.16.101.161"
                },
                "objectId": 91602,
                "port": 80,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91602",
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
                "generation": 0,
                "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                "lastUpdateMicros": 1577719472,
                "name": "101.168.11.139:1129",
                "nodeReference": {
                    "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/101.168.11.139"
                },
                "objectId": 91643,
                "port": 1129,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91643",
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
                "generation": 0,
                "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                "lastUpdateMicros": 1577719472,
                "name": "101.168.12.139:1129",
                "nodeReference": {
                    "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/101.168.12.139"
                },
                "objectId": 91646,
                "port": 1129,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91646",
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
                "generation": 0,
                "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                "lastUpdateMicros": 1577719472,
                "name": "100.192.149.176:8191",
                "nodeReference": {
                    "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/lbsrvcmainupfdpw05"
                },
                "objectId": 91679,
                "port": 8191,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91679",
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
                "generation": 0,
                "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                "lastUpdateMicros": 1577719472,
                "name": "100.192.149.177:8191",
                "nodeReference": {
                    "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/lbsrvcmainupfdpw06"
                },
                "objectId": 91682,
                "port": 8191,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91682",
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
                "generation": 0,
                "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                "lastUpdateMicros": 1577719472,
                "name": "10.2.1.9:1007",
                "nodeReference": {
                    "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/Project7-Node1"
                },
                "objectId": 91742,
                "port": 1007,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91742",
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
                "address": "172.16.101.161",
                "authPartition": "Common",
                "description": "",
                "generation": 0,
                "kind": "tm:cloud:ltm:pool-members:ltmpoolmemberstate",
                "lastUpdateMicros": 1577719551,
                "name": "172.16.101.161:80",
                "nodeReference": {
                    "link": "http://localhost/tm/cloud/ltm/node-addresses/Common/172.16.101.161"
                },
                "objectId": 96255,
                "port": 80,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members/96255",
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
        ],
        "kind": "tm:cloud:ltm:pool-members:ltmpoolmembercollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pool-members",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CloudLtmPoolmembers(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CloudLtmPoolmembers(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
