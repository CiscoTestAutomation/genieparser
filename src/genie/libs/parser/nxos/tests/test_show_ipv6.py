import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

from genie.libs.parser.nxos.show_ipv6 import ShowIpv6NeighborsDetailVrfAll, \
                                             ShowIpv6RoutersVrfAll, \
                                             ShowIpv6IcmpNeighborDetailVrfAll, \
                                             ShowIpv6NdInterfaceVrfAll



#############################################################################
# Unittest For "show ipv6 routers vrf all"
#############################################################################

class test_show_ipv6_routers_vrf_all(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'interfaces': {
            'Ethernet1/1': {
                'interface': 'Ethernet1/1',
                'router_advertisement': {
                    'router': 'fe80::f816:3eff:fe82:6320',
                    'last_update_time_min': '3.2',
                    'current_hop_limit': 64,
                    'lifetime': 1800,
                    'addrFlag': 0,
                    'other_flag': 0,
                    'mtu': 1500,
                    'home_agent_flag': 0,
                    'preference': 'Medium',
                    'reachable_time_msec': 0,
                    'retransmission_time': 0,
                    'prefix': {
                        'prefix': '2010:2:3::/64',
                        'onlink_flag': 1,
                        'autonomous_flag': 1,
                        'valid_lifetime': 2592000,
                        'preferred_lifetime': 604800}}},
            'Ethernet1/2': {
                'interface': 'Ethernet1/2',
                'router_advertisement': {
                    'router': 'fe80::f816:3eff:fe8b:59c9',
                    'last_update_time_min': '1.5',
                    'current_hop_limit': 64,
                    'lifetime': 1800,
                    'addrFlag': 0,
                    'other_flag': 0,
                    'mtu': 1500,
                    'home_agent_flag': 0,
                    'preference': 'Medium',
                    'reachable_time_msec': 0,
                    'retransmission_time': 0,
                    'prefix': {
                        'prefix': '2020:2:3::/64',
                        'onlink_flag': 1,
                        'autonomous_flag': 1,
                        'valid_lifetime': 2592000,
                        'preferred_lifetime': 604800}}},
            'Ethernet1/3': {
                'interface': 'Ethernet1/3',
                'router_advertisement': {
                    'router': 'fe80::f816:3eff:fe19:8682',
                    'last_update_time_min': '2.8',
                    'current_hop_limit': 64,
                    'lifetime': 1800,
                    'addrFlag': 0,
                    'other_flag': 0,
                    'mtu': 1500,
                    'home_agent_flag': 0,
                    'preference': 'Medium',
                    'reachable_time_msec': 0,
                    'retransmission_time': 0,
                    'prefix': {
                        'prefix': '2010:1:3::/64',
                        'onlink_flag': 1,
                        'autonomous_flag': 1,
                        'valid_lifetime': 2592000,
                        'preferred_lifetime': 604800}}},
            'Ethernet1/4': {
                'interface': 'Ethernet1/4',
                'router_advertisement': {
                    'router': 'fe80::f816:3eff:fec7:8140',
                    'last_update_time_min': '2.3',
                    'current_hop_limit': 64,
                    'lifetime': 1800,
                    'addrFlag': 0,
                    'other_flag': 0,
                    'mtu': 1500,
                    'home_agent_flag': 0,
                    'preference': 'Medium',
                    'reachable_time_msec': 0,
                    'retransmission_time': 0,
                    'prefix': {
                        'prefix': '2020:1:3::/64',
                        'onlink_flag': 1,
                        'autonomous_flag': 1,
                        'valid_lifetime': 2592000,
                        'preferred_lifetime': 604800}}}}}

    golden_output1 = {'execute.return_value': '''
        n9kv-3# show ipv6 routers vrf all
        Router fe80::f816:3eff:fe82:6320 on Ethernet1/1 , last update time 3.2 min
        Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
        HomeAgentFlag 0, Preference Medium
        Reachable time 0 msec, Retransmission time 0 msec
          Prefix 2010:2:3::/64  onlink_flag 1 autonomous_flag 1
          valid lifetime 2592000, preferred lifetime 604800
        
        
        Router fe80::f816:3eff:fe8b:59c9 on Ethernet1/2 , last update time 1.5 min
        Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
        HomeAgentFlag 0, Preference Medium
        Reachable time 0 msec, Retransmission time 0 msec
          Prefix 2020:2:3::/64  onlink_flag 1 autonomous_flag 1
          valid lifetime 2592000, preferred lifetime 604800
        
        
        Router fe80::f816:3eff:fe19:8682 on Ethernet1/3 , last update time 2.8 min
        Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
        HomeAgentFlag 0, Preference Medium
        Reachable time 0 msec, Retransmission time 0 msec
          Prefix 2010:1:3::/64  onlink_flag 1 autonomous_flag 1
          valid lifetime 2592000, preferred lifetime 604800
        
        
        Router fe80::f816:3eff:fec7:8140 on Ethernet1/4 , last update time 2.3 min
        Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
        HomeAgentFlag 0, Preference Medium
        Reachable time 0 msec, Retransmission time 0 msec
          Prefix 2020:1:3::/64  onlink_flag 1 autonomous_flag 1
          valid lifetime 2592000, preferred lifetime 604800
    '''}

    def test_show_ipv6_routers_vrf_all_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6RoutersVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_routers_vrf_all_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowIpv6RoutersVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


