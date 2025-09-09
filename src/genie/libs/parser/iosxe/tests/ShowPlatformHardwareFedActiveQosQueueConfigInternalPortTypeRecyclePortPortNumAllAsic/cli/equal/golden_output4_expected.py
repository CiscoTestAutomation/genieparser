expected_output = {
    'voq_details': {
        'Recircport/1': {
            'base_voq_id': 256,
            'base_vsc_ids': [128, 208, 288],
            'interface': 'Recircport/1',
            'interface_hex': '0x1',
            'is_empty': 'Yes',
            'voq_flush': 'Flush not active',
            'voq_oid': 285,
            'voq_oid_hex': '0x11D',
            'voq_profile_details': {
                'associated_voq_offsets': [0, 1, 2, 3, 4, 5, 6, 7],
                'cgm_type': 'Unicast',
                'device_id': 0,
                'fcn_enabled': 'Disabled',
                'for_speeds': 400000000000,
                'hbm_enabled': 'Disabled',
                'is_reserved': 'Yes',
                'profile_oid': 284,
                'profile_oid_hex': '0x11C',
                'profile_reference_count': 48,
                'q_block_size': 384,
                'queue_hw_values': {
                    'red_action': 'Drop',
                    'red_drop_thresholds': '',
                    'red_ema_coefficient': 1.0
                },
                'queue_user_config': {
                    'q_limit_bytes': 983040,
                    'red_ema_coefficient': 1.0,
                    'red_green': {
                        'minimum': 0,
                        'maximum': 983040,
                        'maximum_probability': 0
                    },
                    'red_yellow': {
                        'minimum': 0,
                        'maximum': 0,
                        'maximum_probability': 0
                    }
                },
                'red_enabled': 'Enabled'
            },
            'voq_set_size': 8,
            'voq_state': 'Active'
        }
    }
}

