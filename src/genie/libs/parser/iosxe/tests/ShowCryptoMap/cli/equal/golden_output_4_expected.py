expected_output = {
    'ipv6': {
        'crypto_map_tag': {
            'sdsd': {
                'sequence_number': 3,
                'ipsec': 'ipsec-manual',
                'peer': ['2001::1'],
                'access_list_ss_dynamic': 'False',
                'transform_sets': {
                    'default': ['esp-aes', 'esp-sha-hmac']
                },
                'interfaces_crypto_map': {
                    'crypto_map_tag': 'sdsd',
                    'interfaces': ['TwoGigabitEthernet2/0/17', 'TwoGigabitEthernet2/0/19']
                }
            }
        }
    }
}