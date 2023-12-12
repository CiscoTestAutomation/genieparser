expected_output = {
    1: {
        'Ethernet1/97/1': {
            'status': 'INITIALIZING - Searching for Peer (Waiting to receive first Peer MKPDU)', 
            'local_txSci': 'c4f7.d530.1484/0001', 
            'local_txSsci': '0', 
            'mka_port_identifier': '0', 
            'cak_name': '10000000', 
            'ca_auth_mode': 'PRIMARY-PSK', 
            'member_intentifier': 'B3034A0893A7762D5CC0439C', 
            'message_num': '7515', 
            'mka_policy_name': 'Test-MP1', 
            'key_server_prio': '16', 
            'key_server': 'Yes', 
            'include_icv': 'No', 
            'sak_cipher_suite': 'GCM-AES-256', 
            'sak_cipher_suite_oper': 'No', 
            'replay_window_size': '148809600', 
            'conf_offset': 'CONF-OFFSET-0', 
            'latest_sak_an': '0', 
            'latest_sak_ki': '00000000000000000000000000000000', 
            'latest_sak_kn': '0', 
            'ca_peer_cnt': '1', 
            'eapol_dst_mac': '0180.c200.0003', 
            'ether_type': '0x888e', 
            'peer_status': {
                'peer_mi': '001100000001000100000001', 
                'rx_sci': '0011.0000.0001/0001', 
                'peer_cak': 'Match', 
                'latest_rx_mkpdu': '15:47:12 PST Mon May 08 2023'
            }
        }
    }, 
    2: {
        'Ethernet1/97/2': {
            'status': 'SECURED - Secured MKA Session with MACsec', 
            'local_txSci': 'c4f7.d530.1485/0001', 
            'local_txSsci': '1', 
            'mka_port_identifier': '1', 
            'cak_name': '10100000', 
            'ca_auth_mode': 'PRIMARY-PSK', 
            'member_intentifier': '783DEDF82AF6A5D3CBA13CB6', 
            'message_num': '7516', 
            'mka_policy_name': 'Test-MP2', 
            'key_server_prio': '16', 
            'key_server': 'Yes', 
            'include_icv': 'No', 
            'sak_cipher_suite': 'GCM-AES-256', 
            'sak_cipher_suite_oper': 'GCM-AES-256', 
            'replay_window_size': '148809600', 
            'conf_offset': 'CONF-OFFSET-0', 
            'latest_sak_status': 'Rx & TX', 
            'latest_sak_an': '0', 
            'latest_sak_ki': '783DEDF82AF6A5D3CBA13CB600000001', 
            'latest_sak_kn': '1', 
            'last_sak_key_time': '11:36:51 PST Mon May 08 2023', 
            'ca_peer_cnt': '1', 
            'eapol_dst_mac': '0180.c200.0003', 
            'ether_type': '0x888e', 
            'peer_status': {
                'peer_mi': '002700000001000100000001', 
                'rx_sci': '0027.0000.0001/0001', 
                'peer_cak': 'Match', 
                'latest_rx_mkpdu': '15:47:11 PST Mon May 08 2023'
            }
        }
    }
}