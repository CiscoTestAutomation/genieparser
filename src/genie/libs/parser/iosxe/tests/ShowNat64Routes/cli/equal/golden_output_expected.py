expected_output = {
    'nat64_routes': {
        '27.1.1.10/32': {
            'ipv4_prefix': '27.1.1.10/32',
            'adj_address': '0.0.0.3',
            'enabled': True,
            'vrf': 0,
            'output_if': 'Gi0/0/4',
            'global_ipv6_prefix': {
                'enabled': True,
                'prefix': '2001::/96'
            }
        }
    }
}
