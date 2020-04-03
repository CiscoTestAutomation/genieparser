import unittest
from unittest.mock import Mock

from pyats.topology import loader, Device
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ospf3 import ShowOspf3Interface, ShowOspf3Database

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
                    "sequence-number": "0x80001789"
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2413",
                    "checksum": "0xa440",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "44",
                    "lsa-type": "Link",
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

if __name__ == '__main__':
    unittest.main()