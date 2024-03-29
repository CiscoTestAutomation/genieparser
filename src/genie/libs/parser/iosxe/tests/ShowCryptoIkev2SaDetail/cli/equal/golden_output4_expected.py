expected_output={
    'tunnel_id': {
        1: {
            'local': '10.146.0.154/500',
            'remote': '107.90.29.85/500',
            'fvrf': 'gre',
            'ivrf': 'gre',
            'status': 'ready',
            'remote_subnets': ['10.255.1.238 255.255.255.255'],
            'encryption': 'aes-gcm',
            'keysize': 256,
            'prf': 'sha512',
            'hash': 'none',
            'dh_grp': 21,
            'auth_sign': 'psk',
            'auth_verify': 'psk',
            'life_time': 86400,
            'active_time': 20635,
            'ce_id': 53247,
            'session_id': 494,
            'local_spi': '26E77925771B44B1',
            'remote_spi': '4785C18DB784C439',
            'status_description': 'negotiation done',
            'local_id': 'cedar.flex.example.com',
            'remote_id': 'example-r46.flex.example.com',
            'local_reg_msg_id': 3,
            'remote_req_msg_id': 5,
            'local_next_msg_id': 3,
            'remote_next_msg_id': 5,
            'local_req_queued': 3,
            'remote_req_queued': 5,
            'local_window': 5,
            'remote_window': 5,
            'dpd_configured_time': 10,
            'retry': 2,
            'fragmentation': 'not  configured',
            'dynamic_route_update': 'enabled',
            'extended_authentication': 'not configured',
            'nat_t': 'not detected',
            'cisco_trust_security_sgt': 'disabled',
            'initiator_of_sa': 'no'
        },
        8: {
            'local': '10.146.0.154/4500',
            'remote': '3.130.109.2/4500',
            'fvrf': 'gre',
            'ivrf': 'gre',
            'status': 'ready',
            'remote_subnets': ['172.31.0.4 255.255.255.255'],
            'encryption': 'aes-cbc',
            'keysize': 128,
            'prf': 'sha256',
            'hash': 'sha256',
            'dh_grp': 19,
            'auth_sign': 'psk',
            'auth_verify': 'psk',
            'life_time': 86400,
            'active_time': 16301,
            'ce_id': 0,
            'session_id': 470,
            'local_spi': 'B3A917AB8A5F68A9',
            'remote_spi': 'FBAFD8516EA9D5E8',
            'status_description': 'negotiation done',
            'local_id': 'cedar.flex.example.com',
            'remote_id': 'test-r1.flex.example.com',
            'local_reg_msg_id': 0,
            'remote_req_msg_id': 16,
            'local_next_msg_id': 0,
            'remote_next_msg_id': 16,
            'local_req_queued': 0,
            'remote_req_queued': 16,
            'local_window': 5,
            'remote_window': 5,
            'dpd_configured_time': 10,
            'retry': 2,
            'fragmentation': 'not  configured',
            'dynamic_route_update': 'enabled',
            'extended_authentication': 'not configured',
            'nat_t': 'detected  outside',
            'cisco_trust_security_sgt': 'disabled',
            'initiator_of_sa': 'no'
        },
        9: {
            'local': '10.146.0.154/500',
            'remote': '65.27.58.179/500',
            'fvrf': 'gre',
            'ivrf': 'gre',
            'status': 'ready',
            'remote_subnets': ['10.255.3.229 255.255.255.255'],
            'encryption': 'aes-cbc',
            'keysize': 256,
            'prf': 'sha512',
            'hash': 'sha512',
            'dh_grp': 19,
            'auth_sign': 'psk',
            'auth_verify': 'psk',
            'life_time': 86400,
            'active_time': 16298,
            'ce_id': 0,
            'session_id': 471,
            'local_spi': 'EA7CC2DFCC83A760',
            'remote_spi': 'E4D5BDA3B19BBD80',
            'status_description': 'negotiation done',
            'local_id': 'cedar.flex.example.com',
            'remote_id': 'test2-r1.split.flex.example.com',
            'local_reg_msg_id': 0,
            'remote_req_msg_id': 15,
            'local_next_msg_id': 0,
            'remote_next_msg_id': 15,
            'local_req_queued': 0,
            'remote_req_queued': 15,
            'local_window': 5,
            'remote_window': 5,
            'dpd_configured_time': 10,
            'retry': 2,
            'fragmentation': 'not  configured',
            'dynamic_route_update': 'enabled',
            'extended_authentication': 'not configured',
            'nat_t': 'not detected',
            'cisco_trust_security_sgt': 'disabled',
            'initiator_of_sa': 'no'
        }
    }
}