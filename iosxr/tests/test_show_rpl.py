import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError

from parser.iosxr.show_rpl import ShowRplRoutePolicy

class test_show_rpl_route_policy(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {'NO-EXPORT': {'statements': {10: {'actions': {'actions': 'pass',
                                               'set_community': 'no-export',
                                               'set_community_additive': True},
                                   'conditions': {}}}},
 'all-pass': {'statements': {'1': {'actions': {'actions': 'pass'},
                                   'conditions': {}}}},
 'allpass': {'statements': {10: {'actions': {'actions': 'pass'},
                                 'conditions': {}}}},
 'as-path': {'statements': {10: {'actions': {}, 'conditions': {}}}},
 'aspath': {'statements': {10: {'actions': {'actions': 'pass'},
                                'conditions': {'match_as_path_list': 'test '}},
                           20: {'actions': {'actions': 'drop'},
                                'conditions': {}}}},
 'test': {'statements': {10: {'actions': {'set_route_origin': 'incomplete'},
                              'conditions': {'match_community_list': 'None',
                                             'match_local_pref_eq': '123'}},
                         20: {'actions': {'set_tag': 'None',
                                          'set_weight': '44'},
                              'conditions': {'match_med_eq': 100,
                                             'match_origin_eq': 'None'}},
                         '1': {'actions': {}, 'conditions': {}}}},
 'test2': {'statements': {10: {'actions': {'actions': 'pass'},
                               'conditions': {'match_med_eq': 100,
                                              'match_origin_eq': 'egp'}},
                          20: {'actions': {'actions': 'pass'},
                               'conditions': {'match_nexthop_in': 'test6 ',
                                              'match_prefix_list': 'prefix-set1 '}},
                          30: {'actions': {'actions': 'pass'},
                               'conditions': {'match_community_list': 'test ',
                                              'match_local_pref_eq': '130'}}}},
 'test3': {'statements': {10: {'actions': {'actions': 'pass'},
                               'conditions': {}},
                          20: {'actions': {'actions': 'pass'},
                               'conditions': {'match_area_eq': '1.1.1.1',
                                              'match_level_eq': 'level-1 '
                                                                ', '
                                                                'level-2 '}},
                          30: {'actions': {'actions': 'pass'},
                               'conditions': {}},
                          40: {'actions': {'actions': 'pass'},
                               'conditions': {'match_as_path_length': 7,
                                              'match_as_path_length_oper': 'ge'}},
                          50: {'actions': {'set_as_path_prepend': 100,
                                           'set_as_path_prepend_repeat_n': 10,
                                           'set_community': '100:100',
                                           'set_community_additive': True,
                                           'set_community_delete': 'test',
                                           'set_community_no_advertise': True,
                                           'set_community_no_export': True,
                                           'set_ext_community_delete': 'test',
                                           'set_ext_community_rt': '300:1, '
                                                                   '300:2',
                                           'set_ext_community_rt_additive': True,
                                           'set_ext_community_soo': '100:100',
                                           'set_ext_community_soo_additive': True,
                                           'set_level': 'level-1-2',
                                           'set_local_pref': 100,
                                           'set_med': '113',
                                           'set_metric': '100',
                                           'set_metric_type': 'type-2',
                                           'set_next_hop': 'None',
                                           'set_next_hop_self': True,
                                           'set_ospf_metric': '100',
                                           'set_route_origin': 'egp',
                                           'set_tag': '111',
                                           'set_weight': 'None'},
                               'conditions': {}}}}}

    
    golden_output = {'execute.return_value': '''
        Listing for all Route Policy objects

    route-policy test
      if destination in prefix-set1 and community matches-any cs1 then
        set med 1
        set community 12:34 additive
        #1
      endif
    end-policy
    !
    route-policy test
      if local-preference eq 123 then
        set origin incomplete
      elseif med eq 100 then
        set weight 44
      endif
    end-policy
    !
    route-policy test2
      if origin is egp and med eq 100 then
        pass
      elseif next-hop in prefix-set1 and next-hop in test6 then
        pass
      elseif local-preference eq 130 and community matches-any test then
        pass
      endif
    end-policy
    !
    route-policy test3
      if extcommunity rt matches-any test then
        pass
      elseif ospf-area is 1.1.1.1 and route-type is level-1 and route-type is level-2 then
        pass
      elseif destination in prefix-set1 and as-path in test then
        pass
      elseif as-path length ge 7 then
        pass
      elseif tag in test then
        set origin egp
        set local-preference 100
        set next-hop 1.1.1.1
        set next-hop self
        set med 113
        prepend as-path 100 10
        set community test
        set community test additive
        set community (100:100, no-export, no-advertise) additive
        delete community in test
        set extcommunity rt (100:100, 200:200) additive
        set extcommunity soo (100:100) additive
        set extcommunity rt (300:1, 300:2) additive
        delete extcommunity rt in test
        set level level-1
        set level level-2
        set level level-1-2
        set metric-type internal
        set metric-type external
        set isis-metric 100
        set metric-type type-1
        set metric-type type-2
        set ospf-metric 100
        set tag 111
      endif
    end-policy
    !
    route-policy aspath
      if as-path in test then
        pass
      endif
      if as-path in test then
        pass
      else
        drop
      endif
    end-policy
    !
    route-policy allpass
      pass
    end-policy
    !
    route-policy as-path
    end-policy
    !
    route-policy all-pass
      #1
      pass
    end-policy
    !
    route-policy NO-EXPORT
      if destination in NO-EXPORT then
        set community (no-export)
        pass
      endif
    end-policy
      '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        rpl_route_policy_obj = ShowRplRoutePolicy(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = rpl_route_policy_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        rpl_route_policy_obj = ShowRplRoutePolicy(device=self.device)
        parsed_output = rpl_route_policy_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
