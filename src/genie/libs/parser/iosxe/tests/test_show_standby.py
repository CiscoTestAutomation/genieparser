
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.iosxe.show_standby import ShowStandbyInternal,\
                                      ShowStandbyAll,\
                                      ShowStandbyDelay

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError


# =========================================
#   Unit test for 'show standby internal'
# =========================================

class test_show_standby_internal(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'hsrp_common_process_state': 'not running',
        'hsrp_ha_state': 'capable',
        'hsrp_ipv4_process_state': 'not running',
        'hsrp_ipv6_process_state': 'not running',
        'hsrp_timer_wheel_state': 'running',
        'mac_address_table': {
            166: {
                'group': 10,
                'interface': 'gi2/0/3',
                'mac_address': '0000.0cff.b311'},
            169: {
                'group': 5,
                'interface': 'gi1/0/1',
                'mac_address': '0000.0cff.b30c'},
            172: {
                'group': 0,
                'interface': 'gi2/0/3',
                'mac_address': '0000.0cff.b307'},
            173: {
                'group': 1,
                'interface': 'gi2/0/3',
                'mac_address': '0000.0cff.b308'}},
        'msgQ_max_size': 0,
        'msgQ_size': 0,
        'v3_to_v4_transform': 'disabled',
        'virtual_ip_hash_table': {
            'ipv6': {
                78: {
                    'group': 20,
                    'interface': 'gi1',
                    'ip': '2001:DB8:10:1:1::254',
                }
            },
            'ipv4': {
                103: {'group': 0,
                      'interface': 'gi1/0/1',
                      'ip': '192.168.1.254'},
                106: {'group': 10,
                      'interface': 'gi1/0/2',
                      'ip': '192.168.2.254'}}}}            


    golden_output = {'execute.return_value': '''
        HSRP common process not running
          MsgQ size 0, max 0
        HSRP IPv4 process not running
        HSRP IPv6 process not running
        HSRP Timer wheel running
        HSRP HA capable, v3 to v4 transform disabled

        HSRP virtual IP Hash Table (global)
        103 192.168.1.254                    Gi1/0/1    Grp 0
        106 192.168.2.254                    Gi1/0/2    Grp 10

        HSRP virtual IPv6 Hash Table (global)
        78  2001:DB8:10:1:1::254             Gi1        Grp 20

        HSRP MAC Address Table
        169 Gi1/0/1 0000.0cff.b30c
            Gi1/0/1 Grp 5
        166 Gi2/0/3 0000.0cff.b311
            Gi2/0/3 Grp 10
        172 Gi2/0/3 0000.0cff.b307
            Gi2/0/3 Grp 0
        173 Gi2/0/3 0000.0cff.b308
            Gi2/0/3 Grp 1
    '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        standby_internal_obj = ShowStandbyInternal(device=self.device)
        parsed_output = standby_internal_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        standby_internal_obj = ShowStandbyInternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = standby_internal_obj.parse()


# ======================================
#   Unit test for 'show standby all'
# ======================================

class test_show_standby_all(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = \
    {
    'GigabitEthernet1/0/1': {
      'address_family': {
        'ipv4': {
          'version': {
            2: {
              'groups': {
                0: {
                  'active_router': 'local',
                  'authentication': '5',
                  'authentication_type': 'MD5',
                  'default_priority': 100,
                  'group_number': 0,
                  'hsrp_router_state': 'active',
                  'last_state_change': '1w0d',
                  'local_virtual_mac_address': '0000.0cff.909f',
                  'local_virtual_mac_address_conf': 'v2 '
                  'default',
                  'preempt': True,
                  'preempt_min_delay': 5,
                  'preempt_reload_delay': 10,
                  'preempt_sync_delay': 20,
                  'primary_ipv4_address': {
                    'address': '192.168.1.254'
                  },
                  'priority': 100,
                  'session_name': 'hsrp-Gi1/0/1-0',
                  'standby_ip_address': '192.168.1.2',
                  'standby_router': '192.168.1.2',
                  'standby_priority': 100,
                  'standby_expires_in': 10.624,
                  'statistics': {
                    'num_state_changes': 8
                  },
                  'timers': {
                    'hello_msec_flag': False,
                    'hello_sec': 5,
                    'hold_msec_flag': False,
                    'hold_sec': 20,
                    'next_hello_sent': 2.848
                  },
                  'virtual_mac_address': '0000.0cff.909f',
                  'virtual_mac_address_mac_in_use': True
                  }
                }
              }
            }
          }
      },
      'interface': 'GigabitEthernet1/0/1',
      'redirects_disable': False,
      'use_bia': False
    },
    'GigabitEthernet1/0/2': {
      'address_family': {
        'ipv4': {
          'version': {
            1: {
              'groups': {
                10: {
                  'active_router': 'unknown',
                  'authentication': 'cisco123',
                  'authentication_type': 'MD5',
                  'configured_priority': 110,
                  'group_number': 10,
                  'hsrp_router_state': 'disabled',
                  'local_virtual_mac_address': '0000.0cff.b311',
                  'local_virtual_mac_address_conf': 'v1 '
                  'default',
                  'preempt': True,
                  'primary_ipv4_address': {
                    'address': 'unknown'
                  },
                  'priority': 110,
                  'session_name': 'hsrp-Gi1/0/2-10',
                  'standby_ip_address': 'unknown',
                  'standby_router': 'unknown',
                  'timers': {
                    'hello_msec_flag': False,
                    'hello_sec': 3,
                    'hold_msec_flag': False,
                    'hold_sec': 10
                  },
                  'virtual_mac_address': 'unknown',
                  'virtual_mac_address_mac_in_use': False
                  }
                }
              }
            }
          }
      },
      'interface': 'GigabitEthernet1/0/2',
      'redirects_disable': False,
      'use_bia': False
    },
    'GigabitEthernet3': {
      'address_family': {
        'ipv4': {
          'version': {
            1: {
              'groups': {
                10: {
                  'active_expires_in': 0.816,
                  'active_ip_address': '10.1.2.1',
                  'active_router': '10.1.2.1',
                  'active_router_priority': 120,
                  'configured_priority': 110,
                  'group_number': 10,
                  'hsrp_router_state': 'standby',
                  'local_virtual_mac_address': '0000.0cff.b311',
                  'local_virtual_mac_address_conf': 'v1 '
                  'default',
                  'preempt': True,
                  'primary_ipv4_address': {
                    'address': '10.1.2.254'
                  },
                  'priority': 110,
                  'session_name': 'hsrp-Gi3-10',
                  'standby_router': 'local',
                  'timers': {
                    'hello_msec_flag': False,
                    'hello_sec': 3,
                    'hold_msec_flag': False,
                    'hold_sec': 10,
                    'next_hello_sent': 2.096
                  },
                  'virtual_mac_address': '0050.56ff.c8ce',
                  'virtual_mac_address_mac_in_use': False
                  }
                }
              }
            }
          }
      },
      'interface': 'GigabitEthernet3',
      'redirects_disable': False,
      'use_bia': False
      }
    }

    golden_parsed_output2 = \
    {
    'GigabitEthernet1/0/1.100': {
      'address_family': {
        'ipv4': {
          'version': {
            2: {
              'groups': {
                0: {
                  'active_router': 'local',
                  'authentication': '5',
                  'authentication_type': 'MD5',
                  'default_priority': 100,
                  'group_number': 0,
                  'hsrp_router_state': 'active',
                  'last_state_change': '1w0d',
                  'local_virtual_mac_address': '0000.0cff.909f',
                  'local_virtual_mac_address_conf': 'v2 '
                  'default',
                  'preempt': True,
                  'preempt_min_delay': 5,
                  'preempt_reload_delay': 10,
                  'preempt_sync_delay': 20,
                  'primary_ipv4_address': {
                    'address': '192.168.1.254'
                  },
                  'priority': 100,
                  'session_name': 'hsrp-Gi1/0/1-0',
                  'standby_ip_address': '192.168.1.2',
                  'standby_router': '192.168.1.2',
                  'standby_priority': 100,
                  'standby_expires_in': 10.624,
                  'statistics': {
                    'num_state_changes': 8
                  },
                  'timers': {
                    'hello_msec_flag': False,
                    'hello_sec': 5,
                    'hold_msec_flag': False,
                    'hold_sec': 20,
                    'next_hello_sent': 2.848
                  },
                  'virtual_mac_address': '0000.0cff.909f',
                  'virtual_mac_address_mac_in_use': True
                  }
                }
              }
            }
          }
      },
      'interface': 'GigabitEthernet1/0/1.100',
      'redirects_disable': False,
      'use_bia': False
    },
    'GigabitEthernet1/0/1.200': {
      'address_family': {
        'ipv4': {
          'version': {
            1: {
              'groups': {
                10: {
                  'active_router': 'unknown',
                  'authentication': 'cisco123',
                  'authentication_type': 'MD5',
                  'configured_priority': 110,
                  'group_number': 10,
                  'hsrp_router_state': 'disabled',
                  'local_virtual_mac_address': '0000.0cff.b311',
                  'local_virtual_mac_address_conf': 'v1 '
                  'default',
                  'preempt': True,
                  'primary_ipv4_address': {
                    'address': 'unknown'
                  },
                  'priority': 110,
                  'session_name': 'hsrp-Gi1/0/2-10',
                  'standby_ip_address': 'unknown',
                  'standby_router': 'unknown',
                  'timers': {
                    'hello_msec_flag': False,
                    'hello_sec': 3,
                    'hold_msec_flag': False,
                    'hold_sec': 10
                  },
                  'virtual_mac_address': 'unknown',
                  'virtual_mac_address_mac_in_use': False
                  }
                }
              }
            }
          }
      },
      'interface': 'GigabitEthernet1/0/1.200',
      'redirects_disable': False,
      'use_bia': False
    }
    }


    golden_output = {'execute.return_value': '''
        GigabitEthernet1/0/1 - Group 0 (version 2)
          State is Active
            8 state changes, last state change 1w0d
            Track object 1 (unknown)
          Virtual IP address is 192.168.1.254
          Active virtual MAC address is 0000.0cff.909f (MAC In Use)
            Local virtual MAC address is 0000.0cff.909f (v2 default)
          Hello time 5 sec, hold time 20 sec
            Next hello sent in 2.848 secs
          Authentication MD5, key-chain "5"
          Preemption enabled, delay min 5 secs, reload 10 secs, sync 20 secs
          Active router is local
          Standby router is 192.168.1.2, priority 100 (expires in 10.624 sec)
          Priority 100 (default 100)
          Group name is "hsrp-Gi1/0/1-0" (default)
        GigabitEthernet1/0/2 - Group 10
          State is Disabled
          Virtual IP address is unknown
          Active virtual MAC address is unknown (MAC Not In Use)
            Local virtual MAC address is 0000.0cff.b311 (v1 default)
          Hello time 3 sec, hold time 10 sec
          Authentication MD5, key-chain "cisco123"
          Preemption enabled
          Active router is unknown
          Standby router is unknown
          Priority 110 (configured 110)
          Group name is "hsrp-Gi1/0/2-10" (default)
        GigabitEthernet3 - Group 10
          State is Standby
            1 state change, last state change 00:00:08
          Virtual IP address is 10.1.2.254
          Active virtual MAC address is 0050.56ff.c8ce (MAC Not In Use)
            Local virtual MAC address is 0000.0cff.b311 (v1 default)
          Hello time 3 sec, hold time 10 sec
            Next hello sent in 2.096 secs
          Preemption enabled
          Active router is 10.1.2.1, priority 120 (expires in 0.816 sec)
          Standby router is local
          Priority 110 (configured 110)
          Group name is "hsrp-Gi3-10" (default)
        '''}

    golden_output2 = {'execute.return_value': '''
        GigabitEthernet1/0/1.100 - Group 0 (version 2)
          State is Active
            8 state changes, last state change 1w0d
            Track object 1 (unknown)
          Virtual IP address is 192.168.1.254
          Active virtual MAC address is 0000.0cff.909f (MAC In Use)
            Local virtual MAC address is 0000.0cff.909f (v2 default)
          Hello time 5 sec, hold time 20 sec
            Next hello sent in 2.848 secs
          Authentication MD5, key-chain "5"
          Preemption enabled, delay min 5 secs, reload 10 secs, sync 20 secs
          Active router is local
          Standby router is 192.168.1.2, priority 100 (expires in 10.624 sec)
          Priority 100 (default 100)
          Group name is "hsrp-Gi1/0/1-0" (default)
        GigabitEthernet1/0/1.200 - Group 10
          State is Disabled
          Virtual IP address is unknown
          Active virtual MAC address is unknown (MAC Not In Use)
            Local virtual MAC address is 0000.0cff.b311 (v1 default)
          Hello time 3 sec, hold time 10 sec
          Authentication MD5, key-chain "cisco123"
          Preemption enabled
          Active router is unknown
          Standby router is unknown
          Priority 110 (configured 110)
          Group name is "hsrp-Gi1/0/2-10" (default)
        '''}
    

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        standby_all_obj = ShowStandbyAll(device=self.device)
        parsed_output = standby_all_obj.parse()
        #import pprint ; pprint.pprint(parsed_output)
        self.assertEqual(parsed_output,self.golden_parsed_output)
    
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        standby_all_obj2 = ShowStandbyAll(device=self.device)
        parsed_output2 = standby_all_obj2.parse()
        #import pprint ; pprint.pprint(parsed_output)
        self.assertEqual(parsed_output2,self.golden_parsed_output2)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        standby_all_obj = ShowStandbyAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = standby_all_obj.parse()
    
# =========================================
#   Unit test for 'show standby delay'
# =========================================

class test_show_standby_delay(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = \
    {
      "GigabitEthernet1": {
        "delay": {
          "minimum_delay": 99,
          "reload_delay": 888
        }
      }
    }

    golden_output = {'execute.return_value': '''
    Interface          Minimum Reload 
    GigabitEthernet1   99      888   
    '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        standby_delay_obj = ShowStandbyDelay(device=self.device)
        parsed_output = standby_delay_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        standby_delay_obj = ShowStandbyDelay(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = standby_delay_obj.parse()

if __name__ == '__main__':
    unittest.main()

# vim: ft=python et sw=4
