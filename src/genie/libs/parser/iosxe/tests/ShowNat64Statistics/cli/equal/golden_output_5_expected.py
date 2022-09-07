expected_output = {
    'nat64_stats': {
        'interface_statistics': {
            'FortyGigabitEthernet2/0/7.10': {
                'stateful_prefix': {
                    '2800:1503:2000:1:1::/96': {
                        'packets_dropped': 807260,
                        'packets_translated': {
                            'v4_to_v6': 16,
                            'v6_to_v4': 722725
                        }
                    },
                    'ipv4': 'configured',
                    'ipv6': 'not configured'
                }
            }
        }
    }
}