#############################################################################
# Unittest for 'show ipv6 icmp neighbor detail vrf all'
#############################################################################

class test_show_ipv6_icmp_neighbor_detail_vrf_all(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Eth1/1': {
                'interface': 'Eth1/1',
                'phy_interface': 'Eth1/1',
                'neighbors': {
                    '2010:2:3::2': {
                        'ip': '2010:2:3::2',
                        'age': '00:15:02',
                        'mac_address': 'fa16.3e82.6320',
                        'state': 'STALE'},
                    'fe80::f816:3eff:fe82:6320': {
                        'ip': 'fe80::f816:3eff:fe82:6320',
                        'age': '00:18:33',
                        'mac_address': 'fa16.3e82.6320',
                        'state': 'STALE'}}},
            'Eth1/2': {
                'interface': 'Eth1/2',
                'phy_interface': 'Eth1/2',
                'neighbors': {
                    '2020:2:3::2': {
                        'ip': '2020:2:3::2',
                        'age': '00:03:30',
                        'mac_address': 'fa16.3e8b.59c9',
                        'state': 'STALE'},
                    'fe80::f816:3eff:fe8b:59c9': {
                        'ip': 'fe80::f816:3eff:fe8b:59c9',
                        'age': '00:14:19',
                        'mac_address': 'fa16.3e8b.59c9',
                        'state': 'STALE'}}},
            'Eth1/3': {
                'interface': 'Eth1/3',
                'phy_interface': 'Eth1/3',
                'neighbors': {
                    '2010:1:3::1': {
                        'ip': '2010:1:3::1',
                        'age': '00:15:31',
                        'mac_address': 'fa16.3e19.8682',
                        'state': 'STALE'}}},
            'Eth1/4': {
                'interface': 'Eth1/4',
                'phy_interface': 'Eth1/4',
                'neighbors': {
                    '2020:1:3::1': {
                        'ip': '2020:1:3::1',
                        'age': '00:07:58',
                        'mac_address': 'fa16.3ec7.8140',
                        'state': 'STALE'},
                    'fe80::f816:3eff:fec7:8140': {
                        'ip': 'fe80::f816:3eff:fec7:8140',
                        'age': '00:02:41',
                        'mac_address': 'fa16.3ec7.8140',
                        'state': 'STALE'}}}}}

    golden_output = {'execute.return_value': '''
        n9kv-3# show ipv6 icmp neighbor detail vrf all

        Flags: + - Adjacencies synced via CFSoE
               # - Adjacencies Throttled for Glean
        
        ICMPv6 Adjacency Table for all VRFs 
        Address         Age       MAC Address     State      Interface  Phy-Interface
        2010:2:3::2     00:15:02  fa16.3e82.6320  STALE       Eth1/1      Eth1/1    
        fe80::f816:3eff:fe82:6320                                         
                        00:18:33  fa16.3e82.6320  STALE       Eth1/1      Eth1/1    
        2020:2:3::2     00:03:30  fa16.3e8b.59c9  STALE       Eth1/2      Eth1/2    
        fe80::f816:3eff:fe8b:59c9                                         
                        00:14:19  fa16.3e8b.59c9  STALE       Eth1/2      Eth1/2    
        2010:1:3::1     00:15:31  fa16.3e19.8682  STALE       Eth1/3      Eth1/3    
        fe80::f816:3eff:fe19:8682                                         
                        00:15:31  fa16.3e19.8682  STALE       Eth1/3      Eth1/3    
        2020:1:3::1     00:07:58  fa16.3ec7.8140  STALE       Eth1/4      Eth1/4    
        fe80::f816:3eff:fec7:8140                                         
                        00:02:41  fa16.3ec7.8140  STALE       Eth1/4      Eth1/4 
    '''}

    def test_show_ipv6_icmp_neighbor_detail_vrf_all_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6IcmpNeighborDetailVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_icmp_neighbor_detail_vrf_all_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6IcmpNeighborDetailVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


#############################################################################
# Unittest for 'show ipv6 nd interface vrf all'
#############################################################################

