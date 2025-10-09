expected_output = {
    'session_id': {
        '2300130B0000002CBD0A520E': {
            'acct_session_id': '0x00000037',
            'common_session_id': '2300130B0000002CBD0A520E',
            'current_policy': 'test_dot1x',
            'device_name': 'Unknown Device',
            'device_type': 'Un-Classified Device',
            'domain': 'DATA',
            'handle': '0x31000022',
            'iif_id': '0x1210405D',
            'interface': 'GigabitEthernet2/0/3',
            'ipv4_address': '192.168.10.101',
            'ipv6_address': 'Unknown',
            'mac_address': '0055.6677.8855',
            'method_status_list': {
                'method': 'dot1x',
                'state': 'Authc Success',
            },
            'oper_control_dir': 'both',
            'oper_host_mode': 'multi-domain',
            'server_policies': {
                'vlan_group': 10,
            },
            'session_timeout': {
                'local': 50,
                'remaining': 29,
            },
            'status': 'Authorized',
            'timeout_action': 'Reauthenticate',
            'user_name': 'asp_dot1x_user2',
        },
    },
}