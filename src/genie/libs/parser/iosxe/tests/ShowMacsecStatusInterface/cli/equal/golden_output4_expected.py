expected_output = {
    'capabilities': {
        'access_control': 'must-secure',
        'cipher': 'GCM-AES-128',
        'ciphers_supported': 'GCM-AES-128 GCM-AES-256',
        'confidentiality_offset': 0,
        'delay_protect_enable': False,
        'dot1q_in_clear': '1 Tag(s)',
        'include_sci': True,
        'replay_window': 32,
    },
    'receive_sa': {
        'an': [0, 1],
        'delay_protect_an_lpn': '1/1',
        'next_pn': 501,
    },
    'receive_sc': {
        'receiving': True,
        'sci': 'F6E5D4C3B2A10002',
    },
    'transmit_sa': {
        'delay_protect_an_nextpn': 'NA/0',
        'next_pn': 500,
    },
    'transmit_sc': {
        'sci': 'A1B2C3D4E5F60001',
        'transmitting': True,
    },
}