# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.show_segment_routing import (ShowSegmentRoutingMplsLB,
                                                          ShowSegmentRoutingMplsState,
                                                          ShowSegmentRoutingMplsLbLock,
                                                          ShowSegmentRoutingMplsConnectedPrefixSidMap,
                                                          ShowSegmentRoutingMplsGb,
                                                          ShowSegmentRoutingMplsGbLock,
                                                          ShowSegmentRoutingMplsConnectedPrefixSidMapLocal,
                                                          ShowSegmentRoutingTrafficEngPolicy)


# =============================================================
# Unittest for:
#   * 'show segment-routing mpls connected-prefix-sid-map ipv4'
# =============================================================
class test_show_routing_mpls_connected_prefix_sid_map(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output1 = {
        'segment_routing': {
            'bindings': {
                'local_prefix_sid': {
                    'ipv4': {
                        'ipv4_prefix_sid_local': {
                            '10.4.1.1/32': {
                                'algorithm': {
                                    'ALGO_0': {
                                        'prefix': '10.4.1.1/32',
                                        'algorithm': 'ALGO_0',
                                        'value_type': 'Indx',
                                        'sid': '1',
                                        'range': '1',
                                        'srgb': 'Y',
                                        },
                                    },
                                },
                            },
                        },
                    },
                'connected_prefix_sid_map': {
                    'ipv4': {
                        'ipv4_prefix_sid': {
                            '10.4.1.1/32': {
                                'algorithm': {
                                    'ALGO_0': {
                                        'prefix': '10.4.1.1/32',
                                        'algorithm': 'ALGO_0',
                                        'value_type': 'Indx',
                                        'sid': '1',
                                        'range': '1',
                                        'srgb': 'Y',
                                        'source': 'OSPF Area 8 10.4.1.1',
                                        },
                                    },
                                },
                            '10.16.2.2/32': {
                                'algorithm': {
                                    'ALGO_0': {
                                        'prefix': '10.16.2.2/32',
                                        'algorithm': 'ALGO_0',
                                        'value_type': 'Indx',
                                        'sid': '2',
                                        'range': '1',
                                        'srgb': 'Y',
                                        'source': 'OSPF Area 8 10.16.2.2',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output1 = {'execute.return_value': '''
        PE1#show segment-routing mpls connected-prefix-sid-map ipv4
 
                       PREFIX_SID_CONN_MAP ALGO_0
         
            Prefix/masklen   SID Type Range Flags SRGB
                10.4.1.1/32     1 Indx     1         Y
         
                       PREFIX_SID_PROTOCOL_ADV_MAP ALGO_0
         
            Prefix/masklen   SID Type Range Flags SRGB Source
                10.4.1.1/32     1 Indx     1         Y  OSPF Area 8 10.4.1.1
                10.16.2.2/32     2 Indx     1         Y  OSPF Area 8 10.16.2.2
         
                       PREFIX_SID_CONN_MAP ALGO_1
         
            Prefix/masklen   SID Type Range Flags SRGB
         
                       PREFIX_SID_PROTOCOL_ADV_MAP ALGO_1
         
            Prefix/masklen   SID Type Range Flags SRGB Source
        PE1#
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsConnectedPrefixSidMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(address_family='ipv4')

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowSegmentRoutingMplsConnectedPrefixSidMap(device=self.device)
        parsed_output = obj.parse(address_family='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)


# ==================================
# Unittest for:
#   * 'show segment-routing mpls gb'
# ==================================
class test_show_routing_mpls_gb(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output1 = {
        'default': 'Yes',
        'label_max': 23999,
        'label_min': 16000,
        'state': 'ENABLED'}

    golden_output1 = {'execute.return_value': '''
        PE1#show segment-routing mpls gb
        LABEL-MIN  LABEL_MAX  STATE           DEFAULT   
        16000      23999      ENABLED         Yes       
        PE1#
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsGb(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowSegmentRoutingMplsGb(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


# ==================================
# Unittest for:
#   * 'show segment-routing mpls lb'
# ==================================
class test_show_routing_mpls_lb(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'label_min': 15000,
        'label_max': 15999,
        'state': 'ENABLED',
        'default': 'Yes',
    }

    golden_output = {'execute.return_value': '''
        show segment-routing mpls lb
        LABEL-MIN  LABEL_MAX  STATE           DEFAULT
        15000      15999      ENABLED         Yes
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsLB(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMplsLB(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# =====================================
# Unittest for:
#   * 'show segment-routing mpls state'
# =====================================
class test_show_routing_mpls_state(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'sr_mpls_state': "ENABLED",
    }

    golden_output = {'execute.return_value': '''
        Device#show segment-routing mpls state
        Segment Routing MPLS State : ENABLED
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsState(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMplsState(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ==============================================
# Parser for 'show segment-routing mpls lb lock'
# ==============================================
class test_show_routing_mpls_lb_lock(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'label_min': 15000,
        'label_max': 15999
    }

    golden_output = {'execute.return_value': '''
        show segment-routing mpls lb lock
        SR LB (15000, 15999) Lock Users :
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsLbLock(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMplsLbLock(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ==================================================
# Unit tests for 'show segment-routing mpls gb lock'
# ==================================================
class test_show_segment_routing_mpls_gb_lock(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show segment-routing mpls gb lock
        SR GB (9000, 10000) Lock Users :
    '''}

    golden_parsed_output = {
        'label_min': 9000,
        'label_max': 10000
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsGbLock(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMplsGbLock(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ====================================================================
# Unittest for:
#   * 'show segment-routing mpls connected-prefix-sid-map local ipv4'
#   * 'show segment-routing mpls connected-prefix-sid-map local ipv6'
# ====================================================================
class test_show_routing_mpls_connected_prefix_sid_map_local(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output1 = {
        'segment_routing': {
            'bindings': {
                'local_prefix_sid': {
                    'ipv4': {
                        'ipv4_prefix_sid_local': {
                            '10.4.1.1/32': {
                                'algorithm': {
                                    'ALGO_0': {
                                        'prefix': '10.4.1.1/32',
                                        'algorithm': 'ALGO_0',
                                        'value_type': 'Indx',
                                        'sid': '1',
                                        'range': '1',
                                        'srgb': 'Y',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output1 = {'execute.return_value': '''
        show segment-routing mpls connected-prefix-sid-map local ipv4

               PREFIX_SID_CONN_MAP ALGO_0

        Prefix/masklen   SID Type Range Flags SRGB
            10.4.1.1/32     1 Indx     1         Y

                PREFIX_SID_CONN_MAP ALGO_1

        Prefix/masklen   SID Type Range Flags SRGB
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsConnectedPrefixSidMapLocal(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(address_family='ipv4')

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowSegmentRoutingMplsConnectedPrefixSidMapLocal(device=self.device)
        parsed_output = obj.parse(address_family='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)


# ====================================================================
# Unittest for:
#   * 'show segment-routing traffic-eng policy all'
# ====================================================================
class test_show_segment_routing_traffic_eng_policy(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "test1": {
            "name": "test1",
            "color": 100,
            "end_point": "106.162.196.241",
            "admin_status": "up",
            "oper_status": "up",
            "start": "since 08-28 20:56:55.275",
            "up_time": "09:38:18",
            "candidate_paths": {
                400: {
                    "preference": 400,
                    "dynamic": "(pce) (inactive)",
                    "weight": 0,
                    "metric_type": "TE"
                },
                300: {
                    "preference": 300,
                    "dynamic": "(active)",
                    "weight": 0,
                    "metric_type": "IGP",
                    "path_accumulated_metric": 2200,
                    "prefix_sid": {
                        16063: "106.162.196.241"
                    }
                },
                200: {
                    "preference": 200,
                    "explicit": "segment-list test1 (inactive)",
                    "weight": 0,
                    "metric_type": "TE",
                    "prefix_sid": {
                        16072: "111.87.5.253",
                        16052: "106.187.14.241",
                        16062: "59.128.2.251",
                        16063: "106.162.196.241"
                    }
                },
                100: {
                    "preference": 100,
                    "dynamic": "(inactive)",
                    "weight": 0,
                    "metric_type": "IGP",
                    "path_accumulated_metric": 2200,
                    "prefix_sid": {
                        16063: "106.162.196.241"
                    }
                }
            },
            "attributes": {
                "binding_sid": 15000,
                "allocation_mode": "explicit",
                "state": "Programmed"
            }
        }
    }

    golden_output = {'execute.return_value': '''
        # show segment-routing traffic-eng policy all
        Name: test1 (Color: 100 End-point: 106.162.196.241)
        Status:
            Admin: up, Operational: up for 09:38:18 (since 08-28 20:56:55.275)
        Candidate-paths:
            Preference 400:
            Dynamic (pce) (inactive)
                Weight: 0, Metric Type: TE
            Preference 300:
            Dynamic (active)
                Weight: 0, Metric Type: IGP
                Metric Type: IGP, Path Accumulated Metric: 2200
                16063 [Prefix-SID, 106.162.196.241]
            Preference 200:
            Explicit: segment-list test1 (inactive)
                Weight: 0, Metric Type: TE
                16072 [Prefix-SID, 111.87.5.253]
                16052 [Prefix-SID, 106.187.14.241]
                16062 [Prefix-SID, 59.128.2.251]
                16063 [Prefix-SID, 106.162.196.241]
            Preference 100:
            Dynamic (inactive)
                Weight: 0, Metric Type: IGP
                Metric Type: IGP, Path Accumulated Metric: 2200
                16063 [Prefix-SID, 106.162.196.241]
        Attributes:
            Binding SID: 15000
            Allocation mode: explicit
            State: Programmed
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingTrafficEngPolicy(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingTrafficEngPolicy(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_name(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingTrafficEngPolicy(device=self.device)
        parsed_output = obj.parse(name='test1')
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()