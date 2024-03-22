expected_output = {
    'routing_process': {
        '200': {
            'routing_process': 200,
            'protocol': 'ospf',
            'router_id': '100.1.1.200',
            'role': 'Primary Active',
            'nsr_status': 'enabled',
            'single_tos_route': True,
            'opqaue_lsa': True,
            'flags': {
                'asbr': True
            },
            'spf_schedule_delay': '50 msecs',
            'spf_minimum_hold_time': '200 msecs',
            'spf_maximum_wait_time': '5000 msecs',
            'lsa_throttle_delay': '50 msecs',
            'lsa_throttle_minimum_hold_time': '200 msecs',
            'lsa_throttle_maximum_wait_time': '5000 msecs',
            'minimum_lsa_interval': '200 msecs',
            'minimum_lsa_arrival': '100 msecs',
            'lsa_refresh_interval': '1800 seconds',
            'flood_pacing_interval': '33 msecs',
            'retransmission_pacing_interval': '66 msecs',
            'maximum_configured_interfaces': 1024,
            'external_lsa': 1,
            'external_lsa_checksum': '0x00e9c8',
            'opaque_as_lsa': 0,
            'opaque_as_lsa_checksum': '00000000',
            'dc_bitless': 0,
            'do_not_age': 0,
            'router_areas': {
                'total_router_areas': 2,
                'normal_area': 2,
                'stub_area': 0,
                'nssa_area': 0
            },
            'adjacency_stagger': {
                'disable': False,
                'initial_number': 2,
                'maximum_number': 64,
                'nbrs_forming': 0,
                'nbrs_full': 0,
            },
            'microloop_avoidance': {
                'delay_time': 5000,
                'state': 'Enabled',
                'status': 'not active',
                'type': 'Local (Protected)',
            },
            'segment_routing_global_block_default': '16000-23999',
            'segment_routing_global_block_status': 'not allocated',
            'segment_routing_local_block': '15000-15999',
            'segment_routing_local_block_status': 'allocated',
            'external_flood_list_length': 0,
            'nsf_status': 'enabled',
            'snmp_trap': 'enabled',
            'strict_spf_capability': 'enabled',
            'areas': {
                '0.0.0.0': {
                    'area_id': '0.0.0.0',
                    'area_type': 'normal',
                    'inactive': True,
                    'statistics': {
                        'interfaces_count': 0,
                        'spf_runs_count': 1,
                        'area_scope_lsa_count': 0,
                        'area_scope_lsa_cksum_sum': '00000000',
                        'area_scope_opaque_lsa_count': 0,
                        'area_scope_opaque_lsa_cksum_sum': '00000000',
                        'dcbitless_lsa_count': 0,
                        'indication_lsa_count': 0,
                        'donotage_lsa_count': 0,
                        'flood_list_length': 0
                    }
                },
                '0.0.0.200': {
                    'area_id': '0.0.0.200',
                    'area_type': 'normal',
                    'statistics': {
                        'interfaces_count': 1,
                        'spf_runs_count': 2,
                        'area_scope_lsa_count': 1,
                        'area_scope_lsa_cksum_sum': '0x0028d3',
                        'area_scope_opaque_lsa_count': 0,
                        'area_scope_opaque_lsa_cksum_sum': '00000000',
                        'dcbitless_lsa_count': 0,
                        'indication_lsa_count': 0,
                        'donotage_lsa_count': 0,
                        'flood_list_length': 0
                    }
                }
            }
        }
    }
}
