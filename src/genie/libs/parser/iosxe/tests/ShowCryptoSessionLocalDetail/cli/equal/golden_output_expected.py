expected_output= {
     'interface': {
         'Tunnel1': {
             'peer': {
                 '10.1.1.1': {
                     'port': {
                         '4500': {
                             'desc': 'none',
                             'fvrf': 'none',
                             'ike_sa': {
                                 '1': {
                                     'capabilities': 'DNU',
                                     'conn_id': '1',
                                     'lifetime': '23:59:29',
                                     'local': '4.4.4.1',
                                     'local_port': '4500',
                                     'remote': '10.1.1.1',
                                     'remote_port': '4500',
                                     'sa_status': 'Active',
                                     'session_id': '78',
                                     'version': 'IKEv2',
                                 },
                             },
                             'ipsec_flow': {
                                 'permit ip 0.0.0.0/0.0.0.0 0.0.0.0/0.0.0.0': {
                                     'active_sas': 2,
                                     'inbound_life_kb': '4607999',
                                     'inbound_life_secs': '3569',
                                     'inbound_pkts_decrypted': 2,
                                     'inbound_pkts_drop': 0,
                                     'origin': 'crypto map',
                                     'outbound_life_kb': '4608000',
                                     'outbound_life_secs': '3569',
                                     'outbound_pkts_drop': 0,
                                     'outbound_pkts_encrypted': 0,
                                 },
                             },
                             'ivrf': 'none',
                             'phase1_id': '10.1.1.1',
                         },
                     },
                 },
             },
             'profile': 'IKEV2_PROFILE',
             'session_status': 'UP-ACTIVE',
             'uptime': '00:00:31',
         },
     },
 }