# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

# iosxe show_lisp
from genie.libs.parser.nxos.show_lldp import ShowLldpAll, ShowLldpTimers, \
    ShowLldpTlvSelect, ShowLldpNeighborsDetail, ShowLldpTraffic

# =================================
# Unit test for 'show lldp all'
# =================================
class TestShowLldpAll(unittest.TestCase):
    '''unit test for "show lldp all'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Ethernet1/64':
                {'enabled': True,
                 'tx': True,
                 'rx': True,
                 'dcbx': True
                 },
            'mgmt0':
                {'enabled': True,
                 'tx': True,
                 'rx': True,
                 'dcbx': False
                 }
        }
    }

    golden_output = {'execute.return_value': '''
    Interface Information: Eth1/64 Enable (tx/rx/dcbx): Y/Y/Y
    Interface Information: mgmt0 Enable (tx/rx/dcbx): Y/Y/N
    '''
                     }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLldpAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLldpAll(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show lldp timers'
# =================================
class TestShowLldpTimers(unittest.TestCase):
    '''unit test for show lldp timers'''
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'hold_timer': 120,
        'reinit_timer': 2,
        'hello_timer': 30
    }
    golden_output = {'execute.return_value':
                         '''
                         LLDP Timers:

                             Holdtime in seconds: 120
                             Reinit-time in seconds: 2
                             Transmit interval in seconds: 30
                         '''
                     }

    golden_output_1 = {'execute.return_value': '''
        show lldp timers

        LLDP Timers:

            Holdtime in seconds: 120
            Reinit-time in seconds: 2
            Transmit interval in seconds: 30
            Transmit delay in seconds: 2
            Hold multiplier in seconds: 4
            Notification interval in seconds: 5
    '''
    }

    golden_parsed_output_1 = {
        'hello_timer': 30,
        'hold_multiplier': 4,
        'hold_timer': 120,
        'notification_interval': 5,
        'reinit_timer': 2,
        'transmit_delay': 2
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLldpTimers(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLldpTimers(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowLldpTimers(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

# =================================
# Unit test for 'show lldp tlv-select'
# =================================
class TestShowLldpTlvSelect(unittest.TestCase):
    '''unit test for show lldp tlv-select'''
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'suppress_tlv_advertisement': {
            'port_description': False,
            'system_name': False,
            'system_description': False,
            'system_capabilities': False,
            'management_address_v4': False,
            'management_address_v6': False,
            'power_management': False,
            'port_vlan': False,
            'dcbxp': False
        }
    }
    golden_output = {'execute.return_value': '''
           management-address-v4
           management-address-v6
           port-description
           port-vlan
           power-management
           system-capabilities
           system-description
           system-name
           dcbxp
        '''}

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLldpTlvSelect(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLldpTlvSelect(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show lldp traffic'
# =================================
class TestShowLldpTraffic(unittest.TestCase):
    '''unit test for show lldp traffic'''
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'counters': {
            "total_frames_received": 209,
            "total_frames_transmitted": 349,
            "total_frames_received_in_error": 0,
            "total_frames_discarded": 0,
            'total_unrecognized_tlvs': 0,
            'total_entries_aged': 0
        }
    }
    golden_output = {'execute.return_value': '''
        LLDP traffic statistics:

            Total frames transmitted: 349
            Total entries aged: 0
            Total frames received: 209
            Total frames received in error: 0
            Total frames discarded: 0
            Total unrecognized TLVs: 0
    '''
    }
    
    golden_output_1 = {'execute.return_value': '''
        LLDP traffic statistics: 

            Total frames transmitted: 530516
            Total entries aged: 0
            Total frames received: 496131
            Total frames received in error: 0
            Total frames discarded: 0
            Total unrecognized TLVs: 0
            Total flap count: 1
    '''
    }

    golden_parsed_output_1 = {
        'counters': {
            'total_entries_aged': 0,
            'total_flap_count': 1,
            'total_frames_discarded': 0,
            'total_frames_received': 496131,
            'total_frames_received_in_error': 0,
            'total_frames_transmitted': 530516,
            'total_unrecognized_tlvs': 0
        }
    }

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowLldpTraffic(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLldpTraffic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowLldpTraffic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()
