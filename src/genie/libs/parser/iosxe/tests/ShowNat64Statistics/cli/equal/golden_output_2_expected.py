expected_output = {
    'nat64_stats': {
        'dynamic_mapping_statistics': {
            'access_list': {
                'acl_1': {
                    'pool': {
                        'n64_pool': {
                            'allocated': 0,
                            'end_ip': '135.0.0.100',
                            'nat64_pool_name': 'n64_pool',
                            'packet_count': 0,
                            'percent': 0,
                            'start_ip': '135.0.0.1',
                            'total_address': 100
                        }
                    },
                    'refcount': 0
                },
                'acl_2': {
                    'pool': {
                        'n64_pool2': {
                            'allocated': 0,
                            'end_ip': '136.0.0.100',
                            'nat64_pool_name': 'n64_pool2',
                            'packet_count': 0,
                            'percent': 0,
                            'start_ip': '136.0.0.1',
                            'total_address': 100
                        }
                    },
                    'refcount': 0
                }
            }
        }
    }
}