# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

# iosxe show_lisp
from genie.libs.parser.nxos.show_lldp import ShowLldpAll, ShowLldpTimers, \
    ShowLldpTlvSelect, ShowLldpTraffic


# =================================
# Unit test for 'show lldp all'
# =================================
class test_show_lldp_all(unittest.TestCase):
    '''unit test for "show lldp all'''
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Eth1/64':
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


class test_show_lldp_timers(unittest.TestCase):
    '''unit test for show lldp timers'''
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':
                         '''
                         LLDP Timers:
                     
                             Holdtime in seconds: 120
                             Reinit-time in seconds: 2
                             Transmit interval in seconds: 30
                         '''
                     }
    golden_parsed_output = {
        'hold_timer': 120,
        'reinit_timer': 2,
        'hello_timer': 30
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


class test_show_lldp_tlv_select(unittest.TestCase):
    '''unit test for show lldp tlv-select'''
    empty_output = {'execute.return_value': ''}
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
    golden_parsed_output = {'suppress_tlv_advertisement': {
        'port_description': False,
        'system_name': False,
        'system_description': False,
        'system_capabilities': False,
        'management_address': False,
        'port_vlan': False,
        'dcbxp': False
    }
    }

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


class test_show_lldp_neighbors_detail(unittest.TestCase):
    '''unit test for show lldp neighbors detail'''
    empty_output = {'execute.return_value': ''}
    pass


class test_show_lldp_traffic(unittest.TestCase):
    '''unit test for show lldp traffic'''
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value':'''
                LLDP traffic statistics:
                
                    Total frames transmitted: 349
                    Total entries aged: 0
                    Total frames received: 209
                    Total frames received in error: 0
                    Total frames discarded: 0
                    Total unrecognized TLVs: 0
                    '''
                     }
    golden_parsed_output = {
        "frame_in": 209,
        "frame_out": 349,
        "frame_error_in": 0,
        "frame_discard": 0,
        'tlv_unknown': 0,
        'entries_aged_out': 0
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


if __name__ == '__main__':
    unittest.main()
