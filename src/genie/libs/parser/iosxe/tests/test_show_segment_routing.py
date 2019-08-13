import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.show_segment_routing import (ShowSegmentRoutingMplsLB,
                                                          ShowSegmentRoutingMplsGbLock,
                                                          ShowSegmentRoutingMplsState)

# ============================================
# Parser for 'show segment-routing mpls lb'
# ============================================

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

# ============================================
# Parser for 'show segment-routing mpls state'
# ============================================

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

if __name__ == '__main__':
    unittest.main()