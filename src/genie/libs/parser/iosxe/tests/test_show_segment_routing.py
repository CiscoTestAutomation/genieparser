# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

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
                                                          ShowSegmentRoutingTrafficEngPolicyDetail,
                                                          ShowSegmentRoutingTrafficEngTopology,
                                                          ShowSegmentRoutingMplsMappingServer,
                                                          ShowSegmentRoutingMplsLbAssignedSids)


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

    golden_parsed_output_2 = {
        'nodes': {
            1: {
                'ospf_router_id': '10.19.198.239',
                'area_id': 8,
                'domain_id': 0,
                'asn': 65109,
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

    golden_output_2 = {'execute.return_value': '''
            show segment-routing traffic-eng topology ipv4
            Node 1:
                TE router ID: 10.19.198.239
                OSPF router ID: 10.19.198.239 area ID: 8 domain ID: 0 ASN: 65109
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

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowSegmentRoutingTrafficEngTopology(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


# ====================================================================
# Unittest for:
#   * 'show segment-routing traffic-eng policy all'
#   * 'show segment-routing traffic-eng policy name {name}'
# ====================================================================
class test_show_segment_routing_traffic_eng_policy(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'test1': {
            'name': 'test1',
            'color': 100,
            'end_point': '10.169.196.241',
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
                                        'local_address': '10.169.196.241',
                                    },
                                    2: {
                                        'sid': 16072,
                                        'sid_type': 'Prefix-SID',
                                        'local_address': '10.189.5.253',
                                        'remote_address': '10.189.6.253',
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
                                                'local_address': '10.189.5.253',
                                                'remote_address': '10.189.6.253',
                                            },
                                            2: {
                                                'sid': 16052,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.169.14.241',
                                            },
                                            3: {
                                                'sid': 16062,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.34.2.251',
                                            },
                                            4: {
                                                'sid': 16063,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.169.196.241',
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
        Name: test1 (Color: 100 End-point: 10.169.196.241)
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
                16063 [Prefix-SID, 10.169.196.241]
                16072 [Prefix-SID, 10.189.5.253 - 10.189.6.253]
            Preference 200:
            Explicit: segment-list test1 (inactive)
                Weight: 0, Metric Type: TE
                16072 [Prefix-SID, 10.189.5.253 - 10.189.6.253]
                16052 [Prefix-SID, 10.169.14.241]
                16062 [Prefix-SID, 10.34.2.251]
                16063 [Prefix-SID, 10.169.196.241]
            Preference 100:
            Dynamic (inactive)
                Weight: 0, Metric Type: IGP
                Metric Type: IGP, Path Accumulated Metric: 2200
                16063
        Attributes:
            Binding SID: 15000
            Allocation mode: explicit
            State: Programmed
    '''}

    golden_parsed_output_affinity = {
        'test1': {
            'name': 'test1',
            'color': 100,
            'end_point': '10.169.196.241',
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
                    100: {
                        'constraints': {
                            'affinity': {
                                'include-all': ['green', 'blue']
                            }
                        },
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
                                        'local_address': '10.169.196.241',
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

    golden_output_affinity = {'execute.return_value': '''
            show segment-routing traffic-eng policy all
            Name: test1 (Color: 100 End-point: 10.169.196.241)
            Status:
                Admin: up, Operational: up for 09:38:18 (since 08-28 20:56:55.275)
            Candidate-paths:
                Preference 100:
                    Constraints:
                        Affinity:
                            include-all:
                                green
                                blue
                    Dynamic (inactive)
                        Weight: 0, Metric Type: IGP
                        Metric Type: IGP, Path Accumulated Metric: 2200
                        16063 [Prefix-SID, 10.169.196.241]
            Attributes:
                Binding SID: 15000
                Allocation mode: explicit
                State: Programmed
        '''}

    golden_output2 = {'execute.return_value': '''
        show segment-routing traffic-eng policy all
        Name: test_genie_1 (Color: 0 End-point: )
        Status:
            Admin: down, Operational: down for 00:00:01 (since 05-18 03:50:08.958)
        Candidate-paths:
        Attributes:
        Name: test_genie_2 (Color: 100 End-point: 10.19.198.239)
        Status:
            Admin: down, Operational: down for 00:00:00 (since 05-18 03:50:09.080)
        Candidate-paths:
            Preference 100:
            Dynamic (inactive)
                Weight: 0, Metric Type: TE
        Attributes:
            Binding SID: 257
            Allocation mode: dynamic
            State: Programmed
    '''}

    golden_parsed_output2 = {
        'test_genie_1': {
            'color': 0,
            'name': 'test_genie_1',
            'status': {
                'admin': 'down',
                'operational': {
                    'since': '05-18 03:50:08.958',
                    'state': 'down',
                    'time_for_state': '00:00:01',
                },
            },
        },
        'test_genie_2': {
            'attributes': {
                'binding_sid': {
                    257: {
                        'allocation_mode': 'dynamic',
                        'state': 'programmed',
                    },
                },
            },
            'candidate_paths': {
                'preference': {
                    100: {
                        'path_type': {
                            'dynamic': {
                                'metric_type': 'TE',
                                'status': 'inactive',
                                'weight': 0,
                            },
                        },
                    },
                },
            },
            'color': 100,
            'end_point': '10.19.198.239',
            'name': 'test_genie_2',
            'status': {
                'admin': 'down',
                'operational': {
                    'since': '05-18 03:50:09.080',
                    'state': 'down',
                    'time_for_state': '00:00:00',
                },
            },
        },
    }

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

    def test_golden_affinity(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_affinity)
        obj = ShowSegmentRoutingTrafficEngPolicy(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_affinity)
    
    def test_golden_output2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowSegmentRoutingTrafficEngPolicy(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ====================================================================
# Unittest for:
#   * 'show segment-routing traffic-eng policy all detail'
#   * 'show segment-routing traffic-eng policy name {name} detail'
# ====================================================================
class test_show_segment_routing_traffic_eng_policy_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'maxsid': {
            'name': 'maxsid',
            'color': 100,
            'end_point': '10.169.196.241',
            'status': {
                'admin': 'up',
                'operational': {
                    'state': 'up',
                    'time_for_state': '04:54:31',
                    'since': '09-09 20:19:30.195',
                },
            },
            'candidate_paths': {
                'preference': {
                    200: {
                        'path_type': {
                            'explicit': {
                                'segment_list': {
                                    'maxsid': {
                                        'status': 'active',
                                        'weight': 0,
                                        'metric_type': 'TE',
                                        'hops': {
                                            1: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            2: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            3: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            4: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            5: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            6: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            7: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            8: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            9: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            10: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            11: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            12: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            13: {
                                                'sid': 16063,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.169.196.241',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    100: {
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
                                                'local_address': '10.189.5.253',
                                            },
                                            2: {
                                                'sid': 16052,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.169.14.241',
                                            },
                                            3: {
                                                'sid': 16062,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.34.2.251',
                                            },
                                            4: {
                                                'sid': 16063,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.169.196.241',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'attributes': {
                'binding_sid': {
                    15001: {
                        'allocation_mode': 'explicit',
                        'state': 'programmed',
                    },
                },
            },
            'forwarding_id': '65537',
            'stats': {
                'packets': 1878,
                'bytes': 295606,
            },
            'event_history': {
                1: {
                    'timestamp': '09-09 20:15:58.969',
                    'client': 'CLI AGENT',
                    'event_type': 'Policy created',
                    'context': 'Name: maxsid',
                },
                2: {
                    'timestamp': '09-09 20:16:09.573',
                    'client': 'CLI AGENT',
                    'event_type': 'Set colour',
                    'context': 'Colour: 100',
                },
                3: {
                    'timestamp': '09-09 20:16:09.573',
                    'client': 'CLI AGENT',
                    'event_type': 'Set end point',
                    'context': 'End-point: 10.169.196.241',
                },
                4: {
                    'timestamp': '09-09 20:16:23.728',
                    'client': 'CLI AGENT',
                    'event_type': 'Set explicit path',
                    'context': 'Path option: maxsid',
                },
                5: {
                    'timestamp': '09-09 20:19:30.195',
                    'client': 'FH Resolution',
                    'event_type': 'Policy state UP',
                    'context': 'Status: PATH RESOLVED',
                },
                6: {
                    'timestamp': '09-09 20:19:30.202',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                7: {
                    'timestamp': '09-09 20:56:19.877',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                8: {
                    'timestamp': '09-09 20:57:51.007',
                    'client': 'CLI AGENT',
                    'event_type': 'Set binding SID',
                    'context': 'BSID: Binding SID set',
                },
                9: {
                    'timestamp': '09-09 21:15:51.840',
                    'client': 'CLI AGENT',
                    'event_type': 'Set explicit path',
                    'context': 'Path option: test1',
                },
                10: {
                    'timestamp': '09-09 21:19:04.452',
                    'client': 'CLI AGENT',
                    'event_type': 'Set explicit path',
                    'context': 'Path option: test1',
                },
                11: {
                    'timestamp': '09-09 21:19:04.454',
                    'client': 'FH Resolution',
                    'event_type': 'Policy state UP',
                    'context': 'Status: PATH RESOLVED',
                },
                12: {
                    'timestamp': '09-09 21:19:04.458',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                13: {
                    'timestamp': '09-09 21:20:20.811',
                    'client': 'CLI AGENT',
                    'event_type': 'Remove path option',
                    'context': 'Path option: 300',
                },
                14: {
                    'timestamp': '09-09 21:20:20.812',
                    'client': 'FH Resolution',
                    'event_type': 'Policy state UP',
                    'context': 'Status: PATH RESOLVED',
                },
            },
        },
        'test1': {
            'name': 'test1',
            'color': 100,
            'end_point': '10.169.196.241',
            'status': {
                'admin': 'up',
                'operational': {
                    'state': 'up',
                    'time_for_state': '03:48:03',
                    'since': '09-09 21:25:58.933',
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
                                'metric_type': 'TE',
                                'path_accumulated_metric': 2115,
                                'hops': {
                                    1: {
                                        'sid': 16052,
                                        'sid_type': 'Prefix-SID',
                                        'local_address': '10.169.14.241',
                                    },
                                    2: {
                                        'sid': 24,
                                        'sid_type': 'Adjacency-SID',
                                        'local_address': '10.169.14.33',
                                        'remote_address': '10.169.14.34',
                                    },
                                    3: {
                                        'sid': 16063,
                                        'sid_type': 'Prefix-SID',
                                        'local_address': '10.169.196.241',
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
                                                'local_address': '10.189.5.253',
                                            },
                                            2: {
                                                'sid': 16052,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.169.14.241',
                                            },
                                            3: {
                                                'sid': 16062,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.34.2.251',
                                            },
                                            4: {
                                                'sid': 16063,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.169.196.241',
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
                                'metric_type': 'TE',
                                'path_accumulated_metric': 2115,
                                'hops': {
                                    1: {
                                        'sid': 16052,
                                        'sid_type': 'Prefix-SID',
                                        'local_address': '10.169.14.241',
                                    },
                                    2: {
                                        'sid': 24,
                                        'sid_type': 'Adjacency-SID',
                                        'local_address': '10.169.14.33',
                                        'remote_address': '10.169.14.34',
                                    },
                                    3: {
                                        'sid': 16063,
                                        'sid_type': 'Prefix-SID',
                                        'local_address': '10.169.196.241',
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
            'forwarding_id': '65536',
            'stats': {
                'packets': 44,
                'bytes': 1748,
            },
            'event_history': {
                1: {
                    'timestamp': '08-29 14:51:29.074',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                2: {
                    'timestamp': '08-29 14:51:29.099',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                3: {
                    'timestamp': '08-29 14:51:29.114',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                4: {
                    'timestamp': '08-29 14:51:29.150',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                5: {
                    'timestamp': '08-29 14:51:29.199',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                6: {
                    'timestamp': '08-29 14:51:29.250',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                7: {
                    'timestamp': '08-29 14:51:29.592',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                8: {
                    'timestamp': '08-29 14:51:29.733',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                9: {
                    'timestamp': '08-29 14:51:29.873',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                10: {
                    'timestamp': '08-29 14:51:30.013',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                11: {
                    'timestamp': '08-29 14:51:30.162',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                12: {
                    'timestamp': '08-29 14:51:33.875',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                13: {
                    'timestamp': '08-29 14:51:33.879',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                14: {
                    'timestamp': '08-29 14:51:33.919',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                15: {
                    'timestamp': '08-29 14:51:33.978',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                16: {
                    'timestamp': '08-29 14:51:33.982',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                17: {
                    'timestamp': '08-29 14:51:34.724',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                18: {
                    'timestamp': '08-29 14:51:35.227',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                19: {
                    'timestamp': '09-03 13:06:47.604',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                20: {
                    'timestamp': '09-03 13:06:47.607',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                21: {
                    'timestamp': '09-09 20:15:36.537',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                22: {
                    'timestamp': '09-09 20:15:36.541',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                23: {
                    'timestamp': '09-09 20:15:36.545',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                24: {
                    'timestamp': '09-09 20:15:36.557',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                25: {
                    'timestamp': '09-09 20:15:36.571',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                26: {
                    'timestamp': '09-09 20:15:36.598',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                27: {
                    'timestamp': '09-09 20:15:36.614',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                28: {
                    'timestamp': '09-09 20:15:36.629',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                29: {
                    'timestamp': '09-09 20:15:36.641',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                30: {
                    'timestamp': '09-09 20:15:36.667',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                31: {
                    'timestamp': '09-09 20:15:36.698',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                32: {
                    'timestamp': '09-09 20:15:36.734',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                33: {
                    'timestamp': '09-09 20:15:36.764',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                34: {
                    'timestamp': '09-09 20:15:36.789',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                35: {
                    'timestamp': '09-09 20:15:36.800',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                36: {
                    'timestamp': '09-09 20:15:36.823',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                37: {
                    'timestamp': '09-09 20:16:23.743',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                38: {
                    'timestamp': '09-09 20:16:23.745',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                39: {
                    'timestamp': '09-09 20:19:30.199',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                40: {
                    'timestamp': '09-09 20:19:30.205',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                41: {
                    'timestamp': '09-09 20:50:52.378',
                    'client': 'CLI AGENT',
                    'event_type': 'Set colour',
                    'context': 'Colour: 200',
                },
                42: {
                    'timestamp': '09-09 20:52:04.236',
                    'client': 'CLI AGENT',
                    'event_type': 'Policy ADMIN DOWN',
                    'context': 'shutdown: test1',
                },
                43: {
                    'timestamp': '09-09 20:59:06.432',
                    'client': 'CLI AGENT',
                    'event_type': 'Policy state DOWN',
                    'context': 'no shutdown: test1',
                },
                44: {
                    'timestamp': '09-09 20:59:06.434',
                    'client': 'FH Resolution',
                    'event_type': 'Policy state UP',
                    'context': 'Status: PATH RESOLVED',
                },
                45: {
                    'timestamp': '09-09 20:59:06.442',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                46: {
                    'timestamp': '09-09 21:17:36.909',
                    'client': 'CLI AGENT',
                    'event_type': 'Set colour',
                    'context': 'Colour: 100',
                },
                47: {
                    'timestamp': '09-09 21:18:39.057',
                    'client': 'CLI AGENT',
                    'event_type': 'Policy ADMIN DOWN',
                    'context': 'shutdown: test1',
                },
                48: {
                    'timestamp': '09-09 21:25:58.931',
                    'client': 'CLI AGENT',
                    'event_type': 'Policy state DOWN',
                    'context': 'no shutdown: test1',
                },
                49: {
                    'timestamp': '09-09 21:25:58.933',
                    'client': 'FH Resolution',
                    'event_type': 'Policy state UP',
                    'context': 'Status: PATH RESOLVED',
                },
                50: {
                    'timestamp': '09-09 21:25:58.945',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
        sr_ve-hkgasr01#show segment-routing traffic-eng policy all detail

        Name: maxsid (Color: 100 End-point: 10.169.196.241)
        Status:
            Admin: up, Operational: up for 04:54:31 (since 09-09 20:19:30.195)
        Candidate-paths:
            Preference 200:
            Explicit: segment-list maxsid (active)
                Weight: 0, Metric Type: TE
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16063 [Prefix-SID, 10.169.196.241]
            Preference 100:
            Explicit: segment-list test1 (inactive)
                Weight: 0, Metric Type: TE
                16072 [Prefix-SID, 10.189.5.253]
                16052 [Prefix-SID, 10.169.14.241]
                16062 [Prefix-SID, 10.34.2.251]
                16063 [Prefix-SID, 10.169.196.241]
        Attributes:
            Binding SID: 15001
            Allocation mode: explicit
            State: Programmed
        Forwarding-ID: 65537 (0x1C)
        Stats:
            Packets: 1878       Bytes: 295606

        Event history:
            Timestamp                   Client                  Event type              Context: Value
            ---------                   ------                  ----------              -------: -----
            09-09 20:15:58.969          CLI AGENT               Policy created          Name: maxsid
            09-09 20:16:09.573          CLI AGENT               Set colour              Colour: 100
            09-09 20:16:09.573          CLI AGENT               Set end point           End-point: 10.169.196.241
            09-09 20:16:23.728          CLI AGENT               Set explicit path       Path option: maxsid
            09-09 20:19:30.195          FH Resolution           Policy state UP         Status: PATH RESOLVED
            09-09 20:19:30.202          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:56:19.877          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:57:51.007          CLI AGENT               Set binding SID         BSID: Binding SID set
            09-09 21:15:51.840          CLI AGENT               Set explicit path       Path option: test1
            09-09 21:19:04.452          CLI AGENT               Set explicit path       Path option: test1
            09-09 21:19:04.454          FH Resolution           Policy state UP         Status: PATH RESOLVED
            09-09 21:19:04.458          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 21:20:20.811          CLI AGENT               Remove path option      Path option: 300
            09-09 21:20:20.812          FH Resolution           Policy state UP         Status: PATH RESOLVED

        Name: test1 (Color: 100 End-point: 10.169.196.241)
        Status:
            Admin: up, Operational: up for 03:48:03 (since 09-09 21:25:58.933)
        Candidate-paths:
            Preference 400:
            Dynamic (pce) (inactive)
                Weight: 0, Metric Type: TE
            Preference 300:
            Dynamic (active)
                Weight: 0, Metric Type: TE
                Metric Type: TE, Path Accumulated Metric: 2115
                16052 [Prefix-SID, 10.169.14.241]
                24 [Adjacency-SID, 10.169.14.33 - 10.169.14.34]
                16063 [Prefix-SID, 10.169.196.241]
            Preference 200:
            Explicit: segment-list test1 (inactive)
                Weight: 0, Metric Type: TE
                16072 [Prefix-SID, 10.189.5.253]
                16052 [Prefix-SID, 10.169.14.241]
                16062 [Prefix-SID, 10.34.2.251]
                16063 [Prefix-SID, 10.169.196.241]
            Preference 100:
            Dynamic (inactive)
                Weight: 0, Metric Type: TE
                Metric Type: TE, Path Accumulated Metric: 2115
                16052 [Prefix-SID, 10.169.14.241]
                24 [Adjacency-SID, 10.169.14.33 - 10.169.14.34]
                16063 [Prefix-SID, 10.169.196.241]
        Attributes:
            Binding SID: 15000
            Allocation mode: explicit
            State: Programmed
        Forwarding-ID: 65536 (0x18)
        Stats:
            Packets: 44         Bytes: 1748

        Event history:
            Timestamp                   Client                  Event type              Context: Value
            ---------                   ------                  ----------              -------: -----
            08-29 14:51:29.074          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:29.099          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:29.114          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:29.150          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:29.199          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:29.250          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:29.592          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:29.733          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:29.873          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:30.013          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:30.162          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:33.875          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:33.879          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:33.919          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:33.978          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:33.982          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:34.724          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            08-29 14:51:35.227          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-03 13:06:47.604          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-03 13:06:47.607          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.537          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.541          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.545          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.557          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.571          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.598          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.614          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.629          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.641          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.667          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.698          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.734          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.764          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.789          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.800          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:15:36.823          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:16:23.743          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:16:23.745          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:19:30.199          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:19:30.205          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:50:52.378          CLI AGENT               Set colour              Colour: 200
            09-09 20:52:04.236          CLI AGENT               Policy ADMIN DOWN       shutdown: test1
            09-09 20:59:06.432          CLI AGENT               Policy state DOWN       no shutdown: test1
            09-09 20:59:06.434          FH Resolution           Policy state UP         Status: PATH RESOLVED
            09-09 20:59:06.442          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 21:17:36.909          CLI AGENT               Set colour              Colour: 100
            09-09 21:18:39.057          CLI AGENT               Policy ADMIN DOWN       shutdown: test1
            09-09 21:25:58.931          CLI AGENT               Policy state DOWN       no shutdown: test1
            09-09 21:25:58.933          FH Resolution           Policy state UP         Status: PATH RESOLVED
            09-09 21:25:58.945          FH Resolution           REOPT triggered         Status: REOPTIMIZED
        sr_ve-hkgasr01#
    '''}

    golden_parsed_output_name = {
        'maxsid': {
            'name': 'maxsid',
            'color': 100,
            'end_point': '10.169.196.241',
            'status': {
                'admin': 'up',
                'operational': {
                    'state': 'up',
                    'time_for_state': '06:35:58',
                    'since': '09-09 20:19:30.195',
                },
            },
            'candidate_paths': {
                'preference': {
                    200: {
                        'path_type': {
                            'explicit': {
                                'segment_list': {
                                    'maxsid': {
                                        'status': 'active',
                                        'weight': 0,
                                        'metric_type': 'TE',
                                        'hops': {
                                            1: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            2: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            3: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            4: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            5: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            6: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            7: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            8: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            9: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            10: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            11: {
                                                'sid': 16071,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.252',
                                            },
                                            12: {
                                                'sid': 16072,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.189.5.253',
                                            },
                                            13: {
                                                'sid': 16063,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.169.196.241',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    100: {
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
                                                'local_address': '10.189.5.253',
                                            },
                                            2: {
                                                'sid': 16052,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.169.14.241',
                                            },
                                            3: {
                                                'sid': 16062,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.34.2.251',
                                            },
                                            4: {
                                                'sid': 16063,
                                                'sid_type': 'Prefix-SID',
                                                'local_address': '10.169.196.241',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'attributes': {
                'binding_sid': {
                    15001: {
                        'allocation_mode': 'explicit',
                        'state': 'programmed',
                    },
                },
            },
            'forwarding_id': '65537',
            'stats': {
                'packets': 2520,
                'bytes': 397042,
            },
            'event_history': {
                1: {
                    'timestamp': '09-09 20:15:58.969',
                    'client': 'CLI AGENT',
                    'event_type': 'Policy created',
                    'context': 'Name: maxsid',
                },
                2: {
                    'timestamp': '09-09 20:16:09.573',
                    'client': 'CLI AGENT',
                    'event_type': 'Set colour',
                    'context': 'Colour: 100',
                },
                3: {
                    'timestamp': '09-09 20:16:09.573',
                    'client': 'CLI AGENT',
                    'event_type': 'Set end point',
                    'context': 'End-point: 10.169.196.241',
                },
                4: {
                    'timestamp': '09-09 20:16:23.728',
                    'client': 'CLI AGENT',
                    'event_type': 'Set explicit path',
                    'context': 'Path option: maxsid',
                },
                5: {
                    'timestamp': '09-09 20:19:30.195',
                    'client': 'FH Resolution',
                    'event_type': 'Policy state UP',
                    'context': 'Status: PATH RESOLVED',
                },
                6: {
                    'timestamp': '09-09 20:19:30.202',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                7: {
                    'timestamp': '09-09 20:56:19.877',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                8: {
                    'timestamp': '09-09 20:57:51.007',
                    'client': 'CLI AGENT',
                    'event_type': 'Set binding SID',
                    'context': 'BSID: Binding SID set',
                },
                9: {
                    'timestamp': '09-09 21:15:51.840',
                    'client': 'CLI AGENT',
                    'event_type': 'Set explicit path',
                    'context': 'Path option: test1',
                },
                10: {
                    'timestamp': '09-09 21:19:04.452',
                    'client': 'CLI AGENT',
                    'event_type': 'Set explicit path',
                    'context': 'Path option: test1',
                },
                11: {
                    'timestamp': '09-09 21:19:04.454',
                    'client': 'FH Resolution',
                    'event_type': 'Policy state UP',
                    'context': 'Status: PATH RESOLVED',
                },
                12: {
                    'timestamp': '09-09 21:19:04.458',
                    'client': 'FH Resolution',
                    'event_type': 'REOPT triggered',
                    'context': 'Status: REOPTIMIZED',
                },
                13: {
                    'timestamp': '09-09 21:20:20.811',
                    'client': 'CLI AGENT',
                    'event_type': 'Remove path option',
                    'context': 'Path option: 300',
                },
                14: {
                    'timestamp': '09-09 21:20:20.812',
                    'client': 'FH Resolution',
                    'event_type': 'Policy state UP',
                    'context': 'Status: PATH RESOLVED',
                },
            },
        },
    }

    golden_output_name = {'execute.return_value': '''
        sr_ve-hkgasr01#show segment-routing traffic-eng policy name maxsid detail

        Name: maxsid (Color: 100 End-point: 10.169.196.241)
        Status:
            Admin: up, Operational: up for 06:35:58 (since 09-09 20:19:30.195)
        Candidate-paths:
            Preference 200:
            Explicit: segment-list maxsid (active)
                Weight: 0, Metric Type: TE
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16071 [Prefix-SID, 10.189.5.252]
                16072 [Prefix-SID, 10.189.5.253]
                16063 [Prefix-SID, 10.169.196.241]
            Preference 100:
            Explicit: segment-list test1 (inactive)
                Weight: 0, Metric Type: TE
                16072 [Prefix-SID, 10.189.5.253]
                16052 [Prefix-SID, 10.169.14.241]
                16062 [Prefix-SID, 10.34.2.251]
                16063 [Prefix-SID, 10.169.196.241]
        Attributes:
            Binding SID: 15001
            Allocation mode: explicit
            State: Programmed
        Forwarding-ID: 65537 (0x1C)
        Stats:
            Packets: 2520       Bytes: 397042

        Event history:
            Timestamp                   Client                  Event type              Context: Value
            ---------                   ------                  ----------              -------: -----
            09-09 20:15:58.969          CLI AGENT               Policy created          Name: maxsid
            09-09 20:16:09.573          CLI AGENT               Set colour              Colour: 100
            09-09 20:16:09.573          CLI AGENT               Set end point           End-point: 10.169.196.241
            09-09 20:16:23.728          CLI AGENT               Set explicit path       Path option: maxsid
            09-09 20:19:30.195          FH Resolution           Policy state UP         Status: PATH RESOLVED
            09-09 20:19:30.202          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:56:19.877          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 20:57:51.007          CLI AGENT               Set binding SID         BSID: Binding SID set
            09-09 21:15:51.840          CLI AGENT               Set explicit path       Path option: test1
            09-09 21:19:04.452          CLI AGENT               Set explicit path       Path option: test1
            09-09 21:19:04.454          FH Resolution           Policy state UP         Status: PATH RESOLVED
            09-09 21:19:04.458          FH Resolution           REOPT triggered         Status: REOPTIMIZED
            09-09 21:20:20.811          CLI AGENT               Remove path option      Path option: 300
            09-09 21:20:20.812          FH Resolution           Policy state UP         Status: PATH RESOLVED


        sr_ve-hkgasr01#
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowSegmentRoutingTrafficEngPolicyDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingTrafficEngPolicyDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_name(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_name)
        obj = ShowSegmentRoutingTrafficEngPolicyDetail(device=self.device)
        parsed_output = obj.parse(name='maxsid')
        self.assertEqual(parsed_output, self.golden_parsed_output_name)


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


class test_show_segment_routing_mpls_lb_assigned_sids(unittest.TestCase):
    """ Unit tests for:
            * show segment-routing mpls lb assigned-sids
    """
    device = Device(name="aDevice")
    empty_output = {"execute.return_value": ""}

    golden_output = {"execute.return_value": """
        show segment-routing mpls lb assigned-sids
        Adjacency SID Database
          C=> In conflict
          S=> Shared
          R=> In range
        SID    STATE PROTOCOL TOPOID   LAN PRO NEIGHBOR INTERFACE
         12345  R     ISIS     2        N   N   192.168.0.1 Ethernet1
    """}

    golden_parsed_output = {
        "segment_routing": {
            "sid": {
                "12345": {
                    "state": "R",
                    "state_info": "In range",
                    "protocol": "ISIS",
                    "topoid": 2,
                    "lan": "N",
                    "pro": "N",
                    "neighbor": "192.168.0.1",
                    "interface": "Ethernet1"
                }
            }
        }
    }

    golden_output_partial = {"execute.return_value": """
        show segment-routing mpls lb assigned-sids
        Adjacency SID Database
          C=> In conflict
          S=> Shared
          R=> In range
        SID    STATE PROTOCOL TOPOID   LAN PRO NEIGHBOR INTERFACE
         12345   S
    """}

    golden_parsed_output_partial = {
        "segment_routing": {
            "sid": {
                "12345": {
                    "state": "S",
                    "state_info": "Shared",
                }
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSegmentRoutingMplsLbAssignedSids(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSegmentRoutingMplsLbAssignedSids(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_partial(self):
        self.device = Mock(**self.golden_output_partial)
        obj = ShowSegmentRoutingMplsLbAssignedSids(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_partial)


if __name__ == '__main__':
    unittest.main()