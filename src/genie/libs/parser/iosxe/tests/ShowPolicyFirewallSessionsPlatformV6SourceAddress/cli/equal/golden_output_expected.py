expected_output = {
    'platform_command': 'show platform hardware qfp active feature firewall datapath scb ipv6 2001:1:0:0:0:0:0:1',
    'session_legend': {
        's': 'session',
        'i': 'imprecise channel',
        'c': 'control channel',
        'd': 'data channel',
        'u': 'utd inspect',
        'A/D': 'appfw action allow/deny'
    },
    'sessions': {
        '0x00000002': {
            'session_id': '0x00000002',
            'source_address': '2001:1::1',
            'source_port': '128',
            'destination_address': '2001:2::2',
            'destination_port': '7993',
            'protocol': '58',
            'protocol_info': '(0:0)',
            'protocol_detail': '(0x3:icmp)',
            'channels': '[sd]',
            'session_value': '3046618007'
        }
    }
}
