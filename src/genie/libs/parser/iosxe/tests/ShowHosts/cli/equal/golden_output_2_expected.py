expected_output = {
    'default_domain': 'cisco.com',
    'name_servers': ['8.8.8.8', '8.8.4.4', '171.70.168.183'],
    'hosts': {
        'router1.cisco.com': {
            'ttl': 3600,
            'class': 'IN',
            'type': 'A',
            'data': '10.1.1.1'
        },
        'router2.cisco.com': {
            'ttl': 3600,
            'class': 'IN',
            'type': 'A',
            'data': '10.1.1.2'
        },
        'server.example.com': {
            'ttl': 7200,
            'class': 'IN',
            'type': 'A',
            'data': '192.168.1.100'
        },
        '1.1.1.10.in-addr.arpa': {
            'ttl': 300,
            'class': 'IN',
            'type': 'PTR',
            'data': 'router1.cisco.com'
        }
    }
}