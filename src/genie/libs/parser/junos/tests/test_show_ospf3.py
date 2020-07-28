import unittest
from unittest.mock import Mock

from pyats.topology import loader, Device
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ospf3 import ShowOspf3Interface, \
                                               ShowOspf3Overview, \
                                               ShowOspf3OverviewExtensive, \
                                               ShowOspf3NeighborExtensive, \
                                               ShowOspf3NeighborDetail, \
                                               ShowOspf3Neighbor,\
                                               ShowOspf3Database,\
                                               ShowOspf3InterfaceExtensive, \
                                               ShowOspf3DatabaseExternalExtensive, \
                                               ShowOspf3DatabaseExtensive,\
                                               ShowOspf3DatabaseNetworkDetail,\
                                               ShowOspf3DatabaseLinkAdvertisingRouter,\
                                               ShowOspf3RouteNetworkExtensive


class TestShowOspf3Interface(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {
        'execute.return_value':
        '''
        show ospf3 interface | no-more
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        ge-0/0/1.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        lo0.0               DR      0.0.0.8         10.189.5.252    0.0.0.0            0
    '''
    }

    golden_parsed_output = {
        "ospf3-interface-information": {
            "ospf3-interface": [{
                "bdr-id": "0.0.0.0",
                "dr-id": "0.0.0.0",
                "interface-name": "ge-0/0/0.0",
                "neighbor-count": "1",
                "ospf-area": "0.0.0.8",
                "ospf-interface-state": "PtToPt"
            }, {
                "bdr-id": "0.0.0.0",
                "dr-id": "0.0.0.0",
                "interface-name": "ge-0/0/1.0",
                "neighbor-count": "1",
                "ospf-area": "0.0.0.8",
                "ospf-interface-state": "PtToPt"
            }, {
                "bdr-id": "0.0.0.0",
                "dr-id": "10.189.5.252",
                "interface-name": "lo0.0",
                "neighbor-count": "0",
                "ospf-area": "0.0.0.8",
                "ospf-interface-state": "DR"
            }]
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

    golden_output = {
        'execute.return_value':
        '''
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
    '''
    }

    golden_parsed_output = {
        "ospf3-neighbor-information": {
            "ospf3-neighbor": [{
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
            }, {
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
            }]
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

    golden_output = {
        'execute.return_value':
        '''
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
    '''
    }

    golden_parsed_output = {
        "ospf3-neighbor-information": {
            "ospf3-neighbor": [{
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
            }, {
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
            }]
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

    golden_output = {
        'execute.return_value':
        '''
        show ospf3 neighbor
        ID               Interface              State     Pri   Dead
        10.189.5.253     ge-0/0/0.0             Full      128     35
          Neighbor-address fe80::250:56ff:fe8d:53c0
        10.169.14.240   ge-0/0/1.0             Full      128     33
          Neighbor-address fe80::250:56ff:fe8d:72bd
    '''
    }

    golden_parsed_output = {
        "ospf3-neighbor-information": {
            "ospf3-neighbor": [{
                "activity-timer": "35",
                "interface-name": "ge-0/0/0.0",
                "neighbor-address": "fe80::250:56ff:fe8d:53c0",
                "neighbor-id": "10.189.5.253",
                "neighbor-priority": "128",
                "ospf-neighbor-state": "Full"
            }, {
                "activity-timer": "33",
                "interface-name": "ge-0/0/1.0",
                "neighbor-address": "fe80::250:56ff:fe8d:72bd",
                "neighbor-id": "10.169.14.240",
                "neighbor-priority": "128",
                "ospf-neighbor-state": "Full"
            }]
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

    golden_output_1 = {
        'execute.return_value':
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

    '''
    }

    golden_parsed_output_1 = {
        'ospf3-database-information': [{
            'ospf3-area-header': {
                'ospf-area': '0.0.0.8'
            },
            'ospf3-database': [{
                'advertising-router': '10.34.2.250',
                'age': '2407',
                'checksum': '0xaf2d',
                'lsa-id': '0.0.0.0',
                'lsa-length': '56',
                'lsa-type': 'Router',
                'sequence-number': '0x800018ed'
            }, {
                'advertising-router': '10.34.2.251',
                'age': '532',
                'checksum': '0x1d57',
                'lsa-id': '0.0.0.0',
                'lsa-length': '56',
                'lsa-type': 'Router',
                'sequence-number': '0x80001841'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '2956',
                'checksum': '0x52ba',
                'lsa-id': '0.0.0.0',
                'lsa-length': '72',
                'lsa-type': 'Router',
                'sequence-number': '0x80001a0b'
            }, {
                'advertising-router': '10.169.14.241',
                'age': '1259',
                'checksum': '0x94a3',
                'lsa-id': '0.0.0.0',
                'lsa-length': '72',
                'lsa-type': 'Router',
                'sequence-number': '0x800018b7'
            }, {
                'advertising-router': '10.189.5.252',
                'age': '913',
                'checksum': '0xae6c',
                'lsa-id': '0.0.0.0',
                'lsa-length': '56',
                'lsa-type': 'Router',
                'our-entry': True,
                'sequence-number': '0x80001890'
            }, {
                'advertising-router': '10.189.5.253',
                'age': '915',
                'checksum': '0x8fdc',
                'lsa-id': '0.0.0.0',
                'lsa-length': '56',
                'lsa-type': 'Router',
                'sequence-number': '0x8000182a'
            }, {
                'advertising-router': '10.34.2.250',
                'age': '1657',
                'checksum': '0xc4fc',
                'lsa-id': '0.0.0.1',
                'lsa-length': '76',
                'lsa-type': 'IntraArPfx',
                'sequence-number': '0x8000178c'
            }, {
                'advertising-router': '10.34.2.251',
                'age': '907',
                'checksum': '0x9e2d',
                'lsa-id': '0.0.0.1',
                'lsa-length': '76',
                'lsa-type': 'IntraArPfx',
                'sequence-number': '0x8000178b'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '2683',
                'checksum': '0x6948',
                'lsa-id': '0.0.0.1',
                'lsa-length': '88',
                'lsa-type': 'IntraArPfx',
                'sequence-number': '0x80001808'
            }, {
                'advertising-router': '10.169.14.241',
                'age': '926',
                'checksum': '0xa81e',
                'lsa-id': '0.0.0.1',
                'lsa-length': '88',
                'lsa-type': 'IntraArPfx',
                'sequence-number': '0x800017e6'
            }, {
                'advertising-router': '10.189.5.252',
                'age': '1413',
                'checksum': '0x9b24',
                'lsa-id': '0.0.0.1',
                'lsa-length': '76',
                'lsa-type': 'IntraArPfx',
                'our-entry': True,
                'sequence-number': '0x8000178a'
            }, {
                'advertising-router': '10.189.5.253',
                'age': '415',
                'checksum': '0x8820',
                'lsa-id': '0.0.0.1',
                'lsa-length': '76',
                'lsa-type': 'IntraArPfx',
                'sequence-number': '0x80001788'
            }, {
                'advertising-router': '10.34.2.250',
                'age': '1282',
                'checksum': '0x3c81',
                'lsa-id': '0.0.0.1',
                'lsa-length': '28',
                'lsa-type': 'Extern',
                'sequence-number': '0x8000178e'
            }, {
                'advertising-router': '10.34.2.250',
                'age': '907',
                'checksum': '0x21bf',
                'lsa-id': '0.0.0.3',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x8000178e'
            }, {
                'advertising-router': '10.34.2.250',
                'age': '2783',
                'checksum': '0xcc71',
                'lsa-id': '0.0.0.4',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x80000246'
            }, {
                'advertising-router': '10.34.2.251',
                'age': '1282',
                'checksum': '0x4081',
                'lsa-id': '0.0.0.1',
                'lsa-length': '28',
                'lsa-type': 'Extern',
                'sequence-number': '0x80001789'
            }, {
                'advertising-router': '10.34.2.251',
                'age': '2782',
                'checksum': '0x17d0',
                'lsa-id': '0.0.0.2',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x80001788'
            }, {
                'advertising-router': '10.34.2.251',
                'age': '157',
                'checksum': '0xea52',
                'lsa-id': '0.0.0.3',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x80000246'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '1592',
                'checksum': '0xbddb',
                'lsa-id': '0.0.0.18',
                'lsa-length': '28',
                'lsa-type': 'Extern',
                'sequence-number': '0x80000349'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '774',
                'checksum': '0x3603',
                'lsa-id': '0.0.0.19',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x8000034d'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '2138',
                'checksum': '0xab95',
                'lsa-id': '0.0.0.22',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x800002b9'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '501',
                'checksum': '0x7049',
                'lsa-id': '0.0.0.23',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x80000247'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '2410',
                'checksum': '0x4e6c',
                'lsa-id': '0.0.0.24',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x80000246'
            }, {
                'advertising-router': '10.169.14.241',
                'age': '2593',
                'checksum': '0xd341',
                'lsa-id': '0.0.0.9',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x800002f0'
            }, {
                'advertising-router': '10.169.14.241',
                'age': '593',
                'checksum': '0xd4f2',
                'lsa-id': '0.0.0.10',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x80000246'
            }, {
                'advertising-router': '10.169.14.241',
                'age': '2926',
                'checksum': '0xe6df',
                'lsa-id': '0.0.0.11',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x80000245'
            }, {
                'advertising-router': '10.189.5.252',
                'age': '1913',
                'checksum': '0x3ff4',
                'lsa-id': '0.0.0.1',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'our-entry': True,
                'sequence-number': '0x8000063f'
            }, {
                'advertising-router': '10.189.5.253',
                'age': '1915',
                'checksum': '0x7dcd',
                'lsa-id': '0.0.0.1',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'sequence-number': '0x80000e1e'
            }, {
                'advertising-router': '10.189.5.252',
                'age': '413',
                'checksum': '0xae5c',
                'lsa-id': '0.0.0.2',
                'lsa-length': '56',
                'lsa-type': 'Link',
                'our-entry': True,
                'sequence-number': '0x8000178a'
            }, {
                'advertising-router': '10.189.5.253',
                'age': '2415',
                'checksum': '0x13d7',
                'lsa-id': '0.0.0.2',
                'lsa-length': '56',
                'lsa-type': 'Link',
                'sequence-number': '0x80001787'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '1047',
                'checksum': '0xbe92',
                'lsa-id': '0.0.0.3',
                'lsa-length': '56',
                'lsa-type': 'Link',
                'sequence-number': '0x8000179e'
            }, {
                'advertising-router': '10.189.5.252',
                'age': '2913',
                'checksum': '0x607c',
                'lsa-id': '0.0.0.3',
                'lsa-length': '56',
                'lsa-type': 'Link',
                'our-entry': True,
                'sequence-number': '0x80001789'
            }, {
                'advertising-router': '10.189.5.252',
                'age': '2413',
                'checksum': '0xa440',
                'lsa-id': '0.0.0.1',
                'lsa-length': '44',
                'lsa-type': 'Link',
                'our-entry': True,
                'sequence-number': '0x8000178b'
            }],
            'ospf3-intf-header': [{
                'ospf-area': '0.0.0.8',
                'ospf-intf': 'ge-0/0/0.0'
            }, {
                'ospf-area': '0.0.0.8',
                'ospf-intf': 'ge-0/0/1.0'
            }, {
                'ospf-area': '0.0.0.8',
                'ospf-intf': 'lo0.0'
            }]
        }]
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3Database(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowOspf3Database(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.golden_parsed_output_1)



class TestShowOspf3InterfaceExtensive(unittest.TestCase):

    maxDiff = None

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {
        'execute.return_value':
        """
                    show ospf3 interface extensive | no-more
            Interface           State   Area            DR ID           BDR ID          Nbrs
            ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
            Address fe80::250:56ff:fe8d:c829, Prefix-length 64
            OSPF3-Intf-index 2, Type P2P, MTU 1500, Cost 5
            Adj count: 1, Router LSA ID: 0
            Hello 10, Dead 40, ReXmit 5, Not Stub
            Protection type: None
            ge-0/0/1.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
            Address fe80::250:56ff:fe8d:a96c, Prefix-length 64
            OSPF3-Intf-index 3, Type P2P, MTU 1500, Cost 100
            Adj count: 1, Router LSA ID: 0
            Hello 10, Dead 40, ReXmit 5, Not Stub
            Protection type: None
            lo0.0               DR      0.0.0.8         10.189.5.252    0.0.0.0            0
            Address fe80::250:560f:fc8d:7c08, Prefix-length 128
            OSPF3-Intf-index 1, Type LAN, MTU 65535, Cost 0, Priority 128
            Adj count: 0, Router LSA ID: -
            DR addr fe80::250:560f:fc8d:7c08
            Hello 10, Dead 40, ReXmit 5, Not Stub
            Protection type: None
        """
    }

    golden_parsed_output = {
        "ospf3-interface-information": {
            "ospf3-interface": [{
                "adj-count": "1",
                "bdr-id": "0.0.0.0",
                "dead-interval": "40",
                "dr-id": "0.0.0.0",
                "hello-interval": "10",
                "interface-address": "fe80::250:56ff:fe8d:c829",
                "interface-cost": "5",
                "interface-name": "ge-0/0/0.0",
                "interface-type": "P2P",
                "mtu": "1500",
                "neighbor-count": "1",
                "ospf-area": "0.0.0.8",
                "ospf-interface-protection-type": "None",
                "ospf-interface-state": "PtToPt",
                "ospf-stub-type": "Not Stub",
                "ospf3-interface-index": "2",
                "ospf3-router-lsa-id": "0",
                "prefix-length": "64",
                "retransmit-interval": "5"
            }, {
                "adj-count": "1",
                "bdr-id": "0.0.0.0",
                "dead-interval": "40",
                "dr-id": "0.0.0.0",
                "hello-interval": "10",
                "interface-address": "fe80::250:56ff:fe8d:a96c",
                "interface-cost": "100",
                "interface-name": "ge-0/0/1.0",
                "interface-type": "P2P",
                "mtu": "1500",
                "neighbor-count": "1",
                "ospf-area": "0.0.0.8",
                "ospf-interface-protection-type": "None",
                "ospf-interface-state": "PtToPt",
                "ospf-stub-type": "Not Stub",
                "ospf3-interface-index": "3",
                "ospf3-router-lsa-id": "0",
                "prefix-length": "64",
                "retransmit-interval": "5"
            }, {
                "adj-count": "0",
                "bdr-id": "0.0.0.0",
                "dead-interval": "40",
                "dr-address": "fe80::250:560f:fc8d:7c08",
                "dr-id": "10.189.5.252",
                "hello-interval": "10",
                "interface-address": "fe80::250:560f:fc8d:7c08",
                "interface-cost": "0",
                "interface-name": "lo0.0",
                "interface-type": "LAN",
                "mtu": "65535",
                "neighbor-count": "0",
                "ospf-area": "0.0.0.8",
                "ospf-interface-protection-type": "None",
                "ospf-interface-state": "DR",
                "ospf-stub-type": "Not Stub",
                "ospf3-interface-index": "1",
                "prefix-length": "128",
                "retransmit-interval": "5",
                "router-priority": "128"
            }]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3InterfaceExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3InterfaceExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspf3DatabaseExternalExtensive(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {
        'execute.return_value':
        '''
                show ospf3 database external extensive | no-more
            OSPF3 AS SCOPE link state database
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Extern      0.0.0.1          10.34.2.250     0x8000178e  1412  0x3c81  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:36:27
        Installed 00:23:26 ago, expires in 00:36:28, sent 00:23:24 ago
        Last changed 29w5d 21:04:29 ago, Change count: 1
        Extern      0.0.0.3          10.34.2.250     0x8000178e  1037  0x21bf  44
        Prefix 2001:db8:eb18:ca45::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:42:42
        Installed 00:17:11 ago, expires in 00:42:43, sent 00:17:09 ago
        Last changed 29w5d 21:04:29 ago, Change count: 1
        Extern      0.0.0.4          10.34.2.250     0x80000246  2913  0xcc71  44
        Prefix 2001:db8:eb18:ca45::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:11:26
        Installed 00:48:26 ago, expires in 00:11:27, sent 00:48:24 ago
        Last changed 2w6d 04:51:00 ago, Change count: 1
        Extern      0.0.0.1          10.34.2.251     0x80001789  1412  0x4081  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:36:27
        Installed 00:23:23 ago, expires in 00:36:28, sent 00:23:21 ago
        Last changed 29w5d 21:04:28 ago, Change count: 1
        Extern      0.0.0.2          10.34.2.251     0x80001788  2912  0x17d0  44
        Prefix 2001:db8:eb18:ca45::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:11:27
        Installed 00:48:23 ago, expires in 00:11:28, sent 00:48:21 ago
        Last changed 29w5d 21:04:28 ago, Change count: 1
        Extern      0.0.0.3          10.34.2.251     0x80000246   287  0xea52  44
        Prefix 2001:db8:eb18:ca45::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:55:12
        Installed 00:04:38 ago, expires in 00:55:13, sent 00:04:36 ago
        Last changed 2w6d 04:10:55 ago, Change count: 1
        Extern      0.0.0.18         10.169.14.240   0x80000349  1722  0xbddb  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:31:17
        Installed 00:28:39 ago, expires in 00:31:18, sent 00:28:37 ago
        Last changed 4w1d 01:48:00 ago, Change count: 1
        Extern      0.0.0.19         10.169.14.240   0x8000034d   904  0x3603  44
        Prefix 2001:db8:6aa8:6a53::1001/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:44:55
        Installed 00:15:01 ago, expires in 00:44:56, sent 00:14:59 ago
        Last changed 3w3d 02:05:47 ago, Change count: 3
        Extern      0.0.0.22         10.169.14.240   0x800002b9  2268  0xab95  44
        Prefix 2001:db8:223c:ca45::b/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:22:11
        Installed 00:37:45 ago, expires in 00:22:12, sent 00:37:43 ago
        Last changed 3w0d 17:02:47 ago, Change count: 1
        Extern      0.0.0.23         10.169.14.240   0x80000247   631  0x7049  44
        Prefix 2001:db8:b0f8:ca45::14/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:49:28
        Installed 00:10:28 ago, expires in 00:49:29, sent 00:10:26 ago
        Last changed 2w6d 04:51:04 ago, Change count: 1
        Extern      0.0.0.24         10.169.14.240   0x80000246  2540  0x4e6c  44
        Prefix 2001:db8:b0f8:ca45::13/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:17:39
        Installed 00:42:17 ago, expires in 00:17:40, sent 00:42:15 ago
        Last changed 2w6d 04:50:58 ago, Change count: 1
        Extern      0.0.0.9          10.169.14.241   0x800002f0  2723  0xd341  44
        Prefix 2001:db8:223c:ca45::c/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:14:36
        Installed 00:45:17 ago, expires in 00:14:37, sent 00:45:15 ago
        Last changed 3w2d 03:24:20 ago, Change count: 11
        Extern      0.0.0.10         10.169.14.241   0x80000246   723  0xd4f2  44
        Prefix 2001:db8:b0f8:ca45::13/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:47:56
        Installed 00:11:57 ago, expires in 00:47:57, sent 00:11:55 ago
        Last changed 2w6d 04:10:59 ago, Change count: 1
        Extern      0.0.0.11         10.169.14.241   0x80000246    56  0xe4e0  44
        Prefix 2001:db8:b0f8:ca45::14/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:59:03
        Installed 00:00:50 ago, expires in 00:59:04, sent 00:00:48 ago
        Last changed 2w6d 04:10:53 ago, Change count: 1
        Extern     *0.0.0.1          10.189.5.252     0x8000063f  2043  0x3ff4  44
        Prefix 2001:db8:eb18:ca45::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Gen timer 00:15:56
        Aging timer 00:25:56
        Installed 00:34:03 ago, expires in 00:25:57, sent 00:34:01 ago
        Last changed 3w0d 17:02:47 ago, Change count: 2, Ours
        Extern      0.0.0.1          10.189.5.253     0x80000e1e  2045  0x7dcd  44
        Prefix 2001:db8:eb18:ca45::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:25:54
        Installed 00:34:02 ago, expires in 00:25:55, sent 00:34:01 ago
        Last changed 3w3d 00:31:46 ago, Change count: 15
    '''
    }

    golden_parsed_output = {
        'ospf3-database-information': {
            'ospf3-database': [{
                'advertising-router': '10.34.2.250',
                'age': '1412',
                'checksum': '0x3c81',
                'lsa-id': '0.0.0.1',
                'lsa-length': '28',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:36:27'
                    },
                    'expiration-time': {
                        '#text': '00:36:28'
                    },
                    'installation-time': {
                        '#text': '00:23:26'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '29w5d 21:04:29'
                    },
                    'send-time': {
                        '#text': '00:23:24'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '1',
                    'ospf3-prefix': '::/0',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x8000178e'
            }, {
                'advertising-router': '10.34.2.250',
                'age': '1037',
                'checksum': '0x21bf',
                'lsa-id': '0.0.0.3',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:42:42'
                    },
                    'expiration-time': {
                        '#text': '00:42:43'
                    },
                    'installation-time': {
                        '#text': '00:17:11'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '29w5d '
                        '21:04:29'
                    },
                    'send-time': {
                        '#text': '00:17:09'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:eb18:ca45::2/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x8000178e'
            }, {
                'advertising-router': '10.34.2.250',
                'age': '2913',
                'checksum': '0xcc71',
                'lsa-id': '0.0.0.4',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:11:26'
                    },
                    'expiration-time': {
                        '#text': '00:11:27'
                    },
                    'installation-time': {
                        '#text': '00:48:26'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '2w6d '
                        '04:51:00'
                    },
                    'send-time': {
                        '#text': '00:48:24'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:eb18:ca45::1/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x80000246'
            }, {
                'advertising-router': '10.34.2.251',
                'age': '1412',
                'checksum': '0x4081',
                'lsa-id': '0.0.0.1',
                'lsa-length': '28',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:36:27'
                    },
                    'expiration-time': {
                        '#text': '00:36:28'
                    },
                    'installation-time': {
                        '#text': '00:23:23'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '29w5d '
                        '21:04:28'
                    },
                    'send-time': {
                        '#text': '00:23:21'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '1',
                    'ospf3-prefix': '::/0',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x80001789'
            }, {
                'advertising-router': '10.34.2.251',
                'age': '2912',
                'checksum': '0x17d0',
                'lsa-id': '0.0.0.2',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:11:27'
                    },
                    'expiration-time': {
                        '#text': '00:11:28'
                    },
                    'installation-time': {
                        '#text': '00:48:23'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '29w5d '
                        '21:04:28'
                    },
                    'send-time': {
                        '#text': '00:48:21'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:eb18:ca45::1/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x80001788'
            }, {
                'advertising-router': '10.34.2.251',
                'age': '287',
                'checksum': '0xea52',
                'lsa-id': '0.0.0.3',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:55:12'
                    },
                    'expiration-time': {
                        '#text': '00:55:13'
                    },
                    'installation-time': {
                        '#text': '00:04:38'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '2w6d '
                        '04:10:55'
                    },
                    'send-time': {
                        '#text': '00:04:36'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:eb18:ca45::2/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x80000246'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '1722',
                'checksum': '0xbddb',
                'lsa-id': '0.0.0.18',
                'lsa-length': '28',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:31:17'
                    },
                    'expiration-time': {
                        '#text': '00:31:18'
                    },
                    'installation-time': {
                        '#text': '00:28:39'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '4w1d '
                        '01:48:00'
                    },
                    'send-time': {
                        '#text': '00:28:37'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '1',
                    'ospf3-prefix': '::/0',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x80000349'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '904',
                'checksum': '0x3603',
                'lsa-id': '0.0.0.19',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:44:55'
                    },
                    'expiration-time': {
                        '#text': '00:44:56'
                    },
                    'installation-time': {
                        '#text': '00:15:01'
                    },
                    'lsa-change-count': '3',
                    'lsa-changed-time': {
                        '#text': '3w3d '
                        '02:05:47'
                    },
                    'send-time': {
                        '#text': '00:14:59'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:6aa8:6a53::1001/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x8000034d'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '2268',
                'checksum': '0xab95',
                'lsa-id': '0.0.0.22',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:22:11'
                    },
                    'expiration-time': {
                        '#text': '00:22:12'
                    },
                    'installation-time': {
                        '#text': '00:37:45'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '3w0d '
                        '17:02:47'
                    },
                    'send-time': {
                        '#text': '00:37:43'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:223c:ca45::b/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x800002b9'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '631',
                'checksum': '0x7049',
                'lsa-id': '0.0.0.23',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:49:28'
                    },
                    'expiration-time': {
                        '#text': '00:49:29'
                    },
                    'installation-time': {
                        '#text': '00:10:28'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '2w6d '
                        '04:51:04'
                    },
                    'send-time': {
                        '#text': '00:10:26'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:b0f8:ca45::14/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x80000247'
            }, {
                'advertising-router': '10.169.14.240',
                'age': '2540',
                'checksum': '0x4e6c',
                'lsa-id': '0.0.0.24',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:17:39'
                    },
                    'expiration-time': {
                        '#text': '00:17:40'
                    },
                    'installation-time': {
                        '#text': '00:42:17'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '2w6d '
                        '04:50:58'
                    },
                    'send-time': {
                        '#text': '00:42:15'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:b0f8:ca45::13/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x80000246'
            }, {
                'advertising-router': '10.169.14.241',
                'age': '2723',
                'checksum': '0xd341',
                'lsa-id': '0.0.0.9',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:14:36'
                    },
                    'expiration-time': {
                        '#text': '00:14:37'
                    },
                    'installation-time': {
                        '#text': '00:45:17'
                    },
                    'lsa-change-count': '11',
                    'lsa-changed-time': {
                        '#text': '3w2d '
                        '03:24:20'
                    },
                    'send-time': {
                        '#text': '00:45:15'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:223c:ca45::c/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x800002f0'
            }, {
                'advertising-router': '10.169.14.241',
                'age': '723',
                'checksum': '0xd4f2',
                'lsa-id': '0.0.0.10',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:47:56'
                    },
                    'expiration-time': {
                        '#text': '00:47:57'
                    },
                    'installation-time': {
                        '#text': '00:11:57'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '2w6d '
                        '04:10:59'
                    },
                    'send-time': {
                        '#text': '00:11:55'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:b0f8:ca45::13/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x80000246'
            }, {
                'advertising-router': '10.169.14.241',
                'age': '56',
                'checksum': '0xe4e0',
                'lsa-id': '0.0.0.11',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:59:03'
                    },
                    'expiration-time': {
                        '#text': '00:59:04'
                    },
                    'installation-time': {
                        '#text': '00:00:50'
                    },
                    'lsa-change-count': '1',
                    'lsa-changed-time': {
                        '#text': '2w6d '
                        '04:10:53'
                    },
                    'send-time': {
                        '#text': '00:00:48'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:b0f8:ca45::14/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x80000246'
            }, {
                'advertising-router': '10.189.5.252',
                'age': '2043',
                'checksum': '0x3ff4',
                'lsa-id': '0.0.0.1',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:25:56'
                    },
                    'database-entry-state': 'Ours',
                    'expiration-time': {
                        '#text': '00:25:57'
                    },
                    'generation-timer': {
                        '#text': '00:15:56'
                    },
                    'installation-time': {
                        '#text': '00:34:03'
                    },
                    'lsa-change-count': '2',
                    'lsa-changed-time': {
                        '#text': '3w0d '
                        '17:02:47'
                    },
                    'send-time': {
                        '#text': '00:34:01'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:eb18:ca45::1/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'our-entry': True,
                'sequence-number': '0x8000063f'
            }, {
                'advertising-router': '10.189.5.253',
                'age': '2045',
                'checksum': '0x7dcd',
                'lsa-id': '0.0.0.1',
                'lsa-length': '44',
                'lsa-type': 'Extern',
                'ospf-database-extensive': {
                    'aging-timer': {
                        '#text': '00:25:54'
                    },
                    'expiration-time': {
                        '#text': '00:25:55'
                    },
                    'installation-time': {
                        '#text': '00:34:02'
                    },
                    'lsa-change-count': '15',
                    'lsa-changed-time': {
                        '#text': '3w3d '
                        '00:31:46'
                    },
                    'send-time': {
                        '#text': '00:34:01'
                    }
                },
                'ospf3-external-lsa': {
                    'metric': '50',
                    'ospf3-prefix': '2001:db8:eb18:ca45::2/128',
                    'ospf3-prefix-options': '0x0',
                    'type-value': '1'
                },
                'sequence-number': '0x80000e1e'
            }]
        }
    }

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


class TestShowOspf3Overview(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {
        'execute.return_value':
        '''
        show ospf3 overview
        Instance: master
          Router ID: 10.189.5.252
          Route table index: 0
          Configured overload, expires in 14 seconds
          AS boundary router
          LSA refresh time: 50 minutes
          Post Convergence Backup: Disabled
          Area: 0.0.0.8
            Stub type: Not Stub
            Area border routers: 0, AS boundary routers: 5
            Neighbors
              Up (in full state): 2
            Topology: default (ID 0)
              Prefix export count: 1
              Full SPF runs: 1934
              SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
              Backup SPF: Not Needed
    '''
    }

    golden_parsed_output = {
        "ospf3-overview-information": {
            "ospf-overview": {
                "instance-name": "master",
                "ospf-area-overview": {
                    "ospf-abr-count": "0",
                    "ospf-area": "0.0.0.8",
                    "ospf-asbr-count": "5",
                    "ospf-nbr-overview": {
                        "ospf-nbr-up-count": "2"
                    },
                    "ospf-stub-type": "Not Stub"
                },
                "ospf-lsa-refresh-time": "50",
                "ospf-route-table-index": "0",
                'ospf-configured-overload-remaining-time': '14',
                "ospf-router-id": "10.189.5.252",
                "ospf-tilfa-overview": {
                    "ospf-tilfa-enabled": "Disabled"
                },
                "ospf-topology-overview": {
                    "ospf-backup-spf-status": "Not Needed",
                    "ospf-full-spf-count": "1934",
                    "ospf-prefix-export-count": "1",
                    "ospf-spf-delay": "0.200000",
                    "ospf-spf-holddown": "2",
                    "ospf-spf-rapid-runs": "3",
                    "ospf-topology-id": "0",
                    "ospf-topology-name": "default"
                }
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3Overview(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3Overview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspf3OverviewExtensive(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {
        'execute.return_value':
        '''
        show ospf3 overview extensive
        Instance: master
          Router ID: 10.189.5.252
          Route table index: 0
          AS boundary router
          LSA refresh time: 50 minutes
          Post Convergence Backup: Disabled
          Area: 0.0.0.8
            Stub type: Not Stub
            Area border routers: 0, AS boundary routers: 5
            Neighbors
              Up (in full state): 2
          Topology: default (ID 0)
            Prefix export count: 1
            Full SPF runs: 1934
            SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
            Backup SPF: Not Needed
    '''
    }

    golden_parsed_output = {
        "ospf3-overview-information": {
            "ospf-overview": {
                "instance-name": "master",
                "ospf-area-overview": {
                    "ospf-abr-count": "0",
                    "ospf-area": "0.0.0.8",
                    "ospf-asbr-count": "5",
                    "ospf-nbr-overview": {
                        "ospf-nbr-up-count": "2"
                    },
                    "ospf-stub-type": "Not Stub"
                },
                "ospf-lsa-refresh-time": "50",
                "ospf-route-table-index": "0",
                "ospf-router-id": "10.189.5.252",
                "ospf-tilfa-overview": {
                    "ospf-tilfa-enabled": "Disabled"
                },
                "ospf-topology-overview": {
                    "ospf-backup-spf-status": "Not Needed",
                    "ospf-full-spf-count": "1934",
                    "ospf-prefix-export-count": "1",
                    "ospf-spf-delay": "0.200000",
                    "ospf-spf-holddown": "2",
                    "ospf-spf-rapid-runs": "3",
                    "ospf-topology-id": "0",
                    "ospf-topology-name": "default"
                }
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3OverviewExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3OverviewExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspf3DatabaseExtensive(unittest.TestCase):

    maxDiff = None

    device = Device(name="test-device")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value":
        """

        show ospf3 database extensive

            OSPF3 database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Router      0.0.0.0          10.34.2.250     0x800018ed  2504  0xaf2d  56
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 10.34.2.251
        Type PointToPoint (1), Metric 100
            Loc-If-Id 3, Nbr-If-Id 4, Nbr-Rtr-Id 10.169.14.240
        Type: PointToPoint, Node ID: 10.169.14.240, Metric: 100, Bidirectional
        Type: PointToPoint, Node ID: 10.34.2.251, Metric: 5, Bidirectional
        Aging timer 00:18:16
        Installed 00:41:38 ago, expires in 00:18:16, sent 00:41:36 ago
        Last changed 2w6d 04:50:31 ago, Change count: 196
        Router      0.0.0.0          10.34.2.251     0x80001841   629  0x1d57  56
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 10.34.2.250
        Type PointToPoint (1), Metric 120
            Loc-If-Id 3, Nbr-If-Id 4, Nbr-Rtr-Id 10.169.14.241
        Type: PointToPoint, Node ID: 10.169.14.241, Metric: 120, Bidirectional
        Type: PointToPoint, Node ID: 10.34.2.250, Metric: 5, Bidirectional
        Aging timer 00:49:31
        Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
        Last changed 2w6d 04:10:26 ago, Change count: 208
        Router      0.0.0.0          10.169.14.240   0x80001a0c    53  0x50bb  72
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 10.169.14.241
        Type PointToPoint (1), Metric 100
            Loc-If-Id 3, Nbr-If-Id 3, Nbr-Rtr-Id 10.189.5.252
        Type PointToPoint (1), Metric 100
            Loc-If-Id 4, Nbr-If-Id 3, Nbr-Rtr-Id 10.34.2.250
        Type: PointToPoint, Node ID: 10.34.2.250, Metric: 100, Bidirectional
        Type: PointToPoint, Node ID: 10.189.5.252, Metric: 100, Bidirectional
        Type: PointToPoint, Node ID: 10.169.14.241, Metric: 5, Bidirectional
        Aging timer 00:59:06
        Installed 00:00:50 ago, expires in 00:59:07, sent 00:00:48 ago
        Last changed 2w6d 04:50:31 ago, Change count: 341
        Router      0.0.0.0          10.169.14.241   0x800018b7  1356  0x94a3  72
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 10.169.14.240
        Type PointToPoint (1), Metric 120
            Loc-If-Id 3, Nbr-If-Id 3, Nbr-Rtr-Id 10.189.5.253
        Type PointToPoint (1), Metric 120
            Loc-If-Id 4, Nbr-If-Id 3, Nbr-Rtr-Id 10.34.2.251
        Type: PointToPoint, Node ID: 10.34.2.251, Metric: 120, Bidirectional
        Type: PointToPoint, Node ID: 10.189.5.253, Metric: 120, Bidirectional
        Type: PointToPoint, Node ID: 10.169.14.240, Metric: 5, Bidirectional
        Aging timer 00:37:23
        Installed 00:22:30 ago, expires in 00:37:24, sent 00:22:28 ago
        Last changed 2w6d 04:10:26 ago, Change count: 280
        Router     *0.0.0.0          10.189.5.252     0x80001890  1010  0xae6c  56
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 10.189.5.253
        Type PointToPoint (1), Metric 100
            Loc-If-Id 3, Nbr-If-Id 3, Nbr-Rtr-Id 10.169.14.240
        Type: PointToPoint, Node ID: 10.169.14.240, Metric: 100, Bidirectional
        Type: PointToPoint, Node ID: 10.189.5.253, Metric: 5, Bidirectional
        Gen timer 00:33:09
        Aging timer 00:43:09
        Installed 00:16:50 ago, expires in 00:43:10, sent 00:16:48 ago
        Last changed 3w0d 17:02:09 ago, Change count: 6, Ours
        Router      0.0.0.0          10.189.5.253     0x8000182a  1012  0x8fdc  56
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 10.189.5.252
        Type PointToPoint (1), Metric 120
            Loc-If-Id 3, Nbr-If-Id 3, Nbr-Rtr-Id 10.169.14.241
        Type: PointToPoint, Node ID: 10.169.14.241, Metric: 120, Bidirectional
        Type: PointToPoint, Node ID: 10.189.5.252, Metric: 5, Bidirectional
        Aging timer 00:43:07
        Installed 00:16:49 ago, expires in 00:43:08, sent 00:16:48 ago
        Last changed 3w0d 17:02:14 ago, Change count: 181
        IntraArPfx  0.0.0.1          10.34.2.250     0x8000178c  1754  0xc4fc  76
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 10.34.2.250
        Prefix-count 3
        Prefix 2001:db8:b0f8:3ab::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:db8:eb18:9627::/64
            Prefix-options 0x0, Metric 100
        Prefix 2001:db8:b0f8:ca45::13/128
            Prefix-options 0x2, Metric 0
        Aging timer 00:30:46
        Installed 00:29:08 ago, expires in 00:30:46, sent 00:29:06 ago
        Last changed 29w5d 21:33:07 ago, Change count: 1
        InterArPfx  0.0.0.2          10.4.1.1          0x80000002    52  0x4035  44
        Prefix 2001::11/128
        Prefix-options 0x0, Metric 0
        Aging timer 00:59:08
        Installed 00:00:07 ago, expires in 00:59:08
        Last changed 00:00:07 ago, Change count: 1
        IntraArPfx  0.0.0.1          10.34.2.251     0x8000178b  1004  0x9e2d  76
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 10.34.2.251
        Prefix-count 3
        Prefix 2001:db8:b0f8:3ab::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:db8:eb18:f5e6::/64
            Prefix-options 0x0, Metric 120
        Prefix 2001:db8:b0f8:ca45::14/128
            Prefix-options 0x2, Metric 0
        Aging timer 00:43:16
        Installed 00:16:35 ago, expires in 00:43:16, sent 00:16:33 ago
        Last changed 29w5d 21:33:07 ago, Change count: 1
        IntraArPfx  0.0.0.1          10.169.14.240   0x80001808  2780  0x6948  88
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 10.169.14.240
        Prefix-count 4
        Prefix 2001:db8:eb18:e26e::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:db8:eb18:6337::/64
            Prefix-options 0x0, Metric 100
        Prefix 2001:db8:eb18:9627::/64
            Prefix-options 0x0, Metric 100
        Prefix 2001:db8:eb18:ca45::1/128
            Prefix-options 0x2, Metric 0
        Aging timer 00:13:39
        Installed 00:46:17 ago, expires in 00:13:40, sent 00:46:15 ago
        Last changed 2w6d 04:50:31 ago, Change count: 147
        IntraArPfx  0.0.0.1          10.169.14.241   0x800017e6  1023  0xa81e  88
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 10.169.14.241
        Prefix-count 4
        Prefix 2001:db8:eb18:e26e::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:db8:eb18:6d57::/64
            Prefix-options 0x0, Metric 120
        Prefix 2001:db8:eb18:f5e6::/64
            Prefix-options 0x0, Metric 120
        Prefix 2001:db8:eb18:ca45::2/128
            Prefix-options 0x2, Metric 0
        Aging timer 00:42:56
        Installed 00:16:57 ago, expires in 00:42:57, sent 00:16:55 ago
        Last changed 2w6d 04:10:26 ago, Change count: 111
        IntraArPfx *0.0.0.1          10.189.5.252     0x8000178a  1510  0x9b24  76
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 10.189.5.252
        Prefix-count 3
        Prefix 2001:db8:223c:2c16::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:db8:eb18:6337::/64
            Prefix-options 0x0, Metric 100
        Prefix 2001:db8:223c:ca45::b/128
            Prefix-options 0x2, Metric 0
        Gen timer 00:24:49
        Aging timer 00:34:49
        Installed 00:25:10 ago, expires in 00:34:50, sent 00:25:08 ago
        Last changed 29w5d 21:40:56 ago, Change count: 2, Ours
        IntraArPfx  0.0.0.1          10.189.5.253     0x80001788   512  0x8820  76
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 10.189.5.253
        Prefix-count 3
        Prefix 2001:db8:223c:2c16::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:db8:eb18:6d57::/64
            Prefix-options 0x0, Metric 120
        Prefix 2001:db8:223c:ca45::c/128
            Prefix-options 0x2, Metric 0
        Aging timer 00:51:27
        Installed 00:08:29 ago, expires in 00:51:28, sent 00:08:27 ago
        Last changed 29w5d 21:33:18 ago, Change count: 1
            OSPF3 AS SCOPE link state database
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Extern      0.0.0.1          10.34.2.250     0x8000178e  1379  0x3c81  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:37:01
        Installed 00:22:53 ago, expires in 00:37:01, sent 00:22:51 ago
        Last changed 29w5d 21:03:56 ago, Change count: 1
        Extern      0.0.0.3          10.34.2.250     0x8000178e  1004  0x21bf  44
        Prefix 2001:db8:eb18:ca45::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:43:16
        Installed 00:16:38 ago, expires in 00:43:16, sent 00:16:36 ago
        Last changed 29w5d 21:03:56 ago, Change count: 1
        Extern      0.0.0.4          10.34.2.250     0x80000246  2880  0xcc71  44
        Prefix 2001:db8:eb18:ca45::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:12:00
        Installed 00:47:53 ago, expires in 00:12:00, sent 00:47:51 ago
        Last changed 2w6d 04:50:27 ago, Change count: 1
        Extern      0.0.0.1          10.34.2.251     0x80001789  1379  0x4081  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:37:01
        Installed 00:22:50 ago, expires in 00:37:01, sent 00:22:48 ago
        Last changed 29w5d 21:03:55 ago, Change count: 1
        Extern      0.0.0.2          10.34.2.251     0x80001788  2879  0x17d0  44
        Prefix 2001:db8:eb18:ca45::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:12:01
        Installed 00:47:50 ago, expires in 00:12:01, sent 00:47:48 ago
        Last changed 29w5d 21:03:55 ago, Change count: 1
        Extern      0.0.0.3          10.34.2.251     0x80000246   254  0xea52  44
        Prefix 2001:db8:eb18:ca45::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:55:46
        Installed 00:04:05 ago, expires in 00:55:46, sent 00:04:03 ago
        Last changed 2w6d 04:10:22 ago, Change count: 1
        Extern      0.0.0.18         10.169.14.240   0x80000349  1689  0xbddb  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:31:50
        Installed 00:28:06 ago, expires in 00:31:51, sent 00:28:04 ago
        Last changed 4w1d 01:47:27 ago, Change count: 1
        Extern      0.0.0.19         10.169.14.240   0x8000034d   871  0x3603  44
        Prefix 2001:db8:6aa8:6a53::1001/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:45:28
        Installed 00:14:28 ago, expires in 00:45:29, sent 00:14:26 ago
        Last changed 3w3d 02:05:14 ago, Change count: 3
        Extern      0.0.0.22         10.169.14.240   0x800002b9  2235  0xab95  44
        Prefix 2001:db8:223c:ca45::b/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:22:45
        Installed 00:37:12 ago, expires in 00:22:45, sent 00:37:10 ago
        Last changed 3w0d 17:02:14 ago, Change count: 1
        Extern      0.0.0.23         10.169.14.240   0x80000247   598  0x7049  44
        Prefix 2001:db8:b0f8:ca45::14/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:50:01
        Installed 00:09:55 ago, expires in 00:50:02, sent 00:09:53 ago
        Last changed 2w6d 04:50:31 ago, Change count: 1
        Extern      0.0.0.24         10.169.14.240   0x80000246  2507  0x4e6c  44
        Prefix 2001:db8:b0f8:ca45::13/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:18:12
        Installed 00:41:44 ago, expires in 00:18:13, sent 00:41:42 ago
        Last changed 2w6d 04:50:25 ago, Change count: 1
        Extern      0.0.0.9          10.169.14.241   0x800002f0  2690  0xd341  44
        Prefix 2001:db8:223c:ca45::c/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:15:10
        Installed 00:44:44 ago, expires in 00:15:10, sent 00:44:42 ago
        Last changed 3w2d 03:23:47 ago, Change count: 11
        Extern      0.0.0.10         10.169.14.241   0x80000246   690  0xd4f2  44
        Prefix 2001:db8:b0f8:ca45::13/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:48:30
        Installed 00:11:24 ago, expires in 00:48:30, sent 00:11:22 ago
        Last changed 2w6d 04:10:26 ago, Change count: 1
        Extern      0.0.0.11         10.169.14.241   0x80000246    23  0xe4e0  44
        Prefix 2001:db8:b0f8:ca45::14/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:59:36
        Installed 00:00:17 ago, expires in 00:59:37, sent 00:00:15 ago
        Last changed 2w6d 04:10:20 ago, Change count: 1
        Extern     *0.0.0.1          10.189.5.252     0x8000063f  2010  0x3ff4  44
        Prefix 2001:db8:eb18:ca45::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Gen timer 00:16:29
        Aging timer 00:26:29
        Installed 00:33:30 ago, expires in 00:26:30, sent 00:33:28 ago
        Last changed 3w0d 17:02:14 ago, Change count: 2, Ours
        Extern      0.0.0.1          10.189.5.253     0x80000e1e  2012  0x7dcd  44
        Prefix 2001:db8:eb18:ca45::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:26:27
        Installed 00:33:29 ago, expires in 00:26:28, sent 00:33:28 ago
        Last changed 3w3d 00:31:13 ago, Change count: 15

            OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Link       *0.0.0.2          10.189.5.252     0x8000178a   510  0xae5c  56
        fe80::250:56ff:fe8d:c829
        Options 0x33, Priority 128
        Prefix-count 1
        Prefix 2001:db8:223c:2c16::/64 Prefix-options 0x0
        Gen timer 00:41:29
        Aging timer 00:51:29
        Installed 00:08:30 ago, expires in 00:51:30, sent 00:08:28 ago
        Last changed 29w5d 21:40:56 ago, Change count: 1, Ours
        Link        0.0.0.2          10.189.5.253     0x80001787  2512  0x13d7  56
        fe80::250:56ff:fe8d:53c0
        Options 0x33, Priority 128
        Prefix-count 1
        Prefix 2001:db8:223c:2c16::/64 Prefix-options 0x0
        Aging timer 00:18:07
        Installed 00:41:49 ago, expires in 00:18:08
        Last changed 29w5d 21:33:17 ago, Change count: 1

            OSPF3 Link-Local database, interface ge-0/0/1.0 Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Link        0.0.0.3          10.169.14.240   0x8000179e  1144  0xbe92  56
        fe80::250:56ff:fe8d:72bd
        Options 0x33, Priority 128
        Prefix-count 1
        Prefix 2001:db8:eb18:6337::/64 Prefix-options 0x0
        Aging timer 00:40:56
        Installed 00:19:01 ago, expires in 00:40:56, sent 6w2d 02:47:58 ago
        Last changed 29w5d 21:33:04 ago, Change count: 1
        Link       *0.0.0.3          10.189.5.252     0x8000178a    10  0x5e7d  56
        fe80::250:56ff:fe8d:a96c
        Options 0x33, Priority 128
        Prefix-count 1
        Prefix 2001:db8:eb18:6337::/64 Prefix-options 0x0
        Gen timer 00:49:49
        Aging timer 00:59:49
        Installed 00:00:10 ago, expires in 00:59:50, sent 00:00:08 ago
        Last changed 29w5d 21:40:56 ago, Change count: 1, Ours

            OSPF3 Link-Local database, interface lo0.0 Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Link       *0.0.0.1          10.189.5.252     0x8000178b  2510  0xa440  44
        fe80::250:560f:fc8d:7c08
        Options 0x33, Priority 128
        Prefix-count 0
        Gen timer 00:08:09
        Aging timer 00:18:09
        Installed 00:41:50 ago, expires in 00:18:10
        Last changed 29w5d 21:46:59 ago, Change count: 1, Ours

    """
    }

    golden_parsed_output = {
        "ospf3-database-information": {
            "ospf3-area-header": {
                "ospf-area": "0.0.0.8"
            },
            "ospf3-database": [
                {
                    "advertising-router": "10.34.2.250",
                    "age": "2504",
                    "checksum": "0xaf2d",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "56",
                    "lsa-type": "Router",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:18:16"
                        },
                        "expiration-time": {
                            "#text": "00:18:16"
                        },
                        "installation-time": {
                            "#text": "00:41:38"
                        },
                        "lsa-change-count": "196",
                        "lsa-changed-time": {
                            "#text": "2w6d 04:50:31"
                        },
                        "send-time": {
                            "#text": "00:41:36"
                        },
                    },
                    "ospf3-router-lsa": {
                        "bits":
                        "0x2",
                        "ospf3-link": [
                            {
                                "link-intf-id": "2",
                                "link-metric": "5",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "2",
                                "nbr-rtr-id": "10.34.2.251",
                            },
                            {
                                "link-intf-id": "3",
                                "link-metric": "100",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "4",
                                "nbr-rtr-id": "10.169.14.240",
                            },
                        ],
                        "ospf3-lsa-topology": {
                            "ospf-topology-id":
                            "0",
                            "ospf-topology-name":
                            "default",
                            "ospf3-lsa-topology-link": [
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "100",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.169.14.240",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "5",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.34.2.251",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                            ],
                        },
                        "ospf3-options":
                        "0x33",
                    },
                    "sequence-number": "0x800018ed",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "629",
                    "checksum": "0x1d57",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "56",
                    "lsa-type": "Router",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:49:31"
                        },
                        "expiration-time": {
                            "#text": "00:49:31"
                        },
                        "installation-time": {
                            "#text": "00:10:20"
                        },
                        "lsa-change-count": "208",
                        "lsa-changed-time": {
                            "#text": "2w6d "
                            "04:10:26"
                        },
                        "send-time": {
                            "#text": "00:10:18"
                        },
                    },
                    "ospf3-router-lsa": {
                        "bits":
                        "0x2",
                        "ospf3-link": [
                            {
                                "link-intf-id": "2",
                                "link-metric": "5",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "2",
                                "nbr-rtr-id": "10.34.2.250",
                            },
                            {
                                "link-intf-id": "3",
                                "link-metric": "120",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "4",
                                "nbr-rtr-id": "10.169.14.241",
                            },
                        ],
                        "ospf3-lsa-topology": {
                            "ospf-topology-id":
                            "0",
                            "ospf-topology-name":
                            "default",
                            "ospf3-lsa-topology-link": [
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "120",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.169.14.241",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "5",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.34.2.250",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                            ],
                        },
                        "ospf3-options":
                        "0x33",
                    },
                    "sequence-number": "0x80001841",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "53",
                    "checksum": "0x50bb",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "72",
                    "lsa-type": "Router",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:59:06"
                        },
                        "expiration-time": {
                            "#text": "00:59:07"
                        },
                        "installation-time": {
                            "#text": "00:00:50"
                        },
                        "lsa-change-count": "341",
                        "lsa-changed-time": {
                            "#text": "2w6d "
                            "04:50:31"
                        },
                        "send-time": {
                            "#text": "00:00:48"
                        },
                    },
                    "ospf3-router-lsa": {
                        "bits":
                        "0x2",
                        "ospf3-link": [
                            {
                                "link-intf-id": "2",
                                "link-metric": "5",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "2",
                                "nbr-rtr-id": "10.169.14.241",
                            },
                            {
                                "link-intf-id": "3",
                                "link-metric": "100",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "3",
                                "nbr-rtr-id": "10.189.5.252",
                            },
                            {
                                "link-intf-id": "4",
                                "link-metric": "100",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "3",
                                "nbr-rtr-id": "10.34.2.250",
                            },
                        ],
                        "ospf3-lsa-topology": {
                            "ospf-topology-id":
                            "0",
                            "ospf-topology-name":
                            "default",
                            "ospf3-lsa-topology-link": [
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "100",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.34.2.250",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "100",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.189.5.252",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "5",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.169.14.241",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                            ],
                        },
                        "ospf3-options":
                        "0x33",
                    },
                    "sequence-number": "0x80001a0c",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "1356",
                    "checksum": "0x94a3",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "72",
                    "lsa-type": "Router",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:37:23"
                        },
                        "expiration-time": {
                            "#text": "00:37:24"
                        },
                        "installation-time": {
                            "#text": "00:22:30"
                        },
                        "lsa-change-count": "280",
                        "lsa-changed-time": {
                            "#text": "2w6d "
                            "04:10:26"
                        },
                        "send-time": {
                            "#text": "00:22:28"
                        },
                    },
                    "ospf3-router-lsa": {
                        "bits":
                        "0x2",
                        "ospf3-link": [
                            {
                                "link-intf-id": "2",
                                "link-metric": "5",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "2",
                                "nbr-rtr-id": "10.169.14.240",
                            },
                            {
                                "link-intf-id": "3",
                                "link-metric": "120",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "3",
                                "nbr-rtr-id": "10.189.5.253",
                            },
                            {
                                "link-intf-id": "4",
                                "link-metric": "120",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "3",
                                "nbr-rtr-id": "10.34.2.251",
                            },
                        ],
                        "ospf3-lsa-topology": {
                            "ospf-topology-id":
                            "0",
                            "ospf-topology-name":
                            "default",
                            "ospf3-lsa-topology-link": [
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "120",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.34.2.251",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "120",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.189.5.253",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "5",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.169.14.240",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                            ],
                        },
                        "ospf3-options":
                        "0x33",
                    },
                    "sequence-number": "0x800018b7",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1010",
                    "checksum": "0xae6c",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "56",
                    "lsa-type": "Router",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:43:09"
                        },
                        "database-entry-state": "Ours",
                        "expiration-time": {
                            "#text": "00:43:10"
                        },
                        "generation-timer": {
                            "#text": "00:33:09"
                        },
                        "installation-time": {
                            "#text": "00:16:50"
                        },
                        "lsa-change-count": "6",
                        "lsa-changed-time": {
                            "#text": "3w0d "
                            "17:02:09"
                        },
                        "send-time": {
                            "#text": "00:16:48"
                        },
                    },
                    "ospf3-router-lsa": {
                        "bits":
                        "0x2",
                        "ospf3-link": [
                            {
                                "link-intf-id": "2",
                                "link-metric": "5",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "2",
                                "nbr-rtr-id": "10.189.5.253",
                            },
                            {
                                "link-intf-id": "3",
                                "link-metric": "100",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "3",
                                "nbr-rtr-id": "10.169.14.240",
                            },
                        ],
                        "ospf3-lsa-topology": {
                            "ospf-topology-id":
                            "0",
                            "ospf-topology-name":
                            "default",
                            "ospf3-lsa-topology-link": [
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "100",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.169.14.240",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "5",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.189.5.253",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                            ],
                        },
                        "ospf3-options":
                        "0x33",
                    },
                    "our-entry": True,
                    "sequence-number": "0x80001890",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "1012",
                    "checksum": "0x8fdc",
                    "lsa-id": "0.0.0.0",
                    "lsa-length": "56",
                    "lsa-type": "Router",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:43:07"
                        },
                        "expiration-time": {
                            "#text": "00:43:08"
                        },
                        "installation-time": {
                            "#text": "00:16:49"
                        },
                        "lsa-change-count": "181",
                        "lsa-changed-time": {
                            "#text": "3w0d "
                            "17:02:14"
                        },
                        "send-time": {
                            "#text": "00:16:48"
                        },
                    },
                    "ospf3-router-lsa": {
                        "bits":
                        "0x2",
                        "ospf3-link": [
                            {
                                "link-intf-id": "2",
                                "link-metric": "5",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "2",
                                "nbr-rtr-id": "10.189.5.252",
                            },
                            {
                                "link-intf-id": "3",
                                "link-metric": "120",
                                "link-type-name": "PointToPoint",
                                "link-type-value": "1",
                                "nbr-intf-id": "3",
                                "nbr-rtr-id": "10.169.14.241",
                            },
                        ],
                        "ospf3-lsa-topology": {
                            "ospf-topology-id":
                            "0",
                            "ospf-topology-name":
                            "default",
                            "ospf3-lsa-topology-link": [
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "120",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.169.14.241",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                                {
                                    "link-type-name":
                                    "PointToPoint",
                                    "ospf-lsa-topology-link-metric":
                                    "5",
                                    "ospf-lsa-topology-link-node-id":
                                    "10.189.5.252",
                                    "ospf-lsa-topology-link-state":
                                    "Bidirectional",
                                },
                            ],
                        },
                        "ospf3-options":
                        "0x33",
                    },
                    "sequence-number": "0x8000182a",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1754",
                    "checksum": "0xc4fc",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "76",
                    "lsa-type": "IntraArPfx",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:30:46"
                        },
                        "expiration-time": {
                            "#text": "00:30:46"
                        },
                        "installation-time": {
                            "#text": "00:29:08"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:33:07"
                        },
                        "send-time": {
                            "#text": "00:29:06"
                        },
                    },
                    "ospf3-intra-area-prefix-lsa": {
                        "ospf3-prefix": [
                            "2001:db8:b0f8:3ab::/64",
                            "2001:db8:eb18:9627::/64",
                            "2001:db8:b0f8:ca45::13/128",
                        ],
                        "ospf3-prefix-metric": ["5", "100", "0"],
                        "ospf3-prefix-options": ["0x0", "0x0", "0x2"],
                        "prefix-count":
                        "3",
                        "reference-lsa-id":
                        "0.0.0.0",
                        "reference-lsa-router-id":
                        "10.34.2.250",
                        "reference-lsa-type":
                        "Router",
                    },
                    "sequence-number": "0x8000178c",
                },
                {'advertising-router': '10.4.1.1',
                    'age': '52',
                    'checksum': '0x4035',
                    'lsa-id': '0.0.0.2',
                    'lsa-length': '44',
                    'lsa-type': 'InterArPfx',
                    'ospf-database-extensive': {'aging-timer': {'#text': '00:59:08'},
                                                'expiration-time': {'#text': '00:59:08'},
                                                'installation-time': {'#text': '00:00:07'},
                                                'lsa-change-count': '1',
                                                'lsa-changed-time': {'#text': '00:00:07'}},
                    'ospf3-inter-area-prefix-lsa': {'ospf3-prefix': ['2001::11/128'],
                                                    'ospf3-prefix-metric': ['0'],
                                                    'ospf3-prefix-options': ['0x0']},
                    'sequence-number': '0x80000002'},
                {
                    "advertising-router": "10.34.2.251",
                    "age": "1004",
                    "checksum": "0x9e2d",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "76",
                    "lsa-type": "IntraArPfx",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:43:16"
                        },
                        "expiration-time": {
                            "#text": "00:43:16"
                        },
                        "installation-time": {
                            "#text": "00:16:35"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:33:07"
                        },
                        "send-time": {
                            "#text": "00:16:33"
                        },
                    },
                    "ospf3-intra-area-prefix-lsa": {
                        "ospf3-prefix": [
                            "2001:db8:b0f8:3ab::/64",
                            "2001:db8:eb18:f5e6::/64",
                            "2001:db8:b0f8:ca45::14/128",
                        ],
                        "ospf3-prefix-metric": ["5", "120", "0"],
                        "ospf3-prefix-options": ["0x0", "0x0", "0x2"],
                        "prefix-count":
                        "3",
                        "reference-lsa-id":
                        "0.0.0.0",
                        "reference-lsa-router-id":
                        "10.34.2.251",
                        "reference-lsa-type":
                        "Router",
                    },
                    "sequence-number": "0x8000178b",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2780",
                    "checksum": "0x6948",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "88",
                    "lsa-type": "IntraArPfx",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:13:39"
                        },
                        "expiration-time": {
                            "#text": "00:13:40"
                        },
                        "installation-time": {
                            "#text": "00:46:17"
                        },
                        "lsa-change-count": "147",
                        "lsa-changed-time": {
                            "#text": "2w6d "
                            "04:50:31"
                        },
                        "send-time": {
                            "#text": "00:46:15"
                        },
                    },
                    "ospf3-intra-area-prefix-lsa": {
                        "ospf3-prefix": [
                            "2001:db8:eb18:e26e::/64",
                            "2001:db8:eb18:6337::/64",
                            "2001:db8:eb18:9627::/64",
                            "2001:db8:eb18:ca45::1/128",
                        ],
                        "ospf3-prefix-metric": ["5", "100", "100", "0"],
                        "ospf3-prefix-options": ["0x0", "0x0", "0x0", "0x2"],
                        "prefix-count":
                        "4",
                        "reference-lsa-id":
                        "0.0.0.0",
                        "reference-lsa-router-id":
                        "10.169.14.240",
                        "reference-lsa-type":
                        "Router",
                    },
                    "sequence-number": "0x80001808",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "1023",
                    "checksum": "0xa81e",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "88",
                    "lsa-type": "IntraArPfx",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:42:56"
                        },
                        "expiration-time": {
                            "#text": "00:42:57"
                        },
                        "installation-time": {
                            "#text": "00:16:57"
                        },
                        "lsa-change-count": "111",
                        "lsa-changed-time": {
                            "#text": "2w6d "
                            "04:10:26"
                        },
                        "send-time": {
                            "#text": "00:16:55"
                        },
                    },
                    "ospf3-intra-area-prefix-lsa": {
                        "ospf3-prefix": [
                            "2001:db8:eb18:e26e::/64",
                            "2001:db8:eb18:6d57::/64",
                            "2001:db8:eb18:f5e6::/64",
                            "2001:db8:eb18:ca45::2/128",
                        ],
                        "ospf3-prefix-metric": ["5", "120", "120", "0"],
                        "ospf3-prefix-options": ["0x0", "0x0", "0x0", "0x2"],
                        "prefix-count":
                        "4",
                        "reference-lsa-id":
                        "0.0.0.0",
                        "reference-lsa-router-id":
                        "10.169.14.241",
                        "reference-lsa-type":
                        "Router",
                    },
                    "sequence-number": "0x800017e6",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "1510",
                    "checksum": "0x9b24",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "76",
                    "lsa-type": "IntraArPfx",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:34:49"
                        },
                        "database-entry-state": "Ours",
                        "expiration-time": {
                            "#text": "00:34:50"
                        },
                        "generation-timer": {
                            "#text": "00:24:49"
                        },
                        "installation-time": {
                            "#text": "00:25:10"
                        },
                        "lsa-change-count": "2",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:40:56"
                        },
                        "send-time": {
                            "#text": "00:25:08"
                        },
                    },
                    "ospf3-intra-area-prefix-lsa": {
                        "ospf3-prefix": [
                            "2001:db8:223c:2c16::/64",
                            "2001:db8:eb18:6337::/64",
                            "2001:db8:223c:ca45::b/128",
                        ],
                        "ospf3-prefix-metric": ["5", "100", "0"],
                        "ospf3-prefix-options": ["0x0", "0x0", "0x2"],
                        "prefix-count":
                        "3",
                        "reference-lsa-id":
                        "0.0.0.0",
                        "reference-lsa-router-id":
                        "10.189.5.252",
                        "reference-lsa-type":
                        "Router",
                    },
                    "our-entry": True,
                    "sequence-number": "0x8000178a",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "512",
                    "checksum": "0x8820",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "76",
                    "lsa-type": "IntraArPfx",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:51:27"
                        },
                        "expiration-time": {
                            "#text": "00:51:28"
                        },
                        "installation-time": {
                            "#text": "00:08:29"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:33:18"
                        },
                        "send-time": {
                            "#text": "00:08:27"
                        },
                    },
                    "ospf3-intra-area-prefix-lsa": {
                        "ospf3-prefix": [
                            "2001:db8:223c:2c16::/64",
                            "2001:db8:eb18:6d57::/64",
                            "2001:db8:223c:ca45::c/128",
                        ],
                        "ospf3-prefix-metric": ["5", "120", "0"],
                        "ospf3-prefix-options": ["0x0", "0x0", "0x2"],
                        "prefix-count":
                        "3",
                        "reference-lsa-id":
                        "0.0.0.0",
                        "reference-lsa-router-id":
                        "10.189.5.253",
                        "reference-lsa-type":
                        "Router",
                    },
                    "sequence-number": "0x80001788",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1379",
                    "checksum": "0x3c81",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "28",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:37:01"
                        },
                        "expiration-time": {
                            "#text": "00:37:01"
                        },
                        "installation-time": {
                            "#text": "00:22:53"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:03:56"
                        },
                        "send-time": {
                            "#text": "00:22:51"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "1",
                        "ospf3-prefix": "::/0",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x8000178e",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "1004",
                    "checksum": "0x21bf",
                    "lsa-id": "0.0.0.3",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:43:16"
                        },
                        "expiration-time": {
                            "#text": "00:43:16"
                        },
                        "installation-time": {
                            "#text": "00:16:38"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:03:56"
                        },
                        "send-time": {
                            "#text": "00:16:36"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:eb18:ca45::2/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x8000178e",
                },
                {
                    "advertising-router": "10.34.2.250",
                    "age": "2880",
                    "checksum": "0xcc71",
                    "lsa-id": "0.0.0.4",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:12:00"
                        },
                        "expiration-time": {
                            "#text": "00:12:00"
                        },
                        "installation-time": {
                            "#text": "00:47:53"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "2w6d "
                            "04:50:27"
                        },
                        "send-time": {
                            "#text": "00:47:51"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:eb18:ca45::1/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x80000246",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "1379",
                    "checksum": "0x4081",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "28",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:37:01"
                        },
                        "expiration-time": {
                            "#text": "00:37:01"
                        },
                        "installation-time": {
                            "#text": "00:22:50"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:03:55"
                        },
                        "send-time": {
                            "#text": "00:22:48"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "1",
                        "ospf3-prefix": "::/0",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x80001789",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "2879",
                    "checksum": "0x17d0",
                    "lsa-id": "0.0.0.2",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:12:01"
                        },
                        "expiration-time": {
                            "#text": "00:12:01"
                        },
                        "installation-time": {
                            "#text": "00:47:50"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:03:55"
                        },
                        "send-time": {
                            "#text": "00:47:48"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:eb18:ca45::1/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x80001788",
                },
                {
                    "advertising-router": "10.34.2.251",
                    "age": "254",
                    "checksum": "0xea52",
                    "lsa-id": "0.0.0.3",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:55:46"
                        },
                        "expiration-time": {
                            "#text": "00:55:46"
                        },
                        "installation-time": {
                            "#text": "00:04:05"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "2w6d "
                            "04:10:22"
                        },
                        "send-time": {
                            "#text": "00:04:03"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:eb18:ca45::2/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x80000246",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1689",
                    "checksum": "0xbddb",
                    "lsa-id": "0.0.0.18",
                    "lsa-length": "28",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:31:50"
                        },
                        "expiration-time": {
                            "#text": "00:31:51"
                        },
                        "installation-time": {
                            "#text": "00:28:06"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "4w1d "
                            "01:47:27"
                        },
                        "send-time": {
                            "#text": "00:28:04"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "1",
                        "ospf3-prefix": "::/0",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x80000349",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "871",
                    "checksum": "0x3603",
                    "lsa-id": "0.0.0.19",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:45:28"
                        },
                        "expiration-time": {
                            "#text": "00:45:29"
                        },
                        "installation-time": {
                            "#text": "00:14:28"
                        },
                        "lsa-change-count": "3",
                        "lsa-changed-time": {
                            "#text": "3w3d "
                            "02:05:14"
                        },
                        "send-time": {
                            "#text": "00:14:26"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:6aa8:6a53::1001/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x8000034d",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2235",
                    "checksum": "0xab95",
                    "lsa-id": "0.0.0.22",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:22:45"
                        },
                        "expiration-time": {
                            "#text": "00:22:45"
                        },
                        "installation-time": {
                            "#text": "00:37:12"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "3w0d "
                            "17:02:14"
                        },
                        "send-time": {
                            "#text": "00:37:10"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:223c:ca45::b/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x800002b9",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "598",
                    "checksum": "0x7049",
                    "lsa-id": "0.0.0.23",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:50:01"
                        },
                        "expiration-time": {
                            "#text": "00:50:02"
                        },
                        "installation-time": {
                            "#text": "00:09:55"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "2w6d "
                            "04:50:31"
                        },
                        "send-time": {
                            "#text": "00:09:53"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:b0f8:ca45::14/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x80000247",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "2507",
                    "checksum": "0x4e6c",
                    "lsa-id": "0.0.0.24",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:18:12"
                        },
                        "expiration-time": {
                            "#text": "00:18:13"
                        },
                        "installation-time": {
                            "#text": "00:41:44"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "2w6d "
                            "04:50:25"
                        },
                        "send-time": {
                            "#text": "00:41:42"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:b0f8:ca45::13/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x80000246",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "2690",
                    "checksum": "0xd341",
                    "lsa-id": "0.0.0.9",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:15:10"
                        },
                        "expiration-time": {
                            "#text": "00:15:10"
                        },
                        "installation-time": {
                            "#text": "00:44:44"
                        },
                        "lsa-change-count": "11",
                        "lsa-changed-time": {
                            "#text": "3w2d "
                            "03:23:47"
                        },
                        "send-time": {
                            "#text": "00:44:42"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:223c:ca45::c/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x800002f0",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "690",
                    "checksum": "0xd4f2",
                    "lsa-id": "0.0.0.10",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:48:30"
                        },
                        "expiration-time": {
                            "#text": "00:48:30"
                        },
                        "installation-time": {
                            "#text": "00:11:24"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "2w6d "
                            "04:10:26"
                        },
                        "send-time": {
                            "#text": "00:11:22"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:b0f8:ca45::13/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x80000246",
                },
                {
                    "advertising-router": "10.169.14.241",
                    "age": "23",
                    "checksum": "0xe4e0",
                    "lsa-id": "0.0.0.11",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:59:36"
                        },
                        "expiration-time": {
                            "#text": "00:59:37"
                        },
                        "installation-time": {
                            "#text": "00:00:17"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "2w6d "
                            "04:10:20"
                        },
                        "send-time": {
                            "#text": "00:00:15"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:b0f8:ca45::14/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x80000246",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2010",
                    "checksum": "0x3ff4",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:26:29"
                        },
                        "database-entry-state": "Ours",
                        "expiration-time": {
                            "#text": "00:26:30"
                        },
                        "generation-timer": {
                            "#text": "00:16:29"
                        },
                        "installation-time": {
                            "#text": "00:33:30"
                        },
                        "lsa-change-count": "2",
                        "lsa-changed-time": {
                            "#text": "3w0d "
                            "17:02:14"
                        },
                        "send-time": {
                            "#text": "00:33:28"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:eb18:ca45::1/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "our-entry": True,
                    "sequence-number": "0x8000063f",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "2012",
                    "checksum": "0x7dcd",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "44",
                    "lsa-type": "Extern",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:26:27"
                        },
                        "expiration-time": {
                            "#text": "00:26:28"
                        },
                        "installation-time": {
                            "#text": "00:33:29"
                        },
                        "lsa-change-count": "15",
                        "lsa-changed-time": {
                            "#text": "3w3d "
                            "00:31:13"
                        },
                        "send-time": {
                            "#text": "00:33:28"
                        },
                    },
                    "ospf3-external-lsa": {
                        "metric": "50",
                        "ospf3-prefix": "2001:db8:eb18:ca45::2/128",
                        "ospf3-prefix-options": "0x0",
                        "type-value": "1",
                    },
                    "sequence-number": "0x80000e1e",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "510",
                    "checksum": "0xae5c",
                    "lsa-id": "0.0.0.2",
                    "lsa-length": "56",
                    "lsa-type": "Link",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:51:29"
                        },
                        "database-entry-state": "Ours",
                        "expiration-time": {
                            "#text": "00:51:30"
                        },
                        "generation-timer": {
                            "#text": "00:41:29"
                        },
                        "installation-time": {
                            "#text": "00:08:30"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:40:56"
                        },
                        "send-time": {
                            "#text": "00:08:28"
                        },
                    },
                    "ospf3-link-lsa": {
                        "linklocal-address": "fe80::250:56ff:fe8d:c829",
                        "ospf3-options": "0x33",
                        "ospf3-prefix": "2001:db8:223c:2c16::/64",
                        "ospf3-prefix-options": "0x0",
                        "prefix-count": "1",
                        "router-priority": "128",
                    },
                    "our-entry": True,
                    "sequence-number": "0x8000178a",
                },
                {
                    "advertising-router": "10.189.5.253",
                    "age": "2512",
                    "checksum": "0x13d7",
                    "lsa-id": "0.0.0.2",
                    "lsa-length": "56",
                    "lsa-type": "Link",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:18:07"
                        },
                        "expiration-time": {
                            "#text": "00:18:08"
                        },
                        "installation-time": {
                            "#text": "00:41:49"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:33:17"
                        },
                    },
                    "ospf3-link-lsa": {
                        "linklocal-address": "fe80::250:56ff:fe8d:53c0",
                        "ospf3-options": "0x33",
                        "ospf3-prefix": "2001:db8:223c:2c16::/64",
                        "ospf3-prefix-options": "0x0",
                        "prefix-count": "1",
                        "router-priority": "128",
                    },
                    "sequence-number": "0x80001787",
                },
                {
                    "advertising-router": "10.169.14.240",
                    "age": "1144",
                    "checksum": "0xbe92",
                    "lsa-id": "0.0.0.3",
                    "lsa-length": "56",
                    "lsa-type": "Link",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:40:56"
                        },
                        "expiration-time": {
                            "#text": "00:40:56"
                        },
                        "installation-time": {
                            "#text": "00:19:01"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:33:04"
                        },
                        "send-time": {
                            "#text": "6w2d "
                            "02:47:58"
                        },
                    },
                    "ospf3-link-lsa": {
                        "linklocal-address": "fe80::250:56ff:fe8d:72bd",
                        "ospf3-options": "0x33",
                        "ospf3-prefix": "2001:db8:eb18:6337::/64",
                        "ospf3-prefix-options": "0x0",
                        "prefix-count": "1",
                        "router-priority": "128",
                    },
                    "sequence-number": "0x8000179e",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "10",
                    "checksum": "0x5e7d",
                    "lsa-id": "0.0.0.3",
                    "lsa-length": "56",
                    "lsa-type": "Link",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:59:49"
                        },
                        "database-entry-state": "Ours",
                        "expiration-time": {
                            "#text": "00:59:50"
                        },
                        "generation-timer": {
                            "#text": "00:49:49"
                        },
                        "installation-time": {
                            "#text": "00:00:10"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:40:56"
                        },
                        "send-time": {
                            "#text": "00:00:08"
                        },
                    },
                    "ospf3-link-lsa": {
                        "linklocal-address": "fe80::250:56ff:fe8d:a96c",
                        "ospf3-options": "0x33",
                        "ospf3-prefix": "2001:db8:eb18:6337::/64",
                        "ospf3-prefix-options": "0x0",
                        "prefix-count": "1",
                        "router-priority": "128",
                    },
                    "our-entry": True,
                    "sequence-number": "0x8000178a",
                },
                {
                    "advertising-router": "10.189.5.252",
                    "age": "2510",
                    "checksum": "0xa440",
                    "lsa-id": "0.0.0.1",
                    "lsa-length": "44",
                    "lsa-type": "Link",
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": "00:18:09"
                        },
                        "database-entry-state": "Ours",
                        "expiration-time": {
                            "#text": "00:18:10"
                        },
                        "generation-timer": {
                            "#text": "00:08:09"
                        },
                        "installation-time": {
                            "#text": "00:41:50"
                        },
                        "lsa-change-count": "1",
                        "lsa-changed-time": {
                            "#text": "29w5d "
                            "21:46:59"
                        },
                    },
                    "ospf3-link-lsa": {
                        "linklocal-address": "fe80::250:560f:fc8d:7c08",
                        "ospf3-options": "0x33",
                        "prefix-count": "0",
                        "router-priority": "128",
                    },
                    "our-entry": True,
                    "sequence-number": "0x8000178b",
                },
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
                },
            ],
        }
    }

    golden_output_2 = {'execute.return_value': """
        show ospf3 database advertising-router 10.16.2.2 extensive

        OSPF3 database, Area 0.0.0.0
            Type       ID               Adv Rtr           Seq         Age  Cksum  Len
            Router      0.0.0.0          10.16.2.2          0x80000002   491  0x549c  40
            bits 0x0, Options 0x33
            Type PointToPoint (1), Metric 1
                Loc-If-Id 1, Nbr-If-Id 1, Nbr-Rtr-Id 10.4.1.1
            Type: PointToPoint, Node ID: 10.4.1.1, Metric: 1, Bidirectional
            Aging timer 00:51:48
            Installed 00:08:08 ago, expires in 00:51:49, sent 00:08:06 ago
            Last changed 00:08:37 ago, Change count: 1
            IntraArPfx  0.0.0.1          10.16.2.2          0x80000003   491  0x991d  64
            Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 10.16.2.2
            Prefix-count 2
            Prefix 2001:20::/64
                Prefix-options 0x0, Metric 1
            Prefix 2001::2/128
                Prefix-options 0x2, Metric 0
            Aging timer 00:51:48
            Installed 00:08:08 ago, expires in 00:51:49, sent 00:08:06 ago
            Last changed 00:08:39 ago, Change count: 1

                OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.0
            Type       ID               Adv Rtr           Seq         Age  Cksum  Len
            Link        0.0.0.1          10.16.2.2          0x80000001   520  0x7045  56
            fe80::250:56ff:fe8d:3f55
            Options 0x33, Priority 128
            Prefix-count 1
            Prefix 2001:20::/64 Prefix-options 0x0
            Aging timer 00:51:19
            Installed 00:08:37 ago, expires in 00:51:20
            Last changed 00:08:37 ago, Change count: 1"""}

    golden_parsed_output_2 = {
        'ospf3-database-information': {
            'ospf3-area-header': {
            'ospf-area': '0.0.0.0'
            },
            'ospf3-database': [{
            'lsa-type': 'Router',
            'lsa-id': '0.0.0.0',
            'advertising-router': '10.16.2.2',
            'sequence-number': '0x80000002',
            'age': '491',
            'checksum': '0x549c',
            'lsa-length': '40',
            'ospf3-router-lsa': {
                'bits': '0x0',
                'ospf3-options': '0x33',
                'ospf3-link': [{
                'link-type-name': 'PointToPoint',
                'link-type-value': '1',
                'link-metric': '1',
                'link-intf-id': '1',
                'nbr-intf-id': '1',
                'nbr-rtr-id': '10.4.1.1'
                }],
                'ospf3-lsa-topology': {
                'ospf-topology-id': '0',
                'ospf-topology-name': 'default',
                'ospf3-lsa-topology-link': [{
                    'link-type-name': 'PointToPoint',
                    'ospf-lsa-topology-link-node-id': '10.4.1.1',
                    'ospf-lsa-topology-link-metric': '1',
                    'ospf-lsa-topology-link-state': 'Bidirectional'
                }]
                }
            },
            'ospf-database-extensive': {
                'aging-timer': {
                '#text': '00:51:48'
                },
                'expiration-time': {
                '#text': '00:51:49'
                },
                'installation-time': {
                '#text': '00:08:08'
                },
                'send-time': {
                '#text': '00:08:06'
                },
                'lsa-changed-time': {
                '#text': '00:08:37'
                },
                'lsa-change-count': '1'
            }
            }, {
            'lsa-type': 'IntraArPfx',
            'lsa-id': '0.0.0.1',
            'advertising-router': '10.16.2.2',
            'sequence-number': '0x80000003',
            'age': '491',
            'checksum': '0x991d',
            'lsa-length': '64',
            'ospf3-intra-area-prefix-lsa': {
                'reference-lsa-type': 'Router',
                'reference-lsa-id': '0.0.0.0',
                'reference-lsa-router-id': '10.16.2.2',
                'prefix-count': '2',
                'ospf3-prefix': ['2001:20::/64', '2001::2/128'],
                'ospf3-prefix-options': ['0x0', '0x2'],
                'ospf3-prefix-metric': ['1', '0']
            },
            'ospf-database-extensive': {
                'aging-timer': {
                '#text': '00:51:48'
                },
                'expiration-time': {
                '#text': '00:51:49'
                },
                'installation-time': {
                '#text': '00:08:08'
                },
                'send-time': {
                '#text': '00:08:06'
                },
                'lsa-changed-time': {
                '#text': '00:08:39'
                },
                'lsa-change-count': '1'
            }
            }, {
            'lsa-type': 'Link',
            'lsa-id': '0.0.0.1',
            'advertising-router': '10.16.2.2',
            'sequence-number': '0x80000001',
            'age': '520',
            'checksum': '0x7045',
            'lsa-length': '56',
            'ospf3-link-lsa': {
                'linklocal-address': 'fe80::250:56ff:fe8d:3f55',
                'ospf3-options': '0x33',
                'router-priority': '128',
                'prefix-count': '1',
                'ospf3-prefix': '2001:20::/64',
                'ospf3-prefix-options': '0x0'
            },
            'ospf-database-extensive': {
                'aging-timer': {
                '#text': '00:51:19'
                },
                'expiration-time': {
                '#text': '00:51:20'
                },
                'installation-time': {
                '#text': '00:08:37'
                },
                'lsa-changed-time': {
                '#text': '00:08:37'
                },
                'lsa-change-count': '1'
            }
            }],
            'ospf3-intf-header': [{
            'ospf-intf': 'ge-0/0/0.0',
            'ospf-area': '0.0.0.0'
            }]
        }
        }

    golden_output_3 = {'execute.return_value': """
        show ospf3 database router advertising-router 10.16.2.2 extensive

            OSPF3 database, Area 0.0.0.0
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Router      0.0.0.0          10.16.2.2          0x80000002   823  0x549c  40
        bits 0x0, Options 0x33
        Type PointToPoint (1), Metric 1
            Loc-If-Id 1, Nbr-If-Id 1, Nbr-Rtr-Id 10.4.1.1
        Type: PointToPoint, Node ID: 10.4.1.1, Metric: 1, Bidirectional
        Aging timer 00:46:16
        Installed 00:13:40 ago, expires in 00:46:17, sent 00:13:38 ago
        Last changed 00:14:09 ago, Change count: 1"""}

    golden_parsed_output_3 = {
        'ospf3-database-information': {
            'ospf3-area-header': {
            'ospf-area': '0.0.0.0'
            },
            'ospf3-database': [{
            'lsa-type': 'Router',
            'lsa-id': '0.0.0.0',
            'advertising-router': '10.16.2.2',
            'sequence-number': '0x80000002',
            'age': '823',
            'checksum': '0x549c',
            'lsa-length': '40',
            'ospf3-router-lsa': {
                'bits': '0x0',
                'ospf3-options': '0x33',
                'ospf3-link': [{
                'link-type-name': 'PointToPoint',
                'link-type-value': '1',
                'link-metric': '1',
                'link-intf-id': '1',
                'nbr-intf-id': '1',
                'nbr-rtr-id': '10.4.1.1'
                }],
                'ospf3-lsa-topology': {
                'ospf-topology-id': '0',
                'ospf-topology-name': 'default',
                'ospf3-lsa-topology-link': [{
                    'link-type-name': 'PointToPoint',
                    'ospf-lsa-topology-link-node-id': '10.4.1.1',
                    'ospf-lsa-topology-link-metric': '1',
                    'ospf-lsa-topology-link-state': 'Bidirectional'
                }]
                }
            },
            'ospf-database-extensive': {
                'aging-timer': {
                '#text': '00:46:16'
                },
                'expiration-time': {
                '#text': '00:46:17'
                },
                'installation-time': {
                '#text': '00:13:40'
                },
                'send-time': {
                '#text': '00:13:38'
                },
                'lsa-changed-time': {
                '#text': '00:14:09'
                },
                'lsa-change-count': '1'
            }
            }]
        }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3DatabaseExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3DatabaseExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowOspf3DatabaseExtensive(device=self.device)
        parsed_output = obj.parse(address='10.16.2.2')

        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowOspf3DatabaseExtensive(device=self.device)
        parsed_output = obj.parse(address='10.16.2.2', lsa_type='router')

        self.assertEqual(parsed_output, self.golden_parsed_output_3)


class TestShowOspf3DatabaseNetworkDetail(unittest.TestCase):
    """ Unit tests for:
            * show ospf3 database network detail
    """

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {
        'execute.return_value':
        '''
        show ospf3 database network detail

        OSPF3 database, Area 0.0.0.0
      Type       ID               Adv Rtr           Seq         Age  Cksum  Len
    Network    *0.0.0.9          192.168.219.235   0x8000001d   892  0xf99f  36
      Options 0x33
      Attached router 192.168.219.235
      Attached router 10.69.198.249
      Attached router 192.168.219.236
      Type: Transit, Node ID: 192.168.219.236, Metric: 0, Bidirectional
      Type: Transit, Node ID: 10.69.198.249, Metric: 0, Bidirectional
      Type: Transit, Node ID: 192.168.219.235, Metric: 0, Bidirectional
    Network     0.0.0.3          192.168.219.236   0x80000b14  2142  0x1983  36
      Options 0x33
      Attached router 192.168.219.236
      Attached router 10.69.198.249
      Attached router 192.168.219.235
      Type: Transit, Node ID: 192.168.219.235, Metric: 0, Bidirectional
      Type: Transit, Node ID: 10.69.198.249, Metric: 0, Bidirectional
      Type: Transit, Node ID: 192.168.219.236, Metric: 0, Bidirectional
    Network     0.0.0.4          192.168.219.236   0x80000b11  1092  0xa3d1  32
      Options 0x33
      Attached router 192.168.219.236
      Attached router 192.168.219.235
      Type: Transit, Node ID: 192.168.219.235, Metric: 0, Bidirectional
      Type: Transit, Node ID: 192.168.219.236, Metric: 0, Bidirectional
    Network     0.0.0.6          192.168.219.236   0x80000b11  1692  0x8fe3  32
      Options 0x33
      Attached router 192.168.219.236
      Attached router 192.168.219.235
      Type: Transit, Node ID: 192.168.219.235, Metric: 0, Bidirectional
      Type: Transit, Node ID: 192.168.219.236, Metric: 0, Bidirectional
    '''
    }

    golden_parsed_output = {
        "ospf3-database-information": {
            "ospf3-area-header": {
                "ospf-area": "0.0.0.0"
            },
            "ospf3-database": [{
                "advertising-router": "192.168.219.235",
                "age": "892",
                "checksum": "0xf99f",
                "lsa-id": "0.0.0.9",
                "lsa-length": "36",
                "lsa-type": "Network",
                "ospf3-network-lsa": {
                    "attached-router":
                    ["192.168.219.235", "10.69.198.249", "192.168.219.236"],
                    "ospf3-lsa-topology": {
                        "ospf3-lsa-topology-link": [{
                            "link-type-name":
                            "Transit",
                            "ospf-lsa-topology-link-metric":
                            "0",
                            "ospf-lsa-topology-link-node-id":
                            "192.168.219.236",
                            "ospf-lsa-topology-link-state":
                            "Bidirectional"
                        }, {
                            "link-type-name":
                            "Transit",
                            "ospf-lsa-topology-link-metric":
                            "0",
                            "ospf-lsa-topology-link-node-id":
                            "10.69.198.249",
                            "ospf-lsa-topology-link-state":
                            "Bidirectional"
                        }, {
                            "link-type-name":
                            "Transit",
                            "ospf-lsa-topology-link-metric":
                            "0",
                            "ospf-lsa-topology-link-node-id":
                            "192.168.219.235",
                            "ospf-lsa-topology-link-state":
                            "Bidirectional"
                        }]
                    },
                    "ospf3-options":
                    "0x33"
                },
                "our-entry": True,
                "sequence-number": "0x8000001d"
            }, {
                "advertising-router": "192.168.219.236",
                "age": "2142",
                "checksum": "0x1983",
                "lsa-id": "0.0.0.3",
                "lsa-length": "36",
                "lsa-type": "Network",
                "ospf3-network-lsa": {
                    "attached-router":
                    ["192.168.219.236", "10.69.198.249", "192.168.219.235"],
                    "ospf3-lsa-topology": {
                        "ospf3-lsa-topology-link": [{
                            "link-type-name":
                            "Transit",
                            "ospf-lsa-topology-link-metric":
                            "0",
                            "ospf-lsa-topology-link-node-id":
                            "192.168.219.235",
                            "ospf-lsa-topology-link-state":
                            "Bidirectional"
                        }, {
                            "link-type-name":
                            "Transit",
                            "ospf-lsa-topology-link-metric":
                            "0",
                            "ospf-lsa-topology-link-node-id":
                            "10.69.198.249",
                            "ospf-lsa-topology-link-state":
                            "Bidirectional"
                        }, {
                            "link-type-name":
                            "Transit",
                            "ospf-lsa-topology-link-metric":
                            "0",
                            "ospf-lsa-topology-link-node-id":
                            "192.168.219.236",
                            "ospf-lsa-topology-link-state":
                            "Bidirectional"
                        }]
                    },
                    "ospf3-options":
                    "0x33"
                },
                "sequence-number": "0x80000b14"
            }, {
                "advertising-router": "192.168.219.236",
                "age": "1092",
                "checksum": "0xa3d1",
                "lsa-id": "0.0.0.4",
                "lsa-length": "32",
                "lsa-type": "Network",
                "ospf3-network-lsa": {
                    "attached-router": ["192.168.219.236", "192.168.219.235"],
                    "ospf3-lsa-topology": {
                        "ospf3-lsa-topology-link": [{
                            "link-type-name":
                            "Transit",
                            "ospf-lsa-topology-link-metric":
                            "0",
                            "ospf-lsa-topology-link-node-id":
                            "192.168.219.235",
                            "ospf-lsa-topology-link-state":
                            "Bidirectional"
                        }, {
                            "link-type-name":
                            "Transit",
                            "ospf-lsa-topology-link-metric":
                            "0",
                            "ospf-lsa-topology-link-node-id":
                            "192.168.219.236",
                            "ospf-lsa-topology-link-state":
                            "Bidirectional"
                        }]
                    },
                    "ospf3-options": "0x33"
                },
                "sequence-number": "0x80000b11"
            }, {
                "advertising-router": "192.168.219.236",
                "age": "1692",
                "checksum": "0x8fe3",
                "lsa-id": "0.0.0.6",
                "lsa-length": "32",
                "lsa-type": "Network",
                "ospf3-network-lsa": {
                    "attached-router": ["192.168.219.236", "192.168.219.235"],
                    "ospf3-lsa-topology": {
                        "ospf3-lsa-topology-link": [{
                            "link-type-name":
                            "Transit",
                            "ospf-lsa-topology-link-metric":
                            "0",
                            "ospf-lsa-topology-link-node-id":
                            "192.168.219.235",
                            "ospf-lsa-topology-link-state":
                            "Bidirectional"
                        }, {
                            "link-type-name":
                            "Transit",
                            "ospf-lsa-topology-link-metric":
                            "0",
                            "ospf-lsa-topology-link-node-id":
                            "192.168.219.236",
                            "ospf-lsa-topology-link-state":
                            "Bidirectional"
                        }]
                    },
                    "ospf3-options": "0x33"
                },
                "sequence-number": "0x80000b11"
            }]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3DatabaseNetworkDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3DatabaseNetworkDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspf3DatabaseLinkAdvertisingRouter(unittest.TestCase):
    """ Unit tests for:
            * show ospf3 database link advertising-router {ipaddress} detail
    """

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {
        'execute.return_value':
        '''
        show ospf3 database link advertising-router 192.168.219.235 detail

        OSPF3 Link-Local database, interface ge-0/0/2.0 Area 0.0.0.0
    Type       ID               Adv Rtr           Seq         Age  Cksum  Len
    Link       *0.0.0.9          192.168.219.235   0x80000b10  1379  0xd3b0  56
    fe80::20c:2900:3367:243d
    Options 0x33, Priority 20
    Prefix-count 1
    Prefix 2001:db8:dae9:cf16::/64 Prefix-options 0x0

        OSPF3 Link-Local database, interface ge-0/0/2.1 Area 0.0.0.0
    Type       ID               Adv Rtr           Seq         Age  Cksum  Len
    Link       *0.0.0.10         192.168.219.235   0x80000b0f  1979  0x974d  56
    fe80::20c:2900:3467:243d
    Options 0x33, Priority 128
    Prefix-count 1
    Prefix 2001:db8:dae9:c9df::/64 Prefix-options 0x0

        OSPF3 Link-Local database, interface ge-0/0/3.0 Area 0.0.0.0
    Type       ID               Adv Rtr           Seq         Age  Cksum  Len
    Link       *0.0.0.11         192.168.219.235   0x80000b0f  1829  0x94c2  56
    fe80::20c:2900:3667:2465
    Options 0x33, Priority 20
    Prefix-count 1
    Prefix 2001:db8:dae9:d3e9::/64 Prefix-options 0x0

        OSPF3 Link-Local database, interface ge-0/0/3.1 Area 0.0.0.0
    Type       ID               Adv Rtr           Seq         Age  Cksum  Len
    Link       *0.0.0.12         192.168.219.235   0x80000b0f  1679  0x5660  56
    fe80::20c:2900:3767:2465
    Options 0x33, Priority 128
    Prefix-count 1
    Prefix 2001:db8:dae9:cf16::/64 Prefix-options 0x0

        OSPF3 Link-Local database, interface lo0.0 Area 0.0.0.0
    Type       ID               Adv Rtr           Seq         Age  Cksum  Len
    Link       *0.0.0.7          192.168.219.235   0x80000f62  2729  0xd0a6  44
    fe80::20c:290f:fc40:a033
    Options 0x33, Priority 128
    Prefix-count 0
    '''
    }

    golden_parsed_output = {
        "ospf3-database-information": {
            "ospf3-database": [{
                "@heading":
                "Type       ID               Adv Rtr           Seq         Age  Cksum  Len",
                "advertising-router": "192.168.219.235",
                "age": "1379",
                "checksum": "0xd3b0",
                "lsa-id": "0.0.0.9",
                "lsa-length": "56",
                "lsa-type": "Link",
                "ospf3-link-lsa": {
                    "linklocal-address": "fe80::20c:2900:3367:243d",
                    "ospf3-options": "0x33",
                    "ospf3-prefix": "2001:db8:dae9:cf16::/64",
                    "ospf3-prefix-options": "0x0",
                    "prefix-count": "1",
                    "router-priority": "20"
                },
                "our-entry": True,
                "sequence-number": "0x80000b10"
            }, {
                "@heading":
                "Type       ID               Adv Rtr           Seq         Age  Cksum  Len",
                "advertising-router": "192.168.219.235",
                "age": "1979",
                "checksum": "0x974d",
                "lsa-id": "0.0.0.10",
                "lsa-length": "56",
                "lsa-type": "Link",
                "ospf3-link-lsa": {
                    "linklocal-address": "fe80::20c:2900:3467:243d",
                    "ospf3-options": "0x33",
                    "ospf3-prefix": "2001:db8:dae9:c9df::/64",
                    "ospf3-prefix-options": "0x0",
                    "prefix-count": "1",
                    "router-priority": "128"
                },
                "our-entry": True,
                "sequence-number": "0x80000b0f"
            }, {
                "@heading":
                "Type       ID               Adv Rtr           Seq         Age  Cksum  Len",
                "advertising-router": "192.168.219.235",
                "age": "1829",
                "checksum": "0x94c2",
                "lsa-id": "0.0.0.11",
                "lsa-length": "56",
                "lsa-type": "Link",
                "ospf3-link-lsa": {
                    "linklocal-address": "fe80::20c:2900:3667:2465",
                    "ospf3-options": "0x33",
                    "ospf3-prefix": "2001:db8:dae9:d3e9::/64",
                    "ospf3-prefix-options": "0x0",
                    "prefix-count": "1",
                    "router-priority": "20"
                },
                "our-entry": True,
                "sequence-number": "0x80000b0f"
            }, {
                "@heading":
                "Type       ID               Adv Rtr           Seq         Age  Cksum  Len",
                "advertising-router": "192.168.219.235",
                "age": "1679",
                "checksum": "0x5660",
                "lsa-id": "0.0.0.12",
                "lsa-length": "56",
                "lsa-type": "Link",
                "ospf3-link-lsa": {
                    "linklocal-address": "fe80::20c:2900:3767:2465",
                    "ospf3-options": "0x33",
                    "ospf3-prefix": "2001:db8:dae9:cf16::/64",
                    "ospf3-prefix-options": "0x0",
                    "prefix-count": "1",
                    "router-priority": "128"
                },
                "our-entry": True,
                "sequence-number": "0x80000b0f"
            }, {
                "@heading":
                "Type       ID               Adv Rtr           Seq         Age  Cksum  Len",
                "advertising-router": "192.168.219.235",
                "age": "2729",
                "checksum": "0xd0a6",
                "lsa-id": "0.0.0.7",
                "lsa-length": "44",
                "lsa-type": "Link",
                "ospf3-link-lsa": {
                    "linklocal-address": "fe80::20c:290f:fc40:a033",
                    "ospf3-options": "0x33",
                    "prefix-count": "0",
                    "router-priority": "128"
                },
                "our-entry": True,
                "sequence-number": "0x80000f62"
            }],
            "ospf3-intf-header": [{
                "ospf-area": "0.0.0.0",
                "ospf-intf": "ge-0/0/2.0"
            }, {
                "ospf-area": "0.0.0.0",
                "ospf-intf": "ge-0/0/2.1"
            }, {
                "ospf-area": "0.0.0.0",
                "ospf-intf": "ge-0/0/3.0"
            }, {
                "ospf-area": "0.0.0.0",
                "ospf-intf": "ge-0/0/3.1"
            }, {
                "ospf-area": "0.0.0.0",
                "ospf-intf": "lo0.0"
            }]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3DatabaseLinkAdvertisingRouter(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(ipaddress='192.168.219.235')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3DatabaseLinkAdvertisingRouter(device=self.device)
        parsed_output = obj.parse(ipaddress='192.168.219.235')
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspf3RouteNetworkExtensive(unittest.TestCase):
    """ Unit tests for:
            * show ospf3 route network extensive
    """

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {
        'execute.return_value':
        '''
        show ospf3 route network extensive
        Prefix                                       Path  Route      NH   Metric
                                             Type  Type       Type
        2001::4/128                                  Intra Network    IP   0
        NH-interface lo0.0
        Area 0.0.0.0, Origin 10.64.4.4, Priority low
    '''
    }

    golden_parsed_output = {
        "ospf3-route-information": {
        "ospf-topology-route-table": {
            "ospf3-route": [{
                "ospf3-route-entry": {
                    "address-prefix": "2001::4/128",
                    "interface-cost": "0",
                    "next-hop-type": "IP",
                    "ospf-area": "0.0.0.0",
                    "ospf-next-hop": {
                        "next-hop-name": {
                            "interface-name": "lo0.0"
                        }
                    },
                    "route-origin": "10.64.4.4",
                    "route-path-type": "Intra",
                    "route-priority": "low",
                    "route-type": "Network"
                }
            }]
        }
    }
        
    }

    golden_output2 = {
        'execute.return_value':
        '''
        show ospf3 route network extensive
        Prefix                                       Path  Route      NH   Metric
                                             Type  Type       Type
        2001::1/128                                  Intra Network    IP   0
        NH-interface lo0.0
        Area 0.0.0.0, Origin 10.4.1.1, Priority low
        2001::4/128                                  Intra Network    IP   1
        NH-interface ge-0/0/0.0, NH-addr fe80::250:56ff:fe8d:e8e8
        Area 0.0.0.0, Origin 10.64.4.4, Priority medium
        2001:30::/64                                 Intra Network    IP   1
        NH-interface ge-0/0/1.0
        Area 0.0.0.0, Origin 10.4.1.1, Priority low
        2001:40::/64                                 Intra Network    IP   1
        NH-interface ge-0/0/0.0
        Area 0.0.0.0, Origin 10.64.4.4, Priority low
        2001:50::/64                                 Intra Network    IP   2
        NH-interface ge-0/0/0.0, NH-addr fe80::250:56ff:fe8d:e8e8
        Area 0.0.0.0, Origin 10.64.4.4, Priority medium
    '''
    }

    golden_parsed_output2 = {
        "ospf3-route-information": {
        "ospf-topology-route-table": {
            "ospf3-route": [
                {
                    "ospf3-route-entry": {
                        "address-prefix": "2001::1/128",
                        "interface-cost": "0",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-name": {
                                "interface-name": "lo0.0"
                            }
                        },
                        "route-origin": "10.4.1.1",
                        "route-path-type": "Intra",
                        "route-priority": "low",
                        "route-type": "Network"
                    }
                },
                {
                    "ospf3-route-entry": {
                        "address-prefix": "2001::4/128",
                        "interface-cost": "1",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "route-origin": "10.64.4.4",
                        "route-path-type": "Intra",
                        "route-priority": "medium",
                        "route-type": "Network"
                    }
                },
                {
                    "ospf3-route-entry": {
                        "address-prefix": "2001:30::/64",
                        "interface-cost": "1",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-name": {
                                "interface-name": "ge-0/0/1.0"
                            }
                        },
                        "route-origin": "10.4.1.1",
                        "route-path-type": "Intra",
                        "route-priority": "low",
                        "route-type": "Network"
                    }
                },
                {
                    "ospf3-route-entry": {
                        "address-prefix": "2001:40::/64",
                        "interface-cost": "1",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "ospf-next-hop": {
                            "next-hop-name": {
                                "interface-name": "ge-0/0/0.0"
                            }
                        },
                        "route-origin": "10.64.4.4",
                        "route-path-type": "Intra",
                        "route-priority": "low",
                        "route-type": "Network"
                    }
                },
                {
                    "ospf3-route-entry": {
                        "address-prefix": "2001:50::/64",
                        "interface-cost": "2",
                        "next-hop-type": "IP",
                        "ospf-area": "0.0.0.0",
                        "route-origin": "10.64.4.4",
                        "route-path-type": "Intra",
                        "route-priority": "medium",
                        "route-type": "Network"
                    }
                }
            ]
        }
    }
        
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3RouteNetworkExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3RouteNetworkExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowOspf3RouteNetworkExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


if __name__ == '__main__':
    unittest.main()