expected_output = {
    'capabilities': {
        'access_control': 'must-secure',
        'cipher': 'GCM-AES-128',
        'ciphers_supported': 'GCM-AES-128 GCM-AES-256',
        'confidentiality_offset': 0,
        'delay_protect_enable': False,
        'include_sci': True,
        'replay_window': 64,
    },
    'receive_sa': {
        'an': [0, 1, 2, 3],
        'delay_protect_an_lpn': '0/0',
        'next_pn': 11,
    },
    'receive_sc': {
        'receiving': True,
        'sci': '8C94616AFB02000A',
    },
    'transmit_sa': {
        'delay_protect_an_nextpn': 'NA/0',
        'next_pn': 10,
    },
    'transmit_sc': {
        'sci': '687909AC5482000A',
        'transmitting': True,
    },
}