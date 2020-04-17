import unittest
from unittest.mock import Mock

from pyats.topology import loader, Device
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ospf_database_advertising_router_self_detail import ShowOspfDatabaseAdvertisingRouterSelfDetail

class TestShowOspfDatabaseAdvertisingRouterSelfDetail(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':
    '''
            show ospf database advertising-router self detail

            OSPF database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Router  *111.87.5.252     111.87.5.252     0x80001b9e  1801  0x22 0x1e2  120
        bits 0x2, link count 8
        id 111.87.5.253, data 111.87.5.93, Type PointToPoint (1)
            Topology count: 0, Default metric: 5
        id 111.87.5.92, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 5
        id 106.187.14.240, data 106.187.14.122, Type PointToPoint (1)
            Topology count: 0, Default metric: 100
        id 106.187.14.120, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 100
        id 27.86.198.239, data 27.86.198.25, Type PointToPoint (1)
            Topology count: 0, Default metric: 1000
        id 27.86.198.24, data 255.255.255.252, Type Stub (3)
            Topology count: 0, Default metric: 1000
        id 100.0.0.0, data 255.255.255.0, Type Stub (3)
            Topology count: 0, Default metric: 100
        id 111.87.5.252, data 255.255.255.255, Type Stub (3)
            Topology count: 0, Default metric: 0
        Topology default (ID 0)
            Type: PointToPoint, Node ID: 27.86.198.239
            Metric: 1000, Bidirectional
            Type: PointToPoint, Node ID: 106.187.14.240
            Metric: 100, Bidirectional
            Type: PointToPoint, Node ID: 111.87.5.253
            Metric: 5, Bidirectional
        OpaqArea*1.0.0.1          111.87.5.252     0x80001a15   424  0x22 0xd49a  28
        Opaque LSA
        RtrAddr (1), length 4:
            111.87.5.252
        OpaqArea*1.0.0.3          111.87.5.252     0x80000322   153  0x22 0x95cd 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            111.87.5.253
            LocIfAdr (3), length 4:
            111.87.5.93
            RemIfAdr (4), length 4:
            111.87.5.94
            TEMetric (5), length 4:
            5
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 333, Remote 0
            Color (9), length 4:
            0
        OpaqArea*1.0.0.4          111.87.5.252     0x800013e8  2604  0x22 0xb804 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            106.187.14.240
            LocIfAdr (3), length 4:
            106.187.14.122
            RemIfAdr (4), length 4:
            106.187.14.121
            TEMetric (5), length 4:
            100
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 334, Remote 0
            Color (9), length 4:
            10
        OpaqArea*1.0.0.5          111.87.5.252     0x800001bb  1505  0x22 0x79b5 136
        Opaque LSA
        Link (2), length 112:
            Linktype (1), length 1:
            1
            LinkID (2), length 4:
            27.86.198.239
            LocIfAdr (3), length 4:
            27.86.198.25
            RemIfAdr (4), length 4:
            27.86.198.26
            TEMetric (5), length 4:
            1000
            MaxBW (6), length 4:
            1000Mbps
            MaxRsvBW (7), length 4:
            1000Mbps
            UnRsvBW (8), length 32:
                Priority 0, 1000Mbps
                Priority 1, 1000Mbps
                Priority 2, 1000Mbps
                Priority 3, 1000Mbps
                Priority 4, 1000Mbps
                Priority 5, 1000Mbps
                Priority 6, 1000Mbps
                Priority 7, 1000Mbps
            LinkLocalRemoteIdentifier (11), length 8:
            Local 336, Remote 0
            Color (9), length 4:
            2
        OpaqArea*4.0.0.0          111.87.5.252     0x80001a2a   964  0x22 0xe5ef  44
        Opaque LSA
        SR-Algorithm (8), length 1:
            Algo (1), length 1:
                0
        SID/Label Range (9), length 12:
            Range Size (1), length 3:
                8000
            SID/Label (1), length 3:
            Label (1), length 3:
                16000
        OpaqArea*7.0.0.1          111.87.5.252     0x80001b9e  1801  0x22 0x8c7f  44
        Opaque LSA
        Extended Prefix (1), length 20:
            Route Type (1), length 1:
                1
            Prefix Length (2), length 1:
                32
            AF (3), length 1:
                0
            Flags (4),  length 1:
                0x40
            Prefix (5), length 32:
                111.87.5.252
            Prefix Sid (2), length 8:
            Flags (1), length 1:
                0x00
            MT ID (2), length 1:
                0
            Algorithm (3), length 1:
                0
            SID (4), length 4:
                71
        OpaqArea*8.0.0.52         111.87.5.252     0x80000308   694  0x22 0x7efa  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            106.187.14.240
            Link Data (3), length 4:
            106.187.14.122
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                2567
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                2568
        OpaqArea*8.0.0.54         111.87.5.252     0x800002dc  1235  0x22 0x1839  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            111.87.5.253
            Link Data (3), length 4:
            111.87.5.93
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                28985
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                28986
        OpaqArea*8.0.0.55         111.87.5.252     0x800001bb  2069  0x22 0x92eb  60
        Opaque LSA
        Extended Link (1), length 36:
            Link Type (1), length 1:
            1
            Link Id (2), length 4:
            27.86.198.239
            Link Data (3), length 4:
            27.86.198.25
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0xe0
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                167966
            Adjacency Sid (2), length 7:
                Flags (1), length 1:
                0x60
                MT ID (2), length 1:
                0
                Weight (3), length 1:
                0
                Label (4), length 3:
                167967
            OSPF AS SCOPE link state database
        Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        Extern  *106.187.14.240   111.87.5.252     0x80001a3a  2336  0x22 0xc3fb  36
        mask 255.255.255.255
        Topology default (ID 0)
            Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0

    '''}

    golden_parsed_output = {
        "ospf-database-information": {
            "ospf-area-header": {
                "ospf-area": "0.0.0.8"
            },
            "ospf-database": [
                {
                    "advertising-router": "111.87.5.252",
                    "age": "1810",
                    "checksum": "0x1e2",
                    "lsa-id": "111.87.5.252",
                    "lsa-length": "120",
                    "lsa-type": "Router",
                    "options": "0x22",
                    "ospf-router-lsa": {
                        "bits": "0x2",
                        "link-count": "8",
                        "ospf-link": [
                            {
                                "link-data": "111.87.5.93",
                                "link-id": "111.87.5.253",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "5",
                                "ospf-topology-count": "0"
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "111.87.5.92",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "5",
                                "ospf-topology-count": "0"
                            },
                            {
                                "link-data": "106.187.14.122",
                                "link-id": "106.187.14.240",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "100",
                                "ospf-topology-count": "0"
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "106.187.14.120",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0"
                            },
                            {
                                "link-data": "27.86.198.25",
                                "link-id": "27.86.198.239",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "metric": "1000",
                                "ospf-topology-count": "0"
                            },
                            {
                                "link-data": "255.255.255.252",
                                "link-id": "27.86.198.24",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "1000",
                                "ospf-topology-count": "0"
                            },
                            {
                                "link-data": "255.255.255.0",
                                "link-id": "100.0.0.0",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "100",
                                "ospf-topology-count": "0"
                            },
                            {
                                "link-data": "255.255.255.255",
                                "link-id": "111.87.5.252",
                                "link-type-name": "Stub",
                                "link-type-value": "3",
                                "metric": "0",
                                "ospf-topology-count": "0"
                            }
                        ],
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": [
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "1000",
                                    "ospf-lsa-topology-link-node-id": "27.86.198.239",
                                    "ospf-lsa-topology-link-state": "Bidirectional"
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "100",
                                    "ospf-lsa-topology-link-node-id": "106.187.14.240",
                                    "ospf-lsa-topology-link-state": "Bidirectional"
                                },
                                {
                                    "link-type-name": "PointToPoint",
                                    "ospf-lsa-topology-link-metric": "5",
                                    "ospf-lsa-topology-link-node-id": "111.87.5.253",
                                    "ospf-lsa-topology-link-state": "Bidirectional"
                                }
                            ],
                            "ospf-topology-id": "0",
                            "ospf-topology-name": "default"
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001b9e"
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "433",
                    "checksum": "0xd49a",
                    "lsa-id": "1.0.0.1",
                    "lsa-length": "28",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "tlv-block": {
                            "formatted-tlv-data": "111.87.5.252",
                            "tlv-length": "4",
                            "tlv-type-name": "RtrAddr",
                            "tlv-type-value": "1"
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001a15"
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "162",
                    "checksum": "0x95cd",
                    "lsa-id": "1.0.0.3",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "111.87.5.253",
                                "111.87.5.93",
                                "111.87.5.94",
                                "5",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority 0, 1000Mbps\n                          Priority 1, 1000Mbps\n                          Priority 2, 1000Mbps\n                          Priority 3, 1000Mbps\n                          Priority 4, 1000Mbps\n                          Priority 5, 1000Mbps\n                          Priority 6, 1000Mbps\n                          Priority 7, 1000Mbps",
                                "Local 333, Remote 0",
                                "0"
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4"
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color"
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9"
                            ]
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2"
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x80000322"
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "2613",
                    "checksum": "0xb804",
                    "lsa-id": "1.0.0.4",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "106.187.14.240",
                                "106.187.14.122",
                                "106.187.14.121",
                                "100",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority 0, 1000Mbps\n                          Priority 1, 1000Mbps\n                          Priority 2, 1000Mbps\n                          Priority 3, 1000Mbps\n                          Priority 4, 1000Mbps\n                          Priority 5, 1000Mbps\n                          Priority 6, 1000Mbps\n                          Priority 7, 1000Mbps",
                                "Local 334, Remote 0",
                                "10"
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4"
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color"
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9"
                            ]
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2"
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x800013e8"
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "1514",
                    "checksum": "0x79b5",
                    "lsa-id": "1.0.0.5",
                    "lsa-length": "136",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "1",
                                "27.86.198.239",
                                "27.86.198.25",
                                "27.86.198.26",
                                "1000",
                                "1000Mbps",
                                "1000Mbps",
                                "Priority 0, 1000Mbps\n                          Priority 1, 1000Mbps\n                          Priority 2, 1000Mbps\n                          Priority 3, 1000Mbps\n                          Priority 4, 1000Mbps\n                          Priority 5, 1000Mbps\n                          Priority 6, 1000Mbps\n                          Priority 7, 1000Mbps",
                                "Local 336, Remote 0",
                                "2"
                            ],
                            "tlv-length": [
                                "1",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "4",
                                "32",
                                "8",
                                "4"
                            ],
                            "tlv-type-name": [
                                "Linktype",
                                "LinkID",
                                "LocIfAdr",
                                "RemIfAdr",
                                "TEMetric",
                                "MaxBW",
                                "MaxRsvBW",
                                "UnRsvBW",
                                "LinkLocalRemoteIdentifier",
                                "Color"
                            ],
                            "tlv-type-value": [
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "11",
                                "9"
                            ]
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "",
                            "tlv-length": "112",
                            "tlv-type-name": "Link",
                            "tlv-type-value": "2"
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x800001bb"
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "973",
                    "checksum": "0xe5ef",
                    "lsa-id": "4.0.0.0",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "tlv-block": [
                            {
                                "formatted-tlv-data": "Algo (1), length 1:\n                            0",
                                "tlv-length": "1",
                                "tlv-type-name": "SR-Algorithm",
                                "tlv-type-value": "8"
                            },
                            {
                                "formatted-tlv-data": "Range Size (1), length 3:\n                            8000",
                                "te-subtlv": {
                                    "formatted-tlv-data": "Label (1), length 3:\n                                16000",
                                    "tlv-length": "3",
                                    "tlv-type-name": "SID/Label",
                                    "tlv-type-value": "1"
                                },
                                "tlv-length": "12",
                                "tlv-type-name": "SID/Label Range",
                                "tlv-type-value": "9"
                            }
                        ]
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001a2a"
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "1810",
                    "checksum": "0x8c7f",
                    "lsa-id": "7.0.0.1",
                    "lsa-length": "44",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "tlv-block": {
                            "formatted-tlv-data": "Route Type (1), length 1:\n                            1\n                          Prefix Length (2), length 1:\n                            32\n                          AF (3), length 1:\n                            0\n                          Flags (4),  length 1:\n                            0x40\n                          Prefix (5), length 32:\n                            111.87.5.252",
                            "te-subtlv": {
                                "formatted-tlv-data": "Flags (1), length 1:\n                                0x00\n                               MT ID (2), length 1:\n                                0\n                               Algorithm (3), length 1:\n                                0\n                               SID (4), length 4:\n                                71",
                                "tlv-length": "8",
                                "tlv-type-name": "Prefix Sid",
                                "tlv-type-value": "2"
                            },
                            "tlv-length": "20",
                            "tlv-type-name": "Extended Prefix",
                            "tlv-type-value": "1"
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001b9e"
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "703",
                    "checksum": "0x7efa",
                    "lsa-id": "8.0.0.52",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "Flags (1), length 1:\n                                0xe0\n                              MT ID (2), length 1:\n                                 0\n                              Weight (3), length 1:\n                                 0\n                              Label (4), length 3:\n                                2567",
                                "Flags (1), length 1:\n                                0x60\n                              MT ID (2), length 1:\n                                 0\n                              Weight (3), length 1:\n                                 0\n                              Label (4), length 3:\n                                2568"
                            ],
                            "tlv-length": [
                                "7",
                                "7"
                            ],
                            "tlv-type-name": [
                                "Adjacency Sid",
                                "Adjacency Sid"
                            ],
                            "tlv-type-value": [
                                "2",
                                "2"
                            ]
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "Link Type (1), length 1:\n                         1\n                         Link Id (2), length 4:\n                         106.187.14.240\n                         Link Data (3), length 4:\n                         106.187.14.122",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1"
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x80000308"
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "1244",
                    "checksum": "0x1839",
                    "lsa-id": "8.0.0.54",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "Flags (1), length 1:\n                                    0xe0\n                                  MT ID (2), length 1:\n                                     0\n                                  Weight (3), length 1:\n                                     0\n                                  Label (4), length 3:\n                                    28985",
                                "Flags (1), length 1:\n                                    0x60\n                                  MT ID (2), length 1:\n                                     0\n                                  Weight (3), length 1:\n                                     0\n                                  Label (4), length 3:\n                                    28986"
                            ],
                            "tlv-length": [
                                "7",
                                "7"
                            ],
                            "tlv-type-name": [
                                "Adjacency Sid",
                                "Adjacency Sid"
                            ],
                            "tlv-type-value": [
                                "2",
                                "2"
                            ]
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "Link Type (1), length 1:\n                             1\n                             Link Id (2), length 4:\n                             111.87.5.253\n                             Link Data (3), length 4:\n                             111.87.5.93",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1"
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x800002dc"
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "2078",
                    "checksum": "0x92eb",
                    "lsa-id": "8.0.0.55",
                    "lsa-length": "60",
                    "lsa-type": "OpaqArea",
                    "options": "0x22",
                    "ospf-opaque-area-lsa": {
                        "te-subtlv": {
                            "formatted-tlv-data": [
                                "Flags (1), length 1:\n                                        0xe0\n                                      MT ID (2), length 1:\n                                         0\n                                      Weight (3), length 1:\n                                         0\n                                      Label (4), length 3:\n                                        167966",
                                "Flags (1), length 1:\n                                        0x60\n                                      MT ID (2), length 1:\n                                         0\n                                      Weight (3), length 1:\n                                         0\n                                      Label (4), length 3:\n                                        167967"
                            ],
                            "tlv-length": [
                                "7",
                                "7"
                            ],
                            "tlv-type-name": [
                                "Adjacency Sid",
                                "Adjacency Sid"
                            ],
                            "tlv-type-value": [
                                "2",
                                "2"
                            ]
                        },
                        "tlv-block": {
                            "formatted-tlv-data": "Link Type (1), length 1:\n                                 1\n                                 Link Id (2), length 4:\n                                 27.86.198.239\n                                 Link Data (3), length 4:\n                                 27.86.198.25",
                            "tlv-length": "36",
                            "tlv-type-name": "Extended Link",
                            "tlv-type-value": "1"
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x800001bb"
                },
                {
                    "advertising-router": "111.87.5.252",
                    "age": "2345",
                    "checksum": "0xc3fb",
                    "lsa-id": "106.187.14.240",
                    "lsa-length": "36",
                    "lsa-type": "Extern",
                    "options": "0x22",
                    "ospf-external-lsa": {
                        "address-mask": "255.255.255.255",
                        "ospf-external-lsa-topology": {
                            "forward-address": "0.0.0.0",
                            "ospf-topology-id": "0",
                            "ospf-topology-metric": "50",
                            "ospf-topology-name": "default",
                            "tag": "0.0.0.0",
                            "type-value": "1"
                        }
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001a3a"
                }
            ]
        }
}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspfDatabaseAdvertisingRouterSelfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspfDatabaseAdvertisingRouterSelfDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()