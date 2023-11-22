expected_output = {
    'sessions': {
        1:{
            'username': 'lns@cisco.com',
            'intf': '-',
            'last_chg': '00:10:09',
            'local_id': 3542,
            'remote_id': 56774,
            'state': 'est',
            'tunnel_id': 7658,
            'uniq_id': 645
        },
        2: {'username': 'lns@cisco.com',
            'intf': '-',
            'last_chg': '00:10:08',
            'local_id': 24593,
            'remote_id': 3791,
            'state': 'est',
            'tunnel_id': 11479,
            'uniq_id': 645
        }
    },
    'total_sessions': 2,
    'total_tunnels': 2,
    'tunnels': {
        1: {
            'loc_tun_id': 7658,
            'rem_tun_id': 8656,
            'remote_ip': '18.18.18.1',
            'remote_name': 'LAC',
            'session_count': 1,
            'state': 'est',
            'vpdn_group': '1'
        },
        2: {
            'loc_tun_id': 11479,
            'rem_tun_id': 56539,
            'remote_ip': '14.14.14.2',
            'remote_name': 'LNS2',
            'session_count': 1,
            'state': 'est',
            'vpdn_group': 'TowardsLNS2'
        }
    }
}

