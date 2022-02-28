expected_output = {
        'isakmp_stats': {
            'IPv6':{
                1:{
                    'c_id': 29610,
                    'local_ip': '100.0.10::2',
                    'remote_ip': '100.13.220::2',
                    'status': 'ACTIVE',
                    'encr_algo': 'aes',
                    'hash_algo': 'sha',
                    'auth_type': 'psk',
                    'dh_group': 16,
                    'lifetime': '00:01:47',
                    'capabilities': 'D',
                    'engine_id': 'SW',
                    'conn_id': 12609
                },
                2:{
                    'c_id': 29494,
                    'local_ip': '100.0.10::2',
                    'remote_ip': '100.12.134::2',
                    'status': 'ACTIVE',
                    'encr_algo': 'aes',
                    'hash_algo': 'sha',
                    'auth_type': 'psk',
                    'dh_group': 16,
                    'lifetime': '00:01:12',
                    'capabilities': 'D'
                },
            },
        },
    } 