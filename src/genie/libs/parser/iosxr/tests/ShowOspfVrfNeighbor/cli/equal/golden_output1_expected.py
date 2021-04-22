expected_output = {
    'process_name': 'mpls1',
    'vrf': 'all-inclusive',
    'neighbors': {
        '100.10.0.2': {
            'neighbor_id': '100.100.100.100',
            'priority': '1',
            'state': 'FULL/  -',
            'dead_time': '00:00:38',
            'interface': 'GigabitEthernet0/0/0/0',
            'up_time': '2d18h'
        },
        '100.20.0.2': {
            'neighbor_id': '95.95.95.95',
            'priority': '1',
            'state': 'FULL/  -',
            'dead_time': '00:00:38',
            'interface': 'GigabitEthernet0/0/0/1',
            'up_time': '2d18h'
        },
    },
    'total_neighbor_count': 2,
}
