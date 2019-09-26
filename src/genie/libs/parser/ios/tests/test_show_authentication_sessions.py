#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.ios.show_authentication_sessions import ShowAuthenticationSessions,\
                                                             ShowAuthenticationSessionsInterface
                                                     

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

class test_show_authentication_sessions_interface(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')

    empty_output = {'execute.return_value': ''}


    golden_parsed_output_1 = {
        'interfaces': {
            'GigabitEthernet2/0/47': {
                'mac_address': {
                    'Unknown': {
                        'ipv4_address': 'Unknown',
                        'status': 'Authz Success',
                        'domain': 'DATA',
                        'oper_host_mode': 'multi-host',
                        'oper_control_dir': 'both',
                        'authorized_by': 'Guest Vlan',
                        'vlan_policy': '20',
                        'session_timeout': {
                            'type': 'N/A',
                        },
                        'idle_timeout': 'N/A',
                        'common_session_id': '0A3462C8000000000002763C',
                        'acct_session_id': '0x00000002',
                        'handle': '0x25000000',
                        'method_status': {
                            'mab': {
                                'method': 'mab',
                                'state': 'Failed over',
                            },
                            'dot1x': {
                                'method': 'dot1x',
                                'state': 'Failed over',
                            },
                        },
                    }
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        show authentication sessions interface GigabitEthernet2/0/47

            Interface:  GigabitEthernet2/0/47
          MAC Address:  Unknown
           IP Address:  Unknown
               Status:  Authz Success
               Domain:  DATA
       Oper host mode:  multi-host
     Oper control dir:  both
        Authorized By:  Guest Vlan
          Vlan Policy:  20
      Session timeout:  N/A
         Idle timeout:  N/A
    Common Session ID:  0A3462C8000000000002763C
      Acct Session ID:  0x00000002
               Handle:  0x25000000
Runnable methods list:
       Method   State
       mab      Failed over
       dot1x    Failed over
        '''
    }

    golden_output_2 = {'execute.return_value': '''\

        Switch# show authentication sessions interface gigabitethernet2/0/47
            Interface:  GigabitEthernet2/0/47
          MAC Address:  Unknown
           IP Address:  Unknown
               Status:  Authz Success
               Domain:  DATA
       Oper host mode:  multi-host
     Oper control dir:  both
        Authorized By:  Guest Vlan
          Vlan Policy:  20
      Session timeout:  N/A
         Idle timeout:  N/A
    Common Session ID:  0A3462C8000000000002763C
      Acct Session ID:  0x00000002
               Handle:  0x25000000
Runnable methods list:
       Method   State
       mab      Failed over
       dot1x    Failed over
----------------------------------------
            Interface:  GigabitEthernet2/0/47
          MAC Address:  0005.5e7c.da05
           IP Address:  Unknown
            User-Name:  00055e7cda05
               Status:  Authz Success
               Domain:  VOICE
       Oper host mode:  multi-domain
     Oper control dir:  both
        Authorized By:  Authentication Server
      Session timeout:  N/A
         Idle timeout:  N/A
    Common Session ID:  0A3462C8000000010002A238
      Acct Session ID:  0x00000003
               Handle:  0x91000001
Runnable methods list:
       Method   State
       mab      Authc Success
       dot1x    Not run

    '''
    }
    golden_parsed_output_2 = {
        'interfaces': {
            'GigabitEthernet2/0/47': {
                'mac_address': {
                    '0005.5e7c.da05': {
                        'acct_session_id': '0x00000003',
                        'authorized_by': 'Authentication '
                        'Server',
                        'common_session_id': '0A3462C8000000010002A238',
                        'domain': 'VOICE',
                        'handle': '0x91000001',
                        'idle_timeout': 'N/A',
                        'ipv4_address': 'Unknown',
                        'method_status': {
                            'dot1x': {
                                'method': 'dot1x',
                                'state': 'Not '
                                'run'
                            },
                            'mab': {
                                'method': 'mab',
                                'state': 'Authc Success'
                            }
                        },
                        'oper_control_dir': 'both',
                        'oper_host_mode': 'multi-domain',
                        'session_timeout': {
                            'type': 'N/A',
                        },
                        'status': 'Authz '
                        'Success',
                        'user_name': '00055e7cda05'
                    },
                    'Unknown': {
                        'acct_session_id': '0x00000002',
                        'authorized_by': 'Guest Vlan',
                        'common_session_id': '0A3462C8000000000002763C',
                        'domain': 'DATA',
                        'handle': '0x25000000',
                        'idle_timeout': 'N/A',
                        'ipv4_address': 'Unknown',
                        'method_status': {
                            'dot1x': {
                                'method': 'dot1x',
                                'state': 'Failed over'
                            },
                            'mab': {
                                'method': 'mab',
                                'state': 'Failed over'
                            }
                        },
                        'oper_control_dir': 'both',
                        'oper_host_mode': 'multi-host',
                        'session_timeout': {
                            'type': 'N/A',
                        },
                        'status': 'Authz '
                        'Success',
                        'vlan_policy': '20'
                    }
                }
            }
        }
    }
    
    def test_authentication_sessions_interface_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAuthenticationSessionsInterface(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='GigabitEthernet3/0/2')

    def test_authentication_sessions_interface_1_output(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        obj = ShowAuthenticationSessionsInterface(device=self.dev_c3850)
        parsed_output = obj.parse(interface='GigabitEthernet2/0/47')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_authentication_sessions_interface_multi_ouput(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_2)
        obj = ShowAuthenticationSessionsInterface(device=self.dev_c3850)
        parsed_output = obj.parse(interface='GigabitEthernet2/0/47')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

if __name__ == '__main__':
    unittest.main()
