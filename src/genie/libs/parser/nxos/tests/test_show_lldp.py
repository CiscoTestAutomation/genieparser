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
from genie.libs.parser.nxos.show_lldp import ShowLldpAll, ShowLldpTimers


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


if __name__ == '__main__':
    unittest.main()
