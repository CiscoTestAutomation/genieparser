# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cloud_ltmpools
from genie.libs.parser.bigip.get_cloud_ltmpools import CloudLtmPools

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cloud/ltm/pools'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [
                {
                    "poolMemberReferences": [
                        {
                            "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91297"
                        }
                    ],
                    "objectId": 91294,
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
                    "name": "pool1",
                    "fullPath": "/Common/pool1",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91294",
                },
                {
                    "poolMemberReferences": [
                        {
                            "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91568"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91574"
                        },
                    ],
                    "objectId": 91560,
                    "description": "pl_/Common/pl_web-pool221",
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
                    "name": "pl_web-pool221",
                    "fullPath": "/Common/pl_web-pool221",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91560",
                },
                {
                    "poolMemberReferences": [
                        {
                            "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91602"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91578"
                        },
                    ],
                    "objectId": 91564,
                    "description": "pl_/Common/pl_web-pool101",
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
                    "name": "pl_web-pool101",
                    "fullPath": "/Common/pl_web-pool101",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91564",
                },
                {
                    "poolMemberReferences": [
                        {
                            "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91646"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91643"
                        },
                    ],
                    "objectId": 91640,
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
                    "name": "pool-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                    "fullPath": "/Common/pool-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91640",
                },
                {
                    "poolMemberReferences": [
                        {
                            "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91679"
                        },
                        {
                            "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91682"
                        },
                    ],
                    "objectId": 91676,
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
                    "name": "pool-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                    "fullPath": "/Common/pool-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91676",
                },
                {
                    "poolMemberReferences": [
                        {
                            "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91742"
                        }
                    ],
                    "objectId": 91739,
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
                    "name": "pool-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                    "fullPath": "/Common/pool-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91739",
                },
                {
                    "poolMemberReferences": [
                        {
                            "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/96255"
                        }
                    ],
                    "objectId": 96252,
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
                    "name": "pool-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                    "fullPath": "/Common/pool-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/96252",
                },
            ],
            "generation": 0,
            "lastUpdateMicros": 0,
            "kind": "tm:cloud:ltm:pools:ltmpoolcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools",
        }


class test_get_cloud_ltmpools(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [
            {
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/pool1",
                "generation": 0,
                "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                "lastUpdateMicros": 0,
                "name": "pool1",
                "objectId": 91294,
                "poolMemberReferences": [
                    {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91297"
                    }
                ],
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91294",
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
                "authPartition": "Common",
                "description": "pl_/Common/pl_web-pool221",
                "fullPath": "/Common/pl_web-pool221",
                "generation": 0,
                "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                "lastUpdateMicros": 0,
                "name": "pl_web-pool221",
                "objectId": 91560,
                "poolMemberReferences": [
                    {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91568"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91574"
                    },
                ],
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91560",
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
                "authPartition": "Common",
                "description": "pl_/Common/pl_web-pool101",
                "fullPath": "/Common/pl_web-pool101",
                "generation": 0,
                "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                "lastUpdateMicros": 0,
                "name": "pl_web-pool101",
                "objectId": 91564,
                "poolMemberReferences": [
                    {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91602"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91578"
                    },
                ],
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91564",
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
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/pool-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                "generation": 0,
                "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                "lastUpdateMicros": 0,
                "name": "pool-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                "objectId": 91640,
                "poolMemberReferences": [
                    {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91646"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91643"
                    },
                ],
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91640",
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
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/pool-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                "generation": 0,
                "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                "lastUpdateMicros": 0,
                "name": "pool-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                "objectId": 91676,
                "poolMemberReferences": [
                    {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91679"
                    },
                    {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91682"
                    },
                ],
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91676",
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
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/pool-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                "generation": 0,
                "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                "lastUpdateMicros": 0,
                "name": "pool-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                "objectId": 91739,
                "poolMemberReferences": [
                    {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/91742"
                    }
                ],
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/91739",
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
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/pool-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                "generation": 0,
                "kind": "tm:cloud:ltm:pools:ltmpoolstate",
                "lastUpdateMicros": 0,
                "name": "pool-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                "objectId": 96252,
                "poolMemberReferences": [
                    {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pool-members/96255"
                    }
                ],
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools/96252",
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
        "kind": "tm:cloud:ltm:pools:ltmpoolcollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/cloud/ltm/pools",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CloudLtmPools(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CloudLtmPools(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
