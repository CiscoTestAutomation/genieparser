import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.show_ipv6 import ShowIpv6NeighborsDetail

from genie.libs.parser.iosxe.show_interface import ShowIpv6Interface


#############################################################################
# Unittest For:
#         'show ipv6 neighbors vrf <vrf_id>'
#         'show ipv6 neighbors detail'
#############################################################################

class test_show_ipv6_neighbors_detail(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'interface': {
            'Gi2': {
                'interface': 'Gi2',
                'neighbors': {
                    '2010:1:2::2': {
                        'age': '0',
                        'ip': '2010:1:2::2',
                        'link_layer_address': 'fa16.3eca.3efd',
                        'neighbor_state': 'REACH'},
                    '2010:1:2::11': {
                        'age': '-',
                        'ip': '2010:1:2::11',
                        'link_layer_address': 'aaaa.beef.cccc',
                        'neighbor_state': 'REACH'},
                    'FE80::F816:3EFF:FECA:3EFD': {
                        'age': '1',
                        'ip': 'FE80::F816:3EFF:FECA:3EFD',
                        'link_layer_address': 'fa16.3eca.3efd',
                        'neighbor_state': 'STALE'}}},
            'Gi4': {
                'interface': 'Gi4',
                'neighbors': {
                    '2010:1:3::3': {
                        'age': '0',
                        'ip': '2010:1:3::3',
                        'link_layer_address': '5e01.c002.0007',
                        'neighbor_state': 'STALE'},
                    'FE80::5C01:C0FF:FE02:7': {
                        'age': '2',
                        'ip': 'FE80::5C01:C0FF:FE02:7',
                        'link_layer_address': '5e01.c002.0007',
                        'neighbor_state': 'STALE'}}}}}

    golden_output1 = {'execute.return_value': '''
        csr1kv-1#show ipv6 neighbors 
        IPv6 Address                              Age Link-layer Addr State Interface
        2010:1:2::2                                 0 fa16.3eca.3efd  REACH Gi2
        2010:1:2::11                                - aaaa.beef.cccc  REACH Gi2
        FE80::F816:3EFF:FECA:3EFD                   1 fa16.3eca.3efd  STALE Gi2
        2010:1:3::3                                 0 5e01.c002.0007  STALE Gi4
        FE80::5C01:C0FF:FE02:7                      2 5e01.c002.0007  STALE Gi4
    '''}

    golden_parsed_output2 = {
        'interface': {
            'Gi3': {
                'interface': 'Gi3',
                'neighbors': {
                    '2020:1:2::2': {
                        'age': '0',
                        'ip': '2020:1:2::2',
                        'link_layer_address': 'fa16.3e20.fa5b',
                        'neighbor_state': 'REACH'},
                    '2020:1:3::11': {
                        'age': '-',
                        'ip': '2020:1:3::11',
                        'link_layer_address': 'bbbb.beef.cccc',
                        'neighbor_state': 'REACH'},
                    'FE80::F816:3EFF:FE20:FA5B': {
                        'age': '0',
                        'ip': 'FE80::F816:3EFF:FE20:FA5B',
                        'link_layer_address': 'fa16.3e20.fa5b',
                        'neighbor_state': 'REACH'}}},
            'Gi5': {
                'interface': 'Gi5',
                'neighbors': {
                    '2020:1:3::3': {
                        'age': '0',
                        'ip': '2020:1:3::3',
                        'link_layer_address': '5e01.c002.0007',
                        'neighbor_state': 'REACH'},
                    'FE80::5C01:C0FF:FE02:7': {
                        'age': '1',
                        'ip': 'FE80::5C01:C0FF:FE02:7',
                        'link_layer_address': '5e01.c002.0007',
                        'neighbor_state': 'STALE'}}}}}

    golden_output2 = {'execute.return_value': '''
        csr1kv-1#show ipv6 neighbors vrf vrf1
        IPv6 Address                              Age Link-layer Addr State Interface
        2020:1:2::2                                 0 fa16.3e20.fa5b  REACH Gi3
        2020:1:3::11                                - bbbb.beef.cccc  REACH Gi3
        FE80::F816:3EFF:FE20:FA5B                   0 fa16.3e20.fa5b  REACH Gi3
        2020:1:3::3                                 0 5e01.c002.0007  REACH Gi5
        FE80::5C01:C0FF:FE02:7                      1 5e01.c002.0007  STALE Gi5
    '''}

    def test_show_ipv6_neighbors_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6NeighborsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_neighbors_detail_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowIpv6NeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ipv6_neighbors_vrf_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpv6NeighborsDetail(device=self.device)
        parsed_output = obj.parse(vrf_id='vrf1')
        self.assertEqual(parsed_output, self.golden_parsed_output2)


#############################################################################
# Unittest for 'show ipv6 interface'
#############################################################################

class test_show_ipv6_interface(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'GigabitEthernet2': {
            'enabled': True,
            'oper_status': 'up',
            'ipv6': {
                'FE80::F816:3EFF:FE19:ABBA': {
                    'ip': 'FE80::F816:3EFF:FE19:ABBA',
                    'origin': 'link_layer',
                    'status': 'valid'},
                '2010:1:2::1/64': {
                    'ip': '2010:1:2::1',
                    'prefix_length': '64',
                    'status': 'valid'},
                'enabled': True,
                'icmp': {
                    'error_messages_limited': 100,
                    'redirects': True,
                    'unreachables': 'sent'},
                'nd': {
                    'dad_enabled': True,
                    'dad_attempts': 1,
                    'reachable_time': 30000,
                    'using_time': 30000,
                    'advertised_reachable_time': 0,
                    'advertised_reachable_time_unspecified': True,
                    'advertised_retransmit_interval': 0,
                    'advertised_retransmit_interval_unspecified': True,
                    'router_advertisements_live': 1801,
                    'advertised_default_router_preference': 'Medium'}},
            'joined_group_addresses': ['FF02::1',
                                       'FF02::1:FF00:1',
                                       'FF02::1:FF19:ABBA',
                                       'FF02::2',
                                       'FF02::5',
                                       'FF02::6'],
            'mtu': 1500,
            'addresses_config_method': 'stateless autoconfig'},
        'GigabitEthernet3': {
            'enabled': True,
            'oper_status': 'up',
            'ipv6': {
                'FE80::F816:3EFF:FE72:8407': {
                    'ip': 'FE80::F816:3EFF:FE72:8407',
                    'origin': 'link_layer',
                    'status': 'valid'},
                '2020:1:2::1/64': {
                    'ip': '2020:1:2::1',
                    'prefix_length': '64',
                    'status': 'valid'},
                'enabled': True,
                'icmp': {
                    'error_messages_limited': 100,
                    'redirects': True,
                    'unreachables': 'sent'},
                'nd': {
                    'dad_enabled': True,
                    'dad_attempts': 1,
                    'reachable_time': 30000,
                    'using_time': 30000,
                    'advertised_reachable_time': 0,
                    'advertised_reachable_time_unspecified': True,
                    'advertised_retransmit_interval': 0,
                    'advertised_retransmit_interval_unspecified': True,
                    'router_advertisements_interval': 200,
                    'router_advertisements_live': 1800,
                    'advertised_default_router_preference': 'Medium'}},
            'joined_group_addresses': ['FF02::1',
                                       'FF02::1:FF00:1',
                                       'FF02::1:FF72:8407',
                                       'FF02::2',
                                       'FF02::5',
                                       'FF02::6'],
            'mtu': 1500,
            'vrf': 'vrf1',
            'addresses_config_method': 'stateless autoconfig'},
        'GigabitEthernet4': {
            'enabled': True,
            'oper_status': 'up',
            'ipv6': {
                'FE80::F816:3EFF:FE19:8682': {
                    'ip': 'FE80::F816:3EFF:FE19:8682',
                    'origin': 'link_layer',
                    'status': 'valid'},
                '2010:1:3::1/64': {
                    'ip': '2010:1:3::1',
                    'prefix_length': '64',
                    'status': 'valid'},
                'enabled': True,
                'icmp': {
                    'error_messages_limited': 100,
                    'redirects': True,
                    'unreachables': 'sent'},
                'nd': {
                    'dad_enabled': True,
                    'dad_attempts': 1,
                    'reachable_time': 30000,
                    'using_time': 30000,
                    'advertised_reachable_time': 0,
                    'advertised_reachable_time_unspecified': True,
                    'advertised_retransmit_interval': 0,
                    'advertised_retransmit_interval_unspecified': True,
                    'router_advertisements_interval': 200,
                    'router_advertisements_live': 1800,
                    'advertised_default_router_preference': 'Medium'}},
            'joined_group_addresses': ['FF02::1',
                                       'FF02::1:FF00:1',
                                       'FF02::1:FF19:8682',
                                       'FF02::2',
                                       'FF02::5',
                                       'FF02::6'],
            'mtu': 1500,
            'addresses_config_method': 'stateless autoconfig'},
        'GigabitEthernet5': {
            'enabled': True,
            'oper_status': 'up',
            'ipv6': {
                'FE80::F816:3EFF:FEC7:8140': {
                    'ip': 'FE80::F816:3EFF:FEC7:8140',
                    'origin': 'link_layer',
                    'status': 'valid'},
                '2020:1:3::1/64': {
                    'ip': '2020:1:3::1',
                    'prefix_length': '64',
                    'status': 'valid'},
                'enabled': True,
                'icmp': {
                    'error_messages_limited': 100,
                    'redirects': True,
                    'unreachables': 'sent'},
                'nd': {
                    'dad_enabled': True,
                    'dad_attempts': 1,
                    'reachable_time': 30000,
                    'using_time': 30000,
                    'advertised_reachable_time': 0,
                    'advertised_reachable_time_unspecified': True,
                    'advertised_retransmit_interval': 0,
                    'advertised_retransmit_interval_unspecified': True,
                    'router_advertisements_interval': 200,
                    'router_advertisements_live': 1800,
                    'advertised_default_router_preference': 'Medium'}},
            'joined_group_addresses': ['FF02::1',
                                       'FF02::1:FF00:1',
                                       'FF02::1:FFC7:8140',
                                       'FF02::2',
                                       'FF02::5',
                                       'FF02::6'],
            'mtu': 1500,
            'vrf': 'vrf1',
            'addresses_config_method': 'stateless autoconfig'},
        'Loopback0': {
            'enabled': True,
            'oper_status': 'up',
            'ipv6': {
                'FE80::21E:49FF:FE5D:CC00': {
                    'ip': 'FE80::21E:49FF:FE5D:CC00',
                    'origin': 'link_layer',
                    'status': 'valid'},
                '2001:1:1::1/128': {
                    'ip': '2001:1:1::1',
                    'prefix_length': '128',
                    'status': 'valid'},
                'enabled': True,
                'icmp': {
                    'error_messages_limited': 100,
                    'redirects': True,
                    'unreachables': 'sent'},
                'nd': {
                    'reachable_time': 30000,
                    'using_time': 30000,
                    'advertised_reachable_time': 0,
                    'advertised_reachable_time_unspecified': True,
                    'advertised_retransmit_interval': 0,
                    'advertised_retransmit_interval_unspecified': True,
                    'router_advertisements_live': 1800,
                    'advertised_default_router_preference': 'Medium'}},
            'joined_group_addresses': ['FF02::1',
                                       'FF02::1:FF00:1',
                                       'FF02::1:FF5D:CC00',
                                       'FF02::2',
                                       'FF02::5'],
            'mtu': 1514,
            'addresses_config_method': 'stateless autoconfig'},
        'Loopback1': {
            'enabled': True,
            'oper_status': 'up',
            'ipv6': {
                'FE80::21E:49FF:FE5D:CC00': {
                    'ip': 'FE80::21E:49FF:FE5D:CC00',
                    'origin': 'link_layer',
                    'status': 'valid'},
                '2001:11:11::11/128': {
                    'ip': '2001:11:11::11',
                    'prefix_length': '128',
                    'status': 'valid'},
                'enabled': True,
                'icmp': {
                    'error_messages_limited': 100,
                    'redirects': True,
                    'unreachables': 'sent'},
                'nd': {
                    'reachable_time': 30000,
                    'using_time': 30000,
                    'advertised_reachable_time': 0,
                    'advertised_reachable_time_unspecified': True,
                    'advertised_retransmit_interval': 0,
                    'advertised_retransmit_interval_unspecified': True,
                    'router_advertisements_live': 1800,
                    'advertised_default_router_preference': 'Medium'}},
            'joined_group_addresses': ['FF02::1',
                                       'FF02::1:FF00:11',
                                       'FF02::1:FF5D:CC00',
                                       'FF02::2',
                                       'FF02::5'],
            'mtu': 1514,
            'vrf': 'vrf1',
            'addresses_config_method': 'stateless autoconfig'}}

    golden_output = {'execute.return_value': '''
        csr1kv-1#show ipv6 interface 
        GigabitEthernet2 is up, line protocol is up
            IPv6 is enabled, link-local address is FE80::F816:3EFF:FE19:ABBA 
            No Virtual link-local address(es):
            Global unicast address(es):
              2010:1:2::1, subnet is 2010:1:2::/64 
            Joined group address(es):
                FF02::1
                FF02::2
                FF02::5
                FF02::6
                FF02::1:FF00:1
                FF02::1:FF19:ABBA
            MTU is 1500 bytes
            ICMP error messages limited to one every 100 milliseconds
            ICMP redirects are enabled
            ICMP unreachables are sent
            ND DAD is enabled, number of DAD attempts: 1
            ND reachable time is 30000 milliseconds (using 30000)
            ND advertised reachable time is 0 (unspecified)
            ND advertised retransmit interval is 0 (unspecified)
            ND router advertisements live for 1801 seconds
            ND advertised default router preference is Medium
            ND RAs are suppressed (periodic)
            Hosts use stateless autoconfig for addresses.
        GigabitEthernet3 is up, line protocol is up
            IPv6 is enabled, link-local address is FE80::F816:3EFF:FE72:8407 
            No Virtual link-local address(es):
            Global unicast address(es):
                2020:1:2::1, subnet is 2020:1:2::/64 
            Joined group address(es):
                FF02::1
                FF02::2
                FF02::5
                FF02::6
                FF02::1:FF00:1
                FF02::1:FF72:8407
            MTU is 1500 bytes
            VPN Routing/Forwarding "vrf1"
            ICMP error messages limited to one every 100 milliseconds
            ICMP redirects are enabled
            ICMP unreachables are sent
            ND DAD is enabled, number of DAD attempts: 1
            ND reachable time is 30000 milliseconds (using 30000)
            ND advertised reachable time is 0 (unspecified)
            ND advertised retransmit interval is 0 (unspecified)
            ND router advertisements are sent every 200 seconds
            ND router advertisements live for 1800 seconds
            ND advertised default router preference is Medium
            Hosts use stateless autoconfig for addresses.
        GigabitEthernet4 is up, line protocol is up
            IPv6 is enabled, link-local address is FE80::F816:3EFF:FE19:8682 
            No Virtual link-local address(es):
            Global unicast address(es):
                2010:1:3::1, subnet is 2010:1:3::/64 
            Joined group address(es):
                FF02::1
                FF02::2
                FF02::5
                FF02::6
                FF02::1:FF00:1
                FF02::1:FF19:8682
            MTU is 1500 bytes
            ICMP error messages limited to one every 100 milliseconds
            ICMP redirects are enabled
            ICMP unreachables are sent
            ND DAD is enabled, number of DAD attempts: 1
            ND reachable time is 30000 milliseconds (using 30000)
            ND advertised reachable time is 0 (unspecified)
            ND advertised retransmit interval is 0 (unspecified)
            ND router advertisements are sent every 200 seconds
            ND router advertisements live for 1800 seconds
            ND advertised default router preference is Medium
            Hosts use stateless autoconfig for addresses.
        GigabitEthernet5 is up, line protocol is up
            IPv6 is enabled, link-local address is FE80::F816:3EFF:FEC7:8140 
            No Virtual link-local address(es):
            Global unicast address(es):
                2020:1:3::1, subnet is 2020:1:3::/64 
            Joined group address(es):
                FF02::1
                FF02::2
                FF02::5
                FF02::6
                FF02::1:FF00:1
                FF02::1:FFC7:8140
            MTU is 1500 bytes
            VPN Routing/Forwarding "vrf1"
            ICMP error messages limited to one every 100 milliseconds
            ICMP redirects are enabled
            ICMP unreachables are sent
            ND DAD is enabled, number of DAD attempts: 1
            ND reachable time is 30000 milliseconds (using 30000)
            ND advertised reachable time is 0 (unspecified)
            ND advertised retransmit interval is 0 (unspecified)
            ND router advertisements are sent every 200 seconds
            ND router advertisements live for 1800 seconds
            ND advertised default router preference is Medium
            Hosts use stateless autoconfig for addresses.
        Loopback0 is up, line protocol is up
            IPv6 is enabled, link-local address is FE80::21E:49FF:FE5D:CC00 
            No Virtual link-local address(es):
            Global unicast address(es):
                2001:1:1::1, subnet is 2001:1:1::1/128 
            Joined group address(es):
                FF02::1
                FF02::2
                FF02::5
                FF02::1:FF00:1
                FF02::1:FF5D:CC00
            MTU is 1514 bytes
            ICMP error messages limited to one every 100 milliseconds
            ICMP redirects are enabled
            ICMP unreachables are sent
            ND DAD is not supported
            ND reachable time is 30000 milliseconds (using 30000)
            ND advertised reachable time is 0 (unspecified)
            ND advertised retransmit interval is 0 (unspecified)
            ND router advertisements live for 1800 seconds
            ND advertised default router preference is Medium
            ND RAs are suppressed (periodic)
            Hosts use stateless autoconfig for addresses.
        Loopback1 is up, line protocol is up
            IPv6 is enabled, link-local address is FE80::21E:49FF:FE5D:CC00 
            No Virtual link-local address(es):
            Global unicast address(es):
                2001:11:11::11, subnet is 2001:11:11::11/128 
            Joined group address(es):
                FF02::1
                FF02::2
                FF02::5
                FF02::1:FF00:11
                FF02::1:FF5D:CC00
            MTU is 1514 bytes
            VPN Routing/Forwarding "vrf1"
            ICMP error messages limited to one every 100 milliseconds
            ICMP redirects are enabled
            ICMP unreachables are sent
            ND DAD is not supported
            ND reachable time is 30000 milliseconds (using 30000)
            ND advertised reachable time is 0 (unspecified)
            ND advertised retransmit interval is 0 (unspecified)
            ND router advertisements live for 1800 seconds
            ND advertised default router preference is Medium
            ND RAs are suppressed (periodic)
            Hosts use stateless autoconfig for addresses.
    '''}

    def test_show_ipv6_interface_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6Interface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_interface_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6Interface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()