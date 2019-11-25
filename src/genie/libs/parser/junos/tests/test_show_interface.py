import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.junos.show_interface import (ShowInterfacesTerse,
                                                    ShowInterfacesTerseMatch)

#############################################################################
# unitest For show interfaces terse [| match <interface>]
#############################################################################

class test_show_interfaces_terse(unittest.TestCase):
    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
         'em1': {'admin_state': 'up',
                 'enabled': True,
                 'link_state': 'up',
                 'oper_status': 'up'},
         'em1.0': {'admin_state': 'up',
                   'enabled': True,
                   'link_state': 'up',
                   'oper_status': 'up',
                   'protocol': {'inet': {'10.0.0.4/8': {'local': '10.0.0.4/8'},
                                         '172.16.64.1/2': {'local': '172.16.64.1/2'},
                                         '172.16.64.4/2': {'local': '172.16.64.4/2'}},
                                'inet6': {'fe80::250:56ff:fe82:ba52/64': {'local': 'fe80::250:56ff:fe82:ba52/64'},
                                          '2001:db8:8d82:0:a::4/64': {'local': '2001:db8:8d82:0:a::4/64'}},
                                'tnp': {'0x4': {'local': '0x4'}}}},
         'fxp0': {'admin_state': 'up',
                  'enabled': True,
                  'link_state': 'up',
                  'oper_status': 'up'},
         'fxp0.0': {'admin_state': 'up',
                    'enabled': True,
                    'link_state': 'up',
                    'oper_status': 'up',
                    'protocol': {'inet': {'172.25.192.114/24': {'local': '172.25.192.114/24'}}}},
         'ge-0/0/0': {'admin_state': 'up',
                      'enabled': True,
                      'link_state': 'up',
                      'oper_status': 'up'},
         'ge-0/0/0.0': {'admin_state': 'up',
                        'enabled': True,
                        'link_state': 'up',
                        'oper_status': 'up',
                        'protocol': {'inet': {'10.0.1.1/24': {'local': '10.0.1.1/24'}},
                                     'multiservice': {}}},
         'ge-0/0/1': {'admin_state': 'up',
                      'enabled': True,
                      'link_state': 'up',
                      'oper_status': 'up'},
         'ge-0/0/1.0': {'admin_state': 'up',
                        'enabled': True,
                        'link_state': 'up',
                        'oper_status': 'up',
                        'protocol': {'inet': {'10.0.2.1/24': {'local': '10.0.2.1/24'}},
                                     'multiservice': {}}},
         'ge-0/0/2': {'admin_state': 'up',
                      'enabled': True,
                      'link_state': 'down',
                      'oper_status': 'down'},
         'lc-0/0/0': {'admin_state': 'up',
                      'enabled': True,
                      'link_state': 'up',
                      'oper_status': 'up'},
         'lc-0/0/0.32769': {'admin_state': 'up',
                            'enabled': True,
                            'link_state': 'up',
                            'oper_status': 'up',
                            'protocol': {'vpls': {}}},
         'lo0.0': {'admin_state': 'up',
                   'enabled': True,
                   'link_state': 'up',
                   'oper_status': 'up',
                   'protocol': {'inet': {'10.1.1.1': {'local': '10.1.1.1',
                                                      'remote': '0/0'},
                                         '10.11.11.11': {'local': '10.11.11.11',
                                                         'remote': '0/0'}}}},
         'lo0.16384': {'admin_state': 'up',
                       'enabled': True,
                       'link_state': 'up',
                       'oper_status': 'up',
                       'protocol': {'inet': {'127.0.0.1': {'local': '127.0.0.1',
                                                           'remote': '0/0'}}}},
         'lo0.16385': {'admin_state': 'up',
                       'enabled': True,
                       'link_state': 'up',
                       'oper_status': 'up',
                       'protocol': {'inet': {}}},
         'pfe-0/0/0': {'admin_state': 'up',
                       'enabled': True,
                       'link_state': 'up',
                       'oper_status': 'up'},
         'pfe-0/0/0.16383': {'admin_state': 'up',
                             'enabled': True,
                             'link_state': 'up',
                             'oper_status': 'up',
                             'protocol': {'inet': {}, 'inet6': {}}},
         'pfh-0/0/0': {'admin_state': 'up',
                       'enabled': True,
                       'link_state': 'up',
                       'oper_status': 'up'},
         'pfh-0/0/0.16383': {'admin_state': 'up',
                             'enabled': True,
                             'link_state': 'up',
                             'oper_status': 'up',
                             'protocol': {'inet': {}}},
         'pfh-0/0/0.16384': {'admin_state': 'up',
                             'enabled': True,
                             'link_state': 'up',
                             'oper_status': 'up',
                             'protocol': {'inet': {}}},
    }

    golden_output = {'execute.return_value': '''
        root@junos_vmx1> show interfaces terse 
        Interface               Admin Link Proto    Local                 Remote
        ge-0/0/0                up    up
        ge-0/0/0.0              up    up   inet     10.0.1.1/24     
                                           multiservice
        lc-0/0/0                up    up
        lc-0/0/0.32769          up    up   vpls    
        pfe-0/0/0               up    up
        pfe-0/0/0.16383         up    up   inet    
                                           inet6   
        pfh-0/0/0               up    up
        pfh-0/0/0.16383         up    up   inet    
        pfh-0/0/0.16384         up    up   inet    
        ge-0/0/1                up    up
        ge-0/0/1.0              up    up   inet     10.0.2.1/24     
                                           multiservice
        ge-0/0/2                up    down
        em1                     up    up
        em1.0                   up    up   inet     10.0.0.4/8      
                                                    172.16.64.1/2     
                                                    172.16.64.4/2     
                                           inet6    fe80::250:56ff:fe82:ba52/64
                                                    2001:db8:8d82:0:a::4/64
                                           tnp      0x4  
        fxp0                    up    up
        fxp0.0                  up    up   inet     172.25.192.114/24
        lo0.0                   up    up   inet     10.1.1.1            --> 0/0
                                                    10.11.11.11         --> 0/0
        lo0.16384               up    up   inet     127.0.0.1           --> 0/0
        lo0.16385               up    up   inet  
    '''
    }

    golden_output_interface = {'execute.return_value': """
    root@junos_vmx1 > show interfaces em1.0 terse
    em1.0                   up    up   inet     10.0.0.4/8      
                                                    172.16.64.1/2     
                                                    172.16.64.4/2     
                                           inet6    fe80::250:56ff:fe82:ba52/64
                                                    2001:db8:8d82:0:a::4/64
                                           tnp      0x4 
    """}

    golden_parsed_output_interface = {
        'em1.0': {
            'admin_state': 'up',
            'enabled': True,
            'link_state': 'up',
            'oper_status': 'up',
            'protocol': {
                'inet': {
                    '10.0.0.4/8': {
                        'local': '10.0.0.4/8'
                    },
                    '172.16.64.1/2': {
                        'local': '172.16.64.1/2'
                    },
                    '172.16.64.4/2': {
                        'local': '172.16.64.4/2'
                    }
                },
                'inet6': {
                    'fe80::250:56ff:fe82:ba52/64': {
                        'local': 'fe80::250:56ff:fe82:ba52/64'
                    },
                    '2001:db8:8d82:0:a::4/64': {
                        'local': '2001:db8:8d82:0:a::4/64'
                    }
                },
                'tnp': {
                    '0x4': {
                        'local': '0x4'
                    }
                }
            }
        }
    }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfacesTerse(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesTerse(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_interface(self):
        self.device = Mock(**self.golden_output_interface)
        interface_obj = ShowInterfacesTerse(device=self.device)
        parsed_output = interface_obj.parse(interface='em1.0')
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)


class test_show_interfaces_terse_match(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'fxp0': {'admin_state': 'up',
                 'enabled': True,
                 'link_state': 'up',
                 'oper_status': 'up'},
        'fxp0.0': {'admin_state': 'up',
                   'enabled': True,
                   'link_state': 'up',
                   'oper_status': 'up',
                   'protocol': {'inet': {'172.25.192.114/24': {'local': '172.25.192.114/24'}}}}
    }

    golden_output = {'execute.return_value': '''
        root@junos_vmx1> show interfaces terse | match fxp0 
        fxp0                    up    up
        fxp0.0                  up    up   inet     172.25.192.114/24
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfacesTerseMatch(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesTerseMatch(device=self.device)
        parsed_output = interface_obj.parse(interface='fxp0')
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()

# vim: ft=python et sw=4