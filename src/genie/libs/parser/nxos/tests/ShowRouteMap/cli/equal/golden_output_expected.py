

expected_output = {'BGPPeers':
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
