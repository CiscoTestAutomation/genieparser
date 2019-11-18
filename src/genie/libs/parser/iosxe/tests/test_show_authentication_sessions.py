#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.show_authentication_sessions import ShowAuthenticationSessions,\
                                                             ShowAuthenticationSessionsInterfaceDetails

class TestShowAuthenticationSessions(unittest.TestCase):
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

    golden_output_3 = {'execute.return_value': '''
        GENIE_c3850_SW#show authentication sessions
        Interface                MAC Address    Method  Domain  Status Fg  Session
        ID
        --------------------------------------------------------------------------------------------
        Gi1/0/1                  0050.b6d6.a8b0 mab     DATA    Auth     0A76060A00000018DD109536
        Gi1/0/2                  b4a8.b968.f35b mab     VOICE   Auth     0A76060A0000000D5323681F

        *Session count = 2*    
    '''}

    golden_parsed_output_3 = {
        'interfaces': {
            'GigabitEthernet1/0/1': {
                'client': {
                    '0050.b6d6.a8b0': {
                        'client': '0050.b6d6.a8b0',
                        'domain': 'DATA',
                        'method': 'mab',
                        'session': {
                            '0A76060A00000018DD109536': {
                                'session_id': '0A76060A00000018DD109536'
                            }
                        },
                        'status': 'Auth'
                    }
                },
                'interface': 'GigabitEthernet1/0/1'
            },
            'GigabitEthernet1/0/2': {
                'client': {
                    'b4a8.b968.f35b': {
                        'client': 'b4a8.b968.f35b',
                        'domain': 'VOICE',
                        'method': 'mab',
                        'session': {
                            '0A76060A0000000D5323681F': {
                                'session_id': '0A76060A0000000D5323681F'
                            }
                        },
                        'status': 'Auth'
                    }
                },
                'interface': 'GigabitEthernet1/0/2'
            }
        },
        'session_count': 2
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
        parsed_output = obj.parse(interface='GigabitEthernet1/7/35')
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_3)
        obj = ShowAuthenticationSessions(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

class TestShowAuthenticationSessionsInterfaceDetails(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_3 = {
        'interfaces': {
            'GigabitEthernet3/0/2': {
                'mac_address': {
                    '0010.0010.0001': {
                        'iif_id': '0x1055240000001F6',
                        'ipv6_address': 'Unknown',
                        'ipv4_address': '192.0.2.1',
                        'user_name': 'genie123',
                        'status': 'Authorized',
                        'domain': 'DATA',
                        'current_policy': 'dot1x_dvlan_reauth_hm', 
                        'oper_host_mode': 'single-host',
                        'oper_control_dir': 'both',
                        'session_timeout': {
                            'type': 'N/A',
                        },
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
        'interfaces': {
            'GigabitEthernet1/0/12': {
                'mac_address': {
                    '0010.0010.0001': {
                        'acct_session_id': 'Unknown',
                        'common_session_id': 'AC14FC0A0000101200E28D62',
                        'current_policy': 'dot1x_dvlan_reauth_hm',
                        'domain': 'DATA',
                        'handle': '0xDB003227',
                        'iif_id': '0x1055240000001F6',
                        'ipv4_address': '192.0.2.1',
                        'ipv6_address': 'Unknown',
                        'local_policies': {
                            'template': {
                                'CRITICAL_VLAN': {
                                    'priority': 170
                                }
                            },
                            'vlan_group': {
                                'vlan': 100
                            }
                        },
                        'method_status': {
                            'mab': {
                                'method': 'mab',
                                'state': 'Running'
                            }
                        },
                        'oper_control_dir': 'both',
                        'oper_host_mode': 'single-host',
                        'session_timeout': {
                            'type': 'N/A',
                        },
                        'status': 'Authorized',
                        'user_name': 'genie123'
                    }
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
    
    golden_output_5 = {'execute.return_value': '''\
        show authentication sessions interface gigabitEthernet 1/12 details
        Load for five secs: 30%/7%; one minute: 24%; five minutes: 23%
        Time source is NTP, 13:51:25.306 EDT Wed Sep 11 2019

                    Interface:  GigabitEthernet1/12
                MAC Address:  6390.c2f7.5d21
                IPv6 Address:  Unknown
                IPv4 Address:  10.1.2.102
                    User-Name:  host/genie.cisco.corp
                    Status:  Authorized
                    Domain:  DATA
            Oper host mode:  single-host
            Oper control dir:  in
            Session timeout:  43200s (local), Remaining: 31799s
            Timeout action:  Reauthenticate
            Restart timeout:  N/A
        Periodic Acct timeout:  N/A
            Session Uptime:  22444s
            Common Session ID:  0A805A0A000012C8FDF2EF40
            Acct Session ID:  Unknown
                    Handle:  0x3F000FC8
            Current Policy:  POLICY_Gi1/12

        Local Policies:
            Service Template: DEFAULT_LINKSEC_POLICY_SHOULD_SECURE (priority 150)
            Security Policy:  Should Secure
            Security Status:  Link Unsecure

        Server Policies:

        Method status list: 
            Method           State 

            dot1x            Authc Success
            mab              Stopped
        '''
    }

    golden_parsed_output_5 = {
        'interfaces': {
            'GigabitEthernet1/12': {
                'mac_address': {
                    '6390.c2f7.5d21': {
                        'acct_session_id': 'Unknown',
                        'common_session_id': '0A805A0A000012C8FDF2EF40',
                        'current_policy': 'POLICY_Gi1/12',
                        'domain': 'DATA',
                        'handle': '0x3F000FC8',
                        'ipv4_address': '10.1.2.102',
                        'ipv6_address': 'Unknown',
                        'local_policies': {
                            'security_policy': 'Should Secure',
                            'security_status': 'Link Unsecure',
                            'template': {
                                'DEFAULT_LINKSEC_POLICY_SHOULD_SECURE': {
                                    'priority': 150
                                }
                            }
                        },
                        'method_status': {
                            'dot1x': {
                                'method': 'dot1x',
                                'state': 'Authc Success'
                            },
                            'mab': {
                                'method': 'mab',
                                'state': 'Stopped'
                            }
                        },
                        'oper_control_dir': 'in',
                        'oper_host_mode': 'single-host',
                        'periodic_acct_timeout': 'N/A',
                        'restart_timeout': 'N/A',
                        'session_timeout': {
                            'remaining': '31799s',
                            'timeout': '43200s',
                            'type': 'local'
                        },
                        'session_uptime': '22444s',
                        'status': 'Authorized',
                        'timeout_action': 'Reauthenticate',
                        'user_name': 'host/genie.cisco.corp'
                    }
                }
            }
        }
    }

    golden_output_6 = {'execute.return_value': '''\

                Switch# show authentication sessions interface gigabitethernet2/0/47
                    Interface:  GigabitEthernet2/0/47
                MAC Address:  0001.1010.0101
                IP Address:  10.1.2.3
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
                IP Address:  10.1.3.5
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

    golden_parsed_output_6 = {
        'interfaces': {
            'GigabitEthernet2/0/47': {
                'mac_address': {
                    '0001.1010.0101': {
                        'acct_session_id': '0x00000002',
                        'authorized_by': 'Guest Vlan',
                        'common_session_id': '0A3462C8000000000002763C',
                        'domain': 'DATA',
                        'handle': '0x25000000',
                        'idle_timeout': 'N/A',
                        'ipv4_address': '10.1.2.3',
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
                            'type': 'N/A'
                        },
                        'status': 'Authz Success',
                        'vlan_policy': '20'
                    },
                    '0005.5e7c.da05': {
                        'acct_session_id': '0x00000003',
                        'authorized_by': 'Authentication Server',
                        'common_session_id': '0A3462C8000000010002A238',
                        'domain': 'VOICE',
                        'handle': '0x91000001',
                        'idle_timeout': 'N/A',
                        'ipv4_address': '10.1.3.5',
                        'method_status': {
                            'dot1x': {
                                'method': 'dot1x',
                                'state': 'Not run'
                            },
                            'mab': {
                                'method': 'mab',
                                'state': 'Authc Success'
                            }
                        },
                        'oper_control_dir': 'both',
                        'oper_host_mode': 'multi-domain',
                        'session_timeout': {
                            'type': 'N/A'
                        },
                        'status': 'Authz Success',
                        'user_name': '00055e7cda05'
                    }
                }
            }
        }
    }

    golden_output_7 = {'execute.return_value': '''
        Genie_SW#show authentication sessions interface GigabitEthernet1/0/1 details
        Interface: GigabitEthernet1/0/1
        IIF-ID: 0x156E4683
        MAC Address: 0050.b6d6.a8b0
        IPv6 Address: fe80::2119:3248:786b:40db
        IPv4 Address: 192.168.1.5
        User-Name: 00-50-B6-D6-A8-B0
        Status: Authorized
        Domain: DATA
        Oper host mode: multi-auth
        Oper control dir: both
        Session timeout: N/A
        Common Session ID: 0A76060A00000018DD109536
        Acct Session ID: 0x0000000f
        Handle: 0x0f00000e
        Current Policy: POLICY_Gi1/0/1    
    '''}

    golden_parsed_output_7 = {
        'interfaces': {
            'GigabitEthernet1/0/1': {
                'mac_address': {
                    '0050.b6d6.a8b0': {
                        'acct_session_id': '0x0000000f',
                        'common_session_id': '0A76060A00000018DD109536',
                        'current_policy': 'POLICY_Gi1/0/1',
                        'domain': 'DATA',
                        'handle': '0x0f00000e',
                        'iif_id': '0x156E4683',
                        'ipv4_address': '192.168.1.5',
                        'ipv6_address': 'fe80::2119:3248:786b:40db',
                        'oper_control_dir': 'both',
                        'oper_host_mode': 'multi-auth',
                        'session_timeout': {'type': 'N/A'},
                        'status': 'Authorized',
                        'user_name': '00-50-B6-D6-A8-B0'
                    }
                }
            }
        }
    }

    golden_output_8 = {'execute.return_value': '''
        GENIE_c3850_SW#show authentication sessions interface GigabitEthernet1/0/2
        detail
                    Interface:  GigabitEthernet1/0/2
                    IIF-ID:  0x17B5937E
                MAC Address:  b4a8.b968.f35b
                IPv6 Address:  Unknown
                IPv4 Address:  1.1.1.1
                    User-Name:  B4-A8-B9-68-F3-5B
                    Status:  Authorized
                    Domain:  VOICE
            Oper host mode:  multi-auth
            Oper control dir:  both
            Session timeout:  N/A
            Common Session ID:  0A76060A0000000D5323681F
            Acct Session ID:  0x00000004
                    Handle:  0x90000003
            Current Policy:  POLICY_Gi1/0/2


        Server Policies:
            *ACS ACL: xGENIEx-Test_ACL_CiscoPhones-e23431ede2*
            URL Redirect ACL: ACLSWITCH_Redirect_v1
            URL Redirect: https://cisco.test.com.us:8446/portal/gateway?_sessionId_=
            ACS ACL: xACSACLx-IP-ACL_MABDefault_V3-5da428a4

        Method status list:
            Method           State
                dot1x           Stopped
                mab           Authc Success
    '''}

    golden_parsed_output_8 = {
        'interfaces': {
            'GigabitEthernet1/0/2': {
                'mac_address': {
                    'b4a8.b968.f35b': {
                        'acct_session_id': '0x00000004',
                        'common_session_id': '0A76060A0000000D5323681F',
                        'current_policy': 'POLICY_Gi1/0/2',
                        'domain': 'VOICE',
                        'handle': '0x90000003',
                        'iif_id': '0x17B5937E',
                        'ipv4_address': '1.1.1.1',
                        'ipv6_address': 'Unknown',
                        'method_status': {
                            'dot1x': {
                                'method': 'dot1x',
                                'state': 'Stopped'
                            },
                            'mab': {
                                'method': 'mab',
                                'state': 'Authc Success'
                            }
                        },
                        'oper_control_dir': 'both',
                        'oper_host_mode': 'multi-auth',
                        'server_policies': {
                            1: {
                                'name': 'ACS ACL',
                                'policies': 'xGENIEx-Test_ACL_CiscoPhones-e23431ede2'
                            },
                            2: {'name': 'URL Redirect ACL',
                                'policies': 'ACLSWITCH_Redirect_v1'
                            },
                            3: {
                                'name': 'URL Redirect',
                                'policies': 'https://cisco.test.com.us:8446/portal/gateway?_sessionId_='
                            },
                            4: {
                                'name': 'ACS ACL',
                                'policies': 'xACSACLx-IP-ACL_MABDefault_V3-5da428a4'
                            }
                        },
                        'session_timeout': {'type': 'N/A'},
                        'status': 'Authorized',
                        'user_name': 'B4-A8-B9-68-F3-5B'
                    }
                }
            }
        }
    }
    def test_empty_3(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAuthenticationSessionsInterfaceDetails(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='GigabitEthernet3/0/2')

    def test_golden_4(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_3)
        obj = ShowAuthenticationSessionsInterfaceDetails(device=self.dev_c3850)
        parsed_output = obj.parse(interface='GigabitEthernet3/0/2')
        self.assertEqual(parsed_output,self.golden_parsed_output_3)

    def test_golden_5(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_4)
        obj = ShowAuthenticationSessionsInterfaceDetails(device=self.dev_c3850)
        parsed_output = obj.parse(interface='GigabitEthernet1/0/12')
        self.assertEqual(parsed_output,self.golden_parsed_output_4)

    def test_golden_6(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_5)
        obj = ShowAuthenticationSessionsInterfaceDetails(device=self.dev_c3850)
        parsed_output = obj.parse(interface='GigabitEthernet1/12')
        self.assertEqual(parsed_output,self.golden_parsed_output_5)

    def test_golden_7(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_6)
        obj = ShowAuthenticationSessionsInterfaceDetails(device=self.dev_c3850)
        parsed_output = obj.parse(interface='GigabitEthernet2/0/47')
        self.assertEqual(parsed_output, self.golden_parsed_output_6)
    
    def test_golden_8(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_7)
        obj = ShowAuthenticationSessionsInterfaceDetails(device=self.dev_c3850)
        parsed_output = obj.parse(interface='GigabitEthernet1/0/1')
        self.assertEqual(parsed_output, self.golden_parsed_output_7)

    def test_golden_9(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_8)
        obj = ShowAuthenticationSessionsInterfaceDetails(device=self.dev_c3850)
        parsed_output = obj.parse(interface='GigabitEthernet1/0/2')
        self.assertEqual(parsed_output, self.golden_parsed_output_8)

if __name__ == '__main__':
    unittest.main()
