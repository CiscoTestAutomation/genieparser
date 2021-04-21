
import unittest

from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxr.show_dampening import (ShowImDampening,
                                                    ShowImDampeningIntf)


class TestShowImDampening(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    # show im dampening
    golden_output = {'execute.return_value': '''
Interface                   Protocol           Capsulation          Pen   Sup
--------------------------- ------------------ -------------------- ----- ---
GigabitEthernet0/0/0/0                                                629 NO 
GigabitEthernet0/0/0/1                                               2389 YES
POS0/2/0/0                                                              0 NO 
POS0/2/0/0                  <base>             ppp                      0 NO 
POS0/2/0/0                  ipv4               ipcp                     0 NO '''}

    golden_parsed_output = {
        'interface': {
            'GigabitEthernet0/0/0/0': {
                'index': {
                    1: {
                        'penalty': 629,
                        'suppressed': 'NO'
                    }
                }
            },
            'GigabitEthernet0/0/0/1': {
                'index': {
                    1: {
                        'penalty': 2389,
                        'suppressed': 'YES'
                    }
                }
            },
            'POS0/2/0/0': {
                'index': {
                    1: {
                        'penalty': 0,
                        'suppressed': 'NO'
                    },
                    2: {
                        'capsulation': 'ppp',
                        'penalty': 0,
                        'protocol': '<base>',
                        'suppressed': 'NO'
                    },
                    3: {
                        'capsulation': 'ipcp',
                        'penalty': 0,
                        'protocol': 'ipv4',
                        'suppressed': 'NO'
                    }
                }
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowImDampening(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowImDampening(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowImDampeningIntf(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    # show im dampening int gigabitEthernet 0/2/0/0
    golden_output = {'execute.return_value': '''
Sun Oct 11 12:47:16.746 BST
GigabitEthernet0/2/0/0 (0x080002c0)
Dampening enabled: Penalty 0, not suppressed
  underlying-state:  Up
  half-life:         1        reuse:             750
  suppress:          2000     max-suppress-time: 4
  restart-penalty:   0 '''}

    golden_parsed_output = {
        'interface': {
            'GigabitEthernet0/2/0/0': {
                'currently_suppressed': 'no',
                'dampening_status': 'enabled',
                'half_life': 1,
                'interface_handler': '0x080002c0',
                'max_supress_time': 4,
                'penalty': 0,
                'reuse': 750,
                'suppress': 2000,
                'underlying_state': 'Up'
            }
        }
    }

    # show im dampening interface TenGigaE 0/1/0/0
    golden_output2 = {'execute.return_value': '''
TenGigE 0/1/0/0 (0x01180020)
Dampening enabled: Penalty 1625, SUPPRESSED (42 secs remaining)
  Underlying state: Down
  half-life: 1        reuse:             1000     
  suppress:  1500     max-suppress-time: 4 

Protocol       Capsulation        Pen   Suppression              U-L State  
-------------- ------------------ ----- --------------------- -------------
 ipv6           ipv6               1625  YES    42s  remaining        Down
 ipv4           ipv4               1615  NO     22s  remaining        Down'''}

    golden_parsed_output2 = {
        'interface': {
            'TenGigE 0/1/0/0': {
                'currently_suppressed': 'yes',
                'dampening_status': 'enabled',
                'half_life': 1,
                'index': {
                    1: {
                        'capsulation': 'ipv6',
                        'penalty': 1625,
                        'protocol': 'ipv6',
                        'suppression': 'YES',
                        'suppression_remaining_sec': 42,
                        'underlying_state': 'Down'
                    },
                    2: {
                        'capsulation': 'ipv4',
                        'penalty': 1615,
                        'protocol': 'ipv4',
                        'suppression': 'NO',
                        'suppression_remaining_sec': 22,
                        'underlying_state': 'Down'
                    }
                },
                'interface_handler': '0x01180020',
                'max_supress_time': 4,
                'penalty': 1625,
                'reuse': 1000,
                'suppress': 1500,
                'suppressed_secs_remaining': 42,
                'underlying_state': 'Down'
            }
        }
    }

    # show im dampening interface GigabitEthernet0/2/0/8
    golden_output3 = {'execute.return_value': '''
Mon Oct 12 06:03:36.737 BST
GigabitEthernet0/2/0/8
Dampening not enabled'''}

    golden_parsed_output3 = {
        'interface': {
            'GigabitEthernet0/2/0/8': {
                'dampening_status': 'dampening_not_enabled'
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowImDampeningIntf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='TenGigaE 0/1/0/0')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowImDampeningIntf(device=self.device)
        parsed_output = obj.parse(interface='TenGigaE 0/1/0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowImDampeningIntf(device=self.device)
        parsed_output = obj.parse(interface='TenGigaE 0/1/0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        obj = ShowImDampeningIntf(device=self.device)
        parsed_output = obj.parse(interface='GigabitEthernet0/2/0/8')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

if __name__ == '__main__':
    unittest.main()
