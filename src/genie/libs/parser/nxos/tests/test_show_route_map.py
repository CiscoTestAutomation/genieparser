import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.nxos.show_route_map import ShowRouteMap


class test_show_route_map(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {'BGPPeers':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit'},
                                   'conditions':
                                    {'match_as_number_list': 'list1,list2'}}}},
                            'bgp-to-rib':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit',
                                     'set_distance': 10},
                                   'conditions':
                                    {'match_community_list': '100'}}}},
                            'eigrp-distance':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit',
                                     'set_distance': 10},
                                   'conditions':
                                    {'match_nexthop_in_v6': 'ipv6-nexthop'}}}},
                            'eigrp-filter':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit'},
                                   'conditions':
                                    {'match_nexthop_in': 'ipv4-nexthop'}}}},
                            'foo':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit',
                                     'set_distance': 150},
                                   'conditions':
                                    {'match_route_type': 'inter-area'}},
                                 '20':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit',
                                     'set_distance': 200},
                                   'conditions':
                                      {'match_route_type': 'external'}}}},
                            'isis-distance':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit',
                                     'set_distance': 10},
                                   'conditions':
                                    {'match_interface': 'Ethernet1/1'}}}},
                            'isis-filter':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit'},
                                   'conditions':
                                    {'match_interface': 'Ethernet1/1'}}}},
                            'metric-range':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit',
                                     'set_tag': 5},
                                   'conditions':
                                    {'match_med_eq': 50}}}},
                            'pbr-sample':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit',
                                     'set_next_hop': ['192.168.1.1']},
                                   'conditions': {'match_access_list': 'pbr-sample'}}}},
                            'setrrnh':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit',
                                     'set_next_hop': ['peer-address']},
                                   'conditions': {}}}},
                            'setrrnhv6':
                              {'statements':
                                {'10':
                                  {'actions': 
                                    {'clause': True,
                                     'route_disposition': 'permit'},
                                   'conditions': {}}}},
                            'test':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'clause': True,
                                     'route_disposition': 'permit',
                                     'set_next_hop': ['peer-address'],
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
                                     'set_ext_community_rt_additive': True,
                                     'set_level': 'level-1',
                                     'set_local_pref': 20,
                                     'set_med': 100,
                                     'set_metric_type': 'external',
                                     'set_next_hop': ['10.64.4.4'],
                                     'set_next_hop_v6': ['2001:db8:1::1'],
                                     'set_route_origin': 'igp',
                                     'set_level': 'level-1',
                                     'set_tag': 30},
                                   'conditions': {'match_as_path_list': 'aspathlist1',
                                                  'match_community_list': 'test3',
                                                  'match_ext_community_list': 'testing',
                                                  'match_interface': 'Ethernet2/2',
                                                  'match_med_eq': 20,
                                                  'match_nexthop_in': 'test',
                                                  'match_nexthop_in_v6': 'test2',
                                                  'match_prefix_list': 'test-test',
                                                  'match_prefix_list_v6': 'test-test',
                                                  'match_tag_list': '23 100',
                                                  'match_route_type': 'level-1 '
                                                                      'level-2'}}}}}

    golden_output = {'execute.return_value': '''
route-map BGPPeers, permit, sequence 10 
  Match clauses:
    as-number (as-path-list filter): List1, List2 
    as-number: 64496 64501-64510 
  Set clauses:
route-map bgp-to-rib, permit, sequence 10 
  Match clauses:
    community  (community-list filter): 100 
  Set clauses:
    distance: 10 
route-map eigrp-distance, permit, sequence 10 
  Match clauses:
    ipv6 next-hop prefix-lists: ipv6-nexthop 
  Set clauses:
    distance: 10 
route-map eigrp-filter, permit, sequence 10 
  Match clauses:
    ip next-hop prefix-lists: ipv4-nexthop 
  Set clauses:
route-map foo, permit, sequence 10 
  Match clauses:
    route-type: inter-area 
  Set clauses:
    distance: 150 
route-map foo, permit, sequence 20 
  Match clauses:
    route-type: external 
  Set clauses:
    distance: 200 
route-map isis-distance, permit, sequence 10 
  Match clauses:
    interface: Ethernet1/1 
  Set clauses:
    distance: 10 
route-map isis-filter, permit, sequence 10 
  Match clauses:
    interface: Ethernet1/1 
  Set clauses:
route-map metric-range, permit, sequence 10 
  Match clauses:
    metric: 50 
  Set clauses:
    tag 5 
route-map pbr-sample, permit, sequence 10 
  Match clauses:
    ip address (access-lists): pbr-sample 
  Set clauses:
    ip next-hop 192.168.1.1 
route-map setrrnh, permit, sequence 10 
  Match clauses:
  Set clauses:
    ip next-hop peer-address
route-map setrrnhv6, permit, sequence 10 
  Match clauses:
  Set clauses:
    ipv6 next-hop peer-address
route-map test, permit, sequence 10 
  Match clauses:
    as-path (as-path filter): aspathlist1 
    ip address prefix-lists: test-test 
    ip next-hop prefix-lists: test 
    ipv6 address prefix-lists: test-test 
    ipv6 next-hop prefix-lists: test2 
    interface: Ethernet2/2 
    metric: 20 
    tag: 23 100 
    community  (community-list filter): test3 
    route-type: level-1 level-2 
    extcommunity  (extcommunity-list filter): testing 
  Set clauses:
    ip next-hop 10.64.4.4 
    ipv6 next-hop 2001:db8:1::1 
    tag 30 
    metric 100 
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
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
