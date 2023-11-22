expected_output = {
            'interfaces': {
                'GigabitEthernet3': {
                    'profile': 'ASM-PROFILE',
                    'session_status': 'UP-ACTIVE',
                    'peer_ip': '1.1.1.1',
                    'peer_port': 500,
                    'session_id': 1,
                    'IKEv2':{
                        'local_ip': '1.1.1.2',
                        'local_port': 500,
                        'remote_ip': '1.1.1.1',
                        'remote_port': 500
                    },
                    'ipsec_flow':{
                        1:{
                            'flow': 'permit ip 20.20.20.0/255.255.255.0 10.10.10.0/255.255.255.0',
                            'active_sa': 2,
                            'origin': 'crypto map'
                        },
                        2:{
                            'flow': 'permit ip 40.40.40.0/255.255.255.0 30.30.30.0/255.255.255.0',
                            'active_sa': 0,
                            'origin': 'crypto map'
                        },
                    },   
                },                
            },
        }
