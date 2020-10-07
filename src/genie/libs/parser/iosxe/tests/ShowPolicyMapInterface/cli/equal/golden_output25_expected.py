expected_output = {
    'GigabitEthernet0/0/3.3001': 
        {'service_policy': 
            {'output': 
                {'policy_name': 
                    {'policy1': 
                        {'child_policy_name': 
                            {'policy2': 
                                {'class_map': 
                                    {'class-default': 
                                        {'bandwidth_remaining_percent': 19,
                                        'bytes': 100234922,
                                        'bytes_output': 1437824,
                                        'match': ['any'],
                                        'match_evaluation': 'match-any',
                                        'no_buffer_drops': 0,
                                        'packets': 275144,
                                        'pkts_output': 22466,
                                        'qos_set': 
                                            {'dscp': 
                                                {'default': 
                                                    {'marker_statistics': 'Disabled'}}},
                                        'queue_depth': 0,
                                        'queue_limit_bytes': 312500,
                                        'queueing': True,
                                        'random_detect': 
                                            {'class': 
                                                {'default': 
                                                    {'mark_prob': '1/10',
                                                    'maximum_thresh': '156250',
                                                    'minimum_thresh': '115625',
                                                    'random_drop': '0/0',
                                                    'tail_drop': '0/0',
                                                    'transmitted': '22466/1437824'}},
                                            'exp_weight_constant': '9 (1/512)',
                                            'mean_queue_depth': 64},
                                        'rate':
                                            {'drop_rate_bps': 0,
                                            'interval': 60,
                                            'offered_rate_bps': 0},
                                        'total_drops': 0},
                                    'cm1': 
                                        {'bandwidth_remaining_percent': 1,
                                        'bytes': 262033259,
                                        'bytes_output': 262033337,
                                        'match': ['access-group name accssgroup1'],
                                        'match_evaluation': 'match-any',
                                        'no_buffer_drops': 0,
                                        'packets': 3000453,
                                        'pkts_output': 3000454,
                                        'qos_set': 
                                            {'dscp': 
                                                {'cs6': 
                                                    {'marker_statistics': 'Disabled'}}},
                                        'queue_depth': 0,
                                        'queue_limit_bytes': 525000,
                                        'queueing': True,
                                        'random_detect': 
                                            {'class': 
                                                {'cs6': 
                                                    {'mark_prob': '1/10',
                                                    'maximum_thresh': '262500',
                                                    'minimum_thresh': '225750',
                                                    'random_drop': '0/0',
                                                    'tail_drop': '0/0',
                                                    'transmitted': '3000454/262033337'}},
                                            'exp_weight_constant': '9 (1/512)',
                                            'mean_queue_depth': 94},
                                        'rate': 
                                            {'drop_rate_bps': 0,
                                            'interval': 60,
                                            'offered_rate_bps': 0},
                                        'total_drops': 0},
                                    'cm2': 
                                        {'bandwidth_remaining_percent': 25,
                                        'bytes': 0,
                                        'bytes_output': 0,
                                        'match': ['dscp af41 (34) af42 (36)'],
                                        'match_evaluation': 'match-any',
                                        'no_buffer_drops': 0,
                                        'packets': 0,
                                        'pkts_output': 0,
                                        'qos_set': 
                                            {'dscp': 
                                                {'af41': 
                                                    {'marker_statistics': 'Disabled'}}},
                                        'queue_depth': 0,
                                        'queue_limit_bytes': 312500,
                                        'queueing': True,
                                        'rate': 
                                            {'drop_rate_bps': 0,
                                            'interval': 60,
                                            'offered_rate_bps': 0},
                                        'total_drops': 0},
                                    'cm3': 
                                        {'bandwidth_remaining_percent': 10,
                                        'bytes': 0,
                                        'bytes_output': 0,
                                        'match': ['ip dscp af31 (26) af32 (28)',
                                                  'dscp af31 (26) af32 (28)'],
                                        'match_evaluation': 'match-any',
                                        'no_buffer_drops': 0,
                                        'packets': 0,
                                        'pkts_output': 0,
                                        'qos_set': 
                                            {'dscp': 
                                                {'af31': 
                                                    {'marker_statistics': 'Disabled'}}},
                                        'queue_depth': 0,
                                        'queue_limit_bytes': 312500,
                                        'queueing': True,
                                        'random_detect': 
                                            {'class': 
                                                {'af31': 
                                                    {'mark_prob': '1/10',
                                                    'maximum_thresh': '156250',
                                                    'minimum_thresh': '134375',
                                                    'random_drop': '0/0',
                                                    'tail_drop': '0/0',
                                                    'transmitted': '0/0'}},
                                            'exp_weight_constant': '9 (1/512)',
                                            'mean_queue_depth': 0},
                                        'rate': 
                                            {'drop_rate_bps': 0,
                                            'interval': 60,
                                            'offered_rate_bps': 0},
                                        'total_drops': 0},
                                    'cm4': 
                                        {'bandwidth_remaining_percent': 40,
                                        'bytes': 0,
                                        'bytes_output': 0,
                                        'match': ['ip dscp af21 (18) af22 (20)',
                                                  'dscp af21 (18) af22 (20)'],
                                        'match_evaluation': 'match-any',
                                        'no_buffer_drops': 0,
                                        'packets': 0,
                                        'pkts_output': 0,
                                        'qos_set': 
                                            {'dscp': 
                                                {'af21': 
                                                    {'marker_statistics': 'Disabled'}}},
                                        'queue_depth': 0,
                                        'queue_limit_bytes': 312500,
                                        'queueing': True,
                                        'random_detect': 
                                            {'class': 
                                                {'af21': 
                                                    {'mark_prob': '1/10',
                                                    'maximum_thresh': '156250',
                                                    'minimum_thresh': '134375',
                                                    'random_drop': '0/0',
                                                    'tail_drop': '0/0',
                                                    'transmitted': '0/0'}},
                                            'exp_weight_constant': '9 (1/512)',
                                            'mean_queue_depth': 0},
                                        'rate': 
                                            {'drop_rate_bps': 0,
                                            'interval': 60,
                                            'offered_rate_bps': 0},
                                        'total_drops': 0},
                                    'cm5': 
                                        {'bandwidth_remaining_percent': 5,
                                        'bytes': 0,
                                        'bytes_output': 0,
                                        'match': ['dscp af11 (10) af12 (12)'],
                                        'match_evaluation': 'match-any',
                                        'no_buffer_drops': 0,
                                        'packets': 0,
                                        'pkts_output': 0,
                                        'qos_set': 
                                            {'dscp': 
                                                {'af11': 
                                                    {'marker_statistics': 'Disabled'}}},
                                        'queue_depth': 0,
                                        'queue_limit_bytes': 312500,
                                        'queueing': True,
                                        'random_detect': 
                                            {'class': 
                                                {'af11': 
                                                    {'mark_prob': '1/10',
                                                    'maximum_thresh': '156250',
                                                    'minimum_thresh': '78125',
                                                    'random_drop': '0/0',
                                                    'tail_drop': '0/0',
                                                    'transmitted': '0/0'}},
                                            'exp_weight_constant': '9 (1/512)',
                                            'mean_queue_depth': 0},
                                        'rate': 
                                            {'drop_rate_bps': 0,
                                            'interval': 60,
                                            'offered_rate_bps': 0},
                                         'total_drops': 0}}}},
                        'class_map': 
                            {'class-default': 
                                {'bandwidth': 'remaining ratio 1',
                                'bytes': 362268259,
                                'bytes_output': 263471161,
                                'match': ['any'],
                                'match_evaluation': 'match-any',
                                'no_buffer_drops': 0,
                                'packets': 3275598,
                                'pkts_output': 3022920,
                                'queue_depth': 0,
                                'queue_limit_packets': '208',
                                'queueing': True,
                                'rate': 
                                    {'drop_rate_bps': 0,
                                'interval': 60,
                                'offered_rate_bps': 0},
                                'shape_bc_bps': 200000,
                                'shape_be_bps': 200000,
                                'shape_cir_bps': 50000000,
                                'shape_type': 'average',
                                'target_shape_rate': 50000000,
                                'total_drops': 0}}}}}}}}

