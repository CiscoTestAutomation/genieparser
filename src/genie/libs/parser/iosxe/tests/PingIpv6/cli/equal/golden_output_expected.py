expected_output = {
    'ping': {
        'address': 'FF08::10',
        'data_bytes': 100,
        'repeat': 5,
        'timeout_secs': 2,
        'source': '2012:AA:23::3',
        'interface': 'GigabitEthernet1/0/1',
        'request': {
            '0': [
                {'addr': '2012:AA:1:0:200:23FF:FE53:B72A', 'rtt': 38},
                {'addr': '2012:AA:12::1', 'rtt': 73},
                {'addr': '2012:AA:1::1', 'rtt': 73},
                {'addr': '2012:AA:1:0:200:23FF:FE53:B72A', 'rtt': 73},
                {'addr': '2012:AA:12::1', 'rtt': 73},
                {'addr': '2012:AA:1::1', 'rtt': 73},
                {'addr': '2012:AA:1:0:200:23FF:FE53:B72A', 'rtt': 73}
            ],
            '1': [
                {'addr': '2012:AA:1:0:200:23FF:FE53:B72A', 'rtt': 1},
                {'addr': '2012:AA:12::1', 'rtt': 1},
                {'addr': '2012:AA:12::1', 'rtt': 1}
            ],
            '2': [
                {'addr': '2012:AA:1:0:200:23FF:FE53:B72A', 'rtt': 1},
                {'addr': '2012:AA:12::1', 'rtt': 1},
                {'addr': '2012:AA:12::1', 'rtt': 1}
            ],
            '3': [
                {'addr': '2012:AA:1:0:200:23FF:FE53:B72A', 'rtt': 1},
                {'addr': '2012:AA:12::1', 'rtt': 1},
                {'addr': '2012:AA:12::1', 'rtt': 1}
            ],
            '4': [
                {'addr': '2012:AA:1:0:200:23FF:FE53:B72A', 'rtt': 1},
                {'addr': '2012:AA:12::1', 'rtt': 1},
                {'addr': '2012:AA:12::1', 'rtt': 1}
            ]
        },
        'statistics': {
            'send': 5,
            'received': 5,
            'success_rate_percent': 100.00,
            'multicast_replies': 19,
            'errors': 0,
            'round_trip': {
                'min_ms': 1,
                'avg_ms': 25,
                'max_ms': 73,
            }
        }
    }
}