class test_show_ipv6_nd_interface_vrf_all(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'vrf': 'default',
                'nd_interface': 'ICMPv6 ND',
                'interfaces': {
                    'Ethernet1/1': {
                        'interface': 'Ethernet1/1',
                        'interface_status': 'protocol-up/link-up/admin-up',
                        'ipv6': {
                            'ipv6_address': '2010:2:3::3/64',
                            'ipv6_status': 'VALID'},
                        'ipv6_link_local_address': 'fe80::5c01:c0ff:fe02:7',
                        'nd_mac_extract': 'Disabled',
                        'icmpv6_active_timers': {
                            'last_neighbor_solicitation_sent': '00:06:16',
                            'last_neighbor_advertisement_sent': '00:02:12',
                            'last_router_advertisement_sent': '1d18h',
                            'next_router_advertisement_sent': '0.000000'},
                        'router_advertisement': {
                            'periodic_interval_seconds': '200-201',
                            'managed_address_configuration_flag': 'false',
                            'other_stateful_configuration_flag': 'false',
                            'default_router_preference_value': 'Medium',
                            'current_hop_limit': 64,
                            'mtu': 1500,
                            'router_lifetime_secs': 1801,
                            'reachable_time_ms': 0,
                            'retrans_timer_ms': 0,
                            'suppress_ra': 'Enabled',
                            'suppress_mtu_ra': 'Disabled',
                            'suppress_route_information_option_ra': 'Disabled'},
                        'neighbor_solicitation': {
                            'ns_retransmit_interval_ms': 1000,
                            'nd_nud_retry_base': 1,
                            'nd_nud_retry_interval': 1000,
                            'nd_nud_retry_attempts': 3},
                        'icmpv6_error_message': {
                            'send_redirects': 'true',
                            'send_unreachables': 'false'},
                        'icmpv6_dad': {
                            'maximum_dad_attempts': 1,
                            'current_dad_attempt': 1}},
                    'Ethernet1/3': {
                        'interface': 'Ethernet1/3',
                        'interface_status': 'protocol-up/link-up/admin-up',
                        'ipv6': {
                            'ipv6_address': '2010:1:3::3/64',
                            'ipv6_status': 'VALID'},
                        'ipv6_link_local_address': 'fe80::5c01:c0ff:fe02:7',
                        'nd_mac_extract': 'Disabled',
                        'icmpv6_active_timers': {
                            'last_neighbor_solicitation_sent': '00:07:39',
                            'last_neighbor_advertisement_sent': '02:39:27',
                            'last_router_advertisement_sent': '00:01:33',
                            'next_router_advertisement_sent': '00:03:50'},
                        'router_advertisement': {
                            'periodic_interval_seconds': '200-600',
                            'managed_address_configuration_flag': 'false',
                            'other_stateful_configuration_flag': 'false',
                            'default_router_preference_value': 'Medium',
                            'current_hop_limit': 64,
                            'mtu': 1500,
                            'router_lifetime_secs': 1800,
                            'reachable_time_ms': 0,
                            'retrans_timer_ms': 0,
                            'suppress_ra': 'Disabled',
                            'suppress_mtu_ra': 'Disabled',
                            'suppress_route_information_option_ra': 'Disabled'},
                        'neighbor_solicitation': {
                            'ns_retransmit_interval_ms': 1000,
                            'nd_nud_retry_base': 1,
                            'nd_nud_retry_interval': 1000,
                            'nd_nud_retry_attempts': 3},
                        'icmpv6_error_message': {
                            'send_redirects': 'true',
                            'send_unreachables': 'false'},
                        'icmpv6_dad': {
                            'maximum_dad_attempts': 1,
                            'current_dad_attempt': 1}},
                    'loopback0': {
                        'interface': 'loopback0',
                        'interface_status': 'protocol-up/link-up/admin-up',
                        'ipv6': {
                            'ipv6_address': '2001:3:3::3/128',
                            'ipv6_status': 'VALID'},
                        'ipv6_link_local_address': 'fe80::5c01:c0ff:fe02:0',
                        'nd_mac_extract': 'Disabled',
                        'icmpv6_active_timers': {
                            'last_neighbor_solicitation_sent': 'never',
                            'last_neighbor_advertisement_sent': 'never',
                            'last_router_advertisement_sent': 'never',
                            'next_router_advertisement_sent': 'never'},
                        'router_advertisement': {
                            'periodic_interval_seconds': '200-600',
                            'managed_address_configuration_flag': 'false',
                            'other_stateful_configuration_flag': 'false',
                            'default_router_preference_value': 'Medium',
                            'current_hop_limit': 64,
                            'mtu': 1500,
                            'router_lifetime_secs': 1800,
                            'reachable_time_ms': 0,
                            'retrans_timer_ms': 0,
                            'suppress_ra': 'Disabled',
                            'suppress_mtu_ra': 'Disabled',
                            'suppress_route_information_option_ra': 'Disabled'},
                        'neighbor_solicitation': {
                            'ns_retransmit_interval_ms': 1000,
                            'nd_nud_retry_base': 1,
                            'nd_nud_retry_interval': 1000,
                            'nd_nud_retry_attempts': 3},
                        'icmpv6_error_message': {
                            'send_redirects': 'true',
                            'send_unreachables': 'false'},
                        'icmpv6_dad': {
                            'maximum_dad_attempts': 1,
                            'current_dad_attempt': 0}},
                    'loopback1': {
                        'interface': 'loopback1',
                        'interface_status': 'protocol-up/link-up/admin-up',
                        'ipv6': {
                            'ipv6_address': '2001:33:33::33/128',
                            'ipv6_status': 'VALID'},
                        'ipv6_link_local_address': 'fe80::5c01:c0ff:fe02:0',
                        'nd_mac_extract': 'Disabled',
                        'icmpv6_active_timers': {
                            'last_neighbor_solicitation_sent': 'never',
                            'last_neighbor_advertisement_sent': 'never',
                            'last_router_advertisement_sent': 'never',
                            'next_router_advertisement_sent': 'never'},
                        'router_advertisement': {
                            'periodic_interval_seconds': '200-600',
                            'managed_address_configuration_flag': 'false',
                            'other_stateful_configuration_flag': 'false',
                            'default_router_preference_value': 'Medium',
                            'current_hop_limit': 64,
                            'mtu': 1500,
                            'router_lifetime_secs': 1800,
                            'reachable_time_ms': 0,
                            'retrans_timer_ms': 0,
                            'suppress_ra': 'Disabled',
                            'suppress_mtu_ra': 'Disabled',
                            'suppress_route_information_option_ra': 'Disabled'},
                        'neighbor_solicitation': {
                            'ns_retransmit_interval_ms': 1000,
                            'nd_nud_retry_base': 1,
                            'nd_nud_retry_interval': 1000,
                            'nd_nud_retry_attempts': 3},
                        'icmpv6_error_message': {
                            'send_redirects': 'true',
                            'send_unreachables': 'false'},
                        'icmpv6_dad': {
                            'maximum_dad_attempts': 1,
                            'current_dad_attempt': 0}}}},
            'management': {
                'vrf': 'management',
                'nd_interface': 'ICMPv6 ND'},
            'vrf1': {
                'vrf': 'vrf1',
                'nd_interface': 'ICMPv6 ND',
                'interfaces': {
                    'Ethernet1/2': {
                        'interface': 'Ethernet1/2',
                        'interface_status': 'protocol-up/link-up/admin-up',
                        'ipv6': {
                            'ipv6_address': '2020:2:3::3/64',
                            'ipv6_status': 'VALID'},
                        'ipv6_link_local_address': 'fe80::5c01:c0ff:fe02:7',
                        'nd_mac_extract': 'Disabled',
                        'icmpv6_active_timers': {
                            'last_neighbor_solicitation_sent': '00:09:34',
                            'last_neighbor_advertisement_sent': '00:01:07',
                            'last_router_advertisement_sent': '00:05:42',
                            'next_router_advertisement_sent': '00:01:46'},
                        'router_advertisement': {
                            'periodic_interval_seconds': '200-600',
                            'managed_address_configuration_flag': 'false',
                            'other_stateful_configuration_flag': 'false',
                            'default_router_preference_value': 'Medium',
                            'current_hop_limit': 64,
                            'mtu': 1500,
                            'router_lifetime_secs': 1800,
                            'reachable_time_ms': 0,
                            'retrans_timer_ms': 0,
                            'suppress_ra': 'Disabled',
                            'suppress_mtu_ra': 'Disabled',
                            'suppress_route_information_option_ra': 'Disabled'},
                        'neighbor_solicitation': {
                            'ns_retransmit_interval_ms': 1000,
                            'nd_nud_retry_base': 1,
                            'nd_nud_retry_interval': 1000,
                            'nd_nud_retry_attempts': 3},
                        'icmpv6_error_message': {
                            'send_redirects': 'true',
                            'send_unreachables': 'false'},
                        'icmpv6_dad': {
                            'maximum_dad_attempts': 1,
                            'current_dad_attempt': 1}},
                    'Ethernet1/4': {
                        'interface': 'Ethernet1/4',
                        'interface_status': 'protocol-up/link-up/admin-up',
                        'ipv6': {
                            'ipv6_address': '2020:1:3::3/64',
                            'ipv6_status': 'VALID'},
                        'ipv6_link_local_address': 'fe80::5c01:c0ff:fe02:7',
                        'nd_mac_extract': 'Disabled',
                        'icmpv6_active_timers': {
                            'last_neighbor_solicitation_sent': '00:03:31',
                            'last_neighbor_advertisement_sent': '07:32:12',
                            'last_router_advertisement_sent': '00:08:09',
                            'next_router_advertisement_sent': '00:01:36'},
                        'router_advertisement': {
                            'periodic_interval_seconds': '200-600',
                            'managed_address_configuration_flag': 'false',
                            'other_stateful_configuration_flag': 'false',
                            'default_router_preference_value': 'Medium',
                            'current_hop_limit': 64,
                            'mtu': 1500,
                            'router_lifetime_secs': 1800,
                            'reachable_time_ms': 0,
                            'retrans_timer_ms': 0,
                            'suppress_ra': 'Disabled',
                            'suppress_mtu_ra': 'Disabled',
                            'suppress_route_information_option_ra': 'Disabled'},
                        'neighbor_solicitation': {
                            'ns_retransmit_interval_ms': 1000,
                            'nd_nud_retry_base': 1,
                            'nd_nud_retry_interval': 1000,
                            'nd_nud_retry_attempts': 3},
                        'icmpv6_error_message': {
                            'send_redirects': 'true',
                            'send_unreachables': 'false'},
                        'icmpv6_dad': {
                            'maximum_dad_attempts': 1,
                            'current_dad_attempt': 1}}}}}}

    golden_output = {'execute.return_value': '''
        n9kv-3# show ipv6 nd interface vrf all
        ICMPv6 ND Interfaces for VRF "default"
        Ethernet1/1, Interface status: protocol-up/link-up/admin-up
            IPv6 address: 
                2010:2:3::3/64 [VALID]
            IPv6 link-local address: fe80::5c01:c0ff:fe02:7 [VALID]
            ND mac-extract : Disabled
            ICMPv6 active timers:
                Last Neighbor-Solicitation sent: 00:06:16
                Last Neighbor-Advertisement sent: 00:02:12
                Last Router-Advertisement sent: 1d18h
                Next Router-Advertisement sent in: 0.000000
            Router-Advertisement parameters:
                Periodic interval: 200 to 201 seconds
                Send "Managed Address Configuration" flag: false
                Send "Other Stateful Configuration" flag: false
                Send "Default Router Preference" value: Medium
                Send "Current Hop Limit" field: 64
                Send "MTU" option value: 1500
                Send "Router Lifetime" field: 1801 secs
                Send "Reachable Time" field: 0 ms
                Send "Retrans Timer" field: 0 ms
                Suppress RA: Enabled
                Suppress MTU in RA: Disabled
                Suppress Route Information Option in RA: Disabled
            Neighbor-Solicitation parameters:
                NS retransmit interval: 1000 ms
                ND NUD retry base: 1
                ND NUD retry interval: 1000
                ND NUD retry attempts: 3
            ICMPv6 error message parameters:
                Send redirects: true (0)
                Send unreachables: false
            ICMPv6 DAD parameters:
                Maximum DAD attempts: 1
                Current DAD attempt : 1
        Ethernet1/3, Interface status: protocol-up/link-up/admin-up
            IPv6 address: 
                2010:1:3::3/64 [VALID]
            IPv6 link-local address: fe80::5c01:c0ff:fe02:7 [VALID]
            ND mac-extract : Disabled
            ICMPv6 active timers:
                Last Neighbor-Solicitation sent: 00:07:39
                Last Neighbor-Advertisement sent: 02:39:27
                Last Router-Advertisement sent: 00:01:33
                Next Router-Advertisement sent in: 00:03:50
            Router-Advertisement parameters:
                Periodic interval: 200 to 600 seconds
                Send "Managed Address Configuration" flag: false
                Send "Other Stateful Configuration" flag: false
                Send "Default Router Preference" value: Medium
                Send "Current Hop Limit" field: 64
                Send "MTU" option value: 1500
                Send "Router Lifetime" field: 1800 secs
                Send "Reachable Time" field: 0 ms
                Send "Retrans Timer" field: 0 ms
                Suppress RA: Disabled
                Suppress MTU in RA: Disabled
                Suppress Route Information Option in RA: Disabled
          Neighbor-Solicitation parameters:
              NS retransmit interval: 1000 ms
              ND NUD retry base: 1
              ND NUD retry interval: 1000
              ND NUD retry attempts: 3
          ICMPv6 error message parameters:
              Send redirects: true (0)
              Send unreachables: false
          ICMPv6 DAD parameters:
              Maximum DAD attempts: 1
              Current DAD attempt : 1
        loopback0, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:3:3::3/128 [VALID]
          IPv6 link-local address: fe80::5c01:c0ff:fe02:0 [VALID]
          ND mac-extract : Disabled
          ICMPv6 active timers:
              Last Neighbor-Solicitation sent: never
              Last Neighbor-Advertisement sent: never
              Last Router-Advertisement sent: never
              Next Router-Advertisement sent in: never
          Router-Advertisement parameters:
              Periodic interval: 200 to 600 seconds
              Send "Managed Address Configuration" flag: false
              Send "Other Stateful Configuration" flag: false
              Send "Default Router Preference" value: Medium
              Send "Current Hop Limit" field: 64
              Send "MTU" option value: 1500
              Send "Router Lifetime" field: 1800 secs
              Send "Reachable Time" field: 0 ms
              Send "Retrans Timer" field: 0 ms
              Suppress RA: Disabled
              Suppress MTU in RA: Disabled
              Suppress Route Information Option in RA: Disabled
          Neighbor-Solicitation parameters:
              NS retransmit interval: 1000 ms
              ND NUD retry base: 1
              ND NUD retry interval: 1000
              ND NUD retry attempts: 3
          ICMPv6 error message parameters:
              Send redirects: true (0)
              Send unreachables: false
          ICMPv6 DAD parameters:
              Maximum DAD attempts: 1
              Current DAD attempt : 0
        loopback1, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2001:33:33::33/128 [VALID]
          IPv6 link-local address: fe80::5c01:c0ff:fe02:0 [VALID]
          ND mac-extract : Disabled
          ICMPv6 active timers:
              Last Neighbor-Solicitation sent: never
              Last Neighbor-Advertisement sent: never
              Last Router-Advertisement sent: never
              Next Router-Advertisement sent in: never
          Router-Advertisement parameters:
              Periodic interval: 200 to 600 seconds
              Send "Managed Address Configuration" flag: false
              Send "Other Stateful Configuration" flag: false
              Send "Default Router Preference" value: Medium
              Send "Current Hop Limit" field: 64
              Send "MTU" option value: 1500
              Send "Router Lifetime" field: 1800 secs
              Send "Reachable Time" field: 0 ms
              Send "Retrans Timer" field: 0 ms
              Suppress RA: Disabled
              Suppress MTU in RA: Disabled
              Suppress Route Information Option in RA: Disabled
          Neighbor-Solicitation parameters:
              NS retransmit interval: 1000 ms
              ND NUD retry base: 1
              ND NUD retry interval: 1000
              ND NUD retry attempts: 3
          ICMPv6 error message parameters:
              Send redirects: true (0)
              Send unreachables: false
          ICMPv6 DAD parameters:
              Maximum DAD attempts: 1
              Current DAD attempt : 0
        
        ICMPv6 ND Interfaces for VRF "management"
        
        ICMPv6 ND Interfaces for VRF "vrf1"
        Ethernet1/2, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2020:2:3::3/64 [VALID]
          IPv6 link-local address: fe80::5c01:c0ff:fe02:7 [VALID]
          ND mac-extract : Disabled
          ICMPv6 active timers:
              Last Neighbor-Solicitation sent: 00:09:34
              Last Neighbor-Advertisement sent: 00:01:07
              Last Router-Advertisement sent: 00:05:42
              Next Router-Advertisement sent in: 00:01:46
          Router-Advertisement parameters:
              Periodic interval: 200 to 600 seconds
              Send "Managed Address Configuration" flag: false
              Send "Other Stateful Configuration" flag: false
              Send "Default Router Preference" value: Medium
              Send "Current Hop Limit" field: 64
              Send "MTU" option value: 1500
              Send "Router Lifetime" field: 1800 secs
              Send "Reachable Time" field: 0 ms
              Send "Retrans Timer" field: 0 ms
              Suppress RA: Disabled
              Suppress MTU in RA: Disabled
              Suppress Route Information Option in RA: Disabled
          Neighbor-Solicitation parameters:
              NS retransmit interval: 1000 ms
              ND NUD retry base: 1
              ND NUD retry interval: 1000
              ND NUD retry attempts: 3
          ICMPv6 error message parameters:
              Send redirects: true (0)
              Send unreachables: false
          ICMPv6 DAD parameters:
              Maximum DAD attempts: 1
              Current DAD attempt : 1
        Ethernet1/4, Interface status: protocol-up/link-up/admin-up
          IPv6 address: 
            2020:1:3::3/64 [VALID]
          IPv6 link-local address: fe80::5c01:c0ff:fe02:7 [VALID]
          ND mac-extract : Disabled
          ICMPv6 active timers:
              Last Neighbor-Solicitation sent: 00:03:31
              Last Neighbor-Advertisement sent: 07:32:12
              Last Router-Advertisement sent: 00:08:09
              Next Router-Advertisement sent in: 00:01:36
          Router-Advertisement parameters:
              Periodic interval: 200 to 600 seconds
              Send "Managed Address Configuration" flag: false
              Send "Other Stateful Configuration" flag: false
              Send "Default Router Preference" value: Medium
              Send "Current Hop Limit" field: 64
              Send "MTU" option value: 1500
              Send "Router Lifetime" field: 1800 secs
              Send "Reachable Time" field: 0 ms
              Send "Retrans Timer" field: 0 ms
              Suppress RA: Disabled
              Suppress MTU in RA: Disabled
              Suppress Route Information Option in RA: Disabled
          Neighbor-Solicitation parameters:
              NS retransmit interval: 1000 ms
              ND NUD retry base: 1
              ND NUD retry interval: 1000
              ND NUD retry attempts: 3
          ICMPv6 error message parameters:
              Send redirects: true (0)
              Send unreachables: false
          ICMPv6 DAD parameters:
              Maximum DAD attempts: 1
              Current DAD attempt : 1
         '''}

    def test_show_ipv6_nd_interface_vrf_all_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6NdInterfaceVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_nd_interface_vrf_all_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6NdInterfaceVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


