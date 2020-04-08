import unittest
from unittest.mock import Mock

from pyats.topology import Device
from pyats.topology import loader
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ospf3 import ShowOspf3Interface, \
                                               ShowOspf3NeighborExtensive, \
                                               ShowOspf3NeighborDetail, \
                                               ShowOspf3Neighbor

class TestShowOspf3Interface(unittest.TestCase):

    device = Device(name='aDevice')

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

if __name__ == '__main__':
    unittest.main()