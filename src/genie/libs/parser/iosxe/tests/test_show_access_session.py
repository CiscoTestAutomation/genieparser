#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.show_access_session import ShowAccessSession,\
                                        ShowAccessSessionInterfaceDetails


class test_show_access_session(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'session_count': 1,
        'interfaces': {
            'GigabitEthernet1/0/1': {
                'interface': 'GigabitEthernet1/0/1',
                'client': {
                    'f4cf.beef.acc1': {
                        'client': 'f4cf.beef.acc1',
                        'method': 'dot1x',
                        'domain': 'DATA',
                        'status': 'authenticator',
                        'session': {
                            '000000000000000BB6FC9EAF': {
                                'session_id': '000000000000000BB6FC9EAF',
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Interface                MAC Address    Method  Domain  Status Fg  Session ID
        --------------------------------------------------------------------------------------------
        Gi1/0/1                  f4cf.beef.acc1 dot1x   DATA    Auth        000000000000000BB6FC9EAF

        Session count = 1
    '''
    }
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAccessSession(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowAccessSession(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

class test_show_access_session_interface_details(unittest.TestCase):
    maxDiff = None
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet1/0/21': {
                'mac_address': {
                    '0800.37c8.2dbc': {
                        'iif_id': '0x105B0C0000005F5',
                        'ipv6_address': 'Unknown',
                        'ipv4_address': '10.4.1.1',
                        'user_name': 'genie123',
                        'status': 'Authorized',
                        'domain': 'DATA',
                        'current_policy': 'Test_DOT1X-DEFAULT_V1', 
                        'oper_host_mode': 'multi-auth',
                        'oper_control_dir': 'both',
                        'session_timeout': {
                            'type': 'N/A'
                        },
                        'restart_timeout': 'N/A',
                        'common_session_id': '0A7820020000413CCCE37640',
                        'acct_session_id': '0x00007EAF',
                        'handle': '0x7100056D',
                        'server_policies': {
                            1: {
                                'name': 'ACS ACL',
                                'policies': 'xACSACLx-IP-Test_ACL_XeroxPrinters_v1-597a95c4'
                            }
                        },
                        'method_status': {
                            'dot1x': {
                                'method': 'dot1x',
                                'state': 'Stopped'
                            },
                            'mab': {
                                'method': 'mab',
                                'state': 'Authc Success'
                            }
                        }
                    }
                }
            }
        }
    }
        
    golden_output = {'execute.return_value': '''\
        dev1#show access-session interface Gi1/0/21 details
        Interface: GigabitEthernet1/0/21
        IIF-ID: 0x105B0C0000005F5
        MAC Address: 0800.37c8.2dbc
        IPv6 Address: Unknown
        IPv4 Address: 10.4.1.1
        User-Name: genie123
        Status: Authorized
        Domain: DATA
        Oper host mode: multi-auth
        Oper control dir: both
        Session timeout: N/A
        Restart timeout: N/A
        Common Session ID: 0A7820020000413CCCE37640
        Acct Session ID: 0x00007EAF
        Handle: 0x7100056D
        Current Policy: Test_DOT1X-DEFAULT_V1
        
        Server Policies:
        ACS ACL: xACSACLx-IP-Test_ACL_XeroxPrinters_v1-597a95c4
        
        Method status list:
        Method State
        dot1x Stopped
        mab Authc Success
    '''
    }
    
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowAccessSessionInterfaceDetails(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='GigabitEthernet1/0/21')

    def test_golden(self):
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowAccessSessionInterfaceDetails(device=self.dev_c3850)
        parsed_output = obj.parse(interface='GigabitEthernet1/0/21')
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()

