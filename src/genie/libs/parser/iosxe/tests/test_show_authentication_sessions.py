#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.show_authentication_sessions import ShowAuthenticationSessions,\
                                                             ShowAuthenticationSessionsInterfaceDetails

class test_show_authentication_sessions(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet1/0/48': {
                'interface': 'GigabitEthernet1/0/48',
                'client': {
                    '0015.63b0.f676': {
                        'client': '0015.63b0.f676',
                        'method': 'dot1x',
                        'domain': 'DATA',
                        'status': 'Authz Success',
                        'session': {
                            '0A3462B1000000102983C05C': {
                                'session_id': '0A3462B1000000102983C05C',
                            }
                        }
                    }
                }
            },
            'GigabitEthernet1/0/5': {
                'interface': 'GigabitEthernet1/0/5',
                'client': {
                    '000f.23c4.a401': {
                        'client': '000f.23c4.a401',
                        'method': 'mab',
                        'domain': 'DATA',
                        'status': 'Authz Success',
                        'session': {
                            '0A3462B10000000D24F80B58': {
                                'session_id': '0A3462B10000000D24F80B58',
                            }
                        }
                    }
                }
            },
            'GigabitEthernet1/0/7': {
                'interface': 'GigabitEthernet1/0/7',
                'client': {
                    '0014.bf5d.d26d': {
                        'client': '0014.bf5d.d26d',
                        'method': 'dot1x',
                        'domain': 'DATA',
                        'status': 'Authz Success',
                        'session': {
                            '0A3462B10000000E29811B94': {
                                'session_id': '0A3462B10000000E29811B94',
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        show authentication sessions
        Interface    MAC Address     Method   Domain   Status         Session ID
        Gi1/0/48     0015.63b0.f676  dot1x    DATA     Authz Success  0A3462B1000000102983C05C
        Gi1/0/5      000f.23c4.a401  mab      DATA     Authz Success  0A3462B10000000D24F80B58
        Gi1/0/7      0014.bf5d.d26d  dot1x    DATA     Authz Success  0A3462B10000000E29811B94
    '''
    }

    golden_parsed_output_2 = {
        'interfaces': {
            'GigabitEthernet1/7/35': {
                'interface': 'GigabitEthernet1/7/35',
                'client': {
                    '0000.0022.2222': {
                        'client': '0000.0022.2222',
                        'method': 'dot1x',
                        'domain': 'UNKNOWN',
                        'status': 'Auth',
                        'session': {
                            '141927640000000E0B40EDB0': {
                                'session_id': '141927640000000E0B40EDB0',
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''\
        show authentication sessions interface GigabitEthernet1/7/35

        Interface Identifier     Method Domain  Status Fg Session ID
        -----------------------------------------------------------------------------
        Gi1/7/35  0000.0022.2222 dot1x  UNKNOWN Auth      141927640000000E0B40EDB0
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAuthenticationSessions(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowAuthenticationSessions(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_2)
        obj = ShowAuthenticationSessions(device=self.dev_c3850)
        parsed_output = obj.parse(intf='GigabitEthernet1/7/35')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

class test_show_authentication_sessions_interface_details(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_3 = {
        'authentication_sessions': {
            'index': {
                1: {
                    'interface': 'GigabitEthernet3/0/2',
                    'iif_id': '0x1055240000001F6',
                    'mac_address': '0010.0010.0001', 
                    'ipv6_address': 'Unknown',
                    'ipv4_address': '192.0.2.1',
                    'user_name': 'genie123',
                    'status': 'Authorized',
                    'domain': 'DATA',
                    'current_policy': 'dot1x_dvlan_reauth_hm', 
                    'oper_host_mode': 'single-host',
                    'oper_control_dir': 'both',
                    'session_timeout': 'N/A',
                    'common_session_id': 'AC14FC0A0000101200E28D62',
                    'acct_session_id': 'Unknown',
                    'handle': '0xDB003227',
                    'local_policies': {
                        'template': {
                            'CRITICAL_VLAN': {
                                'priority': 150,
                            }
                        },
                        'vlan_group': {
                            'vlan': 130,
                        }
                    },
                    'method_status': {
                        'dot1x': {
                            'method': 'dot1x',
                            'state': 'Authc Failed',
                        }
                    },
                }
            }
        }
    }

    golden_output_3 = {'execute.return_value': '''\
        show authentication sessions interface GigabitEthernet3/0/2 details

                Interface:  GigabitEthernet3/0/2
                   IIF-ID:  0x1055240000001F6 
              MAC Address:  0010.0010.0001
             IPv6 Address:  Unknown
             IPv4 Address:  192.0.2.1
                User-Name:  genie123
                   Status:  Authorized
                   Domain:  DATA
           Oper host mode:  single-host
         Oper control dir:  both
          Session timeout:  N/A
        Common Session ID:  AC14FC0A0000101200E28D62
          Acct Session ID:  Unknown
                   Handle:  0xDB003227
           Current Policy:  dot1x_dvlan_reauth_hm

        Local Policies:
                 Template: CRITICAL_VLAN (priority 150)
               Vlan Group:  Vlan: 130

        Method status list:
           Method           State
           dot1x            Authc Failed
        '''
    }

    golden_parsed_output_4 = {
        'authentication_sessions': {
            'index': {
                1: {
                    'interface': 'GigabitEthernet1/0/12',
                    'iif_id': '0x1055240000001F6',
                    'mac_address': '0010.0010.0001',   
                    'ipv6_address': 'Unknown',
                    'ipv4_address': '192.0.2.1',
                    'user_name': 'genie123',
                    'status': 'Authorized',
                    'domain': 'DATA',
                    'current_policy': 'dot1x_dvlan_reauth_hm',
                    'oper_host_mode': 'single-host',
                    'oper_control_dir': 'both',
                    'session_timeout': 'N/A',
                    'common_session_id': 'AC14FC0A0000101200E28D62',
                    'acct_session_id': 'Unknown',
                    'handle': '0xDB003227',
                    'local_policies': {
                        'template': {
                            'CRITICAL_VLAN': {
                                'priority': 170,
                            }
                        },
                        'vlan_group': {
                            'vlan': 100,
                        }
                    },
                    'method_status': {
                        'mab': {
                            'method': 'mab',
                            'state': 'Running',
                        }
                    },
                }
            }
        }
    }

    golden_output_4 = {'execute.return_value': '''\
        show authentication sessions interface GigabitEthernet1/0/12 details

                Interface:  GigabitEthernet1/0/12
                   IIF-ID:  0x1055240000001F6 
              MAC Address:  0010.0010.0001
             IPv6 Address:  Unknown
             IPv4 Address:  192.0.2.1
                User-Name:  genie123
                   Status:  Authorized
                   Domain:  DATA
           Oper host mode:  single-host
         Oper control dir:  both
          Session timeout:  N/A
        Common Session ID:  AC14FC0A0000101200E28D62
          Acct Session ID:  Unknown
                   Handle:  0xDB003227
           Current Policy:  dot1x_dvlan_reauth_hm

        Local Policies:
                 Template: CRITICAL_VLAN (priority 170)
               Vlan Group:  Vlan: 100

        Method status list:
           Method           State
           mab              Running
        '''
    }
    def test_empty_3(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAuthenticationSessionsInterfaceDetails(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(intf='GigabitEthernet3/0/2')

    def test_golden_4(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_3)
        obj = ShowAuthenticationSessionsInterfaceDetails(device=self.dev_c3850)
        parsed_output = obj.parse(intf='GigabitEthernet3/0/2')
        self.assertEqual(parsed_output,self.golden_parsed_output_3)

    def test_golden_5(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_4)
        obj = ShowAuthenticationSessionsInterfaceDetails(device=self.dev_c3850)
        parsed_output = obj.parse(intf='GigabitEthernet1/0/12')
        self.assertEqual(parsed_output,self.golden_parsed_output_4)

if __name__ == '__main__':
    unittest.main()