expected_output = {
    'ipv4': {
        'crypto_map_tag': {
            'ikev2-cryptomap': {
                'sequence_number': 1,
                'ipsec': 'ipsec-isakmp',
                'peer': ['172.20.249.12', '172.20.249.3'],
                'access_list_ss_dynamic': 'False',
                'ikev2_profile': 'ikev2profile',
                'extended_ip_access_list': '102',
                'current_peer': '172.20.249.12',
                'security_association_lifetime': {
                    'kilobytes': 4608000,
                    'seconds': 3600
                },
                'dualstack': False,
                'responder_only': False,
                'pfs': False,
                'mixed_mode': 'Disabled',
                'transform_sets': {
                    'aes256-sha1': ['esp-aes', 'esp-sha-hmac']
                },
                'interfaces_crypto_map': {
                    'crypto_map_tag': 'ikev2-cryptomap',
                    'interfaces': ['Vlan1']
                }
            }
        }
    }
}