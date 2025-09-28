expected_output = {
    'voq_details': {
        'Recircport/1': {
            'base_voq_id': 264,
            'base_vsc_ids': [136, 216, 296],
            'interface': 'Recircport/1',
            'interface_hex': '0x1',
            'is_empty': 'Yes',
            'voq_flush': 'Flush not active',
            'voq_oid': 353,
            'voq_oid_hex': '0x161',
            'voq_profile_details': {
                'associated_voq_offsets': [0, 1, 2, 3, 4, 5, 6, 7],
                'cgm_type': 'Unicast',
                'device_id': 3,
                'fcn_enabled': 'Disabled',
                'for_speeds': 10000000000,
                'hbm_enabled': 'Disabled',
                'is_reserved': 'Yes',
                'profile_oid': 352,
                'profile_oid_hex': '0x160',
                'profile_reference_count': 172,
                'q_block_size': 384,
                'queue_hw_values': {
                    'red_action': 'Drop',
                    'red_drop_thresholds': '',
                    'red_ema_coefficient': 1.0
                },
                'queue_user_config': {
                    'q_limit_bytes': 98304,
                    'red_ema_coefficient': 1.0,
                    'red_green': {
                        'minimum': 0,
                        'maximum': 98304,
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
