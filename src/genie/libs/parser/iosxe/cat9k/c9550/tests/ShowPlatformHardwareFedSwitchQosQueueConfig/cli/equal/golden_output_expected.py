expected_output = {
    'interface': {
        'AppGigabitEthernet2/0/2': {
            'base_voq_id': '20160',
            'base_vsc_ids': ['1408', '1472', '0'],
            'interface_id': '0x4F1',
            'is_empty': 'Yes',
            'profile_oid': {
                '342': {
                    'associated_voq_offsets': ['0', '1', '2', '3', '4', '5', '6', '7'],
                    'cgm_type': 'Unicast',
                    'device_id': '0',
                    'fcn_enabled': 'Disabled',
                    'for_speeds': '10000000000',
                    'hbm_enabled': 'Disabled',
                    'is_reserved': 'Yes',
                    'profile_id': '0x156',
                    'profile_reference_count': '216',
                    'q_block_size': '384',
                    'queue_hw_values': {
                        'red_action': 'Drop',
                        'red_drop_thresholds': [],
                        'red_ema_coefficient': '1.000000',
                    },
                    'queue_user_config': {
                        'q_limit_bytes': '98304',
                        'red_ema_coefficient': '1.000000',
                        'red_flag': {
                            'Green': {
                                'maximum': '98304',
                                'maximum_probability': '0',
                                'minimum': '0',
                            },
                            'Yellow': {
                                'maximum': '0',
                                'maximum_probability': '0',
                                'minimum': '0',
                            },
                        },
                    },
                    'red_enabled': 'Enabled',
                },
            },
            'voq_flush': 'Flush not active',
            'voq_id': '0xEB0',
            'voq_oid': '3760',
            'voq_set_size': '8',
            'voq_state': 'Active',
        },
    },
}
