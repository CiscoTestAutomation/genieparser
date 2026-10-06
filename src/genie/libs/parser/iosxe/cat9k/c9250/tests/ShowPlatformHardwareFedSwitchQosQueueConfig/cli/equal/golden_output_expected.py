expected_output =  {
    'interface': {
        'HundredGigE2/0/34': {
            'base_voq_id': '28952',
            'base_vsc_ids': ['728', '792', '856', '920', '984', '1048'],
            'interface_id': '0x54C',
            'is_empty': 'Yes',
            'profile_oid': {
                '2117': {
                    'associated_voq_offsets': ['2'],
                    'cgm_type': 'Unicast',
                    'device_id': '0',
                    'for_speeds': '0',
                    'hbm_enabled': 'Disabled',
                    'is_reserved': 'No',
                    'profile_id': '0x845',
                    'profile_reference_count': '1',
                },
                '433': {
                    'associated_voq_offsets': ['0', '1', '3', '4'],
                    'cgm_type': 'Unicast',
                    'device_id': '0',
                    'fcn_enabled': 'Disabled',
                    'for_speeds': '10000000000',
                    'hbm_enabled': 'Enabled',
                    'hgm_block_size': '6144',
                    'is_reserved': 'Yes',
                    'profile_id': '0x1B1',
                    'profile_reference_count': '73',
                    'queue_hw_values': {
                        'hbm_free_thresholds': ['10000', '20000', '40000', '60000', '124992', '250000', '500000', '1000000'],
                        'hbm_voq_age_thresholds': ['1', '2', '3', '4', '5', '6', '7', '8', '10', '12', '16', '24', '32', '64', '128'],
                        'hbm_voq_thresholds': ['96', '992', '2000', '4000', '6000', '8000', '12000', '16000', '24000', '32000', '40000', '48000', '56000', '64000', '64512', '65536', ''],
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
                        'q_limit_hbm_blocks': '1220',
                        'red_ema_coefficient': '1.000000',
                        'red_flag': {
                            'Green': {
                                'maximum_hbm_blocks': '1220',
                                'maximum_probability': '0',
                                'minimun_hbm_blocks': '0',
                            },
                            'Yellow': {
                                'maximum_hbm_blocks': '0',
                                'maximum_probability': '0',
                                'minimun_hbm_blocks': '0',
                            },
                        },
                    },
                    'red_enabled': 'Enabled',
                },
                '606': {
                    'associated_voq_offsets': ['1'],
                    'cgm_type': 'Unicast',
                    'device_id': '0',
                    'fcn_enabled': 'Disabled',
                    'for_speeds': '40000000000',
                    'hbm_enabled': 'Enabled',
                    'hgm_block_size': '6144',
                    'is_reserved': 'Yes',
                    'profile_id': '0x25E',
                    'profile_reference_count': '51',
                    'queue_hw_values': {
                        'hbm_free_thresholds': ['10000', '20000', '40000', '60000', '124992', '250000', '500000', '1000000'],
                        'hbm_voq_age_thresholds': ['1', '2', '3', '4', '5', '6', '7', '8', '10', '12', '16', '24', '32', '64', '128'],
                        'hbm_voq_thresholds': ['96', '992', '2000', '4000', '6000', '8000', '12000', '16000', '24000', '32000', '40000', '48000', '56000', '64000', '64512', '65536', ''],
                        'red_action': 'Drop',
                        'red_drop_thresholds': ['0', '4882', '4882', '4882', '4882', '4882', '4882', '4882', '4882', '4882', '4882', '4882', '4882', '4882', '4882'],
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
                        'q_limit_hbm_blocks': '4882',
                        'red_ema_coefficient': '1.000000',
                        'red_flag': {
                            'Green': {
                                'maximum_hbm_blocks': '4882',
                                'maximum_probability': '0',
                                'minimun_hbm_blocks': '0',
                            },
                            'Yellow': {
                                'maximum_hbm_blocks': '0',
                                'maximum_probability': '0',
                                'minimun_hbm_blocks': '0',
                            },
                        },
                    },
                    'red_enabled': 'Enabled',
                },
            },
            'voq_flush': 'Flush not active',
            'voq_id': '0x842',
            'voq_oid': '2114',
            'voq_set_size': '3',
            'voq_state': 'Active',
        },
    },
}
