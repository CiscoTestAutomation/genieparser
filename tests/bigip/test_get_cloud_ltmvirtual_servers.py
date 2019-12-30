# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cloud_ltmvirtual_servers
from genie.libs.parser.bigip.get_cloud_ltmvirtual_servers import (
    CloudLtmVirtualservers,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cloud/ltm/virtual-servers'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [
                {
                    "address": "1.1.1.2",
                    "port": 80,
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91294"
                    },
                    "objectId": 91300,
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
                                "name": "clientside.pkts-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.pkts-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.cur-conns",
                                "value": 0.0,
                                "description": "Client side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.max-conns",
                                "value": 0.0,
                                "description": "Client side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.tot-conns",
                                "value": 0.0,
                                "description": "Client side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "status.status-reason",
                                "description": "",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.enabled-state",
                                "description": "enabled",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.availability-state",
                                "description": "unknown",
                                "lastUpdateMicros": 0,
                            },
                        ]
                    },
                    "name": "vip1",
                    "fullPath": "/Common/vip1",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91300",
                },
                {
                    "address": "172.16.100.141",
                    "port": 80,
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91564"
                    },
                    "objectId": 91593,
                    "description": "vs_tcp_80_abc01.xyz.net_172.16.0.141",
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
                                "name": "clientside.pkts-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.pkts-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.cur-conns",
                                "value": 0.0,
                                "description": "Client side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.max-conns",
                                "value": 0.0,
                                "description": "Client side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.tot-conns",
                                "value": 0.0,
                                "description": "Client side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "status.status-reason",
                                "description": "The children pool member(s) are down",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.enabled-state",
                                "description": "enabled",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.availability-state",
                                "description": "offline",
                                "lastUpdateMicros": 0,
                            },
                        ]
                    },
                    "name": "vs_tcp_80_abc01.xyz.net_172.16.100.141",
                    "fullPath": "/Common/vs_tcp_80_abc01.xyz.net_172.16.100.141",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91593",
                },
                {
                    "address": "172.16.220.141",
                    "port": 8220,
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91560"
                    },
                    "objectId": 91584,
                    "description": "vs_tcp_80_abc01.xyz.net_172.16.0.141",
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
                                "name": "clientside.pkts-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.pkts-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.cur-conns",
                                "value": 0.0,
                                "description": "Client side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.max-conns",
                                "value": 0.0,
                                "description": "Client side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.tot-conns",
                                "value": 0.0,
                                "description": "Client side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "status.status-reason",
                                "description": "The children pool member(s) are down",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.enabled-state",
                                "description": "enabled",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.availability-state",
                                "description": "offline",
                                "lastUpdateMicros": 0,
                            },
                        ]
                    },
                    "name": "vs_tcp_80_abc01.xyz.net_172.16.220.141",
                    "fullPath": "/Common/vs_tcp_80_abc01.xyz.net_172.16.220.141",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91584",
                },
                {
                    "address": "101.11.11.139",
                    "port": 9406,
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91640"
                    },
                    "objectId": 91649,
                    "description": "vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
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
                                "name": "clientside.pkts-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.pkts-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.cur-conns",
                                "value": 0.0,
                                "description": "Client side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.max-conns",
                                "value": 0.0,
                                "description": "Client side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.tot-conns",
                                "value": 0.0,
                                "description": "Client side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "status.status-reason",
                                "description": "",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.enabled-state",
                                "description": "enabled",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.availability-state",
                                "description": "unknown",
                                "lastUpdateMicros": 0,
                            },
                        ]
                    },
                    "name": "vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                    "fullPath": "/Common/vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91649",
                },
                {
                    "address": "10.10.34.250",
                    "port": 8191,
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91676"
                    },
                    "objectId": 91685,
                    "description": "CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250-8191",
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
                                "name": "clientside.pkts-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.pkts-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.cur-conns",
                                "value": 0.0,
                                "description": "Client side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.max-conns",
                                "value": 0.0,
                                "description": "Client side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.tot-conns",
                                "value": 0.0,
                                "description": "Client side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "status.status-reason",
                                "description": "",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.enabled-state",
                                "description": "enabled",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.availability-state",
                                "description": "unknown",
                                "lastUpdateMicros": 0,
                            },
                        ]
                    },
                    "name": "vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                    "fullPath": "/Common/vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91685",
                },
                {
                    "address": "10.1.1.7",
                    "port": 9007,
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91739"
                    },
                    "objectId": 91745,
                    "description": "vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
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
                                "name": "clientside.pkts-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.pkts-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.cur-conns",
                                "value": 0.0,
                                "description": "Client side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.max-conns",
                                "value": 0.0,
                                "description": "Client side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.tot-conns",
                                "value": 0.0,
                                "description": "Client side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "status.status-reason",
                                "description": "",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.enabled-state",
                                "description": "enabled",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.availability-state",
                                "description": "unknown",
                                "lastUpdateMicros": 0,
                            },
                        ]
                    },
                    "name": "vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                    "fullPath": "/Common/vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91745",
                },
                {
                    "address": "10.1.1.3",
                    "port": 80,
                    "poolReference": {
                        "link": "https://localhost/mgmt/tm/cloud/ltm/pools/96252"
                    },
                    "objectId": 96258,
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
                                "name": "clientside.pkts-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.pkts-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Packet Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-in",
                                "value": 0.0,
                                "description": "Client side - Incoming Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.bits-out",
                                "value": 0.0,
                                "description": "Client side - Outgoing Bit Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.cur-conns",
                                "value": 0.0,
                                "description": "Client side - Current Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.max-conns",
                                "value": 0.0,
                                "description": "Client side - Maximum Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "clientside.tot-conns",
                                "value": 0.0,
                                "description": "Client side - Total Connection Count",
                                "lastUpdateMicros": 0,
                                "updateType": "BASIC",
                            },
                            {
                                "name": "status.status-reason",
                                "description": "The children pool member(s) are down",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.enabled-state",
                                "description": "enabled",
                                "lastUpdateMicros": 0,
                            },
                            {
                                "name": "status.availability-state",
                                "description": "offline",
                                "lastUpdateMicros": 0,
                            },
                        ]
                    },
                    "name": "vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                    "fullPath": "/Common/vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                    "authPartition": "Common",
                    "generation": 0,
                    "lastUpdateMicros": 0,
                    "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                    "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/96258",
                },
            ],
            "generation": 0,
            "lastUpdateMicros": 0,
            "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualservercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers",
        }


class test_get_cloud_ltmvirtual_servers(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [
            {
                "address": "1.1.1.2",
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/vip1",
                "generation": 0,
                "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                "lastUpdateMicros": 0,
                "name": "vip1",
                "objectId": 91300,
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91294"
                },
                "port": 80,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91300",
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
                            "description": "Client side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "",
                            "lastUpdateMicros": 0,
                            "name": "status.status-reason",
                        },
                        {
                            "description": "enabled",
                            "lastUpdateMicros": 0,
                            "name": "status.enabled-state",
                        },
                        {
                            "description": "unknown",
                            "lastUpdateMicros": 0,
                            "name": "status.availability-state",
                        },
                    ]
                },
            },
            {
                "address": "172.16.100.141",
                "authPartition": "Common",
                "description": "vs_tcp_80_abc01.xyz.net_172.16.0.141",
                "fullPath": "/Common/vs_tcp_80_abc01.xyz.net_172.16.100.141",
                "generation": 0,
                "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                "lastUpdateMicros": 0,
                "name": "vs_tcp_80_abc01.xyz.net_172.16.100.141",
                "objectId": 91593,
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91564"
                },
                "port": 80,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91593",
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
                            "description": "Client side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "The children pool "
                            "member(s) are down",
                            "lastUpdateMicros": 0,
                            "name": "status.status-reason",
                        },
                        {
                            "description": "enabled",
                            "lastUpdateMicros": 0,
                            "name": "status.enabled-state",
                        },
                        {
                            "description": "offline",
                            "lastUpdateMicros": 0,
                            "name": "status.availability-state",
                        },
                    ]
                },
            },
            {
                "address": "172.16.220.141",
                "authPartition": "Common",
                "description": "vs_tcp_80_abc01.xyz.net_172.16.0.141",
                "fullPath": "/Common/vs_tcp_80_abc01.xyz.net_172.16.220.141",
                "generation": 0,
                "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                "lastUpdateMicros": 0,
                "name": "vs_tcp_80_abc01.xyz.net_172.16.220.141",
                "objectId": 91584,
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91560"
                },
                "port": 8220,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91584",
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
                            "description": "Client side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "The children pool "
                            "member(s) are down",
                            "lastUpdateMicros": 0,
                            "name": "status.status-reason",
                        },
                        {
                            "description": "enabled",
                            "lastUpdateMicros": 0,
                            "name": "status.enabled-state",
                        },
                        {
                            "description": "offline",
                            "lastUpdateMicros": 0,
                            "name": "status.availability-state",
                        },
                    ]
                },
            },
            {
                "address": "101.11.11.139",
                "authPartition": "Common",
                "description": "vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                "fullPath": "/Common/vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                "generation": 0,
                "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                "lastUpdateMicros": 0,
                "name": "vs-tcp-9406-IAC-2-IAC-2-101.11.11.139",
                "objectId": 91649,
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91640"
                },
                "port": 9406,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91649",
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
                            "description": "Client side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "",
                            "lastUpdateMicros": 0,
                            "name": "status.status-reason",
                        },
                        {
                            "description": "enabled",
                            "lastUpdateMicros": 0,
                            "name": "status.enabled-state",
                        },
                        {
                            "description": "unknown",
                            "lastUpdateMicros": 0,
                            "name": "status.availability-state",
                        },
                    ]
                },
            },
            {
                "address": "10.10.34.250",
                "authPartition": "Common",
                "description": "CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250-8191",
                "fullPath": "/Common/vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                "generation": 0,
                "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                "lastUpdateMicros": 0,
                "name": "vs-tcp-8191.CG2ABSV2MPG.lbsrvc-out-mainperf.local.net-out-10.10.34.250",
                "objectId": 91685,
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91676"
                },
                "port": 8191,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91685",
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
                            "description": "Client side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "",
                            "lastUpdateMicros": 0,
                            "name": "status.status-reason",
                        },
                        {
                            "description": "enabled",
                            "lastUpdateMicros": 0,
                            "name": "status.enabled-state",
                        },
                        {
                            "description": "unknown",
                            "lastUpdateMicros": 0,
                            "name": "status.availability-state",
                        },
                    ]
                },
            },
            {
                "address": "10.1.1.7",
                "authPartition": "Common",
                "description": "vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                "fullPath": "/Common/vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                "generation": 0,
                "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                "lastUpdateMicros": 0,
                "name": "vs-tcp-9007-Test-Project-7-Test-LOB-7-10.1.1.7",
                "objectId": 91745,
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/cloud/ltm/pools/91739"
                },
                "port": 9007,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/91745",
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
                            "description": "Client side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "",
                            "lastUpdateMicros": 0,
                            "name": "status.status-reason",
                        },
                        {
                            "description": "enabled",
                            "lastUpdateMicros": 0,
                            "name": "status.enabled-state",
                        },
                        {
                            "description": "unknown",
                            "lastUpdateMicros": 0,
                            "name": "status.availability-state",
                        },
                    ]
                },
            },
            {
                "address": "10.1.1.3",
                "authPartition": "Common",
                "description": "",
                "fullPath": "/Common/vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                "generation": 0,
                "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualserverstate",
                "lastUpdateMicros": 0,
                "name": "vs-tcp-9003-Test-Project-3-Test-LOB-3-10.1.1.3",
                "objectId": 96258,
                "poolReference": {
                    "link": "https://localhost/mgmt/tm/cloud/ltm/pools/96252"
                },
                "port": 80,
                "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers/96258",
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
                            "description": "Client side - Incoming "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Packet Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.pkts-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Incoming "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-in",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Outgoing "
                            "Bit Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.bits-out",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Current "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.cur-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Maximum "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.max-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "Client side - Total "
                            "Connection Count",
                            "lastUpdateMicros": 0,
                            "name": "clientside.tot-conns",
                            "updateType": "BASIC",
                            "value": 0.0,
                        },
                        {
                            "description": "The children pool "
                            "member(s) are down",
                            "lastUpdateMicros": 0,
                            "name": "status.status-reason",
                        },
                        {
                            "description": "enabled",
                            "lastUpdateMicros": 0,
                            "name": "status.enabled-state",
                        },
                        {
                            "description": "offline",
                            "lastUpdateMicros": 0,
                            "name": "status.availability-state",
                        },
                    ]
                },
            },
        ],
        "kind": "tm:cloud:ltm:virtual-servers:ltmvirtualservercollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/cloud/ltm/virtual-servers",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CloudLtmVirtualservers(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CloudLtmVirtualservers(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
