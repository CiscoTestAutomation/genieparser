expected_output = {
    'capabilities': {
        'ciphers_supported': 'GCM-AES-128 GCM-AES-256',
        'cipher': 'GCM-AES-128',
        'confidentiality_offset': 0,
        'replay_window': 64,
        'delay_protect_enable': False,
        'access_control': 'must-secure',
        'include_sci': True
    },
    'transmit_sc': {
        'sci': '481BA4654B52000A',
        'transmitting': True
    },
    'transmit_sa': {
        'next_pn': 23427,
        'delay_protect_an_nextpn': 'NA/0'
    },
    'receive_sc': {
        'sci': '488002B3E6800008',
        'receiving': True
    },
    'receive_sa': {
        'next_pn': 615,
        'an': 0,
        'delay_protect_an_lpn': '0/0'
    }
}
