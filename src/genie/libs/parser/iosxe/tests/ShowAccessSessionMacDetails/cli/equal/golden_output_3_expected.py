expected_output = {
    'mac': {
        '000e.83e5.3398': {
            'interface': 'GigabitEthernet1/0/12',
            'iif_id': '0x135C9B47',
            'ipv6_address': 'Unknown',
            'ipv4_address': '194.10.0.1',
            'user_name': 'CP-7970G-SEP000E83E53398',
            'status': 'Authorized',
            'domain': 'VOICE',
            'oper_host_mode': 'multi-domain',
            'oper_control_dir': 'both',
            'session_timeout': {
                'server': 135,
                'remaining': 27
            },
            'timeout_action': 'Reauthenticate',
            'common_session_id': 'EE01060A0000000FBB64DB50',
            'acct_session_id': '0x00000004',
            'handle': '0x00000000',
            'current_policy': 'POLICY_Gi1/0/12',
            'server_policies': {
                'session_timeout': 135,
                'vlan_group': 194,
                'acs_acl': 'xACSACLx-IP-legacy_TC9_permit_user_CP-7970G-SEP000E83E53398-63ced261'
            },
            'method_status_list': {
                'method': 'dot1x',
                'state': 'Authc Success'
            }
        }
    }
}