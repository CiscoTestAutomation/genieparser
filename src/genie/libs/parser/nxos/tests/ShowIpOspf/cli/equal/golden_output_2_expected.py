

expected_output = {
    'vrf':
        {'default':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'1':
                            {'areas':
                                {'0.0.0.0':
                                    {'area_id': '0.0.0.0',
                                    'area_type': 'normal',
                                    'authentication': 'none',
                                    'existed': '1w5d',
                                    'numbers':
                                        {'active_interfaces': 4,
                                        'interfaces': 6,
                                        'loopback_interfaces': 4,
                                        'passive_interfaces': 0},
                                    'statistics':
                                        {'area_scope_lsa_cksum_sum': '1',
                                        'area_scope_lsa_count': 1,
                                        'spf_last_run_time': 0.000447,
                                        'spf_runs_count': 2}}},
                            'auto_cost':
                                {'bandwidth_unit': 'mbps',
                                'enable': False,
                                'reference_bandwidth': 40000},
                            'enable': False,
                            'discard_route_external': True,
                            'discard_route_internal': True,
                            'graceful_restart':
                                {'ietf':
                                    {'enable': True,
                                    'exist_status': 'none',
                                    'restart_interval': 60,
                                    'state': 'Inactive',
                                    'type': 'ietf'}},
                            'instance': 1,
                            'nsr':
                                {'enable': True},
                            'numbers':
                                {'active_areas':
                                    {'normal': 1,
                                    'nssa': 0,
                                    'stub': 0,
                                    'total': 1},
                                'areas':
                                    {'normal': 1,
                                    'nssa': 0,
                                    'stub': 0,
                                    'total': 1}},
                            'opaque_lsa_enable': True,
                            'preference':
                                {'single_value':
                                    {'all': 110}},
                            'router_id': '10.100.2.2',
                            'single_tos_routes_enable': True,
                            'spf_control':
                                {'paths': 8,
                                'throttle':
                                    {'lsa':
                                        {'group_pacing': 10,
                                        'hold': 5000,
                                        'maximum': 5000,
                                        'minimum': 1000,
                                        'numbers':
                                            {'external_lsas':
                                                {'checksum': '0',
                                                'total': 0},
                                            'opaque_as_lsas':
                                                {'checksum': '0',
                                             'total': 0}},
                                        'start': 0.0},
                                        'spf':
                                            {'hold': 1000,
                                        'maximum': 5000,
                                        'start': 200}}}}}}}}}}
