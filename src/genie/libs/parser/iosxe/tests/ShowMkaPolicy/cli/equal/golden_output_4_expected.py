expected_output = {
    'send_secure_announcements': 'DISABLED',
    'policy': {
        'mka_128': {
            'key_server_priority': 5,
            'delay_protect': 'FALSE',
            'confidentiality_offset': 0,
            'sak_rey_key_on_live_peer_loss': 'FALSE',
            'include_icv_indicator': 'TRUE',
            'cipher': 'GCM-AES-128',
        },
        'mka_256': {
            'key_server_priority': 5,
            'delay_protect': 'FALSE',
            'confidentiality_offset': 0,
            'sak_rey_key_on_live_peer_loss': 'FALSE',
            'include_icv_indicator': 'TRUE',
            'cipher': 'GCM-AES-256',
        },
        'mka_xpn_128': {
            'key_server_priority': 5,
            'delay_protect': 'FALSE',
            'confidentiality_offset': 0,
            'sak_rey_key_on_live_peer_loss': 'FALSE',
            'include_icv_indicator': 'TRUE',
            'cipher': 'GCM-AES-XPN-128',
            'interfaces': ['Fif1/0/5'],
        },
        'mka_xpn_256': {
            'key_server_priority': 5,
            'delay_protect': 'FALSE',
            'confidentiality_offset': 0,
            'sak_rey_key_on_live_peer_loss': 'FALSE',
            'include_icv_indicator': 'TRUE',
            'cipher': 'GCM-AES-XPN-256',
        },
    },
}
