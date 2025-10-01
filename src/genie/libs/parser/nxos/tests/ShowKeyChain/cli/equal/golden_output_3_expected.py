expected_output = {
    'keychains': {
    'Test-KC1': {
        'key_type': 'Macsec', 
        '10000000': {
            'encryption_type': '7', 
            'key_octet_string': '0729701e1d5d4c53404a522d26090f010e63647040534355560e007971772a263e30080a0407070303530227257b73213556550958525a771b1650382734362e2a', 
            'crypto_algorithm': 'AES_256_CMAC', 
            'lifetime_state': ' (always valid) [active]'
        }, 
        'active_send_key': '10000000'
    },
    'Test-KC2': {
        'key_type': 'Macsec', 
        '10100000': {
            'encryption_type': '7', 
            'key_octet_string': '0729701e1d5d4c53404a522d26090f010e63647040534355560e007971772a263e30080a0407070303530227257b73213556550958525a771b1650382734362e2a', 
            'crypto_algorithm': 'AES_256_CMAC', 
            'lifetime_state': ' (always valid) [active]'
        }, 
        'active_send_key': '10100000'
    }
    }
}