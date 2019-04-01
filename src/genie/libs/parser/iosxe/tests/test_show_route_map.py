import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.show_route_map import ShowRouteMapAll


class test_show_route_map(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {'test':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'route_disposition': 'permit',
                                     'set_next_hop_self': False,
                                    'set_next_hop_v6': ['2001:DB8:1::1',
                                                        '2001:DB8:2::1'],
                                     'set_tag': '10'},
                                   'conditions':
                                    {'match_interface': 'GigabitEthernet1',
                                     'match_nexthop_in_v6': ['test'],
                                    }}}},
                            'test2':
                              {'statements':
                                {'10':
                                  {'actions':
                                    {'route_disposition': 'permit',
                                     'set_community': '6553700',
                                     'set_community_delete': 'test',
                                     'set_ext_community_rt': ['100:10',
                                                             '100:100',
                                                             '200:200'],
                                     'set_ext_community_rt_additive': True,
                                     'set_ext_community_soo': '100:10',
                                     'set_ext_community_vpn': '100:100',
                                     'set_local_pref': 111,
                                     'set_metric_type': 'external',
                                     'set_metric': 100,
                                     'set_next_hop_self': True,
                                     'set_next_hop': ['10.4.1.1', '10.16.2.2'],
                                     'set_next_hop_v6': ['2001:DB8:1::1', '2001:DB8:2::1'],
                                     'set_route_origin': 'incomplete',
                                     'set_tag': '10'},
                                   'conditions':
                                    {'match_med_eq': 100}
                                  },
                                 '20':
                                  {'actions':
                                    {'route_disposition': 'permit',
                                     'set_metric': -20,
                                     'set_ospf_metric_type': 'type-1',
                                     'set_next_hop': ['10.36.3.3'],
                                     'set_next_hop_self': False,
                                     'set_next_hop_v6': ['2001:DB8:3::1'],
                                     'set_route_origin': 'igp'},
                                   'conditions':
                                    {'match_as_path_list': '100',
                                     'match_community_list': 'test',
                                     'match_ext_community_list': 'test',
                                     'match_prefix_list': 'test test2',
                                     'match_level_eq': 'level-1-2',
                                     'match_interface': 'GigabitEthernet1 GigabitEthernet2'}
                                  }
                                }
                              }
                            }

    golden_output = {'execute.return_value': '''
      STATIC routemaps
      route-map test, permit, sequence 10
        Match clauses:
          interface GigabitEthernet1 
          ipv6 next-hop test
        Set clauses:
          tag 10 
          ipv6 next-hop 2001:DB8:1::1 2001:DB8:2::1
        Policy routing matches: 0 packets, 0 bytes
      route-map test2, permit, sequence 10
        Match clauses:
          metric  100 
        Set clauses:
          metric 100
          metric-type external
          tag 10 
          ip next-hop self
          local-preference 111
          comm-list test delete
          community 6553700
          extended community SoO:100:10
          extended community RT:300:300 RT:400:400
          extended community RT:100:10 RT:100:100 RT:200:200 additive
          extended community VD:100:100
          origin incomplete
          ip next-hop 10.4.1.1 10.16.2.2
           ipv6 next-hop 2001:DB8:1::1 2001:DB8:2::1
        Policy routing matches: 0 packets, 0 bytes
      route-map test2, permit, sequence 20
        Match clauses:
          ip address prefix-lists: test test2 
          route-type level-1 level-2 
          interface GigabitEthernet1 GigabitEthernet2 
          as-path (as-path filter): 100 
          community (community-list filter): test 
          extcommunity (extcommunity-list filter):test 
        Set clauses:
          metric -20
          metric-type type-1
          origin igp
          ip next-hop 10.36.3.3
           ipv6 next-hop 2001:DB8:3::1
        Policy routing matches: 0 packets, 0 bytes
      DYNAMIC routemaps
      Current active dynamic routemaps = 0
      '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        route_map_obj = ShowRouteMapAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = route_map_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        route_map_obj = ShowRouteMapAll(device=self.device)
        parsed_output = route_map_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
