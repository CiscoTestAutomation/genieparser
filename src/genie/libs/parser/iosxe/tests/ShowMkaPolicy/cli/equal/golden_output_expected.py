expected_output = {
    'send_secure_announcements': 'DISABLED',
    'policy': {
        "macsec": {
            'key_server_priority': 0,
            'delay_protect': "FALSE",
            'confidentiality_offset': 30,
            'sak_rey_key_on_live_peer_loss': "FALSE",
            'include_icv_indicator': "TRUE",
            'cipher': "GCM-AES-128",
            'interfaces': ['Te1/0/48', 'Fo1/1/2', 'Gi2/0/12', 'Gi2/0/22', 'Te3/0/46', 'Te3/0/48']
        },
        'macsec1': {
            'cipher': 'GCM-AES-128',
            'confidentiality_offset': 30,
            'delay_protect': 'FALSE',
            'include_icv_indicator': 'TRUE',
            'interfaces': ['Te1/0/48', 'Fo1/1/2'],
            'key_server_priority': 0,
            'sak_rey_key_on_live_peer_loss': 'FALSE'
        },
        'macsec2': {
            'cipher': 'GCM-AES-128',
            'confidentiality_offset': 30,
            'delay_protect': 'FALSE',
            'include_icv_indicator': 'TRUE',
            'interfaces': ['Te1/0/48'],
            'key_server_priority': 0,
            'sak_rey_key_on_live_peer_loss': 'FALSE'
        },
        "DEFAULT POLICY": {
            'key_server_priority': 0,
            'delay_protect': "FALSE",
            'confidentiality_offset': 0,
            'sak_rey_key_on_live_peer_loss': "FALSE",
            'include_icv_indicator': "TRUE",
            'cipher': "GCM-AES-128"
        }
    }
}