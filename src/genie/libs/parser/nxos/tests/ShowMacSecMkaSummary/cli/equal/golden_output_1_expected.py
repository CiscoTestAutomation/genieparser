expected_output = {
    'Ethernet1/97/1': {
        'status': 'Init', 
        'cipher_suite': 'No Cipher', 
        'key_server': 'Yes', 
        'macsec_policy': 'Test-MP1', 
        'keychain': 'Test-KC1', 
        'fallback_keychain': 'no keychain'
    }, 
    'Ethernet1/97/2': {
        'status': 'Secured', 
        'cipher_suite': 'GCM-AES-256', 
        'key_server': 'Yes', 
        'macsec_policy': 'Test-MP2', 
        'keychain': 'Test-KC2', 
        'fallback_keychain': 'no keychain'
    }
}