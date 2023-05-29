expected_output = {
    'http_secure_server': {
        'status': 'Enabled',
        'port': 443,
        'ciphersuite': [
            'rsa-aes-cbc-sha2', 
            'rsa-aes-gcm-sha2',
            'dhe-aes-cbc-sha2', 
            'dhe-aes-gcm-sha2', 
            'ecdhe-rsa-aes-cbc-sha2',
            'ecdhe-rsa-aes-gcm-sha2', 
            'ecdhe-ecdsa-aes-gcm-sha2', 
            'tls13-aes128-gcm-sha256',
            'tls13-aes256-gcm-sha384', 
            'tls13-chacha20-poly1305-sha256'
        ],
        'tls_version': ['TLSv1.3', 'TLSv1.2'],
        'client_authentication': 'Disabled',
        'piv_authentication': 'Disabled',
        'piv_authorization': 'Disabled',
        'trustpoint': 'INVALID_TP',
        'ecdhe_curve': 'secp256r1',
        'active_session_modules': 'ALL'
    }
}