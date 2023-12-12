expected_output = {
    'routing_process': {
        '200': {
            'routing_process': 200,
            'protocol': 'ospfv3',
            'router_id': '1.100.1.1',
            'role': 'Primary Active',
            'nsr_status': 'enabled',
            'flags': {
                'asbr': True
            },
            'spf_schedule_delay': '50 msecs',
            'spf_minimum_hold_time': '200 msecs',
            'spf_maximum_wait_time': '5000 msecs',
            'lsa_throttle_delay': '50 msecs',
            'lsa_throttle_minimum_hold_time': '200 msecs',
            'lsa_throttle_maximum_wait_time': '5000 msecs',
            'maximum_configured_interfaces': 1024,
            'external_lsa': 6,
            'external_lsa_checksum': '0x0285c9',
            'router_areas': {
                'total_router_areas': 1,
                'normal_area': 1,
                'stub_area': 0,
                'nssa_area': 0
            },
            'snmp_trap': 'enabled',
            'areas': {
                '0.0.0.0': {
                    'area_id': '0.0.0.0',
                    'area_type': 'normal',
                    'statistics': {
                        'interfaces_count': 1,
                        'spf_runs_count': 3,
                        'area_scope_lsa_count': 5,
                        'area_scope_lsa_cksum_sum': '0x01ec6e',
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
