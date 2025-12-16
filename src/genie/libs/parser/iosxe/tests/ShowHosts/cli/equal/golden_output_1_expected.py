expected_output = {
    'name_servers': ['171.70.168.183'],
    'hosts': {
        '252.254.255.223.in-addr.arpa': {
            'ttl': 10,
            'class': 'IN',
            'type': 'PTR',
            'data': 'sj20lab-tftp1'
        },
        'sj20lab-tftp1': {
            'ttl': 10,
            'class': 'IN',
            'type': 'A',
            'data': '223.255.254.252'
        }
    }
}