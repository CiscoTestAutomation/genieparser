expected_output = {
    'FiftyGigE6/0/11': {
        'service_policy': {
            'output1': {
                'policy_name': {
                    'child': {
                        'class_map': {
                            'class-default': {
                                'bytes_output': 0,
                                'match': ['any'],
                                'match_evaluation': 'match-any',
                                'packets': 0,
                                'queue_limit_bytes': 7500000,
                                'total_drops': 0
                                },
                            'tc6': {
                                'match': ['traffic-class ' '6'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'priority_level': 2,
                                'shape_bc_bps': 4000000,
                                'shape_be_bps': 4000000,
                                'shape_cir_bps': 1000000000,
                                'shape_type': 'average',
                                'target_shape_rate': 1000000000
                                },
                            'tc7': {
                                'match': ['traffic-class ' '7'],
                                'match_evaluation': 'match-all',
                                'packets': 0,
                                'priority_level': 1,
                                'shape_bc_bps': 4000000,
                                'shape_be_bps': 4000000,
                                'shape_cir_bps': 1000000000,
                                'shape_type': 'average',
                                'target_shape_rate': 1000000000
                                }
                        },
                        'queue_stats_for_all_priority_classes': {
                            'priority_level': {
                                '1': {
                                    'queueing': True,
                                    'queue_limit_bytes': 96000,
                                    'total_drops': 0,
                                    'bytes_output': 0
                                },
                                '2': {
                                    'queueing': True,
                                    'queue_limit_bytes': 96000,
                                    'total_drops': 0,
                                    'bytes_output': 0
                                }
                            }
                        }
                    }
                }
            },
            'output': {
                'policy_name': {
                    'parent': {
                        'class_map': {
                            'class-default': {
                                'bytes_output': 0,
                                'match': ['any'],
                                'match_evaluation': 'match-any',
                                'packets': 0,
                                'queue_limit_bytes': 7500000,
                                'queueing': True,
                                'shape_bc_bps': 8000000,
                                'shape_be_bps': 8000000,
                                'shape_cir_bps': 2000000000,
                                'shape_type': 'average',
                                'target_shape_rate': 2000000000,
                                'total_drops': 0
                            }
                        }
                    }
                }
            }
        }
    }  
}