#############################################################################
# Unittest for 'show ipv6 neighbor detail vrf all'
#############################################################################

class test_show_ipv6_neighbor_detail_vrf_all(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'adjacency_hit': {
            'GLEAN': {
                'byte_count': 0,
                'packet_count': 0},
            'GLOBAL DROP': {
                'byte_count': 0,
                'packet_count': 0},
            'GLOBAL GLEAN': {
                'byte_count': 0,
                'packet_count': 0},
            'GLOBAL PUNT': {
                'byte_count': 0,
                'packet_count': 0},
            'INVALID': {
                'byte_count': 0,
                'packet_count': 0},
            'NORMAL': {
                'byte_count': 0,
                'packet_count': 0}},
        'adjacency_statistics_last_updated_before': 'never',
        'interfaces': {
            'Ethernet1/1': {
                'interface': 'Ethernet1/1',
                'neighbors': {
                    '2010:2:3::2': {
                        'age': '00:09:27',
                        'best': 'Yes',
                        'byte_count': 0,
                        'ip': '2010:2:3::2',
                        'mac_addr': 'fa16.3e82.6320',
                        'packet_count': 0,
                        'physical_interface': 'Ethernet1/1',
                        'preference': '50',
                        'source': 'icmpv6',
                        'throttled': 'No'},
                    '2010:2:3::33': {
                        'age': '2d15h',
                        'best': 'Yes',
                        'byte_count': 0,
                        'ip': '2010:2:3::33',
                        'mac_addr': 'aabb.beef.cccc',
                        'packet_count': 0,
                        'physical_interface': 'Ethernet1/1',
                        'preference': '1',
                        'source': 'Static',
                        'throttled': 'No'},
                    '2010:2:3::34': {
                        'age': '1d18h',
                        'best': 'Yes',
                        'byte_count': 0,
                        'ip': '2010:2:3::34',
                        'mac_addr': 'aaab.beef.ccce',
                        'packet_count': 0,
                        'physical_interface': 'Ethernet1/1',
                        'preference': '1',
                        'source': 'Static',
                        'throttled': 'No'},
                    'fe80::f816:3eff:fe82:6320': {
                        'age': '00:05:42',
                        'best': 'Yes',
                        'byte_count': 0,
                        'ip': 'fe80::f816:3eff:fe82:6320',
                        'mac_addr': 'fa16.3e82.6320',
                        'packet_count': 0,
                        'physical_interface': 'Ethernet1/1',
                        'preference': '50',
                        'source': 'icmpv6',
                        'throttled': 'No'}}},
            'Ethernet1/2': {
                'interface': 'Ethernet1/2',
                'neighbors': {
                    '2020:2:3::2': {
                        'age': '00:09:00',
                        'best': 'Yes',
                        'byte_count': 0,
                        'ip': '2020:2:3::2',
                        'mac_addr': 'fa16.3e8b.59c9',
                        'packet_count': 0,
                        'physical_interface': 'Ethernet1/2',
                        'preference': '50',
                        'source': 'icmpv6',
                        'throttled': 'No'},
                    '2020:2:3::33': {
                        'age': '2d15h',
                        'best': 'Yes',
                        'byte_count': 0,
                        'ip': '2020:2:3::33',
                        'mac_addr': 'aaaa.bbbb.cccc',
                        'packet_count': 0,
                        'physical_interface': 'Ethernet1/2',
                        'preference': '1',
                        'source': 'Static',
                        'throttled': 'No'},
                    'fe80::f816:3eff:fe8b:59c9': {
                        'age': '00:14:08',
                        'best': 'Yes',
                        'byte_count': 0,
                        'ip': 'fe80::f816:3eff:fe8b:59c9',
                        'mac_addr': 'fa16.3e8b.59c9',
                        'packet_count': 0,
                        'physical_interface': 'Ethernet1/2',
                        'preference': '50',
                        'source': 'icmpv6',
                        'throttled': 'No'}}},
            'Ethernet1/3': {
                'interface': 'Ethernet1/3',
                'neighbors': {
                    '2010:1:3::1': {
                        'age': '2d15h',
                        'best': 'Yes',
                        'byte_count': 0,
                        'ip': '2010:1:3::1',
                        'mac_addr': 'fa16.3e19.8682',
                        'packet_count': 0,
                        'physical_interface': 'Ethernet1/3',
                        'preference': '50',
                        'source': 'icmpv6',
                        'throttled': 'No'},
                    'fe80::f816:3eff:fe19:8682': {
                        'age': '2d15h',
                        'best': 'Yes',
                        'byte_count': 0,
                        'ip': 'fe80::f816:3eff:fe19:8682',
                        'mac_addr': 'fa16.3e19.8682',
                        'packet_count': 0,
                        'physical_interface': 'Ethernet1/3',
                        'preference': '50',
                        'source': 'icmpv6',
                        'throttled': 'No'}}},
            'Ethernet1/4': {
                'interface': 'Ethernet1/4',
                'neighbors': {
                    '2020:1:3::1': {
                        'age': '2d15h',
                        'best': 'Yes',
                        'byte_count': 0,
                        'ip': '2020:1:3::1',
                        'mac_addr': 'fa16.3ec7.8140',
                        'packet_count': 0,
                        'physical_interface': 'Ethernet1/4',
                        'preference': '50',
                        'source': 'icmpv6',
                        'throttled': 'No'},
                    'fe80::f816:3eff:fec7:8140': {
                        'age': '2d15h',
                        'best': 'Yes',
                        'byte_count': 0,
                        'ip': 'fe80::f816:3eff:fec7:8140',
                        'mac_addr': 'fa16.3ec7.8140',
                        'packet_count': 0,
                        'physical_interface': 'Ethernet1/4',
                        'preference': '50',
                        'source': 'icmpv6',
                        'throttled': 'No'}}}},
        'total_number_of_entries': 11}

    golden_output = {'execute.return_value': '''
        n9kv-3# show ipv6 neighbor detail vrf all
        No. of Adjacency hit with type INVALID: Packet count 0, Byte count 0
        No. of Adjacency hit with type GLOBAL DROP: Packet count 0, Byte count 0
        No. of Adjacency hit with type GLOBAL PUNT: Packet count 0, Byte count 0
        No. of Adjacency hit with type GLOBAL GLEAN: Packet count 0, Byte count 0
        No. of Adjacency hit with type GLEAN: Packet count 0, Byte count 0
        No. of Adjacency hit with type NORMAL: Packet count 0, Byte count 0
        
        Adjacency statistics last updated before: never
        
        IPv6 Adjacency Table for all VRFs
        Total number of entries: 11
        
        Address :            2010:2:3::2     
        Age :                00:09:27
        MacAddr :            fa16.3e82.6320
        Preference :         50  
        Source :             icmpv6         
        Interface :          Ethernet1/1     
        Physical Interface : Ethernet1/1      
        Packet Count :       0   
        Byte Count :         0   
        Best :               Yes
        Throttled :          No
        
        Address :            2010:2:3::33    
        Age :                2d15h
        MacAddr :            aabb.beef.cccc
        Preference :         1   
        Source :             Static         
        Interface :          Ethernet1/1     
        Physical Interface : Ethernet1/1      
        Packet Count :       0   
        Byte Count :         0   
        Best :               Yes
        Throttled :          No
        
        Address :            2010:2:3::34    
        Age :                1d18h
        MacAddr :            aaab.beef.ccce
        Preference :         1   
        Source :             Static         
        Interface :          Ethernet1/1     
        Physical Interface : Ethernet1/1      
        Packet Count :       0   
        Byte Count :         0   
        Best :               Yes
        Throttled :          No
        
        Address :            fe80::f816:3eff:fe82:6320
        Age :                00:05:42
        MacAddr :            fa16.3e82.6320
        Preference :         50  
        Source :             icmpv6         
        Interface :          Ethernet1/1     
        Physical Interface : Ethernet1/1      
        Packet Count :       0   
        Byte Count :         0   
        Best :               Yes
        Throttled :          No
        
        Address :            2020:2:3::2     
        Age :                00:09:00
        MacAddr :            fa16.3e8b.59c9
        Preference :         50  
        Source :             icmpv6         
        Interface :          Ethernet1/2     
        Physical Interface : Ethernet1/2      
        Packet Count :       0   
        Byte Count :         0   
        Best :               Yes
        Throttled :          No
        
        Address :            2020:2:3::33    
        Age :                2d15h
        MacAddr :            aaaa.bbbb.cccc
        Preference :         1   
        Source :             Static         
        Interface :          Ethernet1/2     
        Physical Interface : Ethernet1/2      
        Packet Count :       0   
        Byte Count :         0   
        Best :               Yes
        Throttled :          No
        
        Address :            fe80::f816:3eff:fe8b:59c9
        Age :                00:14:08
        MacAddr :            fa16.3e8b.59c9
        Preference :         50  
        Source :             icmpv6         
        Interface :          Ethernet1/2     
        Physical Interface : Ethernet1/2      
        Packet Count :       0   
        Byte Count :         0   
        Best :               Yes
        Throttled :          No
        
        Address :            2010:1:3::1     
        Age :                2d15h
        MacAddr :            fa16.3e19.8682
        Preference :         50  
        Source :             icmpv6         
        Interface :          Ethernet1/3     
        Physical Interface : Ethernet1/3      
        Packet Count :       0   
        Byte Count :         0   
        Best :               Yes
        Throttled :          No
        
        Address :            fe80::f816:3eff:fe19:8682
        Age :                2d15h
        MacAddr :            fa16.3e19.8682
        Preference :         50  
        Source :             icmpv6         
        Interface :          Ethernet1/3     
        Physical Interface : Ethernet1/3      
        Packet Count :       0   
        Byte Count :         0   
        Best :               Yes
        Throttled :          No
        
        Address :            2020:1:3::1     
        Age :                2d15h
        MacAddr :            fa16.3ec7.8140
        Preference :         50  
        Source :             icmpv6         
        Interface :          Ethernet1/4     
        Physical Interface : Ethernet1/4      
        Packet Count :       0   
        Byte Count :         0   
        Best :               Yes
        Throttled :          No
        
        Address :            fe80::f816:3eff:fec7:8140
        Age :                2d15h
        MacAddr :            fa16.3ec7.8140
        Preference :         50  
        Source :             icmpv6         
        Interface :          Ethernet1/4     
        Physical Interface : Ethernet1/4      
        Packet Count :       0   
        Byte Count :         0   
        Best :               Yes
        Throttled :          No'''}

    def test_show_ipv6_neighbor_detail_vrf_all_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6NeighborsDetailVrfAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_neighbor_detail_vrf_all_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6NeighborsDetailVrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()