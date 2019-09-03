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
                                                          ShowSegmentRoutingTrafficEngPolicy,
                                                          ShowSegmentRoutingTrafficEngTopology,
                                                          ShowSegmentRoutingMplsMappingServer)


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


# =============================================================
# Unittest for:
#   * 'show segment-routing traffic-eng topology ipv4'
# =============================================================
class test_show_segment_routing_traffic_eng_topology(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'nodes': {
            1: {
                'ospf_router_id': '10.19.198.239',
                'area_id': 8,
                'domain_id': 0,
                'asn': 65109,
                'prefix_sid': {
                    'prefix': '10.19.198.239',
                    'label': 16073,
                    'label_type': 'regular',
                    'domain_id': 0,
                    'flags': 'N , E',
                },
                'links': {
                    0: {
                        'local_address': '10.19.198.26',
                        'remote_address': '10.19.198.25',
                        'local_node': {
                            'ospf_router_id': '10.19.198.239',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'remote_node': {
                            'ospf_router_id': '10.189.5.252',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'metric': {
                            'igp': 1000,
                            'te': 1000,
                            'delay': 1000,
                        },
                        'bandwidth_total': 125000000,
                        'bandwidth_reservable': 0,
                        'admin_groups': '0x00000000',
                        'adj_sid': {
                            '18': 'unprotected',
                            '36': 'protected',
                        },
                    },
                    1: {
                        'local_address': '10.19.198.30',
                        'remote_address': '10.19.198.29',
                        'local_node': {
                            'ospf_router_id': '10.19.198.239',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'remote_node': {
                            'ospf_router_id': '10.189.5.253',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'metric': {
                            'igp': 1000,
                            'te': 1000,
                            'delay': 1000,
                        },
                        'bandwidth_total': 125000000,
                        'bandwidth_reservable': 0,
                        'admin_groups': '0x00000000',
                        'adj_sid': {
                            '37': 'unprotected',
                            '38': 'protected',
                        },
                    },
                },
            },
            2: {
                'ospf_router_id': '10.189.5.252',
                'area_id': 8,
                'domain_id': 0,
                'asn': 65109,
                'prefix_sid': {
                    'prefix': '10.189.5.252',
                    'label': 16071,
                    'label_type': 'regular',
                    'domain_id': 0,
                    'flags': 'N',
                },
                'links': {
                    0: {
                        'local_address': '10.19.198.25',
                        'remote_address': '10.19.198.26',
                        'local_node': {
                            'ospf_router_id': '10.189.5.252',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'remote_node': {
                            'ospf_router_id': '10.19.198.239',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'metric': {
                            'igp': 1000,
                            'te': 1000,
                            'delay': 1000,
                        },
                        'bandwidth_total': 125000000,
                        'bandwidth_reservable': 125000000,
                        'admin_groups': '0x00000000',
                        'adj_sid': {
                            '24': 'protected',
                        },
                    },
                    1: {
                        'local_address': '10.169.14.122',
                        'remote_address': '10.169.14.121',
                        'local_node': {
                            'ospf_router_id': '10.189.5.252',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'remote_node': {
                            'ospf_router_id': '10.169.14.240',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'metric': {
                            'igp': 100,
                            'te': 100,
                            'delay': 100,
                        },
                        'bandwidth_total': 125000000,
                        'bandwidth_reservable': 125000000,
                        'admin_groups': '0x00000000',
                        'adj_sid': {
                            '16': 'protected',
                        },
                    },
                    2: {
                        'local_address': '10.189.5.93',
                        'remote_address': '10.189.5.94',
                        'local_node': {
                            'ospf_router_id': '10.189.5.252',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'remote_node': {
                            'ospf_router_id': '10.189.5.253',
                            'area_id': 8,
                            'domain_id': 0,
                            'asn': 65109,
                        },
                        'metric': {
                            'igp': 5,
                            'te': 5,
                            'delay': 5,
                        },
                        'bandwidth_total': 125000000,
                        'bandwidth_reservable': 125000000,
                        'admin_groups': '0x00000000',
                        'adj_sid': {
                            '19': 'protected',
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
        show segment-routing traffic-eng topology ipv4
        Node 1:
            TE router ID: 10.19.198.239
            OSPF router ID: 10.19.198.239 area ID: 8 domain ID: 0 ASN: 65109
            Prefix SID:
                Prefix 10.19.198.239, label 16073 (regular), domain ID 0, flags: N , E
            Link[0]: local address 10.19.198.26, remote address 10.19.198.25
                Local node:
                OSPF router ID: 10.19.198.239 area ID: 8 domain ID: 0 ASN: 65109
                Remote node:
                TE router ID: 10.189.5.252
                OSPF router ID: 10.189.5.252 area ID: 8 domain ID: 0 ASN: 65109
                Metric: IGP 1000, TE 1000, Delay 1000
                Bandwidth: Total 125000000, Reservable 0
                Admin-groups: 0x00000000
                Adj SID: 18 (unprotected)  36 (protected)
            Link[1]: local address 10.19.198.30, remote address 10.19.198.29
                Local node:
                OSPF router ID: 10.19.198.239 area ID: 8 domain ID: 0 ASN: 65109
                Remote node:
                TE router ID: 10.189.5.253
                OSPF router ID: 10.189.5.253 area ID: 8 domain ID: 0 ASN: 65109
                Metric: IGP 1000, TE 1000, Delay 1000
                Bandwidth: Total 125000000, Reservable 0
                Admin-groups: 0x00000000
                Adj SID: 37 (unprotected)  38 (protected)

        Node 2:
            TE router ID: 10.189.5.252
            OSPF router ID: 10.189.5.252 area ID: 8 domain ID: 0 ASN: 65109
            Prefix SID:
                Prefix 10.189.5.252, label 16071 (regular), domain ID 0, flags: N
            Link[0]: local address 10.19.198.25, remote address 10.19.198.26
                Local node:
                OSPF router ID: 10.189.5.252 area ID: 8 domain ID: 0 ASN: 65109
                Remote node:
                TE router ID: 10.19.198.239
                OSPF router ID: 10.19.198.239 area ID: 8 domain ID: 0 ASN: 65109
                Metric: IGP 1000, TE 1000, Delay 1000
                Bandwidth: Total 125000000, Reservable 125000000
                Admin-groups: 0x00000000
                Adj SID: 24 (protected)
            Link[1]: local address 10.169.14.122, remote address 10.169.14.121
                Local node:
                OSPF router ID: 10.189.5.252 area ID: 8 domain ID: 0 ASN: 65109
                Remote node:
                TE router ID: 10.169.14.240
                OSPF router ID: 10.169.14.240 area ID: 8 domain ID: 0 ASN: 65109
                Metric: IGP 100, TE 100, Delay 100
                Bandwidth: Total 125000000, Reservable 125000000
                Admin-groups: 0x00000000
                Adj SID: 16 (protected)
            Link[2]: local address 10.189.5.93, remote address 10.189.5.94
                Local node:
                OSPF router ID: 10.189.5.252 area ID: 8 domain ID: 0 ASN: 65109
                Remote node:
                TE router ID: 10.189.5.253
                OSPF router ID: 10.189.5.253 area ID: 8 domain ID: 0 ASN: 65109
                Metric: IGP 5, TE 5, Delay 5
                Bandwidth: Total 125000000, Reservable 125000000
                Admin-groups: 0x00000000
                Adj SID: 19 (protected)
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSegmentRoutingTrafficEngTopology(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingTrafficEngTopology(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ====================================================================
# Unittest for:
#   * 'show segment-routing traffic-eng policy all'
# ====================================================================
class test_show_segment_routing_traffic_eng_policy(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'test1': {
            'name': 'test1',
            'color': 100,
            'end_point': '106.162.196.241',
            'status': {
                'admin': 'up',
                'operational': {
                    'state': 'up',
                    'time_for_state': '09:38:18',
                    'since': '08-28 20:56:55.275',
                },
            },
            'candidate_paths': {
                'preference': {
                    400: {
                        'path_type': {
                            'dynamic': {
                                'status': 'inactive',
                                'pce': True,
                                'weight': 0,
                                'metric_type': 'TE',
                            },
                        },
                    },
                    300: {
                        'path_type': {
                            'dynamic': {
                                'status': 'active',
                                'weight': 0,
                                'metric_type': 'IGP',
                                'path_accumulated_metric': 2200,
                                'hops': {
                                    1: {
                                        'sid': 16063,
                                        'sid_type': 'Prefix-SID',
                                        'local_address': '106.162.196.241',
                                    },
                                    2: {
                                        'sid': 16072,
                                        'sid_type': 'Prefix-SID',
                                        'local_address': '111.87.5.253',
                                        'remote_address': '111.87.6.253',
                                    },
                                },
                            },
                        },
                    },
                    200: {
                        'path_type': {
                            'explicit': {
                                'segment_list': {
                                    'test1': {
                                        'status': 'inactive',
                                        'weight': 0,
                                        'metric_type': 'TE',
                                        'hops': {
                                            1: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '111.87.5.253',
                                                'remote_address': '111.87.6.253',
                                            },
                                            2: {
                                                'sid': 16052,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '106.187.14.241',
                                            },
                                            3: {
                                                'sid': 16062,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '59.128.2.251',
                                            },
                                            4: {
                                                'sid': 16063,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '106.162.196.241',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    100: {
                        'path_type': {
                            'dynamic': {
                                'status': 'inactive',
                                'weight': 0,
                                'metric_type': 'IGP',
                                'path_accumulated_metric': 2200,
                                'hops': {
                                    1: {
                                        'sid': 16063,
                                        'sid_type': 'Prefix-SID',
                                        'local_address': '106.162.196.241',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'attributes': {
                'binding_sid': {
                    15000: {
                        'allocation_mode': 'explicit',
                        'state': 'programmed',
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
        show segment-routing traffic-eng policy all
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
                16072 [Prefix-SID, 111.87.5.253 - 111.87.6.253]
            Preference 200:
            Explicit: segment-list test1 (inactive)
                Weight: 0, Metric Type: TE
                16072 [Prefix-SID, 111.87.5.253 - 111.87.6.253]
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


# ====================================================
# Unittest for:
#   * 'show segment-routing mpls mapping-server ipv4'
#   * 'show segment-routing mpls mapping-server ipv6'
# ====================================================
class test_show_segment_routing_mpls_mapping_server(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output1 = {
        'segment_routing': {
            'bindings': {
                'mapping_server': {
                    'policy': {
                        'prefix_sid_remote_export_map': {
                            'ipv4': {
                                'mapping_entry': {
                                    '192.168.111.1/32': {
                                        'algorithm': {
                                            'ALGO_0': {
                                                'prefix': '192.168.111.1/32',
                                                'algorithm': 'ALGO_0',
                                                'value_type': 'Indx',
                                                'sid': 5001,
                                                'range': '1',
                                                'srgb': 'Y',
                                                'source': 'OSPF Area 8 10.229.11.11',
                                                },
                                            },
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
        show segment-routing mpls mapping-server ipv4

                PREFIX_SID_EXPORT_MAP ALGO_0

        Prefix/masklen   SID Type Range Flags SRGB

                PREFIX_SID_REMOTE_EXPORT_MAP ALGO_0

        Prefix/masklen   SID Type Range Flags SRGB Source
        192.168.111.1/32  5001 Indx     1         Y  OSPF Area 8 10.229.11.11

                PREFIX_SID_EXPORT_MAP ALGO_1

        Prefix/masklen   SID Type Range Flags SRGB

                PREFIX_SID_REMOTE_EXPORT_MAP ALGO_1

        Prefix/masklen   SID Type Range Flags SRGB Source
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsMappingServer(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(address_family='ipv4')

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowSegmentRoutingMplsMappingServer(device=self.device)
        parsed_output = obj.parse(address_family='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

if __name__ == '__main__':
    unittest.main()