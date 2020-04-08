import unittest
from unittest.mock import Mock

from pyats.topology import loader, Device
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ospf3 import ShowOspf3Interface, \
                                               ShowOspf3NeighborExtensive, \
                                               ShowOspf3NeighborDetail, \
                                               ShowOspf3Neighbor,\
                                               ShowOspf3Database, \
                                               ShowOspf3DatabaseExternalExtensive

class TestShowOspf3Interface(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ospf3 interface | no-more
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        ge-0/0/1.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        lo0.0               DR      0.0.0.8         10.189.5.252    0.0.0.0            0
    '''}

    golden_parsed_output = {
        "ospf3-interface-information": {
            "ospf3-interface": [
                {
                    "bdr-id": "0.0.0.0",
                    "dr-id": "0.0.0.0",
                    "interface-name": "ge-0/0/0.0",
                    "neighbor-count": "1",
                    "ospf-area": "0.0.0.8",
                    "ospf-interface-state": "PtToPt"
                },
                {
                    "bdr-id": "0.0.0.0",
                    "dr-id": "0.0.0.0",
                    "interface-name": "ge-0/0/1.0",
                    "neighbor-count": "1",
                    "ospf-area": "0.0.0.8",
                    "ospf-interface-state": "PtToPt"
                },
                {
                    "bdr-id": "0.0.0.0",
                    "dr-id": "10.189.5.252",
                    "interface-name": "lo0.0",
                    "neighbor-count": "0",
                    "ospf-area": "0.0.0.8",
                    "ospf-interface-state": "DR"
                }
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3Interface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3Interface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

class TestShowOspf3NeighborExtensive(unittest.TestCase):
    """ Unit tests for:
            * show ospf3 neighbor extensive
    """

    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ospf3 neighbor extensive
        ID               Interface              State     Pri   Dead
        10.189.5.253     ge-0/0/0.0             Full      128     35
          Neighbor-address fe80::250:56ff:fe8d:53c0
          Area 0.0.0.8, opt 0x13, OSPF3-Intf-Index 2
          DR-ID 0.0.0.0, BDR-ID 0.0.0.0
          Up 3w0d 17:07:00, adjacent 3w0d 17:07:00
        10.169.14.240   ge-0/0/1.0             Full      128     33
          Neighbor-address fe80::250:56ff:fe8d:72bd
         Area 0.0.0.8, opt 0x13, OSPF3-Intf-Index 3
          DR-ID 0.0.0.0, BDR-ID 0.0.0.0
          Up 3w0d 17:06:59, adjacent 3w0d 17:06:55
    '''}

    golden_parsed_output = {
        "ospf3-neighbor-information": {
            "ospf3-neighbor": [
                {
                    "activity-timer": "35",
                    "bdr-id": "0.0.0.0",
                    "dr-id": "0.0.0.0",
                    "interface-name": "ge-0/0/0.0",
                    "neighbor-address": "fe80::250:56ff:fe8d:53c0",
                    "neighbor-adjacency-time": {
                        "#text": "3w0d 17:07:00"
                    },
                    "neighbor-id": "10.189.5.253",
                    "neighbor-priority": "128",
                    "neighbor-up-time": {
                        "#text": "3w0d 17:07:00"
                    },
                    "options": "0x13",
                    "ospf-area": "0.0.0.8",
                    "ospf-neighbor-state": "Full",
                    "ospf3-interface-index": "2"
                },
                {
                    "activity-timer": "33",
                    "bdr-id": "0.0.0.0",
                    "dr-id": "0.0.0.0",
                    "interface-name": "ge-0/0/1.0",
                    "neighbor-address": "fe80::250:56ff:fe8d:72bd",
                    "neighbor-adjacency-time": {
                        "#text": "3w0d 17:06:55"
                    },
                    "neighbor-id": "10.169.14.240",
                    "neighbor-priority": "128",
                    "neighbor-up-time": {
                        "#text": "3w0d 17:06:59"
                    },
                    "options": "0x13",
                    "ospf-area": "0.0.0.8",
                    "ospf-neighbor-state": "Full",
                    "ospf3-interface-index": "3"
                }
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3NeighborExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3NeighborExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspf3NeighborDetail(unittest.TestCase):
    """ Unit tests for:
            * show ospf3 neighbor extensive
    """

    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ospf3 neighbor detail
        ID               Interface              State     Pri   Dead
        10.189.5.253     ge-0/0/0.0             Full      128     34
          Neighbor-address fe80::250:56ff:fe8d:53c0
          Area 0.0.0.8, opt 0x13, OSPF3-Intf-Index 2
          DR-ID 0.0.0.0, BDR-ID 0.0.0.0
          Up 3w0d 17:06:45, adjacent 3w0d 17:06:45
        10.169.14.240   ge-0/0/1.0             Full      128     31
          Neighbor-address fe80::250:56ff:fe8d:72bd
          Area 0.0.0.8, opt 0x13, OSPF3-Intf-Index 3
          DR-ID 0.0.0.0, BDR-ID 0.0.0.0
          Up 3w0d 17:06:44, adjacent 3w0d 17:06:40
    '''}

    golden_parsed_output = {
        "ospf3-neighbor-information": {
            "ospf3-neighbor": [
                {
                    "activity-timer": "34",
                    "bdr-id": "0.0.0.0",
                    "dr-id": "0.0.0.0",
                    "interface-name": "ge-0/0/0.0",
                    "neighbor-address": "fe80::250:56ff:fe8d:53c0",
                    "neighbor-adjacency-time": {
                        "#text": "3w0d 17:06:45"
                    },
                    "neighbor-id": "10.189.5.253",
                    "neighbor-priority": "128",
                    "neighbor-up-time": {
                        "#text": "3w0d 17:06:45"
                    },
                    "options": "0x13",
                    "ospf-area": "0.0.0.8",
                    "ospf-neighbor-state": "Full",
                    "ospf3-interface-index": "2"
                },
                {
                    "activity-timer": "31",
                    "bdr-id": "0.0.0.0",
                    "dr-id": "0.0.0.0",
                    "interface-name": "ge-0/0/1.0",
                    "neighbor-address": "fe80::250:56ff:fe8d:72bd",
                    "neighbor-adjacency-time": {
                        "#text": "3w0d 17:06:40"
                    },
                    "neighbor-id": "10.169.14.240",
                    "neighbor-priority": "128",
                    "neighbor-up-time": {
                        "#text": "3w0d 17:06:44"
                    },
                    "options": "0x13",
                    "ospf-area": "0.0.0.8",
                    "ospf-neighbor-state": "Full",
                    "ospf3-interface-index": "3"
                    }
            ]
        }
    }
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3NeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3NeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
class TestShowOspf3Neighbor(unittest.TestCase):
    """ Unit tests for:
            * show ospf3 neighbor
    """

    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ospf3 neighbor | no-more
        ID               Interface              State     Pri   Dead
        10.189.5.253     ge-0/0/0.0             Full      128     35
          Neighbor-address fe80::250:56ff:fe8d:53c0
        10.169.14.240   ge-0/0/1.0             Full      128     33
          Neighbor-address fe80::250:56ff:fe8d:72bd
    '''}

    golden_parsed_output = {
        "ospf3-neighbor-information": {
            "ospf3-neighbor": [
                {
                    "activity-timer": "35",
                    "interface-name": "ge-0/0/0.0",
                    "neighbor-address": "fe80::250:56ff:fe8d:53c0",
                    "neighbor-id": "10.189.5.253",
                    "neighbor-priority": "128",
                    "ospf-neighbor-state": "Full"
                },
                {
                    "activity-timer": "33",
                    "interface-name": "ge-0/0/1.0",
                    "neighbor-address": "fe80::250:56ff:fe8d:72bd",
                    "neighbor-id": "10.169.14.240",
                    "neighbor-priority": "128",
                    "ospf-neighbor-state": "Full"
                }
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3Neighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3Neighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

class TestShowOspf3Database(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':
    '''

        OSPF3 database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Router      0.0.0.0          10.34.2.250     0x800018ed  2407  0xaf2d  56
        Router      0.0.0.0          10.34.2.251     0x80001841   532  0x1d57  56
        Router      0.0.0.0          10.169.14.240   0x80001a0b  2956  0x52ba  72
        Router      0.0.0.0          10.169.14.241   0x800018b7  1259  0x94a3  72
        Router     *0.0.0.0          10.189.5.252     0x80001890   913  0xae6c  56
        Router      0.0.0.0          10.189.5.253     0x8000182a   915  0x8fdc  56
        IntraArPfx  0.0.0.1          10.34.2.250     0x8000178c  1657  0xc4fc  76
        IntraArPfx  0.0.0.1          10.34.2.251     0x8000178b   907  0x9e2d  76
        IntraArPfx  0.0.0.1          10.169.14.240   0x80001808  2683  0x6948  88
        IntraArPfx  0.0.0.1          10.169.14.241   0x800017e6   926  0xa81e  88
        IntraArPfx *0.0.0.1          10.189.5.252     0x8000178a  1413  0x9b24  76
        IntraArPfx  0.0.0.1          10.189.5.253     0x80001788   415  0x8820  76
            OSPF3 AS SCOPE link state database
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Extern      0.0.0.1          10.34.2.250     0x8000178e  1282  0x3c81  28
        Extern      0.0.0.3          10.34.2.250     0x8000178e   907  0x21bf  44
        Extern      0.0.0.4          10.34.2.250     0x80000246  2783  0xcc71  44
        Extern      0.0.0.1          10.34.2.251     0x80001789  1282  0x4081  28
        Extern      0.0.0.2          10.34.2.251     0x80001788  2782  0x17d0  44
        Extern      0.0.0.3          10.34.2.251     0x80000246   157  0xea52  44
        Extern      0.0.0.18         10.169.14.240   0x80000349  1592  0xbddb  28
        Extern      0.0.0.19         10.169.14.240   0x8000034d   774  0x3603  44
        Extern      0.0.0.22         10.169.14.240   0x800002b9  2138  0xab95  44
        Extern      0.0.0.23         10.169.14.240   0x80000247   501  0x7049  44
        Extern      0.0.0.24         10.169.14.240   0x80000246  2410  0x4e6c  44
        Extern      0.0.0.9          10.169.14.241   0x800002f0  2593  0xd341  44
        Extern      0.0.0.10         10.169.14.241   0x80000246   593  0xd4f2  44
        Extern      0.0.0.11         10.169.14.241   0x80000245  2926  0xe6df  44
        Extern     *0.0.0.1          10.189.5.252     0x8000063f  1913  0x3ff4  44
        Extern      0.0.0.1          10.189.5.253     0x80000e1e  1915  0x7dcd  44

            OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Link       *0.0.0.2          10.189.5.252     0x8000178a   413  0xae5c  56
        Link        0.0.0.2          10.189.5.253     0x80001787  2415  0x13d7  56

            OSPF3 Link-Local database, interface ge-0/0/1.0 Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Link        0.0.0.3          10.169.14.240   0x8000179e  1047  0xbe92  56
        Link       *0.0.0.3          10.189.5.252     0x80001789  2913  0x607c  56

            OSPF3 Link-Local database, interface lo0.0 Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Link       *0.0.0.1          10.189.5.252     0x8000178b  2413  0xa440  44

    '''}

    golden_parsed_output = {
        "ospf3-database-information": {
            "ospf3-area-header": {
                "ospf-area": "0.0.0.8"
            },
            "ospf3-database": [
                {
                    "advertising-router": "10.34.2.250",
                    "age": "2407",
                    "checksum": "0xaf2d",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "56",
                    "lsa-type": "Router",
                    "sequence-number": "0x800018ed"
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "532",
                    "checksum": "0x1d57",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "56",
                    "lsa-type": "Router",
                    "sequence-number": "0x80001841"
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2956",
                    "checksum": "0x52ba",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "72",
                    "lsa-type": "Router",
                    "sequence-number": "0x80001a0b"
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "1259",
                    "checksum": "0x94a3",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "72",
                    "lsa-type": "Router",
                    "sequence-number": "0x800018b7"
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "913",
                    "checksum": "0xae6c",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "56",
                    "lsa-type": "Router",
                    "our-entry": True,
                    "sequence-number": "0x80001890"
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "915",
                    "checksum": "0x8fdc",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "56",
                    "lsa-type": "Router",
                    "sequence-number": "0x8000182a"
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1657",
                    "checksum": "0xc4fc",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "76",
                    "lsa-type": "IntraArPfx",
                    "sequence-number": "0x8000178c"
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "907",
                    "checksum": "0x9e2d",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "76",
                    "lsa-type": "IntraArPfx",
                    "sequence-number": "0x8000178b"
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2683",
                    "checksum": "0x6948",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "88",
                    "lsa-type": "IntraArPfx",
                    "sequence-number": "0x80001808"
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "926",
                    "checksum": "0xa81e",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "88",
                    "lsa-type": "IntraArPfx",
                    "sequence-number": "0x800017e6"
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1413",
                    "checksum": "0x9b24",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "76",
                    "lsa-type": "IntraArPfx",
                    "our-entry": True,
                    "sequence-number": "0x8000178a"
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "415",
                    "checksum": "0x8820",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "76",
                    "lsa-type": "IntraArPfx",
                    "sequence-number": "0x80001788"
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1282",
                    "checksum": "0x3c81",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "28",
                    "lsa-type": "Extern",
                    "sequence-number": "0x8000178e"
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "907",
                    "checksum": "0x21bf",
                    "lsa-id": "0.0.0.3",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x8000178e"
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "2783",
                    "checksum": "0xcc71",
                    "lsa-id": "0.0.0.4",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x80000246"
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "1282",
                    "checksum": "0x4081",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "28",
                    "lsa-type": "Extern",
                    "sequence-number": "0x80001789"
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "2782",
                    "checksum": "0x17d0",
                    "lsa-id": "0.0.0.2",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x80001788"
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "157",
                    "checksum": "0xea52",
                    "lsa-id": "0.0.0.3",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x80000246"
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1592",
                    "checksum": "0xbddb",
                    "lsa-id": "0.0.0.18",
                    "lsa-length": "28",
                    "lsa-type": "Extern",
                    "sequence-number": "0x80000349"
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "774",
                    "checksum": "0x3603",
                    "lsa-id": "0.0.0.19",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x8000034d"
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2138",
                    "checksum": "0xab95",
                    "lsa-id": "0.0.0.22",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x800002b9"
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "501",
                    "checksum": "0x7049",
                    "lsa-id": "0.0.0.23",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x80000247"
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2410",
                    "checksum": "0x4e6c",
                    "lsa-id": "0.0.0.24",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x80000246"
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "2593",
                    "checksum": "0xd341",
                    "lsa-id": "0.0.0.9",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x800002f0"
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "593",
                    "checksum": "0xd4f2",
                    "lsa-id": "0.0.0.10",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x80000246"
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "2926",
                    "checksum": "0xe6df",
                    "lsa-id": "0.0.0.11",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x80000245"
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1913",
                    "checksum": "0x3ff4",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "our-entry": True,
                    "sequence-number": "0x8000063f"
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "1915",
                    "checksum": "0x7dcd",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "sequence-number": "0x80000e1e"
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "413",
                    "checksum": "0xae5c",
                    "lsa-id": "0.0.0.2",
                    "lsa-length": "56",
                    "lsa-type": "Link",
                    "our-entry": True,
                    "sequence-number": "0x8000178a"
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "2415",
                    "checksum": "0x13d7",
                    "lsa-id": "0.0.0.2",
                    "lsa-length": "56",
                    "lsa-type": "Link",
                    "sequence-number": "0x80001787"
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1047",
                    "checksum": "0xbe92",
                    "lsa-id": "0.0.0.3",
                    "lsa-length": "56",
                    "lsa-type": "Link",
                    "sequence-number": "0x8000179e"
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2913",
                    "checksum": "0x607c",
                    "lsa-id": "0.0.0.3",
                    "lsa-length": "56",
                    "lsa-type": "Link",
                    "our-entry": True,
                    "sequence-number": "0x80001789"
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2413",
                    "checksum": "0xa440",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "44",
                    "lsa-type": "Link",
                    "our-entry": True,
                    "sequence-number": "0x8000178b"
                }
            ],
            "ospf3-intf-header": [
                {
                    "ospf-area": "0.0.0.8",
                    "ospf-intf": "ge-0/0/0.0"
                },
                {
                    "ospf-area": "0.0.0.8",
                    "ospf-intf": "ge-0/0/1.0"
                },
                {
                    "ospf-area": "0.0.0.8",
                    "ospf-intf": "lo0.0"
                }
            ]
        }
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3Database(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3Database(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

class TestShowOspf3DatabaseExternalExtensive(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
                show ospf3 database external extensive | no-more
            OSPF3 AS SCOPE link state database
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Extern      0.0.0.1          59.128.2.250     0x8000178e  1412  0x3c81  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:36:27
        Installed 00:23:26 ago, expires in 00:36:28, sent 00:23:24 ago
        Last changed 29w5d 21:04:29 ago, Change count: 1
        Extern      0.0.0.3          59.128.2.250     0x8000178e  1037  0x21bf  44
        Prefix 2001:268:fb8f::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:42:42
        Installed 00:17:11 ago, expires in 00:42:43, sent 00:17:09 ago
        Last changed 29w5d 21:04:29 ago, Change count: 1
        Extern      0.0.0.4          59.128.2.250     0x80000246  2913  0xcc71  44
        Prefix 2001:268:fb8f::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:11:26
        Installed 00:48:26 ago, expires in 00:11:27, sent 00:48:24 ago
        Last changed 2w6d 04:51:00 ago, Change count: 1
        Extern      0.0.0.1          59.128.2.251     0x80001789  1412  0x4081  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:36:27
        Installed 00:23:23 ago, expires in 00:36:28, sent 00:23:21 ago
        Last changed 29w5d 21:04:28 ago, Change count: 1
        Extern      0.0.0.2          59.128.2.251     0x80001788  2912  0x17d0  44
        Prefix 2001:268:fb8f::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:11:27
        Installed 00:48:23 ago, expires in 00:11:28, sent 00:48:21 ago
        Last changed 29w5d 21:04:28 ago, Change count: 1
        Extern      0.0.0.3          59.128.2.251     0x80000246   287  0xea52  44
        Prefix 2001:268:fb8f::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:55:12
        Installed 00:04:38 ago, expires in 00:55:13, sent 00:04:36 ago
        Last changed 2w6d 04:10:55 ago, Change count: 1
        Extern      0.0.0.18         106.187.14.240   0x80000349  1722  0xbddb  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:31:17
        Installed 00:28:39 ago, expires in 00:31:18, sent 00:28:37 ago
        Last changed 4w1d 01:48:00 ago, Change count: 1
        Extern      0.0.0.19         106.187.14.240   0x8000034d   904  0x3603  44
        Prefix 2001:268:fa00:200::1001/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:44:55
        Installed 00:15:01 ago, expires in 00:44:56, sent 00:14:59 ago
        Last changed 3w3d 02:05:47 ago, Change count: 3
        Extern      0.0.0.22         106.187.14.240   0x800002b9  2268  0xab95  44
        Prefix 2001:268:fb90::b/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:22:11
        Installed 00:37:45 ago, expires in 00:22:12, sent 00:37:43 ago
        Last changed 3w0d 17:02:47 ago, Change count: 1
        Extern      0.0.0.23         106.187.14.240   0x80000247   631  0x7049  44
        Prefix 2001:268:fb80::14/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:49:28
        Installed 00:10:28 ago, expires in 00:49:29, sent 00:10:26 ago
        Last changed 2w6d 04:51:04 ago, Change count: 1
        Extern      0.0.0.24         106.187.14.240   0x80000246  2540  0x4e6c  44
        Prefix 2001:268:fb80::13/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:17:39
        Installed 00:42:17 ago, expires in 00:17:40, sent 00:42:15 ago
        Last changed 2w6d 04:50:58 ago, Change count: 1
        Extern      0.0.0.9          106.187.14.241   0x800002f0  2723  0xd341  44
        Prefix 2001:268:fb90::c/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:14:36
        Installed 00:45:17 ago, expires in 00:14:37, sent 00:45:15 ago
        Last changed 3w2d 03:24:20 ago, Change count: 11
        Extern      0.0.0.10         106.187.14.241   0x80000246   723  0xd4f2  44
        Prefix 2001:268:fb80::13/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:47:56
        Installed 00:11:57 ago, expires in 00:47:57, sent 00:11:55 ago
        Last changed 2w6d 04:10:59 ago, Change count: 1
        Extern      0.0.0.11         106.187.14.241   0x80000246    56  0xe4e0  44
        Prefix 2001:268:fb80::14/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:59:03
        Installed 00:00:50 ago, expires in 00:59:04, sent 00:00:48 ago
        Last changed 2w6d 04:10:53 ago, Change count: 1
        Extern     *0.0.0.1          111.87.5.252     0x8000063f  2043  0x3ff4  44
        Prefix 2001:268:fb8f::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Gen timer 00:15:56
        Aging timer 00:25:56
        Installed 00:34:03 ago, expires in 00:25:57, sent 00:34:01 ago
        Last changed 3w0d 17:02:47 ago, Change count: 2, Ours
        Extern      0.0.0.1          111.87.5.253     0x80000e1e  2045  0x7dcd  44
        Prefix 2001:268:fb8f::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:25:54
        Installed 00:34:02 ago, expires in 00:25:55, sent 00:34:01 ago
        Last changed 3w3d 00:31:46 ago, Change count: 15
    '''}

    golden_parsed_output = {'ospf3-database-information': {'ospf3-database': [{'advertising-router': '59.128.2.250',
                                                    'age': '1412',
                                                    'checksum': '0x3c81',
                                                    'lsa-id': '0.0.0.1',
                                                    'lsa-length': '28',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:36:27'},
                                                                                'expiration-time': {'#text': '00:36:28'},
                                                                                'installation-time': {'#text': '00:23:26'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '29w5d '
                                                                                                              '21:04:29'},
                                                                                'send-time': {'#text': '00:23:24'}},
                                                    'ospf3-external-lsa': {'metric': '1',
                                                                           'ospf3-prefix': '::/0',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x8000178e'},
                                                   {'advertising-router': '59.128.2.250',
                                                    'age': '1037',
                                                    'checksum': '0x21bf',
                                                    'lsa-id': '0.0.0.3',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:42:42'},
                                                                                'expiration-time': {'#text': '00:42:43'},
                                                                                'installation-time': {'#text': '00:17:11'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '29w5d '
                                                                                                              '21:04:29'},
                                                                                'send-time': {'#text': '00:17:09'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb8f::2/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x8000178e'},
                                                   {'advertising-router': '59.128.2.250',
                                                    'age': '2913',
                                                    'checksum': '0xcc71',
                                                    'lsa-id': '0.0.0.4',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:11:26'},
                                                                                'expiration-time': {'#text': '00:11:27'},
                                                                                'installation-time': {'#text': '00:48:26'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '2w6d '
                                                                                                              '04:51:00'},
                                                                                'send-time': {'#text': '00:48:24'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb8f::1/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x80000246'},
                                                   {'advertising-router': '59.128.2.251',
                                                    'age': '1412',
                                                    'checksum': '0x4081',
                                                    'lsa-id': '0.0.0.1',
                                                    'lsa-length': '28',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:36:27'},
                                                                                'expiration-time': {'#text': '00:36:28'},
                                                                                'installation-time': {'#text': '00:23:23'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '29w5d '
                                                                                                              '21:04:28'},
                                                                                'send-time': {'#text': '00:23:21'}},
                                                    'ospf3-external-lsa': {'metric': '1',
                                                                           'ospf3-prefix': '::/0',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x80001789'},
                                                   {'advertising-router': '59.128.2.251',
                                                    'age': '2912',
                                                    'checksum': '0x17d0',
                                                    'lsa-id': '0.0.0.2',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:11:27'},
                                                                                'expiration-time': {'#text': '00:11:28'},
                                                                                'installation-time': {'#text': '00:48:23'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '29w5d '
                                                                                                              '21:04:28'},
                                                                                'send-time': {'#text': '00:48:21'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb8f::1/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x80001788'},
                                                   {'advertising-router': '59.128.2.251',
                                                    'age': '287',
                                                    'checksum': '0xea52',
                                                    'lsa-id': '0.0.0.3',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:55:12'},
                                                                                'expiration-time': {'#text': '00:55:13'},
                                                                                'installation-time': {'#text': '00:04:38'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '2w6d '
                                                                                                              '04:10:55'},
                                                                                'send-time': {'#text': '00:04:36'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb8f::2/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x80000246'},
                                                   {'advertising-router': '106.187.14.240',
                                                    'age': '1722',
                                                    'checksum': '0xbddb',
                                                    'lsa-id': '0.0.0.18',
                                                    'lsa-length': '28',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:31:17'},
                                                                                'expiration-time': {'#text': '00:31:18'},
                                                                                'installation-time': {'#text': '00:28:39'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '4w1d '
                                                                                                              '01:48:00'},
                                                                                'send-time': {'#text': '00:28:37'}},
                                                    'ospf3-external-lsa': {'metric': '1',
                                                                           'ospf3-prefix': '::/0',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x80000349'},
                                                   {'advertising-router': '106.187.14.240',
                                                    'age': '904',
                                                    'checksum': '0x3603',
                                                    'lsa-id': '0.0.0.19',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:44:55'},
                                                                                'expiration-time': {'#text': '00:44:56'},
                                                                                'installation-time': {'#text': '00:15:01'},
                                                                                'lsa-change-count': '3',
                                                                                'lsa-changed-time': {'#text': '3w3d '
                                                                                                              '02:05:47'},
                                                                                'send-time': {'#text': '00:14:59'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fa00:200::1001/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x8000034d'},
                                                   {'advertising-router': '106.187.14.240',
                                                    'age': '2268',
                                                    'checksum': '0xab95',
                                                    'lsa-id': '0.0.0.22',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:22:11'},
                                                                                'expiration-time': {'#text': '00:22:12'},
                                                                                'installation-time': {'#text': '00:37:45'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '3w0d '
                                                                                                              '17:02:47'},
                                                                                'send-time': {'#text': '00:37:43'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb90::b/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x800002b9'},
                                                   {'advertising-router': '106.187.14.240',
                                                    'age': '631',
                                                    'checksum': '0x7049',
                                                    'lsa-id': '0.0.0.23',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:49:28'},
                                                                                'expiration-time': {'#text': '00:49:29'},
                                                                                'installation-time': {'#text': '00:10:28'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '2w6d '
                                                                                                              '04:51:04'},
                                                                                'send-time': {'#text': '00:10:26'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb80::14/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x80000247'},
                                                   {'advertising-router': '106.187.14.240',
                                                    'age': '2540',
                                                    'checksum': '0x4e6c',
                                                    'lsa-id': '0.0.0.24',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:17:39'},
                                                                                'expiration-time': {'#text': '00:17:40'},
                                                                                'installation-time': {'#text': '00:42:17'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '2w6d '
                                                                                                              '04:50:58'},
                                                                                'send-time': {'#text': '00:42:15'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb80::13/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x80000246'},
                                                   {'advertising-router': '106.187.14.241',
                                                    'age': '2723',
                                                    'checksum': '0xd341',
                                                    'lsa-id': '0.0.0.9',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:14:36'},
                                                                                'expiration-time': {'#text': '00:14:37'},
                                                                                'installation-time': {'#text': '00:45:17'},
                                                                                'lsa-change-count': '11',
                                                                                'lsa-changed-time': {'#text': '3w2d '
                                                                                                              '03:24:20'},
                                                                                'send-time': {'#text': '00:45:15'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb90::c/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x800002f0'},
                                                   {'advertising-router': '106.187.14.241',
                                                    'age': '723',
                                                    'checksum': '0xd4f2',
                                                    'lsa-id': '0.0.0.10',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:47:56'},
                                                                                'expiration-time': {'#text': '00:47:57'},
                                                                                'installation-time': {'#text': '00:11:57'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '2w6d '
                                                                                                              '04:10:59'},
                                                                                'send-time': {'#text': '00:11:55'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb80::13/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x80000246'},
                                                   {'advertising-router': '106.187.14.241',
                                                    'age': '56',
                                                    'checksum': '0xe4e0',
                                                    'lsa-id': '0.0.0.11',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:59:03'},
                                                                                'expiration-time': {'#text': '00:59:04'},
                                                                                'installation-time': {'#text': '00:00:50'},
                                                                                'lsa-change-count': '1',
                                                                                'lsa-changed-time': {'#text': '2w6d '
                                                                                                              '04:10:53'},
                                                                                'send-time': {'#text': '00:00:48'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb80::14/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x80000246'},
                                                   {'advertising-router': '111.87.5.252',
                                                    'age': '2043',
                                                    'checksum': '0x3ff4',
                                                    'lsa-id': '0.0.0.1',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:25:56'},
                                                                                'database-entry-state': 'Ours',
                                                                                'expiration-time': {'#text': '00:25:57'},
                                                                                'generation-timer': {'#text': '00:15:56'},
                                                                                'installation-time': {'#text': '00:34:03'},
                                                                                'lsa-change-count': '2',
                                                                                'lsa-changed-time': {'#text': '3w0d '
                                                                                                              '17:02:47'},
                                                                                'send-time': {'#text': '00:34:01'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb8f::1/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'our-entry': True,
                                                    'sequence-number': '0x8000063f'},
                                                   {'advertising-router': '111.87.5.253',
                                                    'age': '2045',
                                                    'checksum': '0x7dcd',
                                                    'lsa-id': '0.0.0.1',
                                                    'lsa-length': '44',
                                                    'lsa-type': 'Extern',
                                                    'ospf-database-extensive': {'aging-timer': {'#text': '00:25:54'},
                                                                                'expiration-time': {'#text': '00:25:55'},
                                                                                'installation-time': {'#text': '00:34:02'},
                                                                                'lsa-change-count': '15',
                                                                                'lsa-changed-time': {'#text': '3w3d '
                                                                                                              '00:31:46'},
                                                                                'send-time': {'#text': '00:34:01'}},
                                                    'ospf3-external-lsa': {'metric': '50',
                                                                           'ospf3-prefix': '2001:268:fb8f::2/128',
                                                                           'ospf3-prefix-options': '0x0',
                                                                           'type-value': '1'},
                                                    'sequence-number': '0x80000e1e'}]}}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3DatabaseExternalExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3DatabaseExternalExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()