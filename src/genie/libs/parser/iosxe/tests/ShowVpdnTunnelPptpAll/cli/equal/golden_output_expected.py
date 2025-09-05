expected_output = {
        'total_tunnels': 1,
        'total_sessions': 1,
        'tunnels': {
            40512: {
                'active_sessions': 1,
                'state': 'wt-cnnct',
                'time_since_change': '00:00:10',
                'remote_tunnel_name': '100.1.1.1',
                'remote_internet_address': {
                    'ip': '100.1.1.1',
                    'port': 1723,
                },
                'local_tunnel_name': 'PG2',
                'local_internet_address': {
                    'ip': '11.1.1.1',
                    'port': 0,
                },
                'vpdn_group': 'PPTP',
                'packets_sent': 0,
                'packets_received': 0,
                'bytes_sent': 0,
                'bytes_received': 0,
                'last_clearing': 'never',
            }
        }
    }


