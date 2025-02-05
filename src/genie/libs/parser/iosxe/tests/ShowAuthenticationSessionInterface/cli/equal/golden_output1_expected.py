expected_output = {
    'interfaces': {
        'GigabitEthernet2/0/3': {
            'acct_session_id': '0x00000020',
            'common_session_id': '2300130B0000002ABD0A2AF1',
            'current_policy': 'test_dot1x',
            'device_name': 'Cisco IP Phone 7961',
            'device_type': 'Cisco-IP-Phone-7961',
            'domain': 'VOICE',
            'handle': '0xdb000020',
            'iif_id': '0x1D8DDC60',
            'interface': 'GigabitEthernet2/0/3',
            'ipv4_address': '192.168.194.1',
            'ipv6_address': 'Unknown',
            'mac_address': '001a.a136.c68a',
            'method_status': {
                'Method': {
                    'method': 'Method',
                    'state': 'State',
                },
                'Resultant': {
                    'method': 'Resultant',
                    'state': 'Policies:',
                },
                'Server': {
                    'method': 'Server',
                    'state': 'Policies:',
                },
            },
            'oper_control_dir': 'both',
            'oper_host_mode': 'multi-domain',
            'server_policies': {
                'vlan_group': {
                    'vlan': '194',
                },
            },
            'session_timeout': {
                'remaining': '14s',
                'timeout': '50s',
            },
            'status': 'Authorized',
            'timeout_action': 'Reauthenticate',
            'user_name': 'CP-7961G-GE-SEP001AA136C68A',
        },
    },
}