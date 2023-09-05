expected_output = {
    'classmap': {
        'aclv4': {
            'cgid': '0x738310',
            'child_classes': 0,
            'class_seq_number': '0x5FFFFD',
            'clid': '0xC16261',
            'null_bind_count': 1,
            'tccg_ref_count': 1,
        },
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
        'cs5': {
            'cgid': '0x738310',
            'child_classes': 0,
            'class_seq_number': '0x3FFFFE',
            'clid': '0x6A651',
            'filter': {
                'filter_match_ip_dscp': {
                    'value': '0x28',
                },
            },
            'null_bind_count': 1,
            'tccg_ref_count': 1,
        },
    },
    'interface': {
        'Port-channel10': {
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
            'mark_action': 0,
            'no_of_tccg': 4,
            'operational_state': 'IN HARDWARE',
            'parent_info': ['0x0', '0x0', '0'],
            'police_action': 3,
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
                'class_map_name': 'cs5',
                'clid': '0x6A651',
                'null_bind': True,
            },
            '2': {
                'child_cgid': '0x0',
                'class_map_name': 'aclv4',
                'clid': '0xC16261',
                'null_bind': True,
            },
            '3': {
                'child_cgid': '0x0',
                'class_map_name': 'class-default',
                'clid': '0x639',
                'null_bind': True,
            },
        },
    },
}