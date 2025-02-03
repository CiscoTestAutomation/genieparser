expected_output = {
    'interface': {
        'GigabitEthernet2/0/3': {
            'acct_session_id': '0x0000003c',
            'common_session_id': '2300130B0000002ABD0A2AF1',
            'current_policy': 'test_dot1x',
            'device_name': 'Cisco IP Phone 7961',
            'device_type': 'Cisco-IP-Phone-7961',
            'domain': 'VOICE',
            'handle': '0xdb000020',
            'iif_id': '0x1D8DDC60',
            'ipv4_address': '192.168.194.1',
            'ipv6_address': 'Unknown',
            'mac_address': '001a.a136.c68a',
            'method_status_list': {
                'method': 'dot1x',
                'state': 'Authc Success',
            },
            'oper_control_dir': 'both',
            'oper_host_mode': 'multi-domain',
            'resultant_policies': {},
            'server_policies': {
                'vlan_group': 194,
            },
            'session_timeout': {
                'local': 50,
                'remaining': 29,
            },
            'status': 'Authorized',
            'timeout_action': 'Reauthenticate',
            'user_name': 'CP-7961G-GE-SEP001AA136C68A',
        },
    },
}