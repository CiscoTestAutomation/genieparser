import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.nxos.show_route_map import ShowRouteMap

class test_show_route_map(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'test': 
            {'statements': 
                {'10': 
                    {'actions': 
                        {'route_disposition': 'permit',
                        'set_as_path_group': ['10',
                                              '10',
                                              '10'],
                        'set_as_path_prepend': '10',
                        'set_as_path_prepend_repeat_n': 3,
                        'set_community': '100:1',
                        'set_community_additive': True,
                        'set_community_delete': 'test',
                        'set_community_no_advertise': True,
                        'set_community_no_export': True,
                        'set_ext_community_delete': 'cisco',
                        'set_ext_community_rt': '100:10',
                        'set_level': 'level-1',
                        'set_local_pref': 20,
                        'set_med': 20,
                        'set_metric_type': 'external',
                        'set_next_hop': '4.4.4.4',
                        'set_next_hop_v6': '2001:db8:1::1',
                        'set_route_origin': 'igp',
                        'set_tag': 30},
                    'conditions':
                        {'match_as_path_list': 'aspathlist1',
                        'match_community_list': 'test3',
                        'match_ext_community_list': 'testing',
                        'match_interface': 'Ethernet2/2',
                        'match_med_eq': 20,
                        'match_nexthop_in': 'test',
                        'match_nexthop_in_v6': 'test2',
                        'match_prefix_list': 'test-test',
                        'match_prefix_list_v6': 'test-test',
                        'match_route_type': 'level-1 '
                                           'level-2',
                        'match_tag_list': 23}}}}}

    
    golden_output = {'execute.return_value': '''
      route-map test, permit, sequence 10 
        Match clauses:
            as-path (as-path filter): aspathlist1 
            ip address prefix-lists: test-test 
            ip next-hop prefix-lists: test 
            ipv6 address prefix-lists: test-test 
            ipv6 next-hop prefix-lists: test2 
            interface: Ethernet2/2 
            metric: 20 
            tag: 23 
            community  (community-list filter): test3 
            route-type: level-1 level-2
            extcommunity  (extcommunity-list filter): testing  
        Set clauses:
            ip next-hop 4.4.4.4 
            ipv6 next-hop 2001:db8:1::1 
            tag 30 
            metric 20 
            metric-type external 
            level level-1 
            local-preference 20
            origin igp 
            comm-list test delete
            community 100:1 no-export no-advertise additive 
            as-path prepend 10 10 10 
            extcomm-list cisco delete
            extcommunity RT:100:10 additive 
      '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        route_map_obj = ShowRouteMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = route_map_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        route_map_obj = ShowRouteMap(device=self.device)
        parsed_output = route_map_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
