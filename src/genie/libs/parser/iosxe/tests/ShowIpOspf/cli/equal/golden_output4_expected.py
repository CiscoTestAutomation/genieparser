expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        '1': {
                            'adjacency_stagger': {
                                'initial_number': 300,
                                'maximum_number': 300,
                            },
                            'area_transit': True,
                            'areas': {
                                '0.0.0.0': {
                                    'area_id': '0.0.0.0',
                                    'area_type': 'normal',
                                    'ranges': {
                                    },
                                    'statistics': {
                                        'area_scope_lsa_cksum_sum': '0x04AF1A',
                                        'area_scope_lsa_count': 10,
                                        'area_scope_opaque_lsa_cksum_sum': '0x000000',
                                        'area_scope_opaque_lsa_count': 0,
                                        'dcbitless_lsa_count': 0,
                                        'donotage_lsa_count': 0,
                                        'flood_list_length': 0,
                                        'indication_lsa_count': 0,
                                        'interfaces_count': 4,
                                        'loopback_count': 1,
                                        'spf_last_executed': '22:34:17.568',
                                        'spf_runs_count': 10,
                                    },
                                },
                            },
                            'auto_cost': {
                                'bandwidth_unit': 'mbps',
                                'enable': False,
                                'reference_bandwidth': 100,
                            },
                            'bfd': {
                                'enable': False,
                            },
                            'db_exchange_summary_list_optimization': True,
                            'elapsed_time': '22:35:14.402',
                            'enable': True,
                            'event_log': {
                                'enable': True,
                                'max_events': 1000,
                                'mode': 'cyclic',
                            },
                            'external_flood_list_length': 0,
                            'graceful_restart': {
                                'cisco': {
                                    'enable': False,
                                    'helper_enable': True,
                                    'type': 'cisco',
                                },
                                'ietf': {
                                    'enable': False,
                                    'helper_enable': True,
                                    'type': 'ietf',
                                },
                            },
                            'interface_flood_pacing_timer': 33,
                            'lls': True,
                            'lsa_group_pacing_timer': 240,
                            'nsr': {
                                'enable': False,
                            },
                            'nssa': True,
                            'numbers': {
                                'dc_bitless': 0,
                                'do_not_age': 0,
                                'external_lsa': 0,
                                'external_lsa_checksum': '0x000000',
                                'opaque_as_lsa': 0,
                                'opaque_as_lsa_checksum': '0x000000',
                            },
                            'opqaue_lsa': True,
                            'retransmission_pacing_timer': 66,
                            'router_id': '100.1.1.1',
                            'spf_control': {
                                'incremental_spf': False,
                                'throttle': {
                                    'lsa': {
                                        'arrival': 100,
                                        'hold': 200,
                                        'maximum': 5000,
                                        'start': 50,
                                    },
                                    'spf': {
                                        'hold': 200,
                                        'maximum': 5000,
                                        'start': 50,
                                    },
                                },
                            },
                            'start_time': '00:01:36.589',
                            'stub_router': {
                                'always': {
                                    'always': False,
                                    'external_lsa': False,
                                    'include_stub': False,
                                    'summary_lsa': False,
                                },
                            },
                            'total_areas': 1,
                            'total_areas_transit_capable': 0,
                            'total_normal_areas': 1,
                            'total_nssa_areas': 0,
                            'total_stub_areas': 0,
                        },
                        '2': {
                            'adjacency_stagger': {
                                'initial_number': 300,
                                'maximum_number': 300,
                            },
                            'area_transit': True,
                            'areas': {
                                '0.0.0.0': {
                                    'area_id': '0.0.0.0',
                                    'area_type': 'normal',
                                    'ranges': {
                                    },
                                    'statistics': {
                                        'area_scope_lsa_cksum_sum': '0x04A71C',
                                        'area_scope_lsa_count': 10,
                                        'area_scope_opaque_lsa_cksum_sum': '0x000000',
                                        'area_scope_opaque_lsa_count': 0,
                                        'dcbitless_lsa_count': 0,
                                        'donotage_lsa_count': 0,
                                        'flood_list_length': 0,
                                        'indication_lsa_count': 0,
                                        'interfaces_count': 4,
                                        'loopback_count': 1,
                                        'spf_last_executed': '22:34:18.385',
                                        'spf_runs_count': 9,
                                    },
                                },
                            },
                            'auto_cost': {
                                'bandwidth_unit': 'mbps',
                                'enable': False,
                                'reference_bandwidth': 100,
                            },
                            'bfd': {
                                'enable': False,
                            },
                            'db_exchange_summary_list_optimization': True,
                            'domain_id_type': '0x0005',
                            'domain_id_value': '0.0.0.2',
                            'elapsed_time': '22:35:14.353',
                            'enable': True,
                            'external_flood_list_length': 0,
                            'flags': {
                                'abr': True,
                            },
                            'graceful_restart': {
                                'cisco': {
                                    'enable': False,
                                    'helper_enable': True,
                                    'type': 'cisco',
                                },
                                'ietf': {
                                    'enable': False,
                                    'helper_enable': True,
                                    'type': 'ietf',
                                },
                            },
                            'interface_flood_pacing_timer': 33,
                            'lls': True,
                            'lsa_group_pacing_timer': 240,
                            'nsr': {
                                'enable': False,
                            },
                            'nssa': True,
                            'numbers': {
                                'dc_bitless': 0,
                                'do_not_age': 0,
                                'external_lsa': 0,
                                'external_lsa_checksum': '0x000000',
                                'opaque_as_lsa': 0,
                                'opaque_as_lsa_checksum': '0x000000',
                            },
                            'opqaue_lsa': True,
                            'retransmission_pacing_timer': 66,
                            'router_id': '200.1.1.1',
                            'spf_control': {
                                'incremental_spf': False,
                                'throttle': {
                                    'lsa': {
                                        'arrival': 100,
                                        'hold': 200,
                                        'maximum': 5000,
                                        'start': 50,
                                    },
                                    'spf': {
                                        'hold': 200,
                                        'maximum': 5000,
                                        'start': 50,
                                    },
                                },
                            },
                            'start_time': '00:01:36.638',
                            'stub_router': {
                                'always': {
                                    'always': False,
                                    'external_lsa': False,
                                    'include_stub': False,
                                    'summary_lsa': False,
                                },
                            },
                            'total_areas': 1,
                            'total_areas_transit_capable': 0,
                            'total_normal_areas': 1,
                            'total_nssa_areas': 0,
                            'total_stub_areas': 0,
                        },
                    },
                },
            },
        },
    },
}
