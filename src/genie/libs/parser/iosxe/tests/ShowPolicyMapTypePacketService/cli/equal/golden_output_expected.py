expected_output = {
    "packet_services": {
        'epc_policy_match_any_IPV6_test': {
            'classes': {
                'epc_class_match_any_IPV6_test': {
                    'capture': {
                        'name': 'match_any_IPV6_test',
                        'limit': 1000,
                        'ip_type': 'ipv6',
                    },
                },
            },
        },
        'epc_policy_match_any_MAC_test1': {
            'classes': {
                'epc_class_match_any_MAC_test1': {
                    'capture': {
                        'name': 'match_any_MAC_test1',
                        'limit': 1000,
                        'ip_type': 'mac',
                    },
                },
            },
        },
        'epc_policy_match_any_IPV4_test': {
            'classes': {
                'epc_class_match_any_IPV4_test': {
                    'capture': {
                        'name': 'match_any_IPV4_test',
                        'limit': 1000,
                        'ip_type': 'ipv4',
                    },
                },
            },
        },
    }
}