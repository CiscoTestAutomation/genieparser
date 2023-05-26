expected_output = {
    'ipv4': {
        'crypto_map_tag': {
            'vpn_to_switch2': {
                'sequence_number': 1,
                'ipsec': 'ipsec-isakmp',
                'peer': ['172.20.249.12'],
                'access_list_ss_dynamic': 'False',
                'extended_ip_access_list': '101',
                'security_association_lifetime': {
                    'kilobytes': 4608000,
                    'seconds': 3600
                },
                'dualstack': False,
                'responder_only': False,
                'pfs': False,
                'mixed_mode': 'Disabled',
                'transform_sets': {
                    'default': ['esp-aes', 'esp-sha-hmac']
                },
                'interfaces_crypto_map': {
                    'crypto_map_tag': 'VPN_To_Switch2'
                }
            }
        }
    }
}