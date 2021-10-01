

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        '1': {
                            'areas': {
                                '0.0.0.0': {
                                    'area_id': '0.0.0.0',
                                    'area_type': 'normal',
                                    'existed': '2d05h',
                                    'authentication': 'Message-digest',
                                    'numbers': {
                                        'active_interfaces': 3,
                                        'interfaces': 4,
                                        'loopback_interfaces': 1,
                                        'passive_interfaces': 0
                                    },
                                    'statistics': {
                                        'area_scope_lsa_cksum_sum': '35',
                                        'area_scope_lsa_count': 35,
                                        'spf_last_run_time': 0.002091,
                                        'spf_runs_count': 64
                                    }
                                }
                            },
                            'auto_cost': {
                                'bandwidth_unit': 'mbps',
                                'enable': False,
                                'reference_bandwidth': 40000
                            },
                            'discard_route_external': True,
                            'discard_route_internal': True,
                            'enable': True,
                            'graceful_restart': {
                                'ietf': {
                                    'enable': True,
                                    'exist_status': 'none',
                                    'restart_interval': 60,
                                    'state': 'Inactive',
                                    'type': 'ietf'
                                }
                            },
                            'instance': 1,
                            'nsr': {
                                'enable': True
                            },
                            'numbers': {
                                'active_areas': {
                                    'normal': 1,
                                    'nssa': 0,
                                    'stub': 0,
                                    'total': 1
                                },
                                'areas': {
                                    'normal': 1,
                                    'nssa': 0,
                                    'stub': 0,
                                    'total': 1
                                }
                            },
                            'opaque_lsa_enable': True,
                            'preference': {
                                'single_value': {
                                    'all': 110
                                }
                            },
                            'router_id': '10.1.0.105',
                            'single_tos_routes_enable': True,
                            'spf_control': {
                                'paths': 8,
                                'throttle': {
                                    'lsa': {
                                        'group_pacing': 10,
                                        'hold': 50,
                                        'maximum': 500,
                                        'minimum': 50,
                                        'numbers': {
                                            'external_lsas': {
                                                'checksum': '0',
                                                'total': 0
                                            },
                                            'opaque_as_lsas': {
                                                'checksum': '0',
                                                'total': 0
                                            }
                                        },
                                        'start': 20
                                    },
                                    'spf': {
                                        'hold': 50,
                                        'maximum': 500,
                                        'start': 20
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
