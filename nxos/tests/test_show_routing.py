# **************************************************
# test file test_show_routing.py
#
# Python
import unittest
from unittest.mock import Mock
# Ats
from ats.topology import Device
# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError
# nxos show_routing
from parser.nxos.show_routing import ShowRoutingVrfAll


class TestShowRoutingVrfAll(unittest.TestCase):
    ''' unittest for "show routing vrf all bgp"
        "show routing vrf all"
    '''
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'vrf':
            {'VRF1':
                {'bgp_distance_internal_as': 33,
                'bgp_distance_local': 55,
                'ip/mask':
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
                                                'attribute': 'internal',
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
                {'bgp_distance_extern_as': 20,
                'bgp_distance_internal_as': 200,
                'ip/mask':
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
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        bgp_obj = ShowRoutingVrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = bgp_obj.parse()


if __name__ == '__main__':
    unittest.main()
