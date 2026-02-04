# Expected output for: show policy-firewall sessions platform destination-port 0
expected_output = {
    'platform_command': 'show platform hardware qfp active feature firewall datapath scb any any any 0 any all any',
    'legend': {
        'session': 'session',
        'imprecise': 'imprecise channel',
        'control': 'control channel',
        'data': 'data channel',
        'utd': 'utd inspect',
        'appfw': 'appfw action allow/deny'
    }
}
