

expected_output = {
    'isis': {
        'test2': {
            'address_family': {
                'ipv4_unicast': {
                    'advertise': 'passive_only',
                    'metric': '100000',
                    'metric_style': 'wide',
                    'redistribute': 'static '
                                    'level_2 '
                                    'metric '
                                    '10',
                    'router_id': '10.25.5.6',
                    'segment_routing': {'mpls': 'sr-prefer'},
                    'spf': 'prefix_priority '
                           'medium '
                           'ISIS_PREFIX_PRIORITY_MEDIUM',
                    'spf_interval': {'initial_wait': '50',
                                     'maximum_wait': '5000',
                                     'secondary_wait': '150'}}},
                'interfaces': {
                    'Bundle-Ether15': {
                        'address_family': {
                            'ipv4_unicast': {
                                'fast_reroute': 'per_prefix '
                                                'ti_lfa',
                                'metric': '10'}
                        },
                        'other': ['point-to-point']},
                    'HundredGigE0/0/0/100': {
                        'address_family': {
                            'ipv4_unicast': {
                                'fast_reroute': 'per_prefix '
                                                'ti_lfa',
                                'metric': '10'}
                        },
                        'bfd': {
                            'fast_detect': 'ipv4',
                            'minimum_interval': '250',
                            'multiplier': '3'},
                        'other': ['point-to-point']},
                    'HundredGigE0/0/0/101': {
                        'address_family': {
                            'ipv4_unicast': {
                                'fast_reroute': 'per_prefix '
                                                'ti_lfa',
                                'metric': '10'}},
                        'bfd': {
                            'fast_detect': 'ipv4',
                            'minimum_interval': '250',
                            'multiplier': '3'},
                        'other': ['point-to-point']},
                    'HundredGigE0/0/0/102': {
                        'address_family': {
                            'ipv4_unicast': {
                                'metric': '10'}},
                        'bfd': {
                            'fast_detect': 'ipv4',
                            'minimum_interval': '250',
                            'multiplier': '3'},
                        'other': ['point-to-point']},
                    'HundredGigE0/0/0/103': {
                        'address_family': {
                            'ipv4_unicast': {
                                'fast_reroute': 'per_prefix '
                                                'ti_lfa',
                                'metric': '10'}},
                        'bfd': {'fast_detect': 'ipv4',
                                'minimum_interval': '250',
                                'multiplier': '3'},
                        'other': ['point-to-point']},
                    'HundredGigE0/0/0/104': {
                        'address_family': {
                            'ipv4_unicast': {
                                'metric': '100'}
                        },
                        'bfd': {
                            'fast_detect': 'ipv4',
                            'minimum_interval': '250',
                            'multiplier': '3'},
                        'other': ['point-to-point']},
                    'HundredGigE0/0/0/105': {
                        'address_family': {
                            'ipv4_unicast': {
                                'metric': '100'}
                        },
                        'bfd': {
                            'fast_detect': 'ipv4',
                            'minimum_interval': '250',
                            'multiplier': '3'},
                        'other': ['point-to-point']},
                    'HundredGigE0/0/0/106': {
                        'address_family': {
                            'ipv4_unicast': {
                                'metric': '100'}
                            },
                        'bfd': {'fast_detect': 'ipv4',
                                'minimum_interval': '250',
                                'multiplier': '3'},
                        'other': ['point-to-point']},
                    'HundredGigE0/0/0/107': {
                        'address_family': {
                            'ipv4_unicast': {
                                'metric': '100'}},
                        'bfd': {
                            'fast_detect': 'ipv4',
                            'minimum_interval': '250',
                            'multiplier': '3'},
                        'other': ['point-to-point']},
                    'HundredGigE0/0/0/108': {
                        'address_family': {
                            'ipv4_unicast': {
                                'metric': '200000'}},
                                'bfd': {
                                    'fast_detect': 'ipv4',
                                    'minimum_interval': '250',
                                    'multiplier': '3'},
                                'other': ['point-to-point']},
                    'HundredGigE0/0/0/109': {
                        'address_family': {
                            'ipv4_unicast': {
                                'metric': '200000'}
                        },
                        'bfd': {
                            'fast_detect': 'ipv4',
                            'minimum_interval': '250',
                            'multiplier': '3'},
                        'other': ['point-to-point',
                                  'RP/0/RP0/CPU0:spine1-tatooine#']},
                    'Loopback0': {
                        'address_family': {
                            'ipv4_unicast': {
                                'metric': '10',
                                'prefix_sid': 'index '
                                              '288'}
                        },
                        'other': ['passive']},
                    'TenGigE0/0/0/0/200': {},
                    'TenGigE0/0/0/0/201': {
                        'address_family': {
                            'ipv4_unicast': {
                                'metric': '10'}
                        },
                        'bfd': {
                            'fast_detect': 'ipv4',
                            'minimum_interval': '250',
                            'multiplier': '3'},
                        'other': ['point-to-point']},
                    'TenGigE0/0/0/0/202': {
                        'address_family': {
                            'ipv4_unicast': {
                                'metric': '10'}
                        },
                        'bfd': {'fast_detect': 'ipv4',
                              'minimum_interval': '250',
                              'multiplier': '3'},
                        'other': ['point-to-point']}
                    },
        'is_type': 'level-2-only',
        'log': 'adjacency changes',
        'lsp_gen_interval': {
            'initial_wait': '20',
            'maximum_wait': '5000',
            'secondary_wait': '100'},
        'lsp_refresh_interval': '35000',
        'max_lsp_lifetime': '65535',
        'net': '10.9.3.4.5.6',
        'segment_routing': {},
        'set_overload_bit': 'on-startup 300'}
    }
}
