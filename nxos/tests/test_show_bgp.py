# **************************************************
# test file test_show_bgp.py
#
# Python
import unittest
from unittest.mock import Mock
# Ats
from ats.topology import Device
# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError
# nxos show_bgp
from parser.nxos.show_bgp import ShowBgpVrfAllAllDampeningParameters,\
                                 ShowRoutingVrfAll


class TestShowBgpVrfAllAllDampeningParameters(unittest.TestCase):
    ''' unittest for "show bgp vrf all all dampening parameters"
    '''
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vrf':
                            {'VRF1':
                             {'address_family':
                              {'ipv4 unicast':
                               {'dampening': 'True',
                                'dampening_route_map': 'dampening1',
                                'dampening_half_life_time': '45',
                                'dampening_reuse_time': '10000',
                                'dampening_suppress_time': '20000',
                                'dampening_max_suppress_time': '255',
                                'dampening_max_suppress_penalty': '507968'},
                               'ipv6 unicast':
                               {'dampening': 'True',
                                'dampening_route_map': 'dampening2',
                                'dampening_half_life_time': '45',
                                'dampening_reuse_time': '9999',
                                'dampening_suppress_time': '19999',
                                'dampening_max_suppress_time': '255',
                                'dampening_max_suppress_penalty': '507917'}}},
                             'default':
                             {'address_family':
                              {'ipv4 unicast':
                               {'dampening': 'True',
                                'dampening_half_life_time': '45',
                                'dampening_reuse_time': '1111',
                                'dampening_suppress_time': '2222',
                                'dampening_max_suppress_time': '255',
                                'dampening_max_suppress_penalty': '56435'},
                              'vpnv4 unicast':
                               {'dampening': 'True',
                                'route_distinguisher':
                                 {'1:100':
                                  {'rd_vrf': 'vpn1',
                                   'dampening_half_life_time': '1 mins',
                                   'dampening_reuse_time': '10',
                                   'dampening_suppress_time': '30',
                                   'dampening_max_suppress_time': '2 mins',
                                   'dampening_max_suppress_penalty': '40'}}}}}}}

    golden_output = {'execute.return_value': '''
Route Flap Dampening Parameters for VRF VRF1 Address family IPv4 Unicast:

Dampening policy configured: dampening1

Half-life time                 : 45
Suppress penalty               : 20000
Reuse penalty                  : 10000
Max suppress time              : 255
Max suppress penalty           : 507968

Route Flap Dampening Parameters for VRF VRF1 Address family IPv6 Unicast:

Dampening policy configured: dampening2

Half-life time                 : 45
Suppress penalty               : 19999
Reuse penalty                  : 9999
Max suppress time              : 255
Max suppress penalty           : 507917

Route Flap Dampening Parameters for VRF default Address family IPv4 Unicast:

Configured values in use:

Half-life time                 : 45
Suppress penalty               : 2222
Reuse penalty                  : 1111
Max suppress time              : 255
Max suppress penalty           : 56435

Route Flap Dampening Parameters for VRF default Address family VPNv4 Unicast:
Route Distinguisher: 1:100    (VRF vpn1)

Configured values in use:

Half-life time                 : 1 mins
Suppress penalty               : 30
Reuse penalty                  : 10
Max suppress time              : 2 mins
Max suppress penalty           : 40


'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        bgp_obj = ShowBgpVrfAllAllDampeningParameters(device=self.device)
        parsed_output = bgp_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_obj = ShowBgpVrfAllAllDampeningParameters(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_obj.parse()


class TestShowRoutingVrfAll(unittest.TestCase):
    ''' unittest for "show routing vrf all bgp"
    '''
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vrf':
                            {'VRF1':
                             {'ip/mask':
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
                                       'attibute': 'discard',
                                       'tag': '100'}}}}}}},
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
                                       'attibute': 'internal',
                                       'route_table': 'default',
                                       'tag': '100 (mpls-vpn)'}}}}},
                                 'multicast':
                                  {'nexthop':
                                   {'3.3.3.3':
                                    {'protocol':
                                     {'bgp':
                                      {'uptime': '5w0d',
                                       'preference': '33',
                                       'metric': '0',
                                       'protocol_id': '100',
                                       'attibute': 'internal',
                                       'route_table': 'default',
                                       'tag': '100 (mpls-vpn)'}}}}}}},
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
                                       'interface': 'Lo1'},
                                     'direct':
                                      {'uptime': '5w4d',
                                       'preference': '0',
                                       'metric': '0',
                                       'interface': 'Lo1'}}}}}}}}},
                            'default':
                             {'ip/mask':
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
                                       'attibute': 'external',
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
                                       'attibute': 'internal',
                                       'route_table': 'default',
                                       'tag': '333',
                                       'interface': 'Eth1/1'}}}}}}},
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
                                       'metric': '0'}}}}}}}}}}}

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
33.33.33.33/32, ubest/mbest: 1/1
    *via 3.3.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
    **via 3.3.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
11.11.11.11/32, ubest/mbest: 2/0, attached
    *via 11.11.11.11, Lo1, [0/0], 5w4d, local
    *via 11.11.11.11, Lo1, [0/0], 5w4d, direct
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        bgp_obj = ShowRoutingVrfAll(device=self.device)
        parsed_output = bgp_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_obj = ShowRoutingVrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_obj.parse()


if __name__ == '__main__':
    unittest.main()
