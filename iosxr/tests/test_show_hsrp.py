
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from parser.iosxr.show_hsrp import ShowHsrpSummary, ShowHsrpDetail

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError


# ======================================
#   Unit test for 'show hsrp summary'       
# ======================================

class test_show_hsrp_summary(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    'hsrp_summary': {
        'address_family': {
            'ipv4': {
                'intf_down': 1,
                'intf_total': 2,
                'intf_up': 1,
                'state': {
                    'ACTIVE': {
                        'sessions': 1,
                        'slaves': 0,
                        'total': 1},
                    'ALL': {
                        'sessions': 2,
                        'slaves': 0,
                        'total': 2},
                    'INIT': {
                        'sessions': 1,
                        'slaves': 0,
                        'total': 1},
                    'LEARN': {
                        'sessions': 0,
                        'slaves': 0,
                        'total': 0},
                    'LISTEN': {
                        'sessions': 0,
                        'slaves': 0,
                        'total': 0},
                    'SPEAK': {
                        'sessions': 0,
                        'slaves': 0,
                        'total': 0},
                    'STANDBY': {
                        'sessions': 0,
                        'slaves': 0,
                        'total': 0}},
                'virtual_addresses_active': 1,
                'virtual_addresses_inactive': 1,
                'vritual_addresses_total': 2},
            'ipv6': {
                'intf_down': 0,
                'intf_total': 0,
                'intf_up': 0,
                'state': {
                    'ACTIVE': {
                        'sessions': 0,
                        'slaves': 0,
                        'total': 0},
                    'ALL': {
                        'sessions': 0,
                        'slaves': 0,
                        'total': 0},
                    'INIT': {
                        'sessions': 0,
                        'slaves': 0,
                        'total': 0},
                    'LEARN': {
                        'sessions': 0,
                        'slaves': 0,
                        'total': 0},
                    'LISTEN': {
                        'sessions': 0,
                        'slaves': 0,
                        'total': 0},
                    'SPEAK': {
                        'sessions': 0,
                        'slaves': 0,
                        'total': 0},
                    'STANDBY': {
                        'sessions': 0,
                        'slaves': 0,
                        'total': 0}},
                'virtual_addresses_active': 0,
                'virtual_addresses_inactive': 0,
                'vritual_addresses_total': 0}},
            'bfd_sessions_down': 0,
            'bfd_sessions_inactive': 0,
            'bfd_sessions_up': 0,
            'num_bfd_sessions': 0,
            'num_tracked_objects': 3,
            'tracked_objects_down': 2,
            'tracked_objects_up': 1}}

    golden_output = {'execute.return_value': '''
                        IPv4                  IPv6
        State   Sessions Slaves Total  Sessions Slaves Total
        -----   -------- ------ -----  -------- ------ -----
        ALL            2      0     2         0      0     0

        ACTIVE         1      0     1         0      0     0
        STANDBY        0      0     0         0      0     0
        SPEAK          0      0     0         0      0     0
        LISTEN         0      0     0         0      0     0
        LEARN          0      0     0         0      0     0
        INIT           1      0     1         0      0     0

        2    HSRP IPv4 interfaces    (1    up, 1    down)
        0    HSRP IPv6 interfaces    (0    up, 0    down)
        2    Virtual IPv4 addresses  (1    active, 1    inactive)
        0    Virtual IPv6 addresses  (0    active, 0    inactive)
        3    Tracked Objects    (1    up, 2    down)
        0    BFD sessions       (0    up, 0    down, 0    inactive)
        '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        hsrp_summary_obj = ShowHsrpSummary(device=self.device)
        parsed_output = hsrp_summary_obj.parse()
        #import pprint ; pprint.pprint(parsed_output)
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        hsrp_summary_obj = ShowHsrpSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = hsrp_summary_obj.parse()


# ======================================
#   Unit test for 'show hsrp detail'       
# ======================================

class test_show_hsrp_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
    'hsrp_detail': {
        'group': {
            5: {
                'interface': {
                    'GigabitEthernet0/0/0/1': {
                        'address_family': {
                            'ipv4': {
                                'active_router': 'local',
                                'active_priority': 49,
                                'authentication_text': 'cisco123',
                                'config_hellotime': 1000,
                                'config_holdtime': 3000,
                                'hellotime': 1000,
                                'holdtime': 3000,
                                'ip_address': '192.168.1.254',
                                'last_coup_received': 'Never',
                                'last_coup_sent': 'Never',
                                'last_resign_received': 'Never',
                                'last_resign_sent': 'Never',
                                'last_state_change': '2d07h',
                                'local_state': 'active',
                                'min_delay': 5,
                                'num_state_changes': 4,
                                'preempt': True,
                                'priority': 49,
                                'reload_delay': 10,
                                'standby_router': 'unknown',
                                'standby_state': 'active',
                                'standby_virtual_mac_addr': '0000.0c07.ac05',
                                'track_objects': {
                                    '1': {
                                        'priority_decrement': 20},
                                    'apple': {
                                        'priority_decrement': 55},
                                    'banana': {
                                        'priority_decrement': 6},
                                    'num_tracked_objects': 3,
                                    'num_tracked_objects_up': 1},
                                  'version': 1}}}}},
            8: {
                'interface': {
                    'GigabitEthernet0/0/0/2': {
                        'address_family': {
                            'ipv4': {
                                'active_router': 'unknown',
                                'authentication_text': 'cisco123',
                                'hellotime': 3000,
                                'holdtime': 10000,
                                'ip_address': '192.168.2.254',
                                'last_coup_received': 'Never',
                                'last_coup_sent': 'Never',
                                'last_resign_received': 'Never',
                                'last_resign_sent': 'Never',
                                'last_state_change': 'never',
                                'local_state': 'init',
                                'min_delay': 5,
                                'num_state_changes': 0,
                                'preempt': True,
                                'preempt_delay': 10,
                                'priority': 115,
                                'reload_delay': 15,
                                'standby_router': 'unknown',
                                'standby_state': 'stored',
                                'standby_virtual_mac_addr': '0000.0c07.ac08',
                                'version': 1}}}}}}}}

    golden_output = {'execute.return_value': '''
        GigabitEthernet0/0/0/1 - IPv4 Group 5 (version 1)
          Local state is Active, priority 49, may preempt
          Hellotime 1000 msec holdtime 3000 msec
          Configured hellotime 1000 msec holdtime 3000 msec
          Minimum delay 5 sec, reload delay 10 sec
          Hot standby IP address is 192.168.1.254 configured
          Active router is local
          Standby router is unknown expired
          Standby virtual mac address is 0000.0c07.ac05, state is active
          Authentication text, string "cisco123"
          4 state changes, last state change 2d07h
          State change history:
          Mar 14 14:46:46.162 UTC  Init     -> Listen   Delay timer expired
          Mar 14 14:46:49.162 UTC  Listen   -> Speak    Active timer expired
          Mar 14 14:46:52.163 UTC  Speak    -> Standby  Standby timer expired
          Mar 14 14:46:52.163 UTC  Standby  -> Active   Active timer expired
          Last coup sent:       Never
          Last coup received:   Never
          Last resign sent:     Never
          Last resign received: Never
          Tracking states for 3 objects, 1 up:
            Up   1               Priority decrement: 20
            Down apple           Priority decrement: 55
            Down banana          Priority decrement: 6
        GigabitEthernet0/0/0/2 - IPv4 Group 8 (version 1)
          Local state is Init, priority 115, may preempt
          Preemption delay for at least 10 secs
          Hellotime 3000 msec holdtime 10000 msec
          Minimum delay 5 sec, reload delay 15 sec
          Hot standby IP address is 192.168.2.254 configured
          Active router is unknown expired
          Standby router is unknown expired
          Standby virtual mac address is 0000.0c07.ac08, state is stored
          Authentication text, string "cisco123"
          0 state changes, last state change never
          State change history:
          Last coup sent:       Never
          Last coup received:   Never
          Last resign sent:     Never
          Last resign received: Never
        '''}
    
    golden_parsed_output_1 = {
        "hsrp_detail": {
          "group": {
               0: {
                    "interface": {
                         "GigabitEthernet0/0/0/2": {
                              "address_family": {
                                   "ipv4": {
                                        "holdtime": 3000,
                                        "min_delay": 5,
                                        "standby_expire": "00:00:02",
                                        "active_priority": 110,
                                        "reload_delay": 10,
                                        "hellotime": 1000,
                                        "ip_address": "192.168.1.254",
                                        "num_state_changes": 2,
                                        "last_coup_sent": "Aug 11 08:26:25.272 UTC",
                                        "standby_state": "active",
                                        "config_hellotime": 1000,
                                        "version": 1,
                                        "local_state": "active",
                                        "standby_virtual_mac_addr": "0000.0c07.ac00",
                                        "last_resign_sent": "Never",
                                        "last_coup_received": "Never",
                                        "last_resign_received": "Aug 11 08:26:25.272 UTC",
                                        "config_holdtime": 3000,
                                        "priority": 110,
                                        "preempt": True,
                                        "last_state_change": "01:18:43",
                                        "authentication_text": "cisco123",
                                        "active_router": "local",
                                        "standby_router": "192.168.1.2"
                                   }
                              }
                         }
                    }
               },
               1: {
                    "interface": {
                         "GigabitEthernet0/0/0/2": {
                              "address_family": {
                                   "ipv6": {
                                        "holdtime": 3000,
                                        "min_delay": 5,
                                        "standby_expire": "00:00:02",
                                        "active_priority": 120,
                                        "reload_delay": 10,
                                        "hellotime": 1000,
                                        "ip_address": "fe80::205:73ff:fea0:1",
                                        "num_state_changes": 2,
                                        "last_coup_sent": "Aug 11 09:28:07.334 UTC",
                                        "standby_state": "active",
                                        "config_hellotime": 1000,
                                        "version": 2,
                                        "local_state": "active",
                                        "standby_virtual_mac_addr": "0005.73a0.0001",
                                        "last_resign_sent": "Never",
                                        "last_coup_received": "Never",
                                        "last_resign_received": "Aug 11 09:28:07.334 UTC",
                                        "config_holdtime": 3000,
                                        "priority": 120,
                                        "preempt": True,
                                        "last_state_change": "00:17:01",
                                        "active_router": "local",
                                        "standby_router": "fe80::5000:1cff:fe0a:1, 5200.1c0a.0001"
                                   }
                              }
                         }
                    }
               }
          }
     }

    }

    golden_output_1 = {'execute.return_value': '''
        GigabitEthernet0/0/0/2 - IPv4 Group 0 (version 1)
          Local state is Active, priority 110, may preempt
          Hellotime 1000 msec holdtime 3000 msec
          Configured hellotime 1000 msec holdtime 3000 msec
          Minimum delay 5 sec, reload delay 10 sec
          Hot standby IP address is 192.168.1.254 configured
          Active router is local
          Standby router is 192.168.1.2 expires in 00:00:02
          Standby virtual mac address is 0000.0c07.ac00, state is active
          Authentication text, string "cisco123"
          2 state changes, last state change 01:18:43
          State change history:
          Aug 11 08:26:25.137 UTC  Init     -> Listen   Delay timer expired
          Aug 11 08:26:25.253 UTC  Listen   -> Active   Lower priority active received
          Last coup sent:       Aug 11 08:26:25.272 UTC
          Last coup received:   Never
          Last resign sent:     Never
          Last resign received: Aug 11 08:26:25.272 UTC
        GigabitEthernet0/0/0/2 - IPv6 Group 1 (version 2)
          Local state is Active, priority 120, may preempt
          Hellotime 1000 msec holdtime 3000 msec
          Configured hellotime 1000 msec holdtime 3000 msec
          Minimum delay 5 sec, reload delay 10 sec
          Hot standby IP address is fe80::205:73ff:fea0:1 configured
          Active router is local
          Standby router is fe80::5000:1cff:fe0a:1, 5200.1c0a.0001 expires in 00:00:02
          Standby virtual mac address is 0005.73a0.0001, state is active
          2 state changes, last state change 00:17:01
          State change history:
          Aug 11 09:28:07.063 UTC  Init     -> Listen   Delay timer expired
          Aug 11 09:28:07.324 UTC  Listen   -> Active   Lower priority active received
          Last coup sent:       Aug 11 09:28:07.334 UTC
          Last coup received:   Never
          Last resign sent:     Never
          Last resign received: Aug 11 09:28:07.334 UTC
        '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        hsrp_detail_obj = ShowHsrpDetail(device=self.device)
        parsed_output = hsrp_detail_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        hsrp_detail_obj = ShowHsrpDetail(device=self.device)
        parsed_output = hsrp_detail_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        hsrp_detail_obj = ShowHsrpDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = hsrp_detail_obj.parse()


if __name__ == '__main__':
    unittest.main()

# vim: ft=python et sw=4
