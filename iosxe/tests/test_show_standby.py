
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from xbu_shared.parser.iosxe.show_standby import ShowStandbyInternal,\
                                                 ShowStandbyAll

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError


# =========================================
#   Unit test for 'show standby internal'
# =========================================

class test_show_standby_internal(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
    'standby_internal': {
        'hsrp_common_process_state': 'not running',
        'hsrp_ha_state': 'capable',
        'hsrp_ipv4_process_state': 'not running',
        'hsrp_ipv6_process_state': 'not running',
        'hsrp_timer_wheel_state': 'running',
        'mac_address_table': {
            166: {
                'group': 10,
                'interface': 'gi2/0/3',
                'mac_address': '0000.0c07.ac0a'},
            169: {
                'group': 5,
                'interface': 'gi1/0/1',
                'mac_address': '0000.0c07.ac05'},
            172: {
                'group': 0,
                'interface': 'gi2/0/3',
                'mac_address': '0000.0c07.ac00'},
            173: {
                'group': 1,
                'interface': 'gi2/0/3',
                'mac_address': '0000.0c07.ac01'}},
        'msgQ_max_size': 0,
        'msgQ_size': 0,
        'v3_to_v4_transform': 'disabled',
        'virtual_ip_hash_table': {
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

        HSRP MAC Address Table
        169 Gi1/0/1 0000.0c07.ac05
            Gi1/0/1 Grp 5
        166 Gi2/0/3 0000.0c07.ac0a
            Gi2/0/3 Grp 10
        172 Gi2/0/3 0000.0c07.ac00
            Gi2/0/3 Grp 0
        173 Gi2/0/3 0000.0c07.ac01
            Gi2/0/3 Grp 1
    '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        standby_internal_obj = ShowStandbyInternal(device=self.device)
        parsed_output = standby_internal_obj.parse()
        #import pprint ; pprint.pprint(parsed_output)
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
    
    golden_parsed_output = {
    'standby_all': {
        'group': {
            0: {
                'interface': {
                    'GigabitEthernet1/0/1': {
                        'active_mac_in_use': True,
                        'active_router': 'local',
                        'active_virtual_mac_address': '0000.0c9f.f000',
                        'authentication_text': '5',
                        'group_name': 'hsrp-Gi1/0/1-0',
                        'default_priority': 100,
                        'hellotime': 5,
                        'holdtime': 20,
                        'last_state_change': '1w0d',
                        'local_virtual_mac_address': '0000.0c9f.f000',
                        'local_virtual_mac_default': 'v2',
                        'next_hello_time': 2.848,
                        'num_state_changes': 8,
                        'preempt': True,
                        'preempt_min_delay': 5,
                        'preempt_reload_delay': 10,
                        'preempt_sync_delay': 20,
                        'priority': 100,
                        'standby_router': 'unknown',
                        'state': 'active',
                        'track_object': '1',
                        'version': 2,
                        'virtual_ip_address': '192.168.1.254'}}},
            10: {
                'interface': {
                    'GigabitEthernet1/0/2': {
                        'active_mac_in_use': False,
                        'active_router': 'unknown',
                        'active_virtual_mac_address': 'unknown',
                        'authentication_text': 'cisco123',
                        'configured_priority': 110,
                        'group_name': 'hsrp-Gi1/0/2-10',
                        'hellotime': 3,
                        'holdtime': 10,
                        'local_virtual_mac_address': '0000.0c07.ac0a',
                        'local_virtual_mac_default': 'v1',
                        'preempt': True,
                        'priority': 110,
                        'standby_router': 'unknown',
                        'state': 'disabled',
                        'virtual_ip_address': 'unknown'}}}}}}

    golden_output = {'execute.return_value': '''
        GigabitEthernet1/0/1 - Group 0 (version 2)
          State is Active
            8 state changes, last state change 1w0d
            Track object 1 (unknown)
          Virtual IP address is 192.168.1.254
          Active virtual MAC address is 0000.0c9f.f000 (MAC In Use)
            Local virtual MAC address is 0000.0c9f.f000 (v2 default)
          Hello time 5 sec, hold time 20 sec
            Next hello sent in 2.848 secs
          Authentication MD5, key-chain "5"
          Preemption enabled, delay min 5 secs, reload 10 secs, sync 20 secs
          Active router is local
          Standby router is unknown
          Priority 100 (default 100)
          Group name is "hsrp-Gi1/0/1-0" (default)
        GigabitEthernet1/0/2 - Group 10
          State is Disabled
          Virtual IP address is unknown
          Active virtual MAC address is unknown (MAC Not In Use)
            Local virtual MAC address is 0000.0c07.ac0a (v1 default)
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

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        standby_all_obj = ShowStandbyAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = standby_all_obj.parse()


if __name__ == '__main__':
    unittest.main()

# vim: ft=python et sw=4
