expected_output = {
    'policy_name': {
        'llq': {
            'class_map': {
                'tc2': {
                    'average_rate_traffic_shaping': True,
                    'cir_bps': 1000000000,
                    'priority_level': 6,
                },
                'tc3': {
                    'average_rate_traffic_shaping': True,
                    'cir_bps': 100000000,
                    'priority_level': 5,
                },
                'tc4': {
                    'average_rate_traffic_shaping': True,
                    'cir_bps': 100000000,
                    'priority_level': 4,
                },
                'tc5': {
                    'average_rate_traffic_shaping': True,
                    'cir_bps': 150000000,
                    'priority_level': 3,
                },
                'tc6': {
                    'average_rate_traffic_shaping': True,
                    'cir_bps': 100000000,
                    'priority_level': 2,
                },
                'tc7': {
                    'average_rate_traffic_shaping': True,
                    'cir_percent': 2,
                    'priority_level': 1,
                },
            },
        },
    },
}