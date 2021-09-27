

expected_output = {'vrf':
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
                               'dampening_half_life_time': '1',
                               'dampening_reuse_time': '10',
                               'dampening_suppress_time': '30',
                               'dampening_max_suppress_time': '2',
                               'dampening_max_suppress_penalty': '40'}}}}}}}
