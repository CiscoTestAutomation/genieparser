import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

from genie.libs.parser.iosxr.show_ipv6 import ShowIpv6VrfAllInterface, \
                                                   ShowIpv6NeighborsDetail


#############################################################################
# unitest For show ipv6 neighbors detail
#############################################################################

class test_show_ipv6_neighbors_detail(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Gi0/0/0/0': {
                'ipv6_address': {
                    '2010:1:2::1': {
                        'age': '82',
                        'dynamic': 'Y',
                        'link_layer_add': 'fa16.3e19.abba',
                        'location': '0/0/CPU0',
                        'serg_flags': 'ff',
                        'state': 'REACH',
                        'static': '-',
                        'sync': '-'},
                    '2010:1:2::22': {
                        'age': '-',
                        'dynamic': '-',
                        'link_layer_add': 'aaaa.beaf.bbbb',
                        'location': '0/0/CPU0',
                        'serg_flags': 'ff',
                        'state': 'REACH',
                        'static': 'Y',
                        'sync': '-'},
                    'fe80::f816:3eff:fe19:abba': {
                        'age': '158',
                        'dynamic': 'Y',
                        'link_layer_add': 'fa16.3e19.abba',
                        'location': '0/0/CPU0',
                        'serg_flags': 'ff',
                        'state': 'REACH',
                        'static': '-',
                        'sync': '-'}}},
                'Gi0/0/0/1': {
                    'ipv6_address': {
                        '2020:1:2::1': {
                            'age': '4',
                            'dynamic': 'Y',
                            'link_layer_add': 'fa16.3e72.8407',
                            'location': '0/0/CPU0',
                            'serg_flags': 'ff',
                            'state': 'REACH',
                            'static': '-',
                            'sync': '-'},
                        '2020:1:2::22': {
                            'age': '-',
                            'dynamic': '-',
                            'link_layer_add': 'dddd.beef.aaaa',
                            'location': '0/0/CPU0',
                            'serg_flags': 'ff',
                            'state': 'REACH',
                            'static': 'Y',
                            'sync': '-'},
                        'fe80::f816:3eff:fe72:8407': {
                            'age': '37',
                            'dynamic': 'Y',
                            'link_layer_add': 'fa16.3e72.8407',
                            'location': '0/0/CPU0',
                            'serg_flags': 'ff',
                            'state': 'REACH',
                            'static': '-',
                            'sync': '-'}}},
                'Gi0/0/0/2': {
                    'ipv6_address': {
                        '2010:2:3::3': {
                            'age': '1',
                            'dynamic': 'Y',
                            'link_layer_add': '5e01.c002.0007',
                            'location': '0/0/CPU0',
                            'serg_flags': 'ff',
                            'state': 'REACH',
                            'static': '-',
                            'sync': '-'},
                        'fe80::5c01:c0ff:fe02:7': {
                            'age': '12',
                            'dynamic': 'Y',
                            'link_layer_add': '5e01.c002.0007',
                            'location': '0/0/CPU0',
                            'serg_flags': 'ff',
                            'state': 'REACH',
                            'static': '-',
                            'sync': '-'}}},
                'Gi0/0/0/3': {
                    'ipv6_address': {
                        '2020:2:3::3': {
                            'age': '114',
                            'dynamic': 'Y',
                            'link_layer_add': '5e01.c002.0007',
                            'location': '0/0/CPU0',
                            'serg_flags': 'ff',
                            'state': 'REACH',
                            'static': '-',
                            'sync': '-'},
                        'fe80::5c01:c0ff:fe02:7': {
                            'age': '12',
                            'dynamic': 'Y',
                            'link_layer_add': '5e01.c002.0007',
                            'location': '0/0/CPU0',
                            'serg_flags': 'ff',
                            'state': 'REACH',
                            'static': '-',
                            'sync': '-'}}}}}

    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:xr9kv-2#show ipv6 neighbors detail
        Thu Apr 26 13:09:53.379 UTC
        IPv6 Address                             Age  Link-layer Add State Interface            Location      Static Dynamic Sync       Serg-Flags 
        2010:1:2::1                              82   fa16.3e19.abba REACH Gi0/0/0/0            0/0/CPU0        -      Y       -            ff
        2010:1:2::22                                - aaaa.beaf.bbbb REACH Gi0/0/0/0            0/0/CPU0        Y      -       -            ff
        fe80::f816:3eff:fe19:abba                158  fa16.3e19.abba REACH Gi0/0/0/0            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0            0/0/CPU0        -      -       -            ff
        2020:2:3::3                              114  5e01.c002.0007 REACH Gi0/0/0/3            0/0/CPU0        -      Y       -            ff
        fe80::5c01:c0ff:fe02:7                   12   5e01.c002.0007 REACH Gi0/0/0/3            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/3            0/0/CPU0        -      -       -            ff
        2010:2:3::3                              1    5e01.c002.0007 REACH Gi0/0/0/2            0/0/CPU0        -      Y       -            ff
        fe80::5c01:c0ff:fe02:7                   12   5e01.c002.0007 REACH Gi0/0/0/2            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/2            0/0/CPU0        -      -       -            ff
        2020:1:2::1                              4    fa16.3e72.8407 REACH Gi0/0/0/1            0/0/CPU0        -      Y       -            ff
        2020:1:2::22                                - dddd.beef.aaaa REACH Gi0/0/0/1            0/0/CPU0        Y      -       -            ff
        fe80::f816:3eff:fe72:8407                37   fa16.3e72.8407 REACH Gi0/0/0/1            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/1            0/0/CPU0        -      -       -            ff
    '''}

    def test_show_ipv6_neighbors_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6NeighborsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_neighbors_detail_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6NeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        #import pdb;pdb.set_trace()
        self.assertEqual(parsed_output, self.golden_parsed_output)


#############################################################################
# unitest For show ipv6 vrf all interface
#############################################################################

class test_show_ipv6_vrf_all_interface(unittest.TestCase):

    device = Device(name='aDevice')

    device0 = Device(name='bDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'GigabitEthernet0/0/0/0': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2010:1:2::2/64': {
                    'ipv6': '2010:1:2::2',
                    'ipv6_prefix_length': '64',
                    'ipv6_subnet': '2010:1:2::'},
                    'complete_glean_adj': '1',
                    'complete_protocol_adj': '1',
                    'dad_attempts': '1',
                    'dropped_glean_req': '0',
                    'dropped_protocol_req': '0',
                    'icmp_redirects': 'disabled',
                    'icmp_unreachables': 'enabled',
                    'incomplete_glean_adj': '0',
                    'incomplete_protocol_adj': '0',
                    'ipv6_groups': ['ff02::1:ff00:2',
                                    'ff02::1:ffca:3efd',
                                    'ff02::2',
                                    'ff02::1',
                                    'ff02::5',
                                    'ff02::6'],
                    'ipv6_link_local': 'fe80::f816:3eff:feca:3efd',
                    'ipv6_mtu': '1514',
                    'ipv6_mtu_available': '1500',
                    'nd_adv_retrans_int': '0',
                    'nd_cache_limit': '1000000000',
                    'nd_dad': 'enabled',
                    'nd_reachable_time': '0',
                    'stateless_autoconfig': True,
                    'table_id': '0xe0800000'},
                'ipv6_enabled': True,
                'oper_status': 'up',
                'vrf': 'default',
                'vrf_id': '0x60000000'},
        'GigabitEthernet0/0/0/1': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2020:1:2::2/64': {
                    'ipv6': '2020:1:2::2',
                    'ipv6_prefix_length': '64',
                    'ipv6_subnet': '2020:1:2::'},
                'complete_glean_adj': '2',
                'complete_protocol_adj': '0',
                'dad_attempts': '1',
                'dropped_glean_req': '0',
                'dropped_protocol_req': '0',
                'icmp_redirects': 'disabled',
                'icmp_unreachables': 'enabled',
                'incomplete_glean_adj': '0',
                'incomplete_protocol_adj': '0',
                'ipv6_groups': ['ff02::1:ff00:2',
                                'ff02::1:ff20:fa5b',
                                'ff02::2',
                                'ff02::1',
                                'ff02::5',
                                'ff02::6'],
                'ipv6_link_local': 'fe80::f816:3eff:fe20:fa5b',
                'ipv6_mtu': '1514',
                'ipv6_mtu_available': '1500',
                'nd_adv_duration': '160-240',
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '1000000000',
                'nd_dad': 'enabled',
                'nd_reachable_time': '0',
                'nd_router_adv': '1800',
                'stateless_autoconfig': True,
                'table_id': '0xe0800001'},
            'ipv6_enabled': True,
            'oper_status': 'up',
            'vrf': 'vrf1',
            'vrf_id': '0x60000001'},
        'GigabitEthernet0/0/0/2': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2010:2:3::2/64': {
                    'ipv6': '2010:2:3::2',
                    'ipv6_prefix_length': '64',
                    'ipv6_subnet': '2010:2:3::'},
                'complete_glean_adj': '1',
                'complete_protocol_adj': '1',
                'dad_attempts': '1',
                'dropped_glean_req': '0',
                'dropped_protocol_req': '0',
                'icmp_redirects': 'disabled',
                'icmp_unreachables': 'enabled',
                'incomplete_glean_adj': '0',
                'incomplete_protocol_adj': '0',
                'ipv6_groups': ['ff02::1:ff00:2',
                                'ff02::1:ff82:6320',
                                'ff02::2',
                                'ff02::1',
                                'ff02::5',
                                'ff02::6'],
                'ipv6_link_local': 'fe80::f816:3eff:fe82:6320',
                'ipv6_mtu': '1514',
                'ipv6_mtu_available': '1500',
                'nd_adv_duration': '160-240',
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '1000000000',
                'nd_dad': 'enabled',
                'nd_reachable_time': '0',
                'nd_router_adv': '1800',
                'stateless_autoconfig': True,
                'table_id': '0xe0800000'},
            'ipv6_enabled': True,
            'oper_status': 'up',
            'vrf': 'default',
            'vrf_id': '0x60000000'},
        'GigabitEthernet0/0/0/3': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2020:2:3::2/64': {
                    'ipv6': '2020:2:3::2',
                    'ipv6_prefix_length': '64',
                    'ipv6_subnet': '2020:2:3::'},
                'complete_glean_adj': '1',
                'complete_protocol_adj': '1',
                'dad_attempts': '1',
                'dropped_glean_req': '0',
                'dropped_protocol_req': '0',
                'icmp_redirects': 'disabled',
                'icmp_unreachables': 'enabled',
                'incomplete_glean_adj': '0',
                'incomplete_protocol_adj': '0',
                'ipv6_groups': ['ff02::1:ff00:2',
                                'ff02::1:ff8b:59c9',
                                'ff02::2',
                                'ff02::1',
                                'ff02::5',
                                'ff02::6'],
                'ipv6_link_local': 'fe80::f816:3eff:fe8b:59c9',
                'ipv6_mtu': '1514',
                'ipv6_mtu_available': '1500',
                'nd_adv_duration': '160-240',
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '1000000000',
                'nd_dad': 'enabled',
                'nd_reachable_time': '0',
                'nd_router_adv': '1800',
                'stateless_autoconfig': True,
                'table_id': '0xe0800001'},
            'ipv6_enabled': True,
            'oper_status': 'up',
            'vrf': 'vrf1',
            'vrf_id': '0x60000001'},
        'Loopback0': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2001:2:2::2/128': {
                    'ipv6': '2001:2:2::2',
                    'ipv6_prefix_length': '128',
                    'ipv6_subnet': '2001:2:2::2'},
                'complete_glean_adj': '0',
                'complete_protocol_adj': '0',
                'dad_attempts': '0',
                'dropped_glean_req': '0',
                'dropped_protocol_req': '0',
                'icmp_redirects': 'disabled',
                'incomplete_glean_adj': '0',
                'incomplete_protocol_adj': '0',
                'ipv6_groups': ['ff02::1:ff00:2',
                                'ff02::1:ffbd:853e',
                                'ff02::2',
                                'ff02::1'],
                'ipv6_link_local': 'fe80::6983:ecff:febd:853e',
                'ipv6_mtu': '1500',
                'ipv6_mtu_available': '1500',
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '0',
                'nd_dad': 'disabled',
                'nd_reachable_time': '0',
                'stateless_autoconfig': True,
                'table_id': '0xe0800000'},
            'ipv6_enabled': True,
            'oper_status': 'up',
            'vrf': 'default',
            'vrf_id': '0x60000000'},
        'Loopback1': {
            'enabled': True,
            'int_status': 'up',
            'ipv6': {
                '2001:22:22::22/128': {
                    'ipv6': '2001:22:22::22',
                    'ipv6_prefix_length': '128',
                    'ipv6_subnet': '2001:22:22::22'},
                'complete_glean_adj': '0',
                'complete_protocol_adj': '0',
                'dad_attempts': '0',
                'dropped_glean_req': '0',
                'dropped_protocol_req': '0',
                'icmp_redirects': 'disabled',
                'incomplete_glean_adj': '0',
                'incomplete_protocol_adj': '0',
                'ipv6_groups': ['ff02::1:ff00:22',
                                'ff02::1:ffbd:853e',
                                'ff02::2',
                                'ff02::1'],
                'ipv6_link_local': 'fe80::6983:ecff:febd:853e',
                'ipv6_mtu': '1500',
                'ipv6_mtu_available': '1500',
                'nd_adv_retrans_int': '0',
                'nd_cache_limit': '0',
                'nd_dad': 'disabled',
                'nd_reachable_time': '0',
                'stateless_autoconfig': True,
                'table_id': '0xe0800000'},
            'ipv6_enabled': True,
            'oper_status': 'up',
            'vrf': 'default',
            'vrf_id': '0x60000000'},
        'MgmtEth0/RP0/CPU0/0': {
            'enabled': False,
            'int_status': 'shutdown',
            'ipv6_enabled': False,
            'oper_status': 'down',
            'vrf': 'default',
            'vrf_id': '0x60000000'}}

    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:xr9kv-2#show ipv6 vrf all interface 
        Thu Apr 26 13:10:00.784 UTC
        Loopback0 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
            IPv6 is enabled, link-local address is fe80::6983:ecff:febd:853e 
            Global unicast address(es):
              2001:2:2::2, subnet is 2001:2:2::2/128 
            Joined group address(es): ff02::1:ff00:2 ff02::1:ffbd:853e ff02::2
                ff02::1
            MTU is 1500 (1500 is available to IPv6)
            ICMP redirects are disabled
            ICMP unreachables are always on
            ND DAD is disabled, number of DAD attempts 0
            ND reachable time is 0 milliseconds
            ND cache entry limit is 0
            ND advertised retransmit interval is 0 milliseconds
            Hosts use stateless autoconfig for addresses.
            Outgoing access list is not set
            Inbound  common access list is not set, access list is not set
            Table Id is 0xe0800000
            Complete protocol adjacency: 0
            Complete glean adjacency: 0
            Incomplete protocol adjacency: 0
            Incomplete glean adjacency: 0
            Dropped protocol request: 0
            Dropped glean request: 0
        Loopback1 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
            IPv6 is enabled, link-local address is fe80::6983:ecff:febd:853e 
            Global unicast address(es):
              2001:22:22::22, subnet is 2001:22:22::22/128 
            Joined group address(es): ff02::1:ff00:22 ff02::1:ffbd:853e ff02::2
                ff02::1
            MTU is 1500 (1500 is available to IPv6)
            ICMP redirects are disabled
            ICMP unreachables are always on
            ND DAD is disabled, number of DAD attempts 0
            ND reachable time is 0 milliseconds
            ND cache entry limit is 0
            ND advertised retransmit interval is 0 milliseconds
            Hosts use stateless autoconfig for addresses.
            Outgoing access list is not set
            Inbound  common access list is not set, access list is not set
            Table Id is 0xe0800000
            Complete protocol adjacency: 0
            Complete glean adjacency: 0
            Incomplete protocol adjacency: 0
            Incomplete glean adjacency: 0
            Dropped protocol request: 0
            Dropped glean request: 0
        MgmtEth0/RP0/CPU0/0 is Shutdown, ipv6 protocol is Down, Vrfid is default (0x60000000)
            IPv6 is disabled, link-local address unassigned
            No global unicast address is configured
        GigabitEthernet0/0/0/0 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
            IPv6 is enabled, link-local address is fe80::f816:3eff:feca:3efd 
            Global unicast address(es):
                2010:1:2::2, subnet is 2010:1:2::/64 
            Joined group address(es): ff02::1:ff00:2 ff02::1:ffca:3efd ff02::2
                ff02::1 ff02::5 ff02::6
            MTU is 1514 (1500 is available to IPv6)
            ICMP redirects are disabled
            ICMP unreachables are enabled
            ND DAD is enabled, number of DAD attempts 1
            ND reachable time is 0 milliseconds
            ND cache entry limit is 1000000000
            ND advertised retransmit interval is 0 milliseconds
            Hosts use stateless autoconfig for addresses.
            Outgoing access list is not set
            Inbound  common access list is not set, access list is not set
            Table Id is 0xe0800000
            Complete protocol adjacency: 1
            Complete glean adjacency: 1
            Incomplete protocol adjacency: 0
            Incomplete glean adjacency: 0
            Dropped protocol request: 0
            Dropped glean request: 0
        GigabitEthernet0/0/0/1 is Up, ipv6 protocol is Up, Vrfid is vrf1 (0x60000001)
            IPv6 is enabled, link-local address is fe80::f816:3eff:fe20:fa5b 
            Global unicast address(es):
              2020:1:2::2, subnet is 2020:1:2::/64 
            Joined group address(es): ff02::1:ff00:2 ff02::1:ff20:fa5b ff02::2
                ff02::1 ff02::5 ff02::6
            MTU is 1514 (1500 is available to IPv6)
            ICMP redirects are disabled
            ICMP unreachables are enabled
            ND DAD is enabled, number of DAD attempts 1
            ND reachable time is 0 milliseconds
            ND cache entry limit is 1000000000
            ND advertised retransmit interval is 0 milliseconds
            ND router advertisements are sent every 160 to 240 seconds
            ND router advertisements live for 1800 seconds
            Hosts use stateless autoconfig for addresses.
            Outgoing access list is not set
            Inbound  common access list is not set, access list is not set
            Table Id is 0xe0800001
            Complete protocol adjacency: 0
            Complete glean adjacency: 2
            Incomplete protocol adjacency: 0
            Incomplete glean adjacency: 0
            Dropped protocol request: 0
            Dropped glean request: 0
        GigabitEthernet0/0/0/2 is Up, ipv6 protocol is Up, Vrfid is default (0x60000000)
            IPv6 is enabled, link-local address is fe80::f816:3eff:fe82:6320 
            Global unicast address(es):
              2010:2:3::2, subnet is 2010:2:3::/64 
            Joined group address(es): ff02::1:ff00:2 ff02::1:ff82:6320 ff02::2
                ff02::1 ff02::5 ff02::6
            MTU is 1514 (1500 is available to IPv6)
            ICMP redirects are disabled
            ICMP unreachables are enabled
            ND DAD is enabled, number of DAD attempts 1
            ND reachable time is 0 milliseconds
            ND cache entry limit is 1000000000
            ND advertised retransmit interval is 0 milliseconds
            ND router advertisements are sent every 160 to 240 seconds
            ND router advertisements live for 1800 seconds
            Hosts use stateless autoconfig for addresses.
            Outgoing access list is not set
            Inbound  common access list is not set, access list is not set
            Table Id is 0xe0800000
            Complete protocol adjacency: 1
            Complete glean adjacency: 1
            Incomplete protocol adjacency: 0
            Incomplete glean adjacency: 0
            Dropped protocol request: 0
            Dropped glean request: 0
        GigabitEthernet0/0/0/3 is Up, ipv6 protocol is Up, Vrfid is vrf1 (0x60000001)
            IPv6 is enabled, link-local address is fe80::f816:3eff:fe8b:59c9 
            Global unicast address(es):
              2020:2:3::2, subnet is 2020:2:3::/64 
            Joined group address(es): ff02::1:ff00:2 ff02::1:ff8b:59c9 ff02::2
                ff02::1 ff02::5 ff02::6
            MTU is 1514 (1500 is available to IPv6)
            ICMP redirects are disabled
            ICMP unreachables are enabled
            ND DAD is enabled, number of DAD attempts 1
            ND reachable time is 0 milliseconds
            ND cache entry limit is 1000000000
            ND advertised retransmit interval is 0 milliseconds
            ND router advertisements are sent every 160 to 240 seconds
            ND router advertisements live for 1800 seconds
            Hosts use stateless autoconfig for addresses.
            Outgoing access list is not set
            Inbound  common access list is not set, access list is not set
            Table Id is 0xe0800001
            Complete protocol adjacency: 1
            Complete glean adjacency: 1
            Incomplete protocol adjacency: 0
            Incomplete glean adjacency: 0
            Dropped protocol request: 0
            Dropped glean request: 0
    '''}

    def test_show_ipv6_vrf_all_interface_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6VrfAllInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_vrf_all_interface_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6VrfAllInterface(device=self.device)
        parsed_output = obj.parse()
        #import pdb;pdb.set_trace()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()