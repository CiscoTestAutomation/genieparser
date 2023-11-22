expected_output = {
            'interfaces': {
                'Virtual-Access1325': {
                    'profile': 'IKEV2_PROFILE',
                    'uptime': '13:17:14',
                    'session_status': 'UP-ACTIVE',
                    'peer_ip': '17.27.1.11',
                    'peer_port': 38452,
                    'fvrf': 'none',
                    'ivrf': '10',
                    'phase_id': 'scale',
                    'session_id': 22000,
                    'IKEv2':{
                        'local_ip': '1.1.1.1',
                        'local_port': 4500,
                        'remote_ip': '17.27.1.11',
                        'remote_port': 38452,
                        'capabilities': 'DN',
                        'connid': 276,
                        'lifetime': '10:42:46'
                    },
                    'ipsec_flow':{
                        1:{
                            'flow': 'permit ip 0.0.0.0/0.0.0.0 host 7.1.2.40',
                            'active_sa': 2,
                            'origin': 'crypto map',
                            'inbound':{
                                'decrypted': 47673,
                                'dropped': 0,
                                'life_in_kb': 4607772,
                                'life_in_sec': 1874
                            },
                            'outbound':{
                                'encrypted': 47672,
                                'dropped': 0,
                                'life_in_kb': 4607812,
                                'life_in_sec': 1874
                            },
                        },
                    },   
                },
                'Virtual-Access929': {
                    'profile': 'IKEV2_PROFILE',
                    'uptime': '13:16:53',
                    'session_status': 'UP-ACTIVE',
                    'peer_ip': '17.27.1.11',
                    'peer_port': 55411,
                    'fvrf': 'none',
                    'ivrf': '10',
                    'phase_id': 'scale',
                    'session_id': 22062,
                    'IKEv2':{
                        'local_ip': '1.1.1.1',
                        'local_port': 4500,
                        'remote_ip': '17.27.1.11',
                        'remote_port': 55411,
                        'capabilities': 'DN',
                        'connid': 323,
                        'lifetime': '10:43:07'
                    },
                    'ipsec_flow':{
                        1:{
                            'flow': 'permit ip 0.0.0.0/0.0.0.0 host 7.1.2.88',
                            'active_sa': 2,
                            'origin': 'crypto map',
                            'inbound':{
                                'decrypted': 47668,
                                'dropped': 0,
                                'life_in_kb': 4607746,
                                'life_in_sec': 1687
                            },
                            'outbound':{
                                'encrypted': 47694,
                                'dropped': 0,
                                'life_in_kb': 4607791,
                                'life_in_sec': 1687
                            },
                        },
                    },   
                },
            },
        }
