expected_output = {
    'total_tunnels': 1,
    'total_sessions': 1,
    'tunnels': {
        '3217474068': {
            'loc_tunnel_id': 3217474068,
            'rem_tunnel_id': 2611998623,
            'remote_name': 'fg4',
            'state': 'est',
            'remote_address': '100.3.1.1',
            'session_count': 1,
            'l2tp_class_vpdn_group': 'l2tp_class_1',
            'sessions': {
                'session_1': {
                    'loc_id': 2409671146,
                    'rem_id': 3648835555,
                    'tunnel_id': 3217474068,
                    'username': '101',
                    'interface_vcid_circuit': 'Gi0/0/0',
                    'state': 'est',
                    'last_change': '00:00:22',
                    'unique_id': 0
                }
            }
        }
    }
}
