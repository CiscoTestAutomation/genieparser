expected_output = {
    'session': {
        'version': 'Cisco-2.0',
        'incoming': {
            '1': {
                'id': 1,
                'key_exchange': 'ecdh-sha2-nistp256', 
                'pubkey': 'ssh-rsa', 
                'incipher': 'aes128-ctr', 
                'outcipher': 'aes128-ctr', 
                'inmac': 'hmac-sha2-256', 
                'outmac': 'hmac-sha2-256'
            }
        },
        'outgoing': {
            '1': {
                'id': 1, 
                'key_exchange': 'ecdh-sha2-nistp521', 
                'pubkey': 'ecdsa-sha2-nistp256', 
                'incipher': 'aes128-ctr', 
                'outcipher': 'aes128-ctr', 
                'inmac': 'hmac-sha2-512', 
                'outmac': 'hmac-sha2-512'
            }
        }
    }
}
