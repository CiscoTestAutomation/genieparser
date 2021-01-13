# Python
import unittest
from unittest.mock import Mock
# Ats
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# nxos show_routing
from genie.libs.parser.nxos.show_routing import ShowRoutingVrfAll, ShowRoutingIpv6VrfAll,\
                                     ShowIpRoute, ShowIpv6Route, ShowRouting, ShowIpRouteSummary

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
                            {'10.121.0.0/8':
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
                            '10.205.0.1/32':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'attach': 'attached',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'10.205.0.1':
                                                {'protocol':
                                                    {'local':
                                                        {'uptime': '2w6d',
                                                        'interface': 'Bdi1255',
                                                        'preference': '0',
                                                        'metric': '0'}}}}}}},
                            '10.189.1.0/24':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'10.55.130.3':
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
                            '10.21.33.33/32':
                                {'ubest_num': '1',
                                'mbest_num': '1',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'10.36.3.3':
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
                                            {'10.36.3.3':
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
                            "10.16.2.2/32": {
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
                            "10.4.1.1/32": {
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
                            '10.229.11.11/32':
                                {'ubest_num': '2',
                                'mbest_num': '0',
                                'attach': 'attached',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'10.229.11.11':
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
                            {'10.106.0.0/8':
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
                            '10.16.1.0/24':
                                {'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route':
                                    {'unicast':
                                        {'nexthop':
                                            {'2001:db8:8b05::1002':
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
                            '10.106.0.5/8':
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

        10.106.0.0/8, ubest/mbest: 1/0
            *via vrf default, Null0, [20/0], 18:11:28, bgp-333, external, tag 333
        10.16.1.0/24, ubest/mbest: 1/0
            *via 2001:db8:8b05::1002%default, Eth1/1, [200/4444], 15:57:39, bgp-333, internal, tag 333
        10.106.0.5/8, ubest/mbest: 1/0
            *via Null0, [1/0], 18:47:42, static


        IP Route Table for VRF "management"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        IP Route Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        10.121.0.0/8, ubest/mbest: 1/0
            *via Null0, [55/0], 5w0d, bgp-100, discard, tag 100
        10.205.0.1/32, ubest/mbest: 1/0 time, attached
            *via 10.205.0.1, Bdi1255, [0/0], 2w6d, local
        10.21.33.33/32, ubest/mbest: 1/1
            *via 10.36.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
            **via 10.36.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
        10.189.1.0/24, ubest/mbest: 1/0 time
            *via 10.55.130.3%default, [33/0], 3d10h, bgp-1, internal, tag 1 (evpn), segid: 50051 tunnelid: 0x64008203 encap: VXLAN
        10.229.11.11/32, ubest/mbest: 2/0, attached
            *via 10.229.11.11, Lo1, [0/0], 5w4d, local
            *via 10.229.11.11, Lo1, [0/0], 5w4d, direct
        10.4.1.1/32, ubest/mbest: 2/0
            *via 10.2.4.2, Eth2/4, [110/81], 00:18:35, ospf-1, intra (mpls)
            *via 10.3.4.3, Eth2/1, [110/81], 00:18:35, ospf-1, intra (mpls)
        10.16.2.2/32, ubest/mbest: 1/0
            *via 10.2.4.2, Eth2/4, [110/41], 00:18:35, ospf-1, intra (mpls)
    '''}

    golden_parsed_output_custom={
        'vrf':
            {'VRF1':
                 {'address_family':
                      {'vpnv4 unicast':
                           {'bgp_distance_internal_as': 33,
                            'bgp_distance_local': 55,
                            'ip':
                                {'10.121.0.0/8':
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
                                                                    'attribute':
                                                                        'discard',
                                                                    'tag': '100'}}}}}}},
                                 '10.205.0.1/32':
                                     {'ubest_num': '1',
                                      'mbest_num': '0',
                                      'attach': 'attached',
                                      'best_route':
                                          {'unicast':
                                               {'nexthop':
                                                    {'10.205.0.1':
                                                         {'protocol':
                                                              {'local':
                                                                   {'uptime': '2w6d',
                                                                    'interface':
                                                                        'Bdi1255',
                                                                    'preference': '0',
                                                                    'metric': '0'}}}}}}},
                                 '10.189.1.0/24':
                                     {'ubest_num': '1',
                                      'mbest_num': '0',
                                      'best_route':
                                          {'unicast':
                                               {'nexthop':
                                                    {'10.55.130.3':
                                                         {'protocol':
                                                              {'bgp':
                                                                   {'uptime': '3d10h',
                                                                    'preference': '33',
                                                                    'metric': '0',
                                                                    'protocol_id': '1',
                                                                    'attribute':
                                                                        'internal',
                                                                    'tag': '1',
                                                                    'evpn': True,
                                                                    'segid': 50051,
                                                                    'route_table':
                                                                        'default',
                                                                    'tunnelid':
                                                                        '0x64008203',
                                                                    'encap':
                                                                        'vxlan'}}}}}}},
                                 '10.21.33.33/32':
                                     {'ubest_num': '1',
                                      'mbest_num': '1',
                                      'best_route':
                                          {'unicast':
                                               {'nexthop':
                                                    {'10.36.3.3':
                                                         {'protocol':
                                                              {'bgp':
                                                                   {'uptime': '5w0d',
                                                                    'preference': '33',
                                                                    'metric': '0',
                                                                    'protocol_id': '100',
                                                                    'attribute':
                                                                        'internal',
                                                                    'route_table':
                                                                        'default',
                                                                    'mpls_vpn': True,
                                                                    'tag': '100'}}}}},
                                           'multicast':
                                               {'nexthop':
                                                    {'10.36.3.3':
                                                         {'protocol':
                                                              {'bgp':
                                                                   {'uptime': '5w0d',
                                                                    'preference': '33',
                                                                    'metric': '0',
                                                                    'protocol_id': '100',
                                                                    'attribute':
                                                                        'internal',
                                                                    'route_table':
                                                                        'default',
                                                                    'mpls_vpn': True,
                                                                    'tag': '100'}}}}}}},
                                 "10.16.2.2/32": {
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
                                                             "interface":
                                                                 "Ethernet2/4"}}}}}}},
                                 "10.4.1.1/32": {
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
                                                             "interface":
                                                                 "Ethernet2/4"}}},
                                                 "10.3.4.3": {
                                                     "protocol": {
                                                         "ospf": {
                                                             "preference": "110",
                                                             "protocol_id": "1",
                                                             "uptime": "00:18:35",
                                                             "metric": "81",
                                                             "mpls": True,
                                                             "attribute": "intra",
                                                             "interface":
                                                                 "Ethernet2/1"}}}}}}},
                                 '10.229.11.11/32':
                                     {'ubest_num': '2',
                                      'mbest_num': '0',
                                      'attach': 'attached',
                                      'best_route':
                                          {'unicast':
                                               {'nexthop':
                                                    {'10.229.11.11':
                                                         {'protocol':
                                                              {'local':
                                                                   {'uptime': '5w4d',
                                                                    'preference': '0',
                                                                    'metric': '0',
                                                                    'interface':
                                                                        'Loopback1'},
                                                               'direct':
                                                                   {'uptime': '5w4d',
                                                                    'preference': '0',
                                                                    'metric': '0',
                                                                    'interface':
                                                                        'Loopback1'}}}}}}}}}}}}}
    golden_output_custom = {'execute.return_value': '''
        IP Route Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        10.121.0.0/8, ubest/mbest: 1/0
            *via Null0, [55/0], 5w0d, bgp-100, discard, tag 100
        10.205.0.1/32, ubest/mbest: 1/0 time, attached
            *via 10.205.0.1, Bdi1255, [0/0], 2w6d, local
        10.21.33.33/32, ubest/mbest: 1/1
            *via 10.36.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
            **via 10.36.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
        10.189.1.0/24, ubest/mbest: 1/0 time
            *via 10.55.130.3%default, [33/0], 3d10h, bgp-1, internal, tag 1 (evpn), segid: 50051 tunnelid: 0x64008203 encap: VXLAN
        10.229.11.11/32, ubest/mbest: 2/0, attached
            *via 10.229.11.11, Lo1, [0/0], 5w4d, local
            *via 10.229.11.11, Lo1, [0/0], 5w4d, direct
        10.4.1.1/32, ubest/mbest: 2/0
            *via 10.2.4.2, Eth2/4, [110/81], 00:18:35, ospf-1, intra (mpls)
            *via 10.3.4.3, Eth2/1, [110/81], 00:18:35, ospf-1, intra (mpls)
        10.16.2.2/32, ubest/mbest: 1/0
            *via 10.2.4.2, Eth2/4, [110/41], 00:18:35, ospf-1, intra (mpls)
           '''}

    golden_parsed_output1 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4 unicast': {
                        'ip': {
                            '10.36.3.3/32': {
                                'ubest_num': '2',
                                'mbest_num': '0',
                                'attach': 'attached',
                                'best_route': {
                                    'unicast': {
                                        'nexthop': {
                                            '10.36.3.3': {
                                                'protocol': {
                                                    'local': {
                                                        'interface': 'Loopback0',
                                                        'preference': '0',
                                                        'metric': '0',
                                                        'uptime': '1w4d',
                                                    },
                                                    'direct': {
                                                        'interface': 'Loopback0',
                                                        'preference': '0',
                                                        'metric': '0',
                                                        'uptime': '1w4d',
                                                    },
                                                },
                                            },
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
    golden_output1 = {'execute.return_value': '''
        show routing 10.36.3.3
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.36.3.3/32, ubest/mbest: 2/0, attached
            *via 10.36.3.3, Lo0, [0/0], 1w4d, local
            *via 10.36.3.3, Lo0, [0/0], 1w4d, direct
    '''}

    golden_parsed_output2 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4 unicast': {
                        'ip': {
                            '10.4.1.1/32': {
                                'ubest_num': '1',
                                'mbest_num': '0',
                                'best_route': {
                                    'unicast': {
                                        'nexthop': {
                                            '10.13.90.1': {
                                                'protocol': {
                                                    'eigrp': {
                                                        'interface': 'Ethernet1/2.90',
                                                        'preference': '90',
                                                        'metric': '2848',
                                                        'uptime': '1w5d',
                                                        'protocol_id': 'test',
                                                        'attribute': 'internal',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'routes': {
                                    'nexthop': {
                                        '10.4.1.1': {
                                            'protocol': {
                                                'bgp': {
                                                    'preference': '200',
                                                    'metric': '0',
                                                    'uptime': '1w5d',
                                                    'protocol_id': '65000',
                                                    'attribute': 'internal',
                                                    'tag': '65000',
                                                },
                                            },
                                        },
                                        '10.13.110.1': {
                                            'protocol': {
                                                'ospf': {
                                                    'interface': 'Ethernet1/2.110',
                                                    'preference': '110',
                                                    'metric': '41',
                                                    'uptime': '1w5d',
                                                    'protocol_id': '1',
                                                    'attribute': 'intra',
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'bgp_distance_internal_as': 200,
                    },
                },
            },
        },
    }
    golden_output2 = {'execute.return_value': '''
        show routing 10.4.1.1
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.4.1.1/32, ubest/mbest: 1/0
            *via 10.13.90.1, Eth1/2.90, [90/2848], 1w5d, eigrp-test, internal
            via 10.4.1.1, [200/0], 1w5d, bgp-65000, internal, tag 65000 (hidden)
            via 10.13.110.1, Eth1/2.110, [110/41], 1w5d, ospf-1, intra
    '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        bgp_obj = ShowRoutingVrfAll(device=self.device)
        parsed_output = bgp_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_custom(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_custom)
        bgp_obj = ShowRoutingVrfAll(device=self.device)
        parsed_output = bgp_obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_custom)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_obj = ShowRoutingVrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        bgp_obj = ShowRoutingVrfAll(device=self.device)
        parsed_output = bgp_obj.parse(ip='10.36.3.3')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        bgp_obj = ShowRoutingVrfAll(device=self.device)
        parsed_output = bgp_obj.parse(ip='10.4.1.1')
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ===========================================
#  Unit test for 'show routing ipv6  vrf all'
# ===========================================
class test_show_routing_ipv6_vrf_all(unittest.TestCase):

    '''Unit test for show routing ipv6  vrf all'''

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
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
                              "2001:db8:cdc9:121::/64": {
                                   "mbest_num": "0",
                                   "ubest_num": "1",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "::ffff:10.4.1.1": {
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
                              "2001:db8:cdc9:144::/64": {
                                   "mbest_num": "0",
                                   "ubest_num": "1",
                                   "best_route": {
                                        "unicast": {
                                             "nexthop": {
                                                  "::ffff:10.4.1.1": {
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

    golden_output_1 = {'execute.return_value': '''
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
        2001:db8:cdc9:121::/64, ubest/mbest: 1/0
            *via ::ffff:10.4.1.1%default:IPv4, [200/2219], 00:35:51, bgp-100, internal, tag 200  (mpls)

        IPv6 Routing Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        2001:db8:cdc9:144::/64, ubest/mbest: 1/0
            *via ::ffff:10.4.1.1%default:IPv4, [200/2219], 00:35:51, bgp-100, internal, tag 200  (mpls-vpn)
        '''}
    golden_output_custom ={
        'execute.return_value': '''
        IPv6 Routing Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        2001:db8:cdc9:144::/64, ubest/mbest: 1/0
            *via ::ffff:10.4.1.1%default:IPv4, [200/2219], 00:35:51, bgp-100, internal, tag 200  (mpls-vpn)
            '''}

    golden_parsed_output_custom = {'vrf':{
        "VRF1": {
            "address_family": {
                "vpnv6 unicast": {
                    "bgp_distance_internal_as": 200,
                    "ip": {
                        "2001:db8:cdc9:144::/64": {
                            "mbest_num": "0",
                            "ubest_num": "1",
                            "best_route": {
                                "unicast": {
                                    "nexthop": {
                                        "::ffff:10.4.1.1": {
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
    golden_parsed_output_2 = {
        'vrf': {
            'otv-vrf139': {
                'address_family': {
                    'vpnv6 unicast': {
                        'ip': {
                            '2001:112:1:2b3::/64': {
                                'attach': 'attached',
                                'best_route': {
                                    'unicast': {
                                        'nexthop': {
                                            '2001:112:1:2b3::2': {
                                                'protocol': {
                                                    'direct': {
                                                        'interface': 'Vlan1191',
                                                        'metric': '0',
                                                        'preference': '0',
                                                        'uptime': '20:58:10'}}}}}},
                                'mbest_num': '0',
                                'ubest_num': '1'},
                            '2001:112:1:2b3::1/128': {
                                'attach': 'attached',
                                'best_route': {
                                    'unicast': {
                                        'nexthop': {
                                            '2001:112:1:2b3::1': {
                                                'protocol': {
                                                    'hsrp': {
                                                        'interface': 'Vlan1191',
                                                         'metric': '0',
                                                         'preference': '0',
                                                         'uptime': '20:57:53'}}}}}},
                                'mbest_num': '0',
                                'ubest_num': '1'},
                            '2001:112:1:2b3::2/128': {
                                'attach': 'attached',
                                'best_route': {
                                    'unicast': {
                                        'nexthop': {
                                            '2001:112:1:2b3::2': {
                                                'protocol': {
                                                    'local': {
                                                    'interface': 'Vlan1191',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                                'mbest_num': '0',
                                'ubest_num': '1'},
                        '2001:112:1:2b4::/64': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b4::2': {
                                            'protocol': {
                                                'direct': {
                                                    'interface': 'Vlan1192',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b4::1/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b4::1': {
                                            'protocol': {
                                                'hsrp': {
                                                    'interface': 'Vlan1192',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:57:53'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b4::2/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b4::2': {
                                            'protocol': {
                                                'local': {
                                                    'interface': 'Vlan1192',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b5::/64': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                    '2001:112:1:2b5::2': {
                                        'protocol': {
                                            'direct': {
                                                'interface': 'Vlan1193',
                                                'metric': '0',
                                                'preference': '0',
                                                'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b5::1/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b5::1': {
                                            'protocol': {
                                                'hsrp': {
                                                    'interface': 'Vlan1193',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:57:52'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b5::2/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b5::2': {
                                            'protocol': {
                                                'local': {
                                                    'interface': 'Vlan1193',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b6::/64': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b6::2': {
                                            'protocol': {
                                                'direct': {
                                                    'interface': 'Vlan1194',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b6::1/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b6::1': {
                                            'protocol': {
                                                'hsrp': {
                                                    'interface': 'Vlan1194',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:57:52'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b6::2/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b6::2': {
                                            'protocol': {
                                                'local': {
                                                    'interface': 'Vlan1194',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b7::/64': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b7::2': {
                                            'protocol': {
                                                'direct': {
                                                    'interface': 'Vlan1195',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b7::1/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b7::1': {
                                            'protocol': {
                                                'hsrp': {
                                                    'interface': 'Vlan1195',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:57:52'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'},
                        '2001:112:1:2b7::2/128': {
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '2001:112:1:2b7::2': {
                                            'protocol': {
                                                'local': {
                                                    'interface': 'Vlan1195',
                                                    'metric': '0',
                                                    'preference': '0',
                                                    'uptime': '20:58:10'}}}}}},
                            'mbest_num': '0',
                            'ubest_num': '1'}}}}}}}

    golden_output_2 = {'execute.return_value': '''
        IPv6 Routing Table for VRF "otv-vrf139"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        2001:112:1:2b3::/64, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b3::2, Vlan1191, [0/0], 20:58:10, direct, 
        2001:112:1:2b3::1/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b3::1, Vlan1191, [0/0], 20:57:53, hsrp
        2001:112:1:2b3::2/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b3::2, Vlan1191, [0/0], 20:58:10, local
        2001:112:1:2b4::/64, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b4::2, Vlan1192, [0/0], 20:58:10, direct, 
        2001:112:1:2b4::1/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b4::1, Vlan1192, [0/0], 20:57:53, hsrp
        2001:112:1:2b4::2/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b4::2, Vlan1192, [0/0], 20:58:10, local
        2001:112:1:2b5::/64, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b5::2, Vlan1193, [0/0], 20:58:10, direct, 
        2001:112:1:2b5::1/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b5::1, Vlan1193, [0/0], 20:57:52, hsrp
        2001:112:1:2b5::2/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b5::2, Vlan1193, [0/0], 20:58:10, local
        2001:112:1:2b6::/64, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b6::2, Vlan1194, [0/0], 20:58:10, direct, 
        2001:112:1:2b6::1/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b6::1, Vlan1194, [0/0], 20:57:52, hsrp
        2001:112:1:2b6::2/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b6::2, Vlan1194, [0/0], 20:58:10, local
        2001:112:1:2b7::/64, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b7::2, Vlan1195, [0/0], 20:58:10, direct, 
        2001:112:1:2b7::1/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b7::1, Vlan1195, [0/0], 20:57:52, hsrp
        2001:112:1:2b7::2/128, ubest/mbest: 1/0, attached
            *via 2001:112:1:2b7::2, Vlan1195, [0/0], 20:58:10, local
    '''}


    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowRoutingIpv6VrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_custom(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_custom)
        obj = ShowRoutingIpv6VrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_custom)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowRoutingIpv6VrfAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowRoutingIpv6VrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ===========================================
#  Unit test for 'show routing'
# ===========================================
class test_show_routing(unittest.TestCase):
    '''Unit test for show routing'''

    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.106.0.0/8': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': 'vrf default',
                                        'outgoing_interface': 'Null0',
                                        'route_preference': 20,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'external',
                                        'updated': '18:11:28',
                                    },
                                },
                            },
                            'process_id': '333',
                            'route': '10.106.0.0/8',
                            'route_preference': 20,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'external',
                            'tag': 333,
                            'ubest': 1,
                        },
                        '10.106.0.5/8': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': 'Null0',
                                        'route_preference': 1,
                                        'source_protocol': 'static',
                                        'updated': '18:47:42',
                                    },
                                },
                            },
                            'route': '10.106.0.5/8',
                            'route_preference': 1,
                            'source_protocol': 'static',
                            'ubest': 1,
                        },
                        '10.16.1.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 4444,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 4444,
                                        'next_hop': '2001:db8:8b05::1002',
                                        'next_hop_vrf': 'default',
                                        'outgoing_interface': 'Ethernet1/1',
                                        'route_preference': 200,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '15:57:39',
                                    },
                                },
                            },
                            'process_id': '333',
                            'route': '10.16.1.0/24',
                            'route_preference': 200,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'internal',
                            'tag': 333,
                            'ubest': 1,
                        },
                    },
                },
            },
        },
    },
}

    golden_output = {'execute.return_value': '''
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        10.106.0.0/8, ubest/mbest: 1/0
            *via vrf default, Null0, [20/0], 18:11:28, bgp-333, external, tag 333
        10.16.1.0/24, ubest/mbest: 1/0
            *via 2001:db8:8b05::1002%default, Eth1/1, [200/4444], 15:57:39, bgp-333, internal, tag 333
        10.106.0.5/8, ubest/mbest: 1/0
            *via Null0, [1/0], 18:47:42, static

        '''
                     }

    golden_output_2 = {'execute.return_value': '''
    '*' denotes best ucast next-hop
    '**' denotes best mcast next-hop
    '[x/y]' denotes [preference/metric]
    '%' in via output denotes VRF

    show ip route static
    10.111.1.1/32, ubest/mbest: 1/0
    *via 10.144.10.2, [1/0], 13:35:01, static
    via 10.1.10.2, [4/0], 13:35:01, static
    '''}

    golden_parsed_output_2 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.111.1.1/32': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.144.10.2',
                                        'route_preference': 1,
                                        'source_protocol': 'static',
                                        'updated': '13:35:01',
                                    },
                                    2: {
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '10.1.10.2',
                                        'route_preference': 4,
                                        'source_protocol': 'static',
                                        'updated': '13:35:01',
                                    },
                                },
                            },
                            'route': '10.111.1.1/32',
                            'route_preference': 1,
                            'source_protocol': 'static',
                            'ubest': 1,
                        },
                    },
                },
            },
        },
    },
}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_obj = ShowRouting(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        bgp_obj = ShowRouting(device=self.device)
        parsed_output = bgp_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        bgp_obj = ShowRouting(device=self.device)
        parsed_output = bgp_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# ============================================
# Unit tests for:
#   show ip route
#   show ip route vrf {vrf}
#   show ip route vrf all
# =============================================
class test_show_ip_route(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': ''' \
        R2# show ip route
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.16.2.2/32, ubest/mbest: 2/0, attached
            *via 10.16.2.2, Lo1, [0/0], 00:41:07, local
            *via 10.16.2.2, Lo1, [0/0], 00:41:07, direct
        10.144.6.6/32, ubest/mbest: 2/0
            *via 10.2.4.4, Eth1/1, [110/81], 00:20:04, ospf-10, intra
            *via 10.2.5.5, Eth1/2, [110/81], 00:20:04, ospf-10, intra
        10.2.5.0/24, ubest/mbest: 1/0, attached
            *via 10.2.5.2, Eth1/2, [0/0], 00:45:10, direct
        10.2.5.2/32, ubest/mbest: 1/0, attached
            *via 10.2.5.2, Eth1/2, [0/0], 00:45:10, local
        10.166.7.0/24, ubest/mbest: 2/0
            *via 10.2.4.4, Eth1/1, [110/20], 00:20:04, ospf-10, type-2
            *via 10.2.5.5, Eth1/2, [110/20], 00:20:04, ospf-10, type-2
        10.76.23.23/32, ubest/mbest: 2/0, attached
            *via 10.76.23.23, Lo1, [0/0], 00:41:07, local
            *via 10.76.23.23, Lo1, [0/0], 00:41:07, direct
    '''}

    golden_parsed_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.144.6.6/32': {
                            'active': True,
                            'mbest': 0,
                            'metric': 81,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 81,
                                        'next_hop': '10.2.4.4',
                                        'outgoing_interface': 'Ethernet1/1',
                                        'route_preference': 110,
                                        'source_protocol': 'ospf',
                                        'source_protocol_status': 'intra',
                                        'updated': '00:20:04',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 81,
                                        'next_hop': '10.2.5.5',
                                        'outgoing_interface': 'Ethernet1/2',
                                        'route_preference': 110,
                                        'source_protocol': 'ospf',
                                        'source_protocol_status': 'intra',
                                        'updated': '00:20:04',
                                    },
                                },
                            },
                            'process_id': '10',
                            'route': '10.144.6.6/32',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_status': 'intra',
                            'ubest': 2,
                        },
                        '10.16.2.2/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'route_preference': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'route_preference': 0,
                                        'next_hop': '10.16.2.2',
                                        'outgoing_interface': 'Loopback1',
                                        'source_protocol': 'local',
                                        'updated': '00:41:07',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'route_preference': 0,
                                        'next_hop': '10.16.2.2',
                                        'outgoing_interface': 'Loopback1',
                                        'source_protocol': 'direct',
                                        'updated': '00:41:07',
                                    },
                                },
                            },
                            'route': '10.16.2.2/32',
                            'source_protocol': 'direct',
                            'ubest': 2,
                        },
                        '10.166.7.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 20,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 20,
                                        'next_hop': '10.2.4.4',
                                        'outgoing_interface': 'Ethernet1/1',
                                        'route_preference': 110,
                                        'source_protocol': 'ospf',
                                        'source_protocol_status': 'type-2',
                                        'updated': '00:20:04',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 20,
                                        'next_hop': '10.2.5.5',
                                        'outgoing_interface': 'Ethernet1/2',
                                        'route_preference': 110,
                                        'source_protocol': 'ospf',
                                        'source_protocol_status': 'type-2',
                                        'updated': '00:20:04',
                                    },
                                },
                            },
                            'process_id': '10',
                            'route': '10.166.7.0/24',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_status': 'type-2',
                            'ubest': 2,
                        },
                        '10.2.5.0/24': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'route_preference': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'route_preference': 0,
                                        'next_hop': '10.2.5.2',
                                        'outgoing_interface': 'Ethernet1/2',
                                        'source_protocol': 'direct',
                                        'updated': '00:45:10',
                                    },
                                },
                            },
                            'route': '10.2.5.0/24',
                            'source_protocol': 'direct',
                            'ubest': 1,
                        },
                        '10.2.5.2/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'route_preference': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'route_preference': 0,
                                        'next_hop': '10.2.5.2',
                                        'outgoing_interface': 'Ethernet1/2',
                                        'source_protocol': 'local',
                                        'updated': '00:45:10',
                                    },
                                },
                            },
                            'route': '10.2.5.2/32',
                            'source_protocol': 'local',
                            'ubest': 1,
                        },
                        '10.76.23.23/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'route_preference': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'route_preference': 0,
                                        'next_hop': '10.76.23.23',
                                        'outgoing_interface': 'Loopback1',
                                        'source_protocol': 'local',
                                        'updated': '00:41:07',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'route_preference': 0,
                                        'next_hop': '10.76.23.23',
                                        'outgoing_interface': 'Loopback1',
                                        'source_protocol': 'direct',
                                        'updated': '00:41:07',
                                    },
                                },
                            },
                            'route': '10.76.23.23/32',
                            'source_protocol': 'direct',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
    },
}

    golden_output_2 = {'execute.return_value': ''' \
        R2# show ip route vrf vni_10100
        IP Route Table for VRF "vni_10100"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.111.0.0/16, ubest/mbest: 1/0, attached
            *via 10.111.0.1, Vlan101, [0/0], 00:46:14, direct
        10.111.0.1/32, ubest/mbest: 1/0, attached
            *via 10.111.0.1, Vlan101, [0/0], 00:46:14, local
        10.111.1.3/32, ubest/mbest: 1/0, attached
            *via 10.111.1.3, Vlan101, [190/0], 00:35:43, hmm
        10.111.3.4/32, ubest/mbest: 1/0, attached
            *via 10.111.3.4, Vlan101, [190/0], 00:26:50, hmm
        10.111.8.3/32, ubest/mbest: 1/0
            *via 10.84.66.66%default, [200/2000], 00:20:43, bgp-100, internal, tag 200 (
        evpn) segid: 10100 tunnelid: 0x42424242 encap: VXLAN
        
        10.111.8.4/32, ubest/mbest: 1/0
            *via 10.84.66.66%default, [200/2000], 00:20:43, bgp-100, internal, tag 200 (
        evpn) segid: 10100 tunnelid: 0x42424242 encap: VXLAN
        
        10.4.0.0/16, ubest/mbest: 1/0, attached
            *via 10.4.0.1, Vlan102, [0/0], 00:46:13, direct
        10.4.0.1/32, ubest/mbest: 1/0, attached
            *via 10.4.0.1, Vlan102, [0/0], 00:46:13, local
    '''}

    golden_parsed_output_2 = {
    'vrf': {
        'vni_10100': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.111.0.0/16': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.111.0.1',
                                        'outgoing_interface': 'Vlan101',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '00:46:14',
                                    },
                                },
                            },
                            'route': '10.111.0.0/16',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 1,
                        },
                        '10.111.0.1/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.111.0.1',
                                        'outgoing_interface': 'Vlan101',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '00:46:14',
                                    },
                                },
                            },
                            'route': '10.111.0.1/32',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 1,
                        },
                        '10.111.1.3/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.111.1.3',
                                        'outgoing_interface': 'Vlan101',
                                        'route_preference': 190,
                                        'source_protocol': 'hmm',
                                        'updated': '00:35:43',
                                    },
                                },
                            },
                            'route': '10.111.1.3/32',
                            'route_preference': 190,
                            'source_protocol': 'hmm',
                            'ubest': 1,
                        },
                        '10.111.3.4/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.111.3.4',
                                        'outgoing_interface': 'Vlan101',
                                        'route_preference': 190,
                                        'source_protocol': 'hmm',
                                        'updated': '00:26:50',
                                    },
                                },
                            },
                            'route': '10.111.3.4/32',
                            'route_preference': 190,
                            'source_protocol': 'hmm',
                            'ubest': 1,
                        },
                        '10.111.8.3/32': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2000,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2000,
                                        'next_hop': '10.84.66.66',
                                        'next_hop_vrf': 'default',
                                        'route_preference': 200,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '00:20:43',
                                    },
                                },
                            },
                            'process_id': '100',
                            'route': '10.111.8.3/32',
                            'route_preference': 200,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'internal',
                            'tag': 200,
                            'ubest': 1,
                        },
                        '10.111.8.4/32': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2000,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2000,
                                        'next_hop': '10.84.66.66',
                                        'next_hop_vrf': 'default',
                                        'route_preference': 200,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '00:20:43',
                                    },
                                },
                            },
                            'process_id': '100',
                            'route': '10.111.8.4/32',
                            'route_preference': 200,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'internal',
                            'tag': 200,
                            'ubest': 1,
                        },
                        '10.4.0.0/16': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.4.0.1',
                                        'outgoing_interface': 'Vlan102',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '00:46:13',
                                    },
                                },
                            },
                            'route': '10.4.0.0/16',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 1,
                        },
                        '10.4.0.1/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.4.0.1',
                                        'outgoing_interface': 'Vlan102',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '00:46:13',
                                    },
                                },
                            },
                            'route': '10.4.0.1/32',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 1,
                        },
                    },
                },
            },
        },
    },
}

    golden_output_3 = {'execute.return_value': ''' \
        R3_nxosv# show ip route vrf all
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.4.1.1/32, ubest/mbest: 2/0
            *via 10.1.3.1, Eth1/2, [1/0], 01:01:30, static
            *via 10.186.3.1, Eth1/3, [1/0], 01:01:30, static
        10.36.3.3/32, ubest/mbest: 2/0, attached
            *via 10.36.3.3, Lo0, [0/0], 01:01:31, local
            *via 10.36.3.3, Lo0, [0/0], 01:01:31, direct
        10.1.2.0/24, ubest/mbest: 4/0
            *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra
        10.2.3.0/24, ubest/mbest: 1/0, attached
            *via 10.2.3.3, Eth1/4, [0/0], 01:01:33, direct
        10.2.3.3/32, ubest/mbest: 1/0, attached
            *via 10.2.3.3, Eth1/4, [0/0], 01:01:33, local
        10.166.13.13/32, ubest/mbest: 2/0, attached
            *via 10.166.13.13, Lo1, [0/0], 01:01:30, local
            *via 10.166.13.13, Lo1, [0/0], 01:01:30, direct
        10.186.2.0/24, ubest/mbest: 4/0
            *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra
            *via 10.229.3.2, Eth1/1, [110/41], 01:01:18, ospf-1, intra
        10.229.3.0/24, ubest/mbest: 1/0, attached
            *via 10.229.3.3, Eth1/1, [0/0], 01:01:35, direct
        10.229.3.3/32, ubest/mbest: 1/0, attached
            *via 10.229.3.3, Eth1/1, [0/0], 01:01:35, local
        10.234.21.21/32, ubest/mbest: 2/0
            *via 10.1.3.1, Eth1/2, [115/50], 01:01:22, isis-1, L1
            *via 10.186.3.1, Eth1/3, [115/50], 01:01:16, isis-1, L1
        10.19.31.31/32, ubest/mbest: 1/0
            *via 10.229.11.11, [200/0], 01:01:12, bgp-100, internal, tag 100
            *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra, tag 100,

        IP Route Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.4.1.1/32, ubest/mbest: 2/0, attached
            *via 10.4.1.1, Lo4, [0/0], 00:00:10, local
            *via 10.4.1.1, Lo4, [0/0], 00:00:10, direct
    '''}

    golden_parsed_output_3 = {
    'vrf': {
        'VRF1': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.4.1.1/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.4.1.1',
                                        'outgoing_interface': 'Loopback4',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '00:00:10',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '10.4.1.1',
                                        'outgoing_interface': 'Loopback4',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '00:00:10',
                                    },
                                },
                            },
                            'route': '10.4.1.1/32',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.1.2.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 41,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 41,
                                        'next_hop': '10.1.3.1',
                                        'outgoing_interface': 'Ethernet1/2',
                                        'route_preference': 110,
                                        'source_protocol': 'ospf',
                                        'source_protocol_status': 'intra',
                                        'updated': '01:01:18',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.1.2.0/24',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_status': 'intra',
                            'ubest': 4,
                        },
                        '10.166.13.13/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.166.13.13',
                                        'outgoing_interface': 'Loopback1',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '01:01:30',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '10.166.13.13',
                                        'outgoing_interface': 'Loopback1',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '01:01:30',
                                    },
                                },
                            },
                            'route': '10.166.13.13/32',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 2,
                        },
                        '10.186.2.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 41,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 41,
                                        'next_hop': '10.1.3.1',
                                        'outgoing_interface': 'Ethernet1/2',
                                        'route_preference': 110,
                                        'source_protocol': 'ospf',
                                        'source_protocol_status': 'intra',
                                        'updated': '01:01:18',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 41,
                                        'next_hop': '10.229.3.2',
                                        'outgoing_interface': 'Ethernet1/1',
                                        'route_preference': 110,
                                        'source_protocol': 'ospf',
                                        'source_protocol_status': 'intra',
                                        'updated': '01:01:18',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.186.2.0/24',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_status': 'intra',
                            'ubest': 4,
                        },
                        '10.19.31.31/32': {
                            'active': True,
                            'mbest': 0,
                            'metric': 41,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.229.11.11',
                                        'route_preference': 200,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '01:01:12',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 41,
                                        'next_hop': '10.1.3.1',
                                        'outgoing_interface': 'Ethernet1/2',
                                        'route_preference': 110,
                                        'source_protocol': 'ospf',
                                        'source_protocol_status': 'intra',
                                        'updated': '01:01:18',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.19.31.31/32',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_status': 'intra',
                            'tag': 100,
                            'ubest': 1,
                        },
                        '10.2.3.0/24': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.2.3.3',
                                        'outgoing_interface': 'Ethernet1/4',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '01:01:33',
                                    },
                                },
                            },
                            'route': '10.2.3.0/24',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 1,
                        },
                        '10.2.3.3/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.2.3.3',
                                        'outgoing_interface': 'Ethernet1/4',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '01:01:33',
                                    },
                                },
                            },
                            'route': '10.2.3.3/32',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 1,
                        },
                        '10.229.3.0/24': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.229.3.3',
                                        'outgoing_interface': 'Ethernet1/1',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '01:01:35',
                                    },
                                },
                            },
                            'route': '10.229.3.0/24',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 1,
                        },
                        '10.229.3.3/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.229.3.3',
                                        'outgoing_interface': 'Ethernet1/1',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '01:01:35',
                                    },
                                },
                            },
                            'route': '10.229.3.3/32',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 1,
                        },
                        '10.234.21.21/32': {
                            'active': True,
                            'mbest': 0,
                            'metric': 50,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 50,
                                        'next_hop': '10.1.3.1',
                                        'outgoing_interface': 'Ethernet1/2',
                                        'route_preference': 115,
                                        'source_protocol': 'isis',
                                        'source_protocol_status': 'L1',
                                        'updated': '01:01:22',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 50,
                                        'next_hop': '10.186.3.1',
                                        'outgoing_interface': 'Ethernet1/3',
                                        'route_preference': 115,
                                        'source_protocol': 'isis',
                                        'source_protocol_status': 'L1',
                                        'updated': '01:01:16',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.234.21.21/32',
                            'route_preference': 115,
                            'source_protocol': 'isis',
                            'source_protocol_status': 'L1',
                            'ubest': 2,
                        },
                        '10.36.3.3/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.36.3.3',
                                        'outgoing_interface': 'Loopback0',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '01:01:31',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '10.36.3.3',
                                        'outgoing_interface': 'Loopback0',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '01:01:31',
                                    },
                                },
                            },
                            'route': '10.36.3.3/32',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 2,
                        },
                        '10.4.1.1/32': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.1.3.1',
                                        'outgoing_interface': 'Ethernet1/2',
                                        'route_preference': 1,
                                        'source_protocol': 'static',
                                        'updated': '01:01:30',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '10.186.3.1',
                                        'outgoing_interface': 'Ethernet1/3',
                                        'route_preference': 1,
                                        'source_protocol': 'static',
                                        'updated': '01:01:30',
                                    },
                                },
                            },
                            'route': '10.4.1.1/32',
                            'route_preference': 1,
                            'source_protocol': 'static',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
    },
}

    golden_parsed_output_4 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.12.120.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2,
                                        'next_hop': '10.23.120.2',
                                        'outgoing_interface': 'Ethernet1/1.120',
                                        'route_preference': 120,
                                        'source_protocol': 'rip',
                                        'source_protocol_status': 'rip',
                                        'updated': '2w0d',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.12.120.0/24',
                            'route_preference': 120,
                            'source_protocol': 'rip',
                            'source_protocol_status': 'rip',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
    },
}

    golden_output_4 = {'execute.return_value': '''
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.12.120.0/24, ubest/mbest: 2/0
            *via 10.23.120.2, Eth1/1.120, [120/2], 2w0d, rip-1, rip
    '''}

    golden_parsed_output_5 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.12.120.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2,
                                        'next_hop': '10.13.120.1',
                                        'outgoing_interface': 'Ethernet1/2.120',
                                        'route_preference': 120,
                                        'source_protocol': 'rip',
                                        'source_protocol_status': 'rip',
                                        'updated': '2w0d',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.12.120.0/24',
                            'route_preference': 120,
                            'source_protocol': 'rip',
                            'source_protocol_status': 'rip',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
    },
}

    golden_output_5 = {'execute.return_value': '''
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.12.120.0/24, ubest/mbest: 2/0
            *via 10.13.120.1, Eth1/2.120, [120/2], 2w0d, rip-1, rip
    '''}

    golden_parsed_output_6 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.12.120.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2,
                                        'next_hop': '10.13.120.1',
                                        'outgoing_interface': 'Ethernet1/2.120',
                                        'route_preference': 120,
                                        'source_protocol': 'rip',
                                        'source_protocol_status': 'rip',
                                        'updated': '2w0d',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 2,
                                        'next_hop': '10.23.120.2',
                                        'outgoing_interface': 'Ethernet1/1.120',
                                        'route_preference': 120,
                                        'source_protocol': 'rip',
                                        'source_protocol_status': 'rip',
                                        'updated': '2w0d',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.12.120.0/24',
                            'route_preference': 120,
                            'source_protocol': 'rip',
                            'source_protocol_status': 'rip',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
    },
}

    golden_output_6 = {'execute.return_value': '''
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.12.120.0/24, ubest/mbest: 2/0
            *via 10.13.120.1, Eth1/2.120, [120/2], 2w0d, rip-1, rip
            *via 10.23.120.2, Eth1/1.120, [120/2], 2w0d, rip-1, rip
    '''}

    golden_parsed_output_7 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.1.0.0/8': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2,
                                        'next_hop': '10.13.120.1',
                                        'outgoing_interface': 'Ethernet1/2.120',
                                        'route_preference': 120,
                                        'source_protocol': 'rip',
                                        'source_protocol_status': 'rip',
                                        'updated': '2w0d',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.1.0.0/8',
                            'route_preference': 120,
                            'source_protocol': 'rip',
                            'source_protocol_status': 'rip',
                            'ubest': 1,
                        },
                        '10.12.120.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2,
                                        'next_hop': '10.13.120.1',
                                        'outgoing_interface': 'Ethernet1/2.120',
                                        'route_preference': 120,
                                        'source_protocol': 'rip',
                                        'source_protocol_status': 'rip',
                                        'updated': '2w0d',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.12.120.0/24',
                            'route_preference': 120,
                            'source_protocol': 'rip',
                            'source_protocol_status': 'rip',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
    },
}

    golden_output_7 = {'execute.return_value': '''
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.1.0.0/8, ubest/mbest: 1/0
            *via 10.13.120.1, Eth1/2.120, [120/2], 2w0d, rip-1, rip
        10.12.120.0/24, ubest/mbest: 2/0
            *via 10.13.120.1, Eth1/2.120, [120/2], 2w0d, rip-1, rip
    '''}

    golden_parsed_output_8 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.12.120.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2,
                                        'next_hop': '10.13.120.1',
                                        'outgoing_interface': 'Ethernet1/2.120',
                                        'route_preference': 120,
                                        'source_protocol': 'rip',
                                        'source_protocol_status': 'rip',
                                        'updated': '2w0d',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.12.120.0/24',
                            'route_preference': 120,
                            'source_protocol': 'rip',
                            'source_protocol_status': 'rip',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
    },
}

    golden_output_8 = {'execute.return_value': '''
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.12.120.0/24, ubest/mbest: 2/0
            *via 10.13.120.1, Eth1/2.120, [120/2], 2w0d, rip-1, rip
    '''}

    golden_parsed_output_9 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.12.120.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2,
                                        'next_hop': '10.13.120.1',
                                        'outgoing_interface': 'Ethernet1/2.120',
                                        'route_preference': 120,
                                        'source_protocol': 'rip',
                                        'source_protocol_status': 'rip',
                                        'updated': '2w0d',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 2,
                                        'next_hop': '10.23.120.2',
                                        'outgoing_interface': 'Ethernet1/1.120',
                                        'route_preference': 120,
                                        'source_protocol': 'rip',
                                        'source_protocol_status': 'rip',
                                        'updated': '2w0d',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.12.120.0/24',
                            'route_preference': 120,
                            'source_protocol': 'rip',
                            'source_protocol_status': 'rip',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
    },
}

    golden_output_9 = {'execute.return_value': '''
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.12.120.0/24, ubest/mbest: 2/0
            *via 10.13.120.1, Eth1/2.120, [120/2], 2w0d, rip-1, rip
            *via 10.23.120.2, Eth1/1.120, [120/2], 2w0d, rip-1, rip
    '''}

    golden_parsed_output_10 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.12.120.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2,
                                        'next_hop': '10.23.120.2',
                                        'outgoing_interface': 'Ethernet1/1.120',
                                        'route_preference': 120,
                                        'source_protocol': 'rip',
                                        'source_protocol_status': 'rip',
                                        'updated': '2w0d',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.12.120.0/24',
                            'route_preference': 120,
                            'source_protocol': 'rip',
                            'source_protocol_status': 'rip',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
    },
}

    golden_output_10 = {'execute.return_value': '''
        IP Route Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]
        '%<string>' in via output denotes VRF <string>

        10.12.120.0/24, ubest/mbest: 2/0
            *via 10.23.120.2, Eth1/1.120, [120/2], 2w0d, rip-1, rip
    '''}

    golden_output_11 = {'execute.return_value': '''
    '*' denotes best ucast next-hop
    '**' denotes best mcast next-hop
    '[x/y]' denotes [preference/metric]
    '%' in via output denotes VRF
    
    show ip route static
    10.111.1.1/32, ubest/mbest: 1/0
    *via 10.144.10.2, [1/0], 13:35:01, static
    via 10.1.10.2, [4/0], 13:35:01, static
    '''}

    golden_parsed_output_11 = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.111.1.1/32': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'next_hop': '10.144.10.2',
                                        'source_protocol': 'static',
                                        'updated': '13:35:01',
                                        'route_preference': 1,
                                        'metric': 0,
                                    },
                                    2: {
                                        'index': 2,
                                        'next_hop': '10.1.10.2',
                                        'source_protocol': 'static',
                                        'updated': '13:35:01',
                                        'route_preference': 4,
                                        'metric': 0,
                                    },
                                },
                            },
                            'route': '10.111.1.1/32',
                            'route_preference': 1,
                            'source_protocol': 'static',
                            'ubest': 1,
                        },
                    },
                },
            },
        },
    },
}

    golden_output_12 = {'execute.return_value': '''
         IP Route Table for VRF "default"
         '*' denotes best ucast next-hop
         '**' denotes best mcast next-hop
         '[x/y]' denotes [preference/metric]

         10.106.0.0/8, ubest/mbest: 1/0
             *via vrf default, Null0, [20/0], 18:11:28, bgp-333, external, tag 333
         10.16.1.0/24, ubest/mbest: 1/0
             *via 2001:db8:8b05::1002%default, Eth1/1, [200/4444], 15:57:39, bgp-333, internal, tag 333
         10.106.0.5/8, ubest/mbest: 1/0
             *via Null0, [1/0], 18:47:42, static


         IP Route Table for VRF "management"
         '*' denotes best ucast next-hop
         '**' denotes best mcast next-hop
         '[x/y]' denotes [preference/metric]

         IP Route Table for VRF "VRF1"
         '*' denotes best ucast next-hop
         '**' denotes best mcast next-hop
         '[x/y]' denotes [preference/metric]

         10.121.0.0/8, ubest/mbest: 1/0
             *via Null0, [55/0], 5w0d, bgp-100, discard, tag 100
         10.205.0.1/32, ubest/mbest: 1/0 time, attached
             *via 10.205.0.1, Bdi1255, [0/0], 2w6d, local
         10.21.33.33/32, ubest/mbest: 1/1
             *via 10.36.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
             **via 10.36.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
         10.189.1.0/24, ubest/mbest: 1/0 time
             *via 10.55.130.3%default, [33/0], 3d10h, bgp-1, internal, tag 1 (evpn), segid: 50051 tunnelid: 0x64008203 encap: VXLAN
         10.229.11.11/32, ubest/mbest: 2/0, attached
             *via 10.229.11.11, Lo1, [0/0], 5w4d, local
             *via 10.229.11.11, Lo1, [0/0], 5w4d, direct
         10.4.1.1/32, ubest/mbest: 2/0
             *via 10.2.4.2, Eth2/4, [110/81], 00:18:35, ospf-1, intra (mpls)
             *via 10.3.4.3, Eth2/1, [110/81], 00:18:35, ospf-1, intra (mpls)
         10.16.2.2/32, ubest/mbest: 1/0
             *via 10.2.4.2, Eth2/4, [110/41], 00:18:35, ospf-1, intra (mpls)
    '''}

    golden_parsed_output_12 = {
    'vrf': {
        'VRF1': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.121.0.0/8': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': 'Null0',
                                        'route_preference': 55,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'discard',
                                        'updated': '5w0d',
                                    },
                                },
                            },
                            'process_id': '100',
                            'route': '10.121.0.0/8',
                            'route_preference': 55,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'discard',
                            'tag': 100,
                            'ubest': 1,
                        },
                        '10.16.2.2/32': {
                            'active': True,
                            'mbest': 0,
                            'metric': 41,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 41,
                                        'next_hop': '10.2.4.2',
                                        'outgoing_interface': 'Ethernet2/4',
                                        'route_preference': 110,
                                        'source_protocol': 'ospf',
                                        'source_protocol_status': 'intra',
                                        'updated': '00:18:35',
                                        'mpls': True,
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.16.2.2/32',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_status': 'intra',
                            'ubest': 1,
                        },
                        '10.189.1.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.55.130.3',
                                        'next_hop_vrf': 'default',
                                        'route_preference': 33,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '3d10h',
                                        'encap': 'vxlan',
                                        'evpn': True,
                                        'tunnelid': '0x64008203',
                                        'segid': 50051,
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.189.1.0/24',
                            'route_preference': 33,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'internal',
                            'tag': 1,
                            'ubest': 1,
                        },
                        '10.205.0.1/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.205.0.1',
                                        'outgoing_interface': 'Bdi1255',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '2w6d',
                                    },
                                },
                            },
                            'route': '10.205.0.1/32',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 1,
                        },
                        '10.21.33.33/32': {
                            'active': True,
                            'mbest': 1,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.36.3.3',
                                        'next_hop_vrf': 'default',
                                        'route_preference': 33,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '5w0d',
                                        'mpls_vpn': True,
                                    },
                                    2: {
                                        'best_mcast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '10.36.3.3',
                                        'next_hop_vrf': 'default',
                                        'route_preference': 33,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '5w0d',
                                        'mpls_vpn': True,
                                    },
                                },
                            },
                            'process_id': '100',
                            'route': '10.21.33.33/32',
                            'route_preference': 33,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'internal',
                            'tag': 100,
                            'ubest': 1,
                        },
                        '10.229.11.11/32': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '10.229.11.11',
                                        'outgoing_interface': 'Loopback1',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '5w4d',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '10.229.11.11',
                                        'outgoing_interface': 'Loopback1',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '5w4d',
                                    },
                                },
                            },
                            'route': '10.229.11.11/32',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 2,
                        },
                        '10.4.1.1/32': {
                            'active': True,
                            'mbest': 0,
                            'metric': 81,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 81,
                                        'next_hop': '10.2.4.2',
                                        'outgoing_interface': 'Ethernet2/4',
                                        'route_preference': 110,
                                        'source_protocol': 'ospf',
                                        'source_protocol_status': 'intra',
                                        'updated': '00:18:35',
                                        'mpls': True,
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 81,
                                        'next_hop': '10.3.4.3',
                                        'outgoing_interface': 'Ethernet2/1',
                                        'route_preference': 110,
                                        'source_protocol': 'ospf',
                                        'source_protocol_status': 'intra',
                                        'updated': '00:18:35',
                                        'mpls': True,
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '10.4.1.1/32',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_status': 'intra',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '10.106.0.0/8': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': 'vrf default',
                                        'outgoing_interface': 'Null0',
                                        'route_preference': 20,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'external',
                                        'updated': '18:11:28',
                                    },
                                },
                            },
                            'process_id': '333',
                            'route': '10.106.0.0/8',
                            'route_preference': 20,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'external',
                            'tag': 333,
                            'ubest': 1,
                        },
                        '10.106.0.5/8': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': 'Null0',
                                        'route_preference': 1,
                                        'source_protocol': 'static',
                                        'updated': '18:47:42',
                                    },
                                },
                            },
                            'route': '10.106.0.5/8',
                            'route_preference': 1,
                            'source_protocol': 'static',
                            'ubest': 1,
                        },
                        '10.16.1.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 4444,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 4444,
                                        'next_hop': '2001:db8:8b05::1002',
                                        'next_hop_vrf': 'default',
                                        'outgoing_interface': 'Ethernet1/1',
                                        'route_preference': 200,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '15:57:39',
                                    },
                                },
                            },
                            'process_id': '333',
                            'route': '10.16.1.0/24',
                            'route_preference': 200,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'internal',
                            'tag': 333,
                            'ubest': 1,
                        },
                    },
                },
            },
        },
        'management': {
            'address_family': {
                'ipv4': {
                    'routes': {
                    },
                },
            },
        },
    },
}


    golden_output_00 = {'execute.return_value': '''
         show ip route ospf-100 vrf default
         IP Route Table for VRF "default"

        '*' denotes best ucast next-hop

        '**' denotes best mcast next-hop

        '[x/y]' denotes [preference/metric]

        '%<string>' in via output denotes VRF <string>



        10.144.6.0/24, ubest/mbest: 1/0, pending ufdm

            *via 10.36.3.2, Eth1/4, [110/80], 00:01:54, ospf-100, intra

        192.168.1.1/32, ubest/mbest: 1/0, pending ufdm

            *via 10.64.4.2, Eth1/3, [110/41], 00:01:54, ospf-100, intra

        192.168.3.3/32, ubest/mbest: 1/0, pending ufdm

            *via 10.36.3.2, Eth1/4, [110/41], 00:01:54, ospf-100, intra
    '''}

    golden_parsed_output_00 = {
        'vrf': 
            {'default': 
                {'address_family': 
                    {'ipv4': 
                        {'routes': 
                            {'192.168.1.1/32': 
                                {'active': True,
                                                'attached': False,
                                                'mbest': 0,
                                                'metric': 41,
                                                'next_hop': {'next_hop_list': {1: {'best_ucast_nexthop': True,
                                                                                    'index': 1,
                                                                                    'metric': 41,
                                                                                    'next_hop': '10.64.4.2',
                                                                                    'outgoing_interface': 'Ethernet1/3',
                                                                                    'route_preference': 110,
                                                                                    'source_protocol': 'ospf',
                                                                                    'source_protocol_status': 'intra',
                                                                                    'updated': '00:01:54'}}},
                                                'process_id': '100',
                                                'route': '192.168.1.1/32',
                                                'route_preference': 110,
                                                'source_protocol': 'ospf',
                                                'source_protocol_status': 'intra',
                                                'ubest': 1},
                            '192.168.3.3/32': {'active': True,
                                                'attached': False,
                                                'mbest': 0,
                                                'metric': 41,
                                                'next_hop': {'next_hop_list': {1: {'best_ucast_nexthop': True,
                                                                                    'index': 1,
                                                                                    'metric': 41,
                                                                                    'next_hop': '10.36.3.2',
                                                                                    'outgoing_interface': 'Ethernet1/4',
                                                                                    'route_preference': 110,
                                                                                    'source_protocol': 'ospf',
                                                                                    'source_protocol_status': 'intra',
                                                                                    'updated': '00:01:54'}}},
                                                'process_id': '100',
                                                'route': '192.168.3.3/32',
                                                'route_preference': 110,
                                                'source_protocol': 'ospf',
                                                'source_protocol_status': 'intra',
                                                'ubest': 1},
                            '10.144.6.0/24': {'active': True,
                                            'attached': False,
                                            'mbest': 0,
                                            'metric': 80,
                                            'next_hop': {'next_hop_list': {1: {'best_ucast_nexthop': True,
                                                                                'index': 1,
                                                                                'metric': 80,
                                                                                'next_hop': '10.36.3.2',
                                                                                'outgoing_interface': 'Ethernet1/4',
                                                                                'route_preference': 110,
                                                                                'source_protocol': 'ospf',
                                                                                'source_protocol_status': 'intra',
                                                                                'updated': '00:01:54'}}},
                                            'process_id': '100',
                                            'route': '10.144.6.0/24',
                                            'route_preference': 110,
                                            'source_protocol': 'ospf',
                                            'source_protocol_status': 'intra',
                                            'ubest': 1}}}}}}
                }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRoute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_route(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ip_route_vrf_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(vrf="vni_10100")
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_show_ip_route_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(vrf="all")
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_show_ip_route_route_protocol_interface_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(route='10.12.120.0/24',
                                  protocol='rip',
                                  interface='e1/1.120',
                                  vrf='default')
        self.assertEqual(parsed_output,self.golden_parsed_output_4)
    
    def test_show_ip_route_route_protocol_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(route='10.12.120.0/24',
                                  protocol='rip',
                                  interface='e1/2.120')
        self.assertEqual(parsed_output, self.golden_parsed_output_5)
    
    def test_show_ip_route_route_protocol_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_6)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(route='10.12.120.0/24',
                                  protocol='rip',
                                  vrf='default')
        self.assertEqual(parsed_output, self.golden_parsed_output_6)
    
    def test_show_ip_route_protocol_interface_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_7)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(protocol='rip',
                                  interface='e1/2.120',
                                  vrf='default')
        self.assertEqual(parsed_output, self.golden_parsed_output_7)
    
    def test_show_ip_route_route_interface_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_8)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(route='10.12.120.0/24',
                                  interface='e1/2.120',
                                  vrf='default')
        self.assertEqual(parsed_output, self.golden_parsed_output_8)
    
    def test_show_ip_route_route_protocol(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_9)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(route='10.12.120.0/24',
                                  protocol='rip')
        self.assertEqual(parsed_output, self.golden_parsed_output_9)
    
    def test_show_ip_route_protocol_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_10)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse(protocol='rip',
                                  interface='e1/1.120')
        self.assertEqual(parsed_output, self.golden_parsed_output_10)

    def test_show_ip_route_11(self):
        self.device = Mock(**self.golden_output_11)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_11)

    def test_show_ip_route_12(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_12)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_12)

    def test_show_ip_route_00(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_00)
        obj = ShowIpRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_00)


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
            *via ::ffff:10.229.11.11%default:IPv4, [200/0], 01:01:43, bgp-100, internal,
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

    '''}
    golden_parsed_output_1 = {
    'vrf': {
        'VRF1': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        '2001:1:1:1::1/128': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:1:1:1::1',
                                        'outgoing_interface': 'Loopback4',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '00:00:35',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '2001:1:1:1::1',
                                        'outgoing_interface': 'Loopback4',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '00:00:35',
                                    },
                                },
                            },
                            'route': '2001:1:1:1::1/128',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
        'default': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        '2001:10:1:2::/64': {
                            'active': True,
                            'mbest': 0,
                            'metric': 41,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 41,
                                        'next_hop': 'fe80::5054:ff:fe64:bd2e',
                                        'outgoing_interface': 'Ethernet1/3',
                                        'route_preference': 110,
                                        'source_protocol': 'ospfv3',
                                        'source_protocol_status': 'intra',
                                        'updated': '01:01:10',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 41,
                                        'next_hop': 'fe80::5054:ff:fea5:6e95',
                                        'outgoing_interface': 'Ethernet1/2',
                                        'route_preference': 110,
                                        'source_protocol': 'ospfv3',
                                        'source_protocol_status': 'intra',
                                        'updated': '01:01:10',
                                    },
                                    3: {
                                        'best_ucast_nexthop': True,
                                        'index': 3,
                                        'metric': 41,
                                        'next_hop': 'fe80::5054:ff:fea7:1341',
                                        'outgoing_interface': 'Ethernet1/4',
                                        'route_preference': 110,
                                        'source_protocol': 'ospfv3',
                                        'source_protocol_status': 'intra',
                                        'updated': '01:01:10',
                                    },
                                    4: {
                                        'best_ucast_nexthop': True,
                                        'index': 4,
                                        'metric': 41,
                                        'next_hop': 'fe80::5054:ff:feb3:b312',
                                        'outgoing_interface': 'Ethernet1/1',
                                        'route_preference': 110,
                                        'source_protocol': 'ospfv3',
                                        'source_protocol_status': 'intra',
                                        'updated': '01:01:10',
                                    },
                                },
                            },
                            'process_id': '1',
                            'route': '2001:10:1:2::/64',
                            'route_preference': 110,
                            'source_protocol': 'ospfv3',
                            'source_protocol_status': 'intra',
                            'ubest': 4,
                        },
                        '2001:1:1:1::1/128': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:10:1:3::1',
                                        'outgoing_interface': 'Ethernet1/2',
                                        'route_preference': 1,
                                        'source_protocol': 'static',
                                        'updated': '01:02:00',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '2001:20:1:3::1',
                                        'outgoing_interface': 'Ethernet1/3',
                                        'route_preference': 1,
                                        'source_protocol': 'static',
                                        'updated': '01:02:00',
                                    },
                                },
                            },
                            'route': '2001:1:1:1::1/128',
                            'route_preference': 1,
                            'source_protocol': 'static',
                            'ubest': 2,
                        },
                        '2001:31:31:31::31/128': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '::ffff:10.229.11.11',
                                        'next_hop_af': 'ipv4',
                                        'next_hop_vrf': 'default',
                                        'route_preference': 200,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '01:01:43',
                                    },
                                },
                            },
                            'process_id': '100',
                            'route': '2001:31:31:31::31/128',
                            'route_preference': 200,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'internal',
                            'tag': 100,
                            'ubest': 1,
                        },
                        '2001:32:32:32::32/128': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': 'fe80::5054:ff:fea7:1341',
                                        'outgoing_interface': 'Ethernet1/4',
                                        'route_preference': 200,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '01:01:24',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': 'fe80::5054:ff:feb3:b312',
                                        'outgoing_interface': 'Ethernet1/1',
                                        'route_preference': 200,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '01:01:24',
                                    },
                                },
                            },
                            'process_id': '100',
                            'route': '2001:32:32:32::32/128',
                            'route_preference': 200,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'internal',
                            'tag': 100,
                            'ubest': 2,
                        },
                        '2001:33:33:33::33/128': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:33:33:33::33',
                                        'outgoing_interface': 'Loopback3',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '01:02:01',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '2001:33:33:33::33',
                                        'outgoing_interface': 'Loopback3',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '01:02:01',
                                    },
                                },
                            },
                            'route': '2001:33:33:33::33/128',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
        'management': {
            'address_family': {
                'ipv6': {
                    'routes': {
                    },
                },
            },
        },
    },
}

    golden_output_2 = {'execute.return_value': '''
        R3_nx# show ipv6 route vrf all
        IPv6 Routing Table for VRF "default"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        2001:1:1:1::1/128, ubest/mbest: 1/0
            *via fe80::f816:3eff:fef8:e824, Eth1/2.90, [90/2848], 03:55:29, eigrp-test, internal
        2001:2:2:2::2/128, ubest/mbest: 1/0
            *via fe80::f816:3eff:fe80:67f4, Eth1/1.90, [90/2842], 03:51:46, eigrp-test, internal
        2001:3:3:3::3/128, ubest/mbest: 2/0, attached
            *via 2001:3:3:3::3, Lo0, [0/0], 03:55:33, direct, 
            *via 2001:3:3:3::3, Lo0, [0/0], 03:55:33, local
        2001:10:12:90::/64, ubest/mbest: 2/0
            *via fe80::f816:3eff:fe80:67f4, Eth1/1.90, [90/3072], 03:51:46, eigrp-test, internal
            *via fe80::f816:3eff:fef8:e824, Eth1/2.90, [90/3072], 03:55:29, eigrp-test, internal
        2001:10:12:120::/64, ubest/mbest: 1/0
            *via fe80::f816:3eff:fef8:e824, Eth1/2.90, [90/3072], 03:39:27, eigrp-test, internal
        2001:10:13:90::/64, ubest/mbest: 1/0, attached
            *via 2001:10:13:90::3, Eth1/2.90, [0/0], 03:55:45, direct, 
        2001:10:13:90::3/128, ubest/mbest: 1/0, attached
            *via 2001:10:13:90::3, Eth1/2.90, [0/0], 03:55:45, local
        2001:10:23:120::/64, ubest/mbest: 1/0, attached
            *via 2001:10:23:120::3, Eth1/1.120, [0/0], 02:50:42, direct, 
        2001:10:23:120::3/128, ubest/mbest: 1/0, attached
            *via 2001:10:23:120::3, Eth1/1.120, [0/0], 02:50:42, local

            IPv6 Routing Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        2001:1:1:1::1/128, ubest/mbest: 1/0
            *via fe80::f816:3eff:fef8:e824, Eth1/2.390, [90/2848], 03:55:29, eigrp-test, internal
        2001:2:2:2::2/128, ubest/mbest: 1/0
            *via fe80::f816:3eff:fe80:67f4, Eth1/1.390, [90/2842], 03:51:47, eigrp-test, internal
        2001:3:3:3::3/128, ubest/mbest: 2/0, attached
            *via 2001:3:3:3::3, Lo300, [0/0], 03:55:33, direct, 
            *via 2001:3:3:3::3, Lo300, [0/0], 03:55:33, local
        2001:10:12:90::/64, ubest/mbest: 2/0
            *via fe80::f816:3eff:fe80:67f4, Eth1/1.390, [90/3072], 03:51:47, eigrp-test, internal
            *via fe80::f816:3eff:fef8:e824, Eth1/2.390, [90/3072], 03:55:29, eigrp-test, internal
        2001:10:12:120::/64, ubest/mbest: 1/0
            *via fe80::f816:3eff:fef8:e824, Eth1/2.390, [90/3072], 03:25:35, eigrp-test, internal
        2001:10:13:90::/64, ubest/mbest: 1/0, attached
            *via 2001:10:13:90::3, Eth1/2.390, [0/0], 03:55:44, direct, 
        2001:10:13:110::3/128, ubest/mbest: 1/0, attached
            *via 2001:10:13:110::3, Eth1/2.410, [0/0], 03:55:43, local
        2001:10:13:115::/64, ubest/mbest: 1/0, attached
            *via 2001:10:13:115::3, Eth1/2.415, [0/0], 03:55:43, direct, 
        2001:10:13:120::3/128, ubest/mbest: 1/0, attached
    '''}

    golden_parsed_output_2 = {
    'vrf': {
        'VRF1': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        '2001:10:12:120::/64': {
                            'active': True,
                            'mbest': 0,
                            'metric': 3072,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 3072,
                                        'next_hop': 'fe80::f816:3eff:fef8:e824',
                                        'outgoing_interface': 'Ethernet1/2.390',
                                        'route_preference': 90,
                                        'source_protocol': 'eigrp',
                                        'source_protocol_status': 'internal',
                                        'updated': '03:25:35',
                                    },
                                },
                            },
                            'process_id': 'test',
                            'route': '2001:10:12:120::/64',
                            'route_preference': 90,
                            'source_protocol': 'eigrp',
                            'source_protocol_status': 'internal',
                            'ubest': 1,
                        },
                        '2001:10:12:90::/64': {
                            'active': True,
                            'mbest': 0,
                            'metric': 3072,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 3072,
                                        'next_hop': 'fe80::f816:3eff:fe80:67f4',
                                        'outgoing_interface': 'Ethernet1/1.390',
                                        'route_preference': 90,
                                        'source_protocol': 'eigrp',
                                        'source_protocol_status': 'internal',
                                        'updated': '03:51:47',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 3072,
                                        'next_hop': 'fe80::f816:3eff:fef8:e824',
                                        'outgoing_interface': 'Ethernet1/2.390',
                                        'route_preference': 90,
                                        'source_protocol': 'eigrp',
                                        'source_protocol_status': 'internal',
                                        'updated': '03:55:29',
                                    },
                                },
                            },
                            'process_id': 'test',
                            'route': '2001:10:12:90::/64',
                            'route_preference': 90,
                            'source_protocol': 'eigrp',
                            'source_protocol_status': 'internal',
                            'ubest': 2,
                        },
                        '2001:10:13:110::3/128': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:10:13:110::3',
                                        'outgoing_interface': 'Ethernet1/2.410',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '03:55:43',
                                    },
                                },
                            },
                            'route': '2001:10:13:110::3/128',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 1,
                        },
                        '2001:10:13:115::/64': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:10:13:115::3',
                                        'outgoing_interface': 'Ethernet1/2.415',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '03:55:43',
                                    },
                                },
                            },
                            'route': '2001:10:13:115::/64',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 1,
                        },
                        '2001:10:13:120::3/128': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'route': '2001:10:13:120::3/128',
                            'ubest': 1,
                        },
                        '2001:10:13:90::/64': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:10:13:90::3',
                                        'outgoing_interface': 'Ethernet1/2.390',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '03:55:44',
                                    },
                                },
                            },
                            'route': '2001:10:13:90::/64',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 1,
                        },
                        '2001:1:1:1::1/128': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2848,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2848,
                                        'next_hop': 'fe80::f816:3eff:fef8:e824',
                                        'outgoing_interface': 'Ethernet1/2.390',
                                        'route_preference': 90,
                                        'source_protocol': 'eigrp',
                                        'source_protocol_status': 'internal',
                                        'updated': '03:55:29',
                                    },
                                },
                            },
                            'process_id': 'test',
                            'route': '2001:1:1:1::1/128',
                            'route_preference': 90,
                            'source_protocol': 'eigrp',
                            'source_protocol_status': 'internal',
                            'ubest': 1,
                        },
                        '2001:2:2:2::2/128': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2842,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2842,
                                        'next_hop': 'fe80::f816:3eff:fe80:67f4',
                                        'outgoing_interface': 'Ethernet1/1.390',
                                        'route_preference': 90,
                                        'source_protocol': 'eigrp',
                                        'source_protocol_status': 'internal',
                                        'updated': '03:51:47',
                                    },
                                },
                            },
                            'process_id': 'test',
                            'route': '2001:2:2:2::2/128',
                            'route_preference': 90,
                            'source_protocol': 'eigrp',
                            'source_protocol_status': 'internal',
                            'ubest': 1,
                        },
                        '2001:3:3:3::3/128': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:3:3:3::3',
                                        'outgoing_interface': 'Loopback300',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '03:55:33',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '2001:3:3:3::3',
                                        'outgoing_interface': 'Loopback300',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '03:55:33',
                                    },
                                },
                            },
                            'route': '2001:3:3:3::3/128',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 2,
                        },
                    },
                },
            },
        },
        'default': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        '2001:10:12:120::/64': {
                            'active': True,
                            'mbest': 0,
                            'metric': 3072,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 3072,
                                        'next_hop': 'fe80::f816:3eff:fef8:e824',
                                        'outgoing_interface': 'Ethernet1/2.90',
                                        'route_preference': 90,
                                        'source_protocol': 'eigrp',
                                        'source_protocol_status': 'internal',
                                        'updated': '03:39:27',
                                    },
                                },
                            },
                            'process_id': 'test',
                            'route': '2001:10:12:120::/64',
                            'route_preference': 90,
                            'source_protocol': 'eigrp',
                            'source_protocol_status': 'internal',
                            'ubest': 1,
                        },
                        '2001:10:12:90::/64': {
                            'active': True,
                            'mbest': 0,
                            'metric': 3072,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 3072,
                                        'next_hop': 'fe80::f816:3eff:fe80:67f4',
                                        'outgoing_interface': 'Ethernet1/1.90',
                                        'route_preference': 90,
                                        'source_protocol': 'eigrp',
                                        'source_protocol_status': 'internal',
                                        'updated': '03:51:46',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 3072,
                                        'next_hop': 'fe80::f816:3eff:fef8:e824',
                                        'outgoing_interface': 'Ethernet1/2.90',
                                        'route_preference': 90,
                                        'source_protocol': 'eigrp',
                                        'source_protocol_status': 'internal',
                                        'updated': '03:55:29',
                                    },
                                },
                            },
                            'process_id': 'test',
                            'route': '2001:10:12:90::/64',
                            'route_preference': 90,
                            'source_protocol': 'eigrp',
                            'source_protocol_status': 'internal',
                            'ubest': 2,
                        },
                        '2001:10:13:90::/64': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:10:13:90::3',
                                        'outgoing_interface': 'Ethernet1/2.90',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '03:55:45',
                                    },
                                },
                            },
                            'route': '2001:10:13:90::/64',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 1,
                        },
                        '2001:10:13:90::3/128': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:10:13:90::3',
                                        'outgoing_interface': 'Ethernet1/2.90',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '03:55:45',
                                    },
                                },
                            },
                            'route': '2001:10:13:90::3/128',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 1,
                        },
                        '2001:10:23:120::/64': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:10:23:120::3',
                                        'outgoing_interface': 'Ethernet1/1.120',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '02:50:42',
                                    },
                                },
                            },
                            'route': '2001:10:23:120::/64',
                            'route_preference': 0,
                            'source_protocol': 'direct',
                            'ubest': 1,
                        },
                        '2001:10:23:120::3/128': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:10:23:120::3',
                                        'outgoing_interface': 'Ethernet1/1.120',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '02:50:42',
                                    },
                                },
                            },
                            'route': '2001:10:23:120::3/128',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 1,
                        },
                        '2001:1:1:1::1/128': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2848,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2848,
                                        'next_hop': 'fe80::f816:3eff:fef8:e824',
                                        'outgoing_interface': 'Ethernet1/2.90',
                                        'route_preference': 90,
                                        'source_protocol': 'eigrp',
                                        'source_protocol_status': 'internal',
                                        'updated': '03:55:29',
                                    },
                                },
                            },
                            'process_id': 'test',
                            'route': '2001:1:1:1::1/128',
                            'route_preference': 90,
                            'source_protocol': 'eigrp',
                            'source_protocol_status': 'internal',
                            'ubest': 1,
                        },
                        '2001:2:2:2::2/128': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2842,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2842,
                                        'next_hop': 'fe80::f816:3eff:fe80:67f4',
                                        'outgoing_interface': 'Ethernet1/1.90',
                                        'route_preference': 90,
                                        'source_protocol': 'eigrp',
                                        'source_protocol_status': 'internal',
                                        'updated': '03:51:46',
                                    },
                                },
                            },
                            'process_id': 'test',
                            'route': '2001:2:2:2::2/128',
                            'route_preference': 90,
                            'source_protocol': 'eigrp',
                            'source_protocol_status': 'internal',
                            'ubest': 1,
                        },
                        '2001:3:3:3::3/128': {
                            'active': True,
                            'attached': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '2001:3:3:3::3',
                                        'outgoing_interface': 'Loopback0',
                                        'route_preference': 0,
                                        'source_protocol': 'direct',
                                        'updated': '03:55:33',
                                    },
                                    2: {
                                        'best_ucast_nexthop': True,
                                        'index': 2,
                                        'metric': 0,
                                        'next_hop': '2001:3:3:3::3',
                                        'outgoing_interface': 'Loopback0',
                                        'route_preference': 0,
                                        'source_protocol': 'local',
                                        'updated': '03:55:33',
                                    },
                                },
                            },
                            'route': '2001:3:3:3::3/128',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'ubest': 2,
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

    golden_parsed_output_4 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'routes': {
                            '2001:1:1:1::1/128': {
                                'route': '2001:1:1:1::1/128',
                                'active': True,
                                'ubest': 1,
                                'mbest': 0,
                                'metric': 2848,
                                'route_preference': 90,
                                'process_id': '65000',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'metric': 2848,
                                            'route_preference': 90,
                                            'next_hop': 'fe80::f816:3eff:feb2:c76f',
                                            'source_protocol': 'eigrp',
                                            'source_protocol_status': 'internal',
                                            'best_ucast_nexthop': True,
                                            'updated': '2w0d',
                                            'outgoing_interface': 'Ethernet1/2.390',
                                        },
                                        2: {
                                            'index': 2,
                                            'metric': 2,
                                            'route_preference': 120,
                                            'next_hop': 'fe80::f816:3eff:feb2:c76f',
                                            'source_protocol': 'rip',
                                            'source_protocol_status': 'rip',
                                            'updated': '2w0d',
                                            'outgoing_interface': 'Ethernet1/2.420',
                                        },
                                        3: {
                                            'index': 3,
                                            'metric': 0,
                                            'route_preference': 200,
                                            'next_hop': 'fe80::f816:3eff:feb2:c76f',
                                            'source_protocol': 'bgp',
                                            'source_protocol_status': 'internal',
                                            'updated': '2w0d',
                                            'outgoing_interface': 'Ethernet1/2.390',
                                        },
                                    },
                                },
                                'source_protocol': 'bgp',
                                'source_protocol_status': 'internal',
                                'hidden': True,
                                'tag': 65000,
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output_4 = {'execute.return_value': '''
        IPv6 Routing Table for VRF "VRF1"
        '*' denotes best ucast next-hop
        '**' denotes best mcast next-hop
        '[x/y]' denotes [preference/metric]

        2001:1:1:1::1/128, ubest/mbest: 1/0
            *via fe80::f816:3eff:feb2:c76f, Eth1/2.390, [90/2848], 2w0d, eigrp-test, internal
            via fe80::f816:3eff:feb2:c76f, Eth1/2.420, [120/2], 2w0d, rip-1, rip
            via fe80::f816:3eff:feb2:c76f, Eth1/2.390, [200/0], 2w0d, bgp-65000, internal, tag 65000 (hidden)
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

    def test_show_ipv6_route_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6Route(device=self.device)
        parsed_output = obj.parse(vrf="all")
        self.assertEqual(parsed_output,self.golden_parsed_output_2)
    
    def test_show_ipv6_route_4(self):
        self.device = Mock(**self.golden_output_4)
        obj = ShowIpv6Route(device=self.device)
        parsed_output = obj.parse(vrf='VRF1',
                                  route='2001:2:2:2::2/128',
                                  protocol='eigrp')
        self.assertEqual(parsed_output,self.golden_parsed_output_4)


# ================================================
#  Unit test for 'show ip route summary vrf all'
# =================================================

class test_show_ip_route_summary(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    # show ip route summary
    golden_output = {'execute.return_value': '''
        IP Route Table for VRF "default"
        Total number of routes: 17
        Total number of paths:  20

        Best paths per protocol:      Backup paths per protocol:
          am             : 1            None
          local          : 4     
          direct         : 4     
          broadcast      : 5     
          ospf-1         : 6         
          ospf-2         : 6  
          bgp-100        : 1000

        Number of routes per mask-length:
          /8 : 1       /24: 4       /32: 12      


        IP Route Table for VRF "management"
        Total number of routes: 11
        Total number of paths:  11

        Best paths per protocol:      Backup paths per protocol:
          am             : 3            None
          local          : 1     
          direct         : 1     
          static         : 1     
          broadcast      : 5     

        Number of routes per mask-length:
          /0 : 1       /8 : 1       /24: 1       /32: 8       


        IP Route Table for VRF "evpn-tenant-0002"
        Total number of routes: 11
        Total number of paths:  11

        Best paths per protocol:      Backup paths per protocol:
          local          : 2            None
          direct         : 2     
          broadcast      : 7     

        Number of routes per mask-length:
          /8 : 1       /16: 2       /32: 8       


        IP Route Table for VRF "evpn-t-0003"
        Total number of routes: 11
        Total number of paths:  11

        Best paths per protocol:      Backup paths per protocol:
          local          : 2            None
          direct         : 2     
          broadcast      : 7     

        Number of routes per mask-length:
          /8 : 1       /16: 2       /32: 8       
            '''}

    golden_parsed_output = {
    'vrf': {
        'default': {
            'backup_paths': {
            },
            'best_paths': {
                'am': 1,
                'broadcast': 5,
                'bgp-100': 1000,
                'direct': 4,
                'local': 4,
                'ospf-1': 6,
                'ospf-2': 6,
            },
            'num_routes_per_mask': {
                '/24': 4,
                '/32': 12,
                '/8': 1,
            },
            'total_paths': 20,
            'total_routes': 17,
        },
        'evpn-tenant-0002': {
            'backup_paths': {
            },
            'best_paths': {
                'broadcast': 7,
                'direct': 2,
                'local': 2,
            },
            'num_routes_per_mask': {
                '/16': 2,
                '/32': 8,
                '/8': 1,
            },
            'total_paths': 11,
            'total_routes': 11,
        },
        'evpn-t-0003': {
            'backup_paths': {
            },
            'best_paths': {
                'broadcast': 7,
                'direct': 2,
                'local': 2,
            },
            'num_routes_per_mask': {
                '/16': 2,
                '/32': 8,
                '/8': 1,
            },
            'total_paths': 11,
            'total_routes': 11,
        },
        'management': {
            'backup_paths': {
            },
            'best_paths': {
                'am': 3,
                'broadcast': 5,
                'direct': 1,
                'local': 1,
                'static': 1,
            },
            'num_routes_per_mask': {
                '/0': 1,
                '/24': 1,
                '/32': 8,
                '/8': 1,
            },
            'total_paths': 11,
            'total_routes': 11,
        },
    },
}

    # show ip route summary vrf all
    golden_output_2 = {'execute.return_value':'''
    IP Route Table for VRF "xxx"
    Total number of routes: 308
    Total number of paths:  332
    
    Best paths per protocol:      Backup paths per protocol:
      am             : 214          ospf-1000      : 10
      local          : 14    
      direct         : 14    
      broadcast      : 29    
      hsrp           : 10    
      ospf-1000      : 41
    '''}

    golden_parsed_output_2 = {
    'vrf': {
        'xxx': {
            'backup_paths': {
                'ospf-1000': 10,
            },
            'best_paths': {
                'am': 214,
                'broadcast': 29,
                'direct': 14,
                'hsrp': 10,
                'local': 14,
                'ospf-1000': 41,
            },
            'total_paths': 332,
            'total_routes': 308,
        },
    },
}

    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpRouteSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_route_summary_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpRouteSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ip_route_summary_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpRouteSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

if __name__ == '__main__':
    unittest.main()
