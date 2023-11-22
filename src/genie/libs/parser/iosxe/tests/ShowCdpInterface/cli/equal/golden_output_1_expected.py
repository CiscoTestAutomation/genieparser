expected_output = {
    'cdp_enabled_interfaces': 172,
    'interfaces_up': 7,
    'interfaces_down': 166,
    'interface': {
        'GigabitEthernet0/0': {
            'state': 'up',
            'protocol_state': 'up',
            'encapsulation': 'ARPA',
            'cdp_interval': 60,
            'hold_time': 180,
        },
        'TwoGigabitEthernet1/0/1': {
            'state': 'down',
            'protocol_state': 'down',
            'encapsulation': 'ARPA',
            'cdp_interval': 90,
            'hold_time': 160,
        },
        'TwoGigabitEthernet1/0/2': {
            'state': 'down',
            'protocol_state': 'down',
            'encapsulation': 'ARPA',
            'cdp_interval': 60,
            'hold_time': 180,
        },
        'TwentyFiveGigE3/1/1': {
            'state': 'down',
            'protocol_state': 'down',
            'encapsulation': 'ARPA',
            'cdp_interval': 60,
            'hold_time': 180,
        },
        'AppGigabitEthernet3/0/1': {
            'state': 'up',
            'protocol_state': 'up',
            'encapsulation': 'ARPA',
            'cdp_interval': 60,
            'hold_time': 180,
        }
    }
}