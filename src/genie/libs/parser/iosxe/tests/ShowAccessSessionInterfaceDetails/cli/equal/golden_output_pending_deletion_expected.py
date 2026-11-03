# Captured CSCwu92597 output, also used by the MAC-details golden fixture.
expected_output = {
    'interfaces': {
        'GigabitEthernet1/0/25': {
            'mac_address': {
                '0011.0100.0001': {
                    'iif_id': '0x1BDCBD00',
                    'ipv6_address': 'Unknown',
                    'ipv4_address': 'Unknown',
                    'user_name': 'Vegas_1',
                    'status': 'Authorized',
                    'domain': 'DATA',
                    'oper_host_mode': 'multi-host',
                    'oper_control_dir': 'both',
                    'session_timeout': {'type': 'N/A'},
                    'common_session_id': '920C140B00000010CB83F27F',
                    'acct_session_id': '0x00000005',
                    'handle': '0xc5000006',
                    'current_policy': 'DOT1X_MD5_POLICY',
                    'blocked_on': ['Pending Deletion', 'SM Accounting Feature'],
                    'method_status': {
                        'dot1x': {'method': 'dot1x', 'state': 'Authc Success'},
                    },
                },
            },
        },
    },
}
