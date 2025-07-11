expected_output =  {
    'interface': {
        'HundredGigE1/0/5': {
            'base_voq_id': '52576',
            'base_vsc_ids': ['352', '416', '480', '544', '608', '672'],
            'interface_id': '0x40A',
            'is_empty': 'Yes',
            'profile_oid': {
                '424': {
                    'associated_voq_offsets': ['0', '1', '2', '3', '4', '5', '6', '7'],
                    'cgm_type': 'Unicast',
                    'device_id': '0',
                    'fcn_enabled': 'Disabled',
                    'for_speeds': '10000000000',
                    'hbm_enabled': 'Enabled',
                    'hgm_block_size': '6144',
                    'is_reserved': 'Yes',
                    'profile_id': '0x1A8',
                    'profile_reference_count': '197',
                    'queue_hw_values': {
                        'hbm_free_thresholds': ['10000', '20000', '40000', '60000', '124992', '250000', '500000', '1000000'],
                        'hbm_voq_age_thresholds': ['1', '2', '3', '4', '5', '6', '7', '8', '10', '12', '16', '24', '32', '64', '128'],
                        'red_action': 'Drop',
                        'red_drop_thresholds': ['0', '1220', '1220', '1220', '1220', '1220', '1220', '1220', '1220', '1220', '1220', '1220', '1220', '1220', '1220'],
                        'red_flag': {
                            'Green': {
                                'red_drop_probabilities': ['0.000000', '0.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000'],
                            },
                            'Yellow': {
                                'red_drop_probabilities': ['0.000000', '0.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000', '1.000000'],
                            },
                        },
                    },
                    'queue_user_config': {
                        'red_ema_coefficient': '1.000000',
                        'red_flag': {
                            'Green': {
                                'maximum_probability': '0',
                            },
                            'Yellow': {
                                'maximum_probability': '0',
                            },
                        },
                    },
                    'red_enabled': 'Enabled',
                },
            },
            'voq_flush': 'Flush not active',
            'voq_id': '0x60A',
            'voq_oid': '1546',
            'voq_set_size': '8',
            'voq_state': 'Active',
        },
    },
}