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
                        'discard_class': 255,
                        'marking_method': 'Tablemap',
                        'qos_group': 255,
                        'traffic_class': 255,
                        'default_behavior': 'Copy',
                        'default_value': 0,
                        'map': {
                            'dscp_to_dscp': {
                                16: 32,
                                32: 24,
                                40: 24,
                                48: 56,
                                8: 16
                            }
                        },
                        'table_id': '0x3B8D',
                        'table_name': 't1'
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