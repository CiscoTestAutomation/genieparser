expected_output = {
    'nat64_stats': {
        'active_sessions': 0,
        'active_translations': {
            'dynamic': 0,
            'extended': 0,
            'static': 1,
            'total_translations': 1
        },
        'expired_sessions': 0,
        'global_statistics': {
            'prefix': {
                '2002:1::/96': {
                    'packets_dropped': 0,
                    'packets_translated': {
                        'v4_to_v6': 0,
                        'v6_to_v4': 0
                    },
                    'prefix_vrf_name': 'nat64_vrf'
                },
                '64:FF9B::/96': {
                    'packets_dropped': 0,
                    'packets_translated': {
                        'v4_to_v6': 0,
                        'v6_to_v4': 0
                    }
                }
            }
        },
        'hits_misses': {
            'hit_pkts': 0, 
            'miss_pkts': 0
        },
        'nat64_enabled_interfaces': 2
    }
}