expected_output =  {
    'macsec_policy': {
        'MP1': {
            'cipher_suite': 'Enforce-Peer', 
            'priority': 32, 
            'window': 100000, 
            'offset': 30, 
            'security': 'must-secure', 
            'sak_rekey_time': '70',
            'icv_indicator': 'TRUE', 
            'include_sci': 'FALSE',
            'enforce_peer_cipher_suite': 'GCM-AES-128'
        }, 
        'Test-MP1': {
            'cipher_suite': 'Enforce-Peer', 
            'priority': 16, 
            'window': 148809600, 
            'offset': 0, 
            'security': 'should-secure',
            'sak_rekey_time': 'pn-rollover', 
            'icv_indicator': 'FALSE', 
            'include_sci': 'TRUE',
            'enforce_peer_cipher_suite': 'GCM-AES-256 GCM-AES-XPN-256 GCM-AES-XPN-128 GCM-AES-128'
        }, 
        'Test-MP2': {
            'cipher_suite': 'Enforce-Peer', 
            'priority': 16, 
            'window': 148809600, 
            'offset': 0, 
            'security': 'should-secure', 
            'sak_rekey_time': 'pn-rollover', 
            'icv_indicator': 'FALSE', 
            'include_sci': 'TRUE',
            'enforce_peer_cipher_suite': 'GCM-AES-256'
        }, 
        'system-default-macsec-policy': {
            'cipher_suite': 'GCM-AES-XPN-256', 
            'priority': 16, 
            'window': 148809600, 
            'offset': 0, 
            'security': 'should-secure', 
            'sak_rekey_time': 'pn-rollover', 
            'icv_indicator': 'FALSE', 
            'include_sci': 'TRUE'
        }
    }
}