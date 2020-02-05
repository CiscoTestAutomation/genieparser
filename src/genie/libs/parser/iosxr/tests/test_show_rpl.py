############################################################################
# Unitest For Show PRL ROUTE POLICY PARSER
############################################################################

import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxr.show_rpl import ShowRplRoutePolicy

class TestShowRplRoutePolicy(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {'NO-EXPORT': {'statements': {10: {'actions': {'actions': 'pass',
                                               'set_community_list': 'no-export'},
                                   'conditions': {'match_prefix_list': 'NO-EXPORT'}}}},
 'all-pass': {'statements': {1: {'actions': {'actions': 'pass'},
                                 'conditions': {}}}},
 'allpass': {'statements': {10: {'actions': {'actions': 'pass'},
                                 'conditions': {}}}},
 'as-path': {'statements': {10: {'actions': {}, 'conditions': {}}}},
 'aspath': {'statements': {10: {'actions': {'actions': 'pass'},
                                'conditions': {'match_as_path_list': 'test'}},
                           20: {'actions': {'actions': 'drop'},
                                'conditions': {}}}},
 'test': {'statements': {1: {'actions': {}, 'conditions': {}},
                         10: {'actions': {'set_route_origin': 'incomplete'},
                              'conditions': {'match_local_pref_eq': '123'}},
                         20: {'actions': {'set_weight': '44'},
                              'conditions': {'match_med_eq': 100}}}},
 'test-community': {'statements': {10: {'actions': {'set_community': ['100:1',
                                                                      '200:1',
                                                                      '300:1'],
                                                    'set_community_no_advertise': True,
                                                    'set_community_no_export': True},
                                        'conditions': {'match_med_eq': 90}},
                                   20: {'actions': {'set_community': ['111:1',
                                                                      '222:1'],
                                                    'set_community_additive': True,
                                                    'set_community_no_advertise': True,
                                                    'set_ext_community_rt': ['100:1',
                                                                             '200:1'],
                                                    'set_ext_community_rt_additive': True},
                                        'conditions': {'match_local_pref_eq': '30'}}}},
 'test2': {'statements': {10: {'actions': {'actions': 'pass'},
                               'conditions': {'match_med_eq': 100,
                                              'match_origin_eq': 'egp'}},
                          20: {'actions': {'actions': 'pass'},
                               'conditions': {'match_nexthop_in': 'prefix-set1'}},
                          30: {'actions': {'actions': 'pass'},
                               'conditions': {
                                   'match_ext_community_list': ['test'],
                                   'match_local_pref_eq': '130'}}}},
 'test3': {'statements': {10: {'actions': {'actions': 'pass'},
                               'conditions': {}},
                          20: {'actions': {'actions': 'pass'},
                               'conditions': {'match_area_eq': '10.4.1.1',
                                              'match_level_eq': 'level-2'}},
                          30: {'actions': {'actions': 'pass'},
                               'conditions': {'match_as_path_list': 'test',
                                              'match_prefix_list': 'prefix-set1'}},
                          40: {'actions': {'actions': 'pass'},
                               'conditions': {}},
                          50: {'actions': {'set_as_path_prepend': 100,
                                           'set_as_path_prepend_repeat_n': 10,
                                           'set_community': ['100:100'],
                                           'set_community_additive': True,
                                           'set_community_delete': 'test',
                                           'set_community_list': 'test',
                                           'set_community_no_advertise': True,
                                           'set_community_no_export': True,
                                           'set_ext_community_delete': 'test',
                                           'set_ext_community_rt': ['300:1',
                                                                    '300:2'],
                                           'set_ext_community_rt_additive': True,
                                           'set_ext_community_soo': '100:100',
                                           'set_ext_community_soo_additive': True,
                                           'set_level': 'level-1-2',
                                           'set_local_pref': 100,
                                           'set_med': 113,
                                           'set_metric': '100',
                                           'set_metric_type': 'type-2',
                                           'set_next_hop': '10.4.1.1',
                                           'set_ospf_metric': '100',
                                           'set_route_origin': 'egp',
                                           'set_tag': '111'},
                               'conditions': {}}}},
 'testtest': {'statements': {10: {'actions': {'set_local_pref': 120,
                                              'set_med': 111,
                                              'set_metric_type': 'type-1',
                                              'set_next_hop': '192.168.1.1'},
                                  'conditions': {'match_area_eq': '0',
                                                 'match_local_pref_eq': '100',
                                                 'match_med_eq': 100}}}},
 'testtest2': {'statements': {10: {'actions': {'set_community_additive': True,
                                               'set_community_list': 'no-export',
                                               'set_med': 222},
                                   'conditions': {'match_local_pref_eq': '99',
                                                  'match_med_eq': 88}}}}}
    
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
      elseif next-hop in prefix-set1 then
        pass
      elseif local-preference eq 130 and community matches-any test then
        pass
      endif
    end-policy
    !
    route-policy test3
      if extcommunity rt matches-any test then
        pass
      elseif ospf-area is 10.4.1.1 and route-type is level-2 then
        pass
      elseif destination in prefix-set1 and as-path in test then
        pass
      elseif as-path length ge 7 then
        pass
      elseif tag in test then
        set origin egp
        set local-preference 100
        set next-hop 10.4.1.1
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
    !
    route-policy testtest
      if med eq 100 and local-preference eq 100 and ospf-area is 0 then
        set local-preference 120
        set next-hop 192.168.1.1
        set med 111
        set metric-type type-1
      endif
    end-policy
    !
    route-policy test-community
      if med eq 90 then
        set community (100:1, 200:1, 300:1, no-export, no-advertise)
      elseif local-preference eq 30 then
        set community (111:1, 222:1, no-advertise) additive
        set extcommunity rt (100:1, 200:1) additive
      endif
    end-policy
    !
    route-policy testtest2
      if local-preference eq 99 and med eq 88 then
        set community (no-export) additive
        set med 222
      endif
    end-policy
      '''}

    device_output = {'execute.return_value': '''
        route-policy test0
      # Allowing 0.0.0.0 (Default Route) only
      if destination in (0.0.0.0/0) then
        pass
      endif
    end-policy
    !
        route-policy test1
      if destination in Test-test_test0 then
        set spf-priority high
      elseif destination in (0.0.0.0/0 eq 32) then
        set spf-priority medium
      endif
    end-policy
    !
    '''}
    parsed_output = {
        'test0': {
            'statements': {
                10: {
                    'actions': {
                        'actions': 'pass',
                    },
                    'conditions': {
                        'match_prefix_list': '(0.0.0.0/0)',
                    },
                },
            },
        },
        'test1': {
            'statements': {
                10: {
                    'actions': {
                        'set_spf_priority': 'high',
                    },
                    'conditions': {
                        'match_prefix_list': 'Test-test_test0',
                    },
                },
                20: {
                    'actions': {
                        'set_spf_priority': 'medium',
                    },
                    'conditions': {
                        'match_prefix_list': '(0.0.0.0/0 eq 32)',
                    },
                },
            },
        },
    }

    device_output2 = {'execute.return_value': '''
            Mon Oct 21 19:00:38.337 EDT
        Listing for all Route Policy objects
        route-policy INTERNAL-route
          if (community matches-any CMT-TP or community matches-any CMT-OLDTP or community matches-any CMT-SBTP or community matches-any CMT-FP) then
            drop
          else
            pass
          endif
        end-policy
        !
    '''}
    parsed_output2 = {
        'INTERNAL-route': {
            'statements': {
                10: {
                    'actions': {
                        'actions': 'drop',
                    },
                    'conditions': {
                        'match_ext_community_list': ['CMT-TP', 'CMT-OLDTP', 'CMT-SBTP', 'CMT-FP'],
                    },
                },
                20: {
                    'actions': {
                        'actions': 'pass',
                    },
                    'conditions': {
                    },
                },
            },
        },
    }

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

    def test_2(self):
        self.device = Mock(**self.device_output)
        rpl_route_policy_obj = ShowRplRoutePolicy(device=self.device)
        parsed_output = rpl_route_policy_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.parsed_output)

    def test_3(self):
        self.device = Mock(**self.device_output2)
        rpl_route_policy_obj = ShowRplRoutePolicy(device=self.device)
        parsed_output = rpl_route_policy_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.parsed_output2)

if __name__ == '__main__':
    unittest.main()
