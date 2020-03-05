
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_hsrp import ShowHsrpSummary, ShowHsrpAll,\
                                             ShowHsrpDelay

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError


# =================================
# Unit test for 'show hsrp summary'       
# =================================
class test_show_hsrp_summary(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'global_hsrp_bfd': 'enabled',
        'intf_total': 1,
        'nsf': 'enabled',
        'nsf_time': 10,
        'pkt_unknown_groups': 0,
        'total_mts_rx': 85,
        'stats': {
            'total_groups': 3,
            'active': 0,
            'listen': 0,
            'standby': 0,
            'v1_ipv4': 0,
            'v2_ipv4': 3,
            'v2_ipv6': 0,
            'v6_active': 0,
            'v6_listen': 0,
            'v6_standby': 0
        },
        'total_packets': {
            'rx_good': 0,
            'tx_fail': 0,
            'tx_pass': 0,
        }}

    golden_output = {'execute.return_value': '''
        HSRP Summary:

        Extended-hold (NSF) enabled, 10 seconds 
        Global HSRP-BFD enabled

        Total Groups: 3
             Version::    V1-IPV4: 0       V2-IPV4: 3      V2-IPV6: 0   
               State::     Active: 0       Standby: 0       Listen: 0   
               State::  V6-Active: 0    V6-Standby: 0    V6-Listen: 0   

        Total HSRP Enabled interfaces: 1

        Total Packets: 
                     Tx - Pass: 0       Fail: 0
                     Rx - Good: 0      

        Packet for unknown groups: 0

        Total MTS: Rx: 85
        '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        hsrp_summary_obj = ShowHsrpSummary(device=self.device)
        parsed_output = hsrp_summary_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        hsrp_summary_obj = ShowHsrpSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = hsrp_summary_obj.parse()


# =============================
# Unit test for 'show hsrp all'       
# =============================
class test_show_hsrp_all(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output_1 = {
        'Ethernet4/1':
            {'address_family':
                {'ipv4':
                    {'version':
                        {2:
                            {'groups':
                                {0:
                                    {'active_router': 'unknown',
                                    'authentication': 'cisco123',
                                    'configured_priority': 110,
                                    'group_number': 0,
                                    'hsrp_router_state': 'initial',
                                    'hsrp_router_state_reason': 'interface down',
                                    'last_state_change': 'never',
                                    'lower_fwd_threshold': 1,
                                    'num_state_changes': 0,
                                    'preempt': True,
                                    'primary_ipv4_address':
                                        {'address': '192.168.1.254',
                                        'virtual_ip_learn': False},
                                    'priority': 110,
                                    'session_name': 'hsrp-Eth4/1-0',
                                    'standby_router': 'unknown',
                                    'timers':
                                        {'hello_msec_flag': False,
                                        'hello_sec': 1,
                                        'hold_msec_flag': False,
                                        'hold_sec': 3},
                                    'upper_fwd_threshold': 110,
                                    'virtual_mac_address': '0000.0cff.909f',
                                    'virtual_mac_address_status': 'default'},
                                },
                            },
                        },
                    },
                },
            'interface': 'Ethernet4/1',
            'use_bia': False},
        }

    golden_output_1 = {'execute.return_value': '''
        Ethernet4/1 - Group 0 (HSRP-V2) (IPv4)
          Local state is Initial(Interface Down), priority 110 (Cfged 110), may preempt
            Forwarding threshold(for vPC), lower: 1 upper: 110 
          Hellotime 1 sec, holdtime 3 sec
          Virtual IP address is 192.168.1.254 (Cfged)
          Active router is unknown
          Standby router is unknown 
          Authentication MD5, key-string "cisco123"
          Virtual mac address is 0000.0cff.909f (Default MAC)
          0 state changes, last state change never
          IP redundancy name is hsrp-Eth4/1-0 (default)
        '''}

    golden_parsed_output_2 = {
        'Ethernet1/3':
            {'address_family':
                {'ipv4':
                    {'version':
                        {2:
                            {'groups':
                                {0:
                                    {'active_priority': 110,
                                    'active_router': 'local',
                                    'authentication': 'cisco123',
                                    'configured_priority': 110,
                                    'group_number': 0,
                                    'hsrp_router_state': 'active',
                                    'last_state_change': '00:01:43',
                                    'lower_fwd_threshold': 0,
                                    'num_state_changes': 10,
                                    'preempt': True,
                                    'primary_ipv4_address':
                                        {'address': '192.168.1.254',
                                        'virtual_ip_learn': False},
                                    'priority': 110,
                                    'session_name': 'hsrp-Eth1/3-0',
                                    'standby_expire': 2.429,
                                    'standby_ip_address': '192.168.1.2',
                                    'standby_priority': 90,
                                    'standby_router': '192.168.1.2',
                                    'timers': {
                                        'hello_msec_flag': False,
                                        'hello_sec': 1,
                                        'hold_msec_flag': False,
                                        'hold_sec': 3},
                                    'tracked_objects':
                                        {1:
                                            {'object_name': 1,
                                            'priority_decrement': 22,
                                            'status': 'UP'},
                                        },
                                    'upper_fwd_threshold': 110,
                                    'virtual_mac_address': '0000.0cff.909f',
                                    'virtual_mac_address_status': 'default'
                                    },
                                2:
                                    {'active_router': 'unknown',
                                    'authentication': 'cisco',
                                    'configured_priority': 1,
                                    'group_number': 2,
                                    'hsrp_router_state': 'disabled',
                                    'hsrp_router_state_reason': 'virtual ip not cfged',
                                    'last_state_change': 'never',
                                    'lower_fwd_threshold': 0,
                                    'num_state_changes': 0,
                                    'priority': 1,
                                    'session_name': 'hsrp-Eth1/3-2',
                                    'standby_router': 'unknown',
                                    'timers':
                                        {'hello_msec_flag': False,
                                        'hello_sec': 3,
                                        'hold_msec_flag': False,
                                        'hold_sec': 10},
                                    'upper_fwd_threshold': 1,
                                    'virtual_mac_address': '0000.0cff.90a1',
                                    'virtual_mac_address_status': 'default'},
                                },
                            },
                        },
                    },
                'ipv6':
                    {'version':
                        {2:
                            {'groups':
                                {2:
                                    {'active_priority': 100,
                                    'active_router': 'local',
                                    'authentication': 'cisco',
                                    'configured_priority': 100,
                                    'global_ipv6_addresses':
                                        {'2001:db8:7746:fa41::1':
                                            {'address': '2001:db8:7746:fa41::1'
                                      }
                                    },
                                    'group_number': 2,
                                    'hsrp_router_state': 'active',
                                    'last_state_change': '02:43:40',
                                    'link_local_ipv6_address':
                                        {'address': 'fe80::5:73ff:feff:a0a2',
                                        'auto_configure': True},
                                    'lower_fwd_threshold': 0,
                                    'num_state_changes': 2,
                                    'priority': 100,
                                    'secondary_vips': ['2001:db8:7746:fa41::1'],
                                    'session_name': 'hsrp-Eth1/3-2-V6',
                                    'standby_expire': 8.96,
                                    'standby_ipv6_address': 'fe80::20c:29ff:fe69:14bb',
                                    'standby_priority': 90,
                                    'standby_router': 'fe80::20c:29ff:fe69:14bb',
                                    'timers':
                                        {'hello_msec_flag': False,
                                        'hello_sec': 3,
                                        'hold_msec_flag': False,
                                        'hold_sec': 10},
                                    'upper_fwd_threshold': 100,
                                    'virtual_mac_address': '0005.73ff.a0a2',
                                    'virtual_mac_address_status': 'default'},
                                },
                            },
                        },
                    },
                },
            'interface': 'Ethernet1/3',
            'use_bia': False},
            }

    golden_output_2 = {'execute.return_value': '''
      Ethernet1/3 - Group 0 (HSRP-V2) (IPv4)
        Local state is Active, priority 110 (Cfged 110), may preempt
          Forwarding threshold(for vPC), lower: 0 upper: 110 
        Hellotime 1 sec, holdtime 3 sec
        Next hello sent in 0.502000 sec(s)
        Virtual IP address is 192.168.1.254 (Cfged)
        Active router is local
        Standby router is 192.168.1.2 , priority 90 expires in 2.429000 sec(s)
        Authentication MD5, key-string "cisco123"
        Virtual mac address is 0000.0cff.909f (Default MAC)
        10 state changes, last state change 00:01:43
          Track object 1 state UP decrement 22        
        IP redundancy name is hsrp-Eth1/3-0 (default)

      Ethernet1/3 - Group 2 (HSRP-V2) (IPv4)
        Local state is Disabled(Virtual IP not cfged), priority 1 (Cfged 1)
          Forwarding threshold(for vPC), lower: 0 upper: 1 
        Hellotime 3 sec, holdtime 10 sec
        Virtual IP address is unknown 
        Active router is unknown
        Standby router is unknown 
        Authentication text "cisco"
        Virtual mac address is 0000.0cff.90a1 (Default MAC)
        0 state changes, last state change never
        IP redundancy name is hsrp-Eth1/3-2 (default)

      Ethernet1/3 - Group 2 (HSRP-V2) (IPv6)
        Local state is Active, priority 100 (Cfged 100)
          Forwarding threshold(for vPC), lower: 0 upper: 100 
        Hellotime 3 sec, holdtime 10 sec
        Next hello sent in 0.455000 sec(s)
        Virtual IP address is fe80::5:73ff:feff:a0a2 (Auto)
        Active router is local
        Standby router is fe80::20c:29ff:fe69:14bb , priority 90 expires in 8.960000 sec(s)
        Authentication text "cisco"
        Virtual mac address is 0005.73ff.a0a2 (Default MAC)
        2 state changes, last state change 02:43:40
        IP redundancy name is hsrp-Eth1/3-2-V6 (default)
        Secondary VIP(s):
                        2001:db8:7746:fa41::1
      '''}

    golden_parsed_output_3 = {
        'Ethernet1/3': 
        {'address_family': 
          {'ipv4': 
            {'version': 
              {1: 
                {'groups': 
                  {1: 
                    {'active_router': 'local',
                    'active_priority': 100,
                    'authentication': 'cisco',
                    'configured_priority': 100,
                    'group_number': 1,
                    'last_state_change': '00:05:57',
                    'hsrp_router_state': 'active',
                    'lower_fwd_threshold': 0,
                    'num_state_changes': 2,
                    'primary_ipv4_address': 
                        {'address': '192.168.255.1',
                        'virtual_ip_learn': False},
                    'priority': 100,
                    'session_name': 'hsrp-Eth1/3-1',
                    'standby_router': 'unknown',
                    'timers': 
                        {'hello_msec_flag': False,
                        'hello_sec': 3,
                        'hold_msec_flag': False,
                        'hold_sec': 10},
                    'upper_fwd_threshold': 100,
                    'virtual_mac_address': '0000.0cff.b308',
                    'virtual_mac_address_status': 'default'}}}}}},
        'interface': 'Ethernet1/3',
        'use_bia': False}}

    golden_output_3 = {'execute.return_value': '''
        nx1# show hsrp all
        Ethernet1/3 - Group 1 (HSRP-V1) (IPv4)
          Local state is Active, priority 100 (Cfged 100)
            Forwarding threshold(for vPC), lower: 0 upper: 100
          Hellotime 3 sec, holdtime 10 sec
          Next hello sent in 0.400000 sec(s)
          Virtual IP address is 192.168.255.1 (Cfged)
          Active router is local
          Standby router is unknown
          Authentication text "cisco"
          Virtual mac address is 0000.0cff.b308 (Default MAC)
          2 state changes, last state change 00:05:57
          IP redundancy name is hsrp-Eth1/3-1 (default)
        '''}

    golden_parsed_output_4 = {}

    golden_output_4 = {'execute.return_value': '''
        +++ CE1: executing command 'show hsrp all' +++
        show hsrp all

                      ^
        % Invalid command at '^' marker.
        '''}

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        hsrp_all_obj = ShowHsrpAll(device=self.device)
        parsed_output = hsrp_all_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        hsrp_all_obj = ShowHsrpAll(device=self.device)
        parsed_output = hsrp_all_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        hsrp_all_obj = ShowHsrpAll(device=self.device)
        parsed_output = hsrp_all_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_3)

    def test_golden_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowHsrpAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        hsrp_all_obj = ShowHsrpAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = hsrp_all_obj.parse()


# ===============================
# Unit test for 'show hsrp delay'
# ===============================
class test_show_hsrp_delay(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'GigabitEthernet1': {
            'delay': {
                'minimum_delay': 99,
                'reload_delay': 888,
            }
        },
        'GigabitEthernet3': {
            'delay': {
                'minimum_delay': 1,
                'reload_delay': 5,
            }
        }
    }

    golden_output = {'execute.return_value': '''
        Interface          Minimum Reload
        GigabitEthernet1   99      888
        GigabitEthernet3   1       5
        '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        hsrp_delay_obj = ShowHsrpDelay(device=self.device)
        parsed_output = hsrp_delay_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        hsrp_delay_obj = ShowHsrpDelay(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = hsrp_delay_obj.parse()

if __name__ == '__main__':
    unittest.main()

# vim: ft=python et sw=4
