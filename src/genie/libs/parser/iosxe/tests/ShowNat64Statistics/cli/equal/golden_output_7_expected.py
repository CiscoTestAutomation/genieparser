expected_output = {
    'nat64_stats': {
        'interface_statistics': {
            'GigabitEthernet0/0/4': {
                'ipv4': 'not configured',
                'ipv6': 'configured',
                'packets_translated': {
                    'ipv4_to_ipv6': {
                        'stateless': 0,
                        'stateful': 0,
                        'nat46': 0,
                        'map_t': 0,
                        'map_e': 0
                    },
                    'ipv6_to_ipv4': {
                        'stateless': 0,
                        'stateful': 0,
                        'nat46': 0,
                        'map_t': 0,
                        'map_e': 0
                    }
                },
                'packets_dropped': 539
            }
        }
    }
}