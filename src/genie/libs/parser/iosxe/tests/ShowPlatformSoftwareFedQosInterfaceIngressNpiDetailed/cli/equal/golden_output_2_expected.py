expected_output = {
    'classmap': {
        'class-default': {
            'cgid': '0x738310',
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
        'cs1': {
            'cgid': '0x738310',
            'child_classes': 0,
            'class_seq_number': '0x1FFFFF',
            'clid': '0x6A611',
            'filter': {
                'filter_match_ip_dscp': {
                    'value': '0x8',
                },
            },
            'null_bind_count': 1,
            'tccg_ref_count': 1,
        },
        'cs2': {
            'cgid': '0x738310',
            'child_classes': 0,
            'class_seq_number': '0x3FFFFE',
            'clid': '0x6A621',
            'filter': {
                'filter_match_ip_dscp': {
                    'value': '0x10',
                },
            },
            'null_bind_count': 1,
            'tccg_ref_count': 1,
        },
        'mcastv6': {
            'cgid': '0x738310',
            'child_classes': 0,
            'class_seq_number': '0x8003FC',
            'clid': '0x5259A1',
            'null_bind_count': 1,
            'tccg_ref_count': 1,
        },
    },
    'interface': {
        'HundredGigE1/0/5.100': {
            'cgid': '0x738310',
            'filter_state': 'UP TO DATE',
            'no_of_classes': 4,
            'tcg_ref_count': 1,
            'vmr_state': 'UP TO DATE',
        },
    },
    'tcg': {
        'npi_tcg': {
            'child_tcg': 0,
            'config_state': 'VALID',
            'mark_action': 2,
            'no_of_tccg': 4,
            'operational_state': 'IN HARDWARE',
            'parent_info': ['0x0', '0x0', '0'],
            'police_action': 4,
            'queue_action': 0,
        },
        'tccg': {
            '0': {
                'child_cgid': '0x0',
                'class_map_name': 'cs1',
                'clid': '0x6A611',
                'null_bind': True,
            },
            '1': {
                'child_cgid': '0x0',
                'class_map_name': 'cs2',
                'clid': '0x6A621',
                'null_bind': True,
            },
            '2': {
                'action': {
                    '0': {
                        'action_type': 'Marking',
                        'discard_class': 255,
                        'mark_type': 'DSCP',
                        'mark_value': 56,
                        'marking_method': 'Normal',
                        'qos_group': 255,
                        'traffic_class': 6,
                    },
                },
                'child_cgid': '0x0',
                'class_map_name': 'mcastv6',
                'clid': '0x5259A1',
                'null_bind': True,
            },
            '3': {
                'action': {
                    '0': {
                        'action_type': 'Marking',
                        'discard_class': 255,
                        'mark_type': 'INVALID',
                        'mark_value': 0,
                        'marking_method': 'Normal',
                        'qos_group': 255,
                        'traffic_class': 2,
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