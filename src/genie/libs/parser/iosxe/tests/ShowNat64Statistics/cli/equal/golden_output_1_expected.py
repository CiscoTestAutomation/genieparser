expected_output = {
    'nat64_stats': {
        'global_statistics': {
            'prefix': {
                '1001::/96': {
                    'packets_dropped': 0,
                    'packets_translated': {
                        'v4_to_v6': 0,
                        'v6_to_v4': 14
                    }
                },
                '64:FF9B::/64': {
                    'packets_dropped': 0,
                    'packets_translated': {
                        'v4_to_v6': 10,
                        'v6_to_v4': 20
                    }
                },
                '64:FF9B::/96': {
                    'packets_dropped': 0,
                    'packets_translated': {
                        'v4_to_v6': 0,
                        'v6_to_v4': 0
                    }
                }
            }
        }
    }
}