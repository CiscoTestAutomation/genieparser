expected_output = {
    'classmap': {
        'class-default': {
            'cgid': '0x92B890',
            'child_classes': 0,
            'class_seq_number': '0xFFFFFFFF',
            'clid': '0x639',
            'filter': {
                'filter_match_any': {
                    'value': '0x0',
                },
            },
            'null_bind_count': 1,
            'tccg_ref_count': 1,
        },
    },
    'interface': {
        'HundredGigE1/0/3': {
            'cgid': '0x92B890',
            'filter_state': 'UP TO DATE',
            'no_of_classes': 1,
            'tcg_ref_count': 1,
            'vmr_state': 'DIRTY',
        },
    },
    'tcg': {
        'npi_tcg': {
            'child_tcg': 0,
            'config_state': 'VALID',
            'mark_action': 1,
            'no_of_tccg': 1,
            'operational_state': 'IN HARDWARE',
            'parent_info': ['0x0', '0x0', '0'],
            'police_action': 1,
            'queue_action': 0,
        },
        'tccg': {
            '0': {
                'action': {
                    '0': {
                        'action_type': 'Marking',
                        'default_behavior': 'Copy',
                        'default_value': 0,
                        'discard_class': 255,
                        'map': {
                            'l2_cos_to_traffic_class': {
                                1: 7,
                                2: 6,
                                3: 5,
                                4: 4,
                                5: 2,
                            },
                        },
                        'marking_method': 'Tablemap',
                        'qos_group': 255,
                        'table_id': '0x3B8D',
                        'table_name': 't1',
                        'traffic_class': 255,
                    },
                },
                'child_cgid': '0x0',
                'class_map_name': 'class-default',
                'clid': '0x639',
                'null_bind': True,
            },
        },
    },
}