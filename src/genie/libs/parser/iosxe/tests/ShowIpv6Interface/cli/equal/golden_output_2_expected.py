expected_output={
    'GigabitEthernet2': {
        'joined_group_addresses': ['FF02::1', 'FF02::1:FF00:1', 'FF02::1:FF8D:EF3D'],
        'oper_status': 'up',
        'mtu': 1500,
        'enabled': True,
        'ipv6': {
            'nd': {
                'dad_attempts': 1,
                'using_time': 30000,
                'suppress': False,
                'dad_enabled': True,
                'ns_retransmit_interval': 1000,
                'reachable_time': 30000,
            },
            '2001:111::1/64': {
                'status': 'valid',
                'ip': '2001:111::1',
                'prefix_length': '64',
            },
            'icmp': {
                'unreachables': 'sent',
                'redirects': True,
                'error_messages_limited': 100,
            },
            'enabled': True,
            'FE80::250:56FF:FE8D:EF3D': {
                'origin': 'link_layer',
                'ip': 'FE80::250:56FF:FE8D:EF3D',
                'status': 'valid',
            },
        },
    },
}