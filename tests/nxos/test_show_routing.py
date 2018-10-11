
# Python
import unittest
from unittest.mock import Mock

# Ats
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# nxos show_routing
from genie.libs.parser.nxos.show_routing import ShowRoutingVrfAll, ShowRoutingIpv6VrfAll,\
                                     ShowIpRoute, ShowIpv6Route

# =====================================
#  Unit test for 'show routing vrf all'
# =====================================

class test_show_routing_vrf_all(unittest.TestCase):
    
    '''Unit test for show routing vrf all'''
    
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'vrf':
            {'VRF1':
                {'address_family':
                    {'vpnv4 unicast':
                        {'bgp_distance_internal_as': 33,
                        'bgp_distance_local': 55,
                        'ip':
                            {'11.0.0.0/8':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'Null0':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '5w0d',
                                                        'preference': '55',
                                                        'metric': '0',
                                                        'protocol_id': '100',
                                                        'attribute': 'discard',
                                                        'tag': '100'}}}}}}},
                            '30.5.0.1/32':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'attach': 'attached',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'30.5.0.1':
                                                {'protocol':
                                                    {'local':
                                                        {'uptime': '2w6d',
                                                        'interface': 'Bdi1255',
                                                        'preference': '0',
                                                        'metric': '0'}}}}}}},
                            '57.0.1.0/24':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'100.0.130.3':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '3d10h',
                                                        'preference': '33',
                                                        'metric': '0',
                                                        'protocol_id': '1',
                                                        'attribute': 'internal',
                                                        'tag': '1',
                                                        'evpn': True,
                                                        'segid': 50051,
                                                        'route_table': 'default',
                                                        'tunnelid': '0x64008203',
                                                        'encap': 'vxlan'}}}}}}},
                            '33.33.33.33/32':
                                {'ubest_num': '1',
                                'mbest_num': '1',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'3.3.3.3':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '5w0d',
                                                        'preference': '33',
                                                        'metric': '0',
                                                        'protocol_id': '100',
                                                        'attribute': 'internal',
                                                        'route_table': 'default',
                                                        'mpls_vpn': True,
                                                        'tag': '100'}}}}},
                                    'multicast':
                                        {'nexthop':
                                            {'3.3.3.3':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '5w0d',
                                                        'preference': '33',
                                                        'metric': '0',
                                                        'protocol_id': '100',
                                                        'attribute': 'internal',
                                                        'route_table': 'default',
                                                        'mpls_vpn': True,
                                                        'tag': '100'}}}}}}},
                            "2.2.2.2/32": {
                               "mbest_num": "0",
                               "ubest_num": "1",
                               "best_route": {
                                    "unicast": {
                                         "nexthop": {
                                              "10.2.4.2": {
                                                   "protocol": {
                                                        "ospf": {
                                                             "preference": "110",
                                                             "protocol_id": "1",
                                                             "uptime": "00:18:35",
                                                             "metric": "41",
                                                             "mpls": True,
                                                             "attribute": "intra",
                                                             "interface": "Ethernet2/4"}}}}}}},
                            "1.1.1.1/32": {
                               "mbest_num": "0",
                               "ubest_num": "2",
                               "best_route": {
                                    "unicast": {
                                         "nexthop": {
                                              "10.2.4.2": {
                                                   "protocol": {
                                                        "ospf": {
                                                             "preference": "110",
                                                             "protocol_id": "1",
                                                             "uptime": "00:18:35",
                                                             "metric": "81",
                                                             "mpls": True,
                                                             "attribute": "intra",
                                                             "interface": "Ethernet2/4"}}},
                                              "10.3.4.3": {
                                                   "protocol": {
                                                        "ospf": {
                                                             "preference": "110",
                                                             "protocol_id": "1",
                                                             "uptime": "00:18:35",
                                                             "metric": "81",
                                                             "mpls": True,
                                                             "attribute": "intra",
                                                             "interface": "Ethernet2/1"}}}}}}},
                            '11.11.11.11/32':
                                {'ubest_num': '2',
                                'mbest_num': '0',
                                'attach': 'attached',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'11.11.11.11':
                                                {'protocol':
                                                    {'local':
                                                        {'uptime': '5w4d',
                                                        'preference': '0',
                                                        'metric': '0',
                                                        'interface': 'Loopback1'},
                                                    'direct':
                                                        {'uptime': '5w4d',
                                                        'preference': '0',
                                                        'metric': '0',
                                                        'interface': 'Loopback1'}}}}}}}}}}},
            'default':
                {'address_family':
                    {'ipv4 unicast':
                        {'bgp_distance_extern_as': 20,
                        'bgp_distance_internal_as': 200,
                        'ip':
                            {'104.0.0.0/8':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'vrf default':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '18:11:28',
                                                        'preference': '20',
                                                        'metric': '0',
                                                        'protocol_id': '333',
                                                        'attribute': 'external',
                                                        'tag': '333',
                                                        'interface': 'Null0'}}}}}}},
                            '1.3.1.0/24':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'fec1::1002':
                                                {'protocol':
                                                    {'bgp':
                                                        {'uptime': '15:57:39',
                                                        'preference': '200',
                                                        'metric': '4444',
                                                        'protocol_id': '333',
                                                        'attribute': 'internal',
                                                        'route_table': 'default',
                                                        'tag': '333',
                                                        'interface': 'Ethernet1/1'}}}}}}},
                            '104.0.0.5/8':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'Null0':
                                                {'protocol':
                                                    {'static':
                                                        {'uptime': '18:47:42',
                                                        'preference': '1',
                                                        'metric': '0'}}}}}}}}}}}}}

    golden_output = {'execute.return_value': '''
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        104.0.0.0/8, ubest/mbest: 1/0
            *via vrf default, Null0, [20/0], 18:11:28, bgp-333, external, tag 333
        1.3.1.0/24, ubest/mbest: 1/0
            *via fec1::1002%default, Eth1/1, [200/4444], 15:57:39, bgp-333, internal, tag 333
        104.0.0.5/8, ubest/mbest: 1/0
            *via Null0, [1/0], 18:47:42, static


        IP Route Table for VRF "management"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        IP Route Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        11.0.0.0/8, ubest/mbest: 1/0
            *via Null0, [55/0], 5w0d, bgp-100, discard, tag 100
        30.5.0.1/32, ubest/mbest: 1/0 time, attached
            *via 30.5.0.1, Bdi1255, [0/0], 2w6d, local
        33.33.33.33/32, ubest/mbest: 1/1
            *via 3.3.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
            **via 3.3.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
        57.0.1.0/24, ubest/mbest: 1/0 time
            *via 100.0.130.3%default, [33/0], 3d10h, bgp-1, internal, tag 1 (evpn), segid: 50051 tunnelid: 0x64008203 encap: VXLAN
        11.11.11.11/32, ubest/mbest: 2/0, attached
            *via 11.11.11.11, Lo1, [0/0], 5w4d, local
            *via 11.11.11.11, Lo1, [0/0], 5w4d, direct
        1.1.1.1/32, ubest/mbest: 2/0
            *via 10.2.4.2, Eth2/4, [110/81], 00:18:35, ospf-1, intra (mpls)
            *via 10.3.4.3, Eth2/1, [110/81], 00:18:35, ospf-1, intra (mpls)
        2.2.2.2/32, ubest/mbest: 1/0
            *via 10.2.4.2, Eth2/4, [110/41], 00:18:35, ospf-1, intra (mpls)
        '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        bgp_obj = ShowRoutingVrfAll(device=self.device)
        parsed_output = bgp_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_obj = ShowRoutingVrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_obj.parse()

# ===========================================
#  Unit test for 'show routing ipv6  vrf all'
# ===========================================

class test_show_routing_ipv6_vrf_all(unittest.TestCase):
    
    '''Unit test for show routing ipv6  vrf all'''
    
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrf": {
            "default": {
               "address_family": {
                    "ipv6 unicast": {
                         "bgp_distance_internal_as": 200,
                         "ip": {
                              "2001:db8:1:1::1/128": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8:1:1::1": {
                                                       "protocol": {
                                                            "local": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"
                              },
                              "2001:db8:1:1::/64": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8:1:1::1": {
                                                       "protocol": {
                                                            "direct": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"
                              },
                              "2001:db8:2:2::2/128": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8:2:2::2": {
                                                       "protocol": {
                                                            "local": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "tag": "222",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"
                              },
                              "2001:db8::5054:ff:fed5:63f9/128": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8::5054:ff:fed5:63f9": {
                                                       "protocol": {
                                                            "local": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"
                              },
                              "2001:db8::/64": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8::5054:ff:fed5:63f9": {
                                                       "protocol": {
                                                            "direct": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"
                              },
                              "615:11:11::/64": {
                                   "mbest_num": "0",
                                   "ubest_num": "1",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "::ffff:1.1.1.1": {
                                                       "protocol": {
                                                            "bgp": {
                                                                 "uptime": "00:35:51",
                                                                 "tag": "200",
                                                                 "route_table": "default:IPv4",
                                                                 "attribute": "internal",
                                                                 "mpls": True,
                                                                 "metric": "2219",
                                                                 "preference": "200",
                                                                 "protocol_id": "100"}}}}}}},
                              "2001:db8:2:2::/64": {
                                   "attach": "attached",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "2001:db8:2:2::2": {
                                                       "protocol": {
                                                            "direct": {
                                                                 "interface": "Ethernet1/1",
                                                                 "metric": "0",
                                                                 "tag": "222",
                                                                 "uptime": "00:15:46",
                                                                 "preference": "0"}}}}}},
                                   "mbest_num": "0",
                                   "ubest_num": "1"}}}}},
            "VRF1": {
               "address_family": {
                    "vpnv6 unicast": {
                         "bgp_distance_internal_as": 200,
                         "ip": {
                              "615:11:11:1::/64": {
                                   "mbest_num": "0",
                                   "ubest_num": "1",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "::ffff:1.1.1.1": {
                                                       "protocol": {
                                                            "bgp": {
                                                                 "uptime": "00:35:51",
                                                                 "tag": "200",
                                                                 "mpls_vpn": True,
                                                                 "attribute": "internal",
                                                                 "route_table": "default:IPv4",
                                                                 "metric": "2219",
                                                                 "preference": "200",
                                                                 "protocol_id": "100"}}}}}}}}}}}}
    }

    golden_output = {'execute.return_value': '''
        IPv6 Routing Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        2001:db8::/64, ubest/mbest: 1/0, attached
            *via 2001:db8::5054:ff:fed5:63f9, Eth1/1, [0/0], 00:15:46, direct, 
        2001:db8::5054:ff:fed5:63f9/128, ubest/mbest: 1/0, attached
            *via 2001:db8::5054:ff:fed5:63f9, Eth1/1, [0/0], 00:15:46, local
        2001:db8:1:1::/64, ubest/mbest: 1/0, attached
            *via 2001:db8:1:1::1, Eth1/1, [0/0], 00:15:46, direct, 
        2001:db8:1:1::1/128, ubest/mbest: 1/0, attached
            *via 2001:db8:1:1::1, Eth1/1, [0/0], 00:15:46, local
        2001:db8:2:2::/64, ubest/mbest: 1/0, attached
            *via 2001:db8:2:2::2, Eth1/1, [0/0], 00:15:46, direct, , tag 222
        2001:db8:2:2::2/128, ubest/mbest: 1/0, attached
            *via 2001:db8:2:2::2, Eth1/1, [0/0], 00:15:46, local, tag 222
        615:11:11::/64, ubest/mbest: 1/0
            *via ::ffff:1.1.1.1%default:IPv4, [200/2219], 00:35:51, bgp-100, internal, tag 200  (mpls)

        IPv6 Routing Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        615:11:11:1::/64, ubest/mbest: 1/0
            *via ::ffff:1.1.1.1%default:IPv4, [200/2219], 00:35:51, bgp-100, internal, tag 200  (mpls-vpn)
        '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        bgp_obj = ShowRoutingIpv6VrfAll(device=self.device)
        parsed_output = bgp_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_obj = ShowRoutingIpv6VrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_obj.parse()


# ============================================
# unit test for 'show ip route'
# =============================================
class test_show_ip_route(unittest.TestCase):
    """
       unit test for show ip route
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_1 = {'execute.return_value': '''
    R3_nxosv# show ip route vrf all
    IP Route Table for VRF "default"
    '*' denotes best ucast next-hop
    '**' denotes best mcast next-hop
    '[x/y]' denotes [preference/metric]
    '%<string>' in via output denotes VRF <string>

    1.1.1.1/32, ubest/mbest: 2/0
        *via 10.1.3.1, Eth1/2, [1/0], 01:01:30, static
        *via 20.1.3.1, Eth1/3, [1/0], 01:01:30, static
    2.2.2.2/32, ubest/mbest: 2/0
        *via 10.2.3.2, Eth1/4, [1/0], 01:01:30, static
        *via 20.2.3.2, Eth1/1, [1/0], 01:01:29, static
    3.3.3.3/32, ubest/mbest: 2/0, attached
        *via 3.3.3.3, Lo0, [0/0], 01:01:31, local
        *via 3.3.3.3, Lo0, [0/0], 01:01:31, direct
    10.1.2.0/24, ubest/mbest: 4/0
        *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra
        *via 10.2.3.2, Eth1/4, [110/41], 01:01:18, ospf-1, intra
        *via 20.1.3.1, Eth1/3, [110/41], 01:01:18, ospf-1, intra
        *via 20.2.3.2, Eth1/1, [110/41], 01:01:18, ospf-1, intra
    33.33.33.33/32, ubest/mbest: 2/0, attached
        *via 33.33.33.33, Lo3, [0/0], 01:01:30, local
        *via 33.33.33.33, Lo3, [0/0], 01:01:30, direct

    IP Route Table for VRF "VRF1"
    '*' denotes best ucast next-hop
    '**' denotes best mcast next-hop
    '[x/y]' denotes [preference/metric]
    '%<string>' in via output denotes VRF <string>

    1.1.1.1/32, ubest/mbest: 2/0, attached
        *via 1.1.1.1, Lo4, [0/0], 00:00:10, local
        *via 1.1.1.1, Lo4, [0/0], 00:00:10, direct
    '''
}
    golden_parsed_output_1 = {
        'vrf':{
            'default':{
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'active': True,
                                'ubest':2,
                                'mbest':0,
                                'route_preference': 1,
                                'metric': 0,
                                'source_protocol':'static',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.1.3.1',
                                            'outgoing_interface': 'Ethernet1/2',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:01:30',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '20.1.3.1',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/3',
                                            'updated': '01:01:30',
                                        },
                                    },
                                },
                            },
                            '2.2.2.2/32': {
                                'route': '2.2.2.2/32',
                                'active': True,
                                'ubest': 2,
                                'mbest': 0,
                                'route_preference': 1,
                                'metric': 0,
                                'source_protocol': 'static',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.2.3.2',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/4',
                                            'updated': '01:01:30',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '20.2.3.2',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/1',
                                            'updated': '01:01:29',
                                        },
                                    },
                                },
                            },
                            '3.3.3.3/32': {
                                'route': '3.3.3.3/32',
                                'active': True,
                                'attached': True,
                                'ubest': 2,
                                'mbest': 0,
                                'route_preference': 0,
                                'source_protocol': 'local',
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '3.3.3.3',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Loopback0',
                                            'updated': '01:01:31',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '3.3.3.3',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Loopback0',
                                            'updated': '01:01:31',
                                        },
                                    },
                                },
                            },
                            '10.1.2.0/24': {
                                'route': '10.1.2.0/24',
                                'active': True,
                                'ubest': 4,
                                'mbest': 0,
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'process_id': 1,
                                'source_protocol_status': 'intra',
                                'metric': 41,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '10.1.3.1',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/2',
                                            'updated': '01:01:18',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '10.2.3.2',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/4',
                                            'updated': '01:01:18',
                                        },
                                        3: {
                                            'index': 3,
                                            'next_hop': '20.1.3.1',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/3',
                                            'updated': '01:01:18',
                                        },
                                        4: {
                                            'index': 4,
                                            'next_hop': '20.2.3.2',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/1',
                                            'updated': '01:01:18',
                                        },

                                    },
                                },
                            },
                            '33.33.33.33/32': {
                                'route': '33.33.33.33/32',
                                'active': True,
                                'attached': True,
                                'ubest': 2,
                                'mbest': 0,
                                'route_preference': 0,
                                'source_protocol': 'local',
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '33.33.33.33',
                                            'outgoing_interface': 'Loopback3',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:01:30',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '33.33.33.33',
                                            'outgoing_interface': 'Loopback3',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:01:30',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '1.1.1.1/32': {
                                'route': '1.1.1.1/32',
                                'attached': True,
                                'active': True,
                                'ubest': 2,
                                'mbest': 0,
                                'route_preference': 0,
                                'metric': 0,
                                'source_protocol': 'local',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '1.1.1.1',
                                            'outgoing_interface': 'Loopback4',
                                            'best_ucast_nexthop': True,
                                            'updated': '00:00:10',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '1.1.1.1',
                                            'outgoing_interface': 'Loopback4',
                                            'best_ucast_nexthop': True,
                                            'updated': '00:00:10',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRoute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(vrf="all")
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

# ============================================
# unit test for 'show ipv6 route'
# =============================================
class test_show_ipv6_route(unittest.TestCase):
    """
       unit test for show ipv6 route
    """
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_1 = {'execute.return_value': '''
    R3_nxosv# show ipv6 route vrf all
    IPv6 Routing Table for VRF "default"
    '*' denotes best ucast next-hop
    '**' denotes best mcast next-hop
    '[x/y]' denotes [preference/metric]

    2001:1:1:1::1/128, ubest/mbest: 2/0
        *via 2001:10:1:3::1, Eth1/2, [1/0], 01:02:00, static
        *via 2001:20:1:3::1, Eth1/3, [1/0], 01:02:00, static
    2001:10:1:2::/64, ubest/mbest: 4/0
        *via fe80::5054:ff:fe64:bd2e, Eth1/3, [110/41], 01:01:10, ospfv3-1, intra
        *via fe80::5054:ff:fea5:6e95, Eth1/2, [110/41], 01:01:10, ospfv3-1, intra
        *via fe80::5054:ff:fea7:1341, Eth1/4, [110/41], 01:01:10, ospfv3-1, intra
        *via fe80::5054:ff:feb3:b312, Eth1/1, [110/41], 01:01:10, ospfv3-1, intra

    2001:31:31:31::31/128, ubest/mbest: 1/0
        *via ::ffff:11.11.11.11%default:IPv4, [200/0], 01:01:43, bgp-100, internal,
    tag 100
    2001:32:32:32::32/128, ubest/mbest: 2/0
        *via fe80::5054:ff:fea7:1341, Eth1/4, [200/0], 01:01:24, bgp-100, internal,
    tag 100
        *via fe80::5054:ff:feb3:b312, Eth1/1, [200/0], 01:01:24, bgp-100, internal,
    tag 100
    2001:33:33:33::33/128, ubest/mbest: 2/0, attached
        *via 2001:33:33:33::33, Lo3, [0/0], 01:02:01, direct,
        *via 2001:33:33:33::33, Lo3, [0/0], 01:02:01, local

    IPv6 Routing Table for VRF "VRF1"
    '*' denotes best ucast next-hop
    '**' denotes best mcast next-hop
    '[x/y]' denotes [preference/metric]

    2001:1:1:1::1/128, ubest/mbest: 2/0, attached
        *via 2001:1:1:1::1, Lo4, [0/0], 00:00:35, direct,
        *via 2001:1:1:1::1, Lo4, [0/0], 00:00:35, local

    IPv6 Routing Table for VRF "management"
    '*' denotes best ucast next-hop
    '**' denotes best mcast next-hop
    '[x/y]' denotes [preference/metric]

    '''
}
    golden_parsed_output_1 = {
        'vrf':{
            'default':{
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'active': True,
                                'ubest':2,
                                'mbest':0,
                                'route_preference': 1,
                                'metric': 0,
                                'source_protocol':'static',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '2001:10:1:3::1',
                                            'outgoing_interface': 'Ethernet1/2',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:02:00',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '2001:20:1:3::1',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/3',
                                            'updated': '01:02:00',
                                        },
                                    },
                                },
                            },
                            '2001:10:1:2::/64': {
                                'route': '2001:10:1:2::/64',
                                'active': True,
                                'ubest': 4,
                                'mbest': 0,
                                'route_preference': 110,
                                'metric': 41,
                                'source_protocol': 'ospfv3',
                                'process_id': 1,
                                'source_protocol_status': 'intra',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fe64:bd2e',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/3',
                                            'updated': '01:01:10',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': 'fe80::5054:ff:fea5:6e95',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/2',
                                            'updated': '01:01:10',
                                        },
                                        3: {
                                            'index': 3,
                                            'next_hop': 'fe80::5054:ff:fea7:1341',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/4',
                                            'updated': '01:01:10',
                                        },
                                        4: {
                                            'index': 4,
                                            'next_hop': 'fe80::5054:ff:feb3:b312',
                                            'best_ucast_nexthop': True,
                                            'outgoing_interface': 'Ethernet1/1',
                                            'updated': '01:01:10',
                                        },
                                    },
                                },
                            },
                            '2001:31:31:31::31/128': {
                                'route': '2001:31:31:31::31/128',
                                'active': True,
                                'ubest': 1,
                                'mbest': 0,
                                'route_preference': 200,
                                'source_protocol': 'bgp',
                                'source_protocol_status': 'internal',
                                'process_id': 100,
                                'tag': 100,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '::ffff:11.11.11.11',
                                            'next_hop_vrf': 'default',
                                            'next_hop_af': 'ipv4',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:01:43',
                                        },

                                    },
                                },
                            },
                            '2001:32:32:32::32/128': {
                                'route': '2001:32:32:32::32/128',
                                'active': True,
                                'ubest': 2,
                                'mbest': 0,
                                'route_preference': 200,
                                'source_protocol': 'bgp',
                                'source_protocol_status': 'internal',
                                'process_id': 100,
                                'tag': 100,
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': 'fe80::5054:ff:fea7:1341',
                                            'outgoing_interface': 'Ethernet1/4',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:01:24',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': 'fe80::5054:ff:feb3:b312',
                                            'outgoing_interface': 'Ethernet1/1',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:01:24',
                                        },
                                    },
                                },
                            },
                            '2001:33:33:33::33/128': {
                                'route': '2001:33:33:33::33/128',
                                'active': True,
                                'attached': True,
                                'ubest': 2,
                                'mbest': 0,
                                'route_preference': 0,
                                'source_protocol': 'local',
                                'metric': 0,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '2001:33:33:33::33',
                                            'outgoing_interface': 'Loopback3',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:02:01',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '2001:33:33:33::33',
                                            'outgoing_interface': 'Loopback3',
                                            'best_ucast_nexthop': True,
                                            'updated': '01:02:01',
                                        },
                                    },
                                },
                            },

                        },
                    },
                },
            },
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'attached': True,
                                'active': True,
                                'ubest': 2,
                                'mbest': 0,
                                'route_preference': 0,
                                'metric': 0,
                                'source_protocol': 'local',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '2001:1:1:1::1',
                                            'outgoing_interface': 'Loopback4',
                                            'best_ucast_nexthop': True,
                                            'updated': '00:00:35',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '2001:1:1:1::1',
                                            'outgoing_interface': 'Loopback4',
                                            'best_ucast_nexthop': True,
                                            'updated': '00:00:35',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


    golden_output_3 = {'execute.return_value': '''
        R3_nxosv# show ipv6 route vrf VRF3
        No IP Route Table for VRF "VRF3"
    '''}


    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6Route(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_route_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpv6Route(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='VRF3')

    def test_show_ipv6_route_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpv6Route(device=self.device)
        parsed_output = obj.parse(vrf="all")
        self.assertEqual(parsed_output,self.golden_parsed_output_1)



if __name__ == '__main__':
    unittest.main()
