expected_output= {
     'interface': {
         'Tunnel1': {
             'peer': {
                 '10.1.1.1': {
                     'port': {
                         '4500': {
                             'ike_sa': {
                                 '1': {
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
                                     'origin': 'crypto map',
                                 },
                             },
                         },
                     },
                 },
             },
             'profile': 'IKEV2_PROFILE',
             'session_status': 'UP-ACTIVE',
         },
     },
 }