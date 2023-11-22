expected_output = {
    'socket_connections': {
        'total_socket_connections': 4, 
        'sockets_in_listen_state': ['Tunnel1-head-0', 'Tunnel2-head-0', 'Tunnel3-head-0', 'Tunnel20-head-0'], 
        'Tu1': {
            'peers': {
                    'remote_ip': '10.0.0.2', 
                    'local_ip': '85.45.1.1'
            }, 
            'local_ident': {
                'protocol': 47, 
                'mask': '255.255.255.255', 
                'port': 0, 
                'address': '85.45.1.1'
            },  
            'remote_ident': {
                'protocol': 47, 
                'mask': '255.255.255.255', 
                'port': 0, 
                'address': '10.0.0.2'
            }, 
            'socket_state': 'Open', 
            'ipsec_profile': 'star', 
            'client_state': 'Active',
            'client_name': 'TUNNEL SEC'
        }, 
        'Tu2': {
            'peers': {
                'remote_ip': '10.0.0.2', 
                'local_ip': '85.45.2.1'
            }, 
            'local_ident': {
                'protocol': 47, 
                'mask': '255.255.255.255', 
                'port': 0, 
                'address': '85.45.2.1'
            }, 
            'remote_ident': {
                'protocol': 47, 
                'mask': '255.255.255.255', 
                'port': 0, 
                'address': '10.0.0.2'
            }, 
            'socket_state': 'Open', 
            'ipsec_profile': 'star', 
            'client_state': 'Active',
            'client_name': 'TUNNEL SEC'
        }, 
        'Tu3': {
            'peers': {
                'remote_ip': '10.0.0.2', 
                'local_ip': '85.45.3.1'
            }, 
            'local_ident': {
                'protocol': 47, 
                'mask': '255.255.255.255', 
                'port': 0, 
                'address': '85.45.3.1'
            }, 
            'remote_ident': {
                'protocol': 47, 
                'mask': '255.255.255.255', 
                'port': 0, 
                'address': '10.0.0.2'
            }, 
            'socket_state': 'Open', 
            'ipsec_profile': 'star', 
            'client_state': 'Active', 
            'client_name': 'TUNNEL SEC',
            'true_ident': ['0.0.0.0/0.0.0.0/0/0 -> 0.0.0.0/0.0.0.0/0/0', '::/0/0/0 -> ::/0/0/0']
        }, 
        'Tu20': {
            'peers': {
                'remote_ip': '22.1.1.1', 
                'local_ip': '21.1.1.1'
            }, 
            'local_ident': {
                'protocol': 0, 
                'mask': '0.0.0.0', 
                'port': 0, 
                'address': '0.0.0.0'
            },  
            'remote_ident': {
                'protocol': 0, 
                'mask': '0.0.0.0', 
                'port': 0, 
                'address': '0.0.0.0'
            }, 
            'socket_state': 'Open', 
            'ipsec_profile': 'IPSEC_PROFILE', 
            'client_state': 'Active',
            'client_name': 'TUNNEL SEC', 
            'true_ident': ['172.18.1.0/255.255.255.0/0/0 -> 10.4.0.0/255.255.255.0/0/0', 
                '172.17.1.0/255.255.255.0/0/0 -> 10.4.0.0/255.255.255.0/0/0', 
                '172.17.1.0/255.255.255.0/0/0 -> 10.1.0.0/255.255.255.0/0/0', 
                '172.16.1.0/255.255.255.0/0/0 -> 10.1.0.0/255.255.255.0/0/0', 
                '6664:3038:6162:6364::/64/0/0 -> 6664:3038:6665:6564::/64/0/0']
        }
    }
}