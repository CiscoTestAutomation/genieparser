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
                                                          )

# =============================================================
# Unittest for:
#   * 'show segment-routing mpls connected-prefix-sid-map ipv4'
# =============================================================
class test_show_routing_mpls_connected_prefix_sid_map(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output1 = {
        'segment_routing':
            {'bindings':
                {'connected_prefix_sid_map':
                    {'ipv4':
                        {'ipv4_prefix_sid':
                            {'1.1.1.1':
                                {'algorithm':
                                    {'ALGO_0':
                                        {'algorithm': 'ALGO_0',
                                        'prefix': '1.1.1.1',
                                        'range': '1',
                                        'source': 'OSPF Area 8 1.1.1.1',
                                        'srgb': 'Y',
                                        'start_sid': '1',
                                        'value_type': 'Indx'}}},
                            '2.2.2.2': 
                                {'algorithm': 
                                    {'ALGO_0': 
                                        {'algorithm': 'ALGO_0',
                                        'prefix': '2.2.2.2',
                                        'range': '1',
                                        'source': 'OSPF Area 8 2.2.2.2',
                                        'srgb': 'Y',
                                        'start_sid': '2',
                                        'value_type': 'Indx'}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        PE1#show segment-routing mpls connected-prefix-sid-map ipv4
 
                       PREFIX_SID_CONN_MAP ALGO_0
         
            Prefix/masklen   SID Type Range Flags SRGB
                1.1.1.1/32     1 Indx     1         Y
         
                       PREFIX_SID_PROTOCOL_ADV_MAP ALGO_0
         
            Prefix/masklen   SID Type Range Flags SRGB Source
                1.1.1.1/32     1 Indx     1         Y  OSPF Area 8 1.1.1.1
                2.2.2.2/32     2 Indx     1         Y  OSPF Area 8 2.2.2.2
         
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
            parsed_output = obj.parse(af='ipv4')

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowSegmentRoutingMplsConnectedPrefixSidMap(device=self.device)
        parsed_output = obj.parse(af='ipv4')
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

<<<<<<< HEAD
=======
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
>>>>>>> dev

if __name__ == '__main__':
    unittest.main()
