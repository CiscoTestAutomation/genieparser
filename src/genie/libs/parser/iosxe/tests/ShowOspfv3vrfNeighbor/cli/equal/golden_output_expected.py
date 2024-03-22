expected_output = {
    'process_id': 2,
    'address_family': 'ipv6',
    'router_id': '173.19.2.2',
    'vrfs': {
        2: {
            'neighbor_id': {
                '173.19.2.6': {
                    'priority': 1,
                    'state': 'FULL/DROTHER',
                    'dead_time': '00:00:39',
                    'address': 19,
                    'interface': 'GigabitEthernet0/0/3.11'
                },
                '173.19.3.8': {
                    'priority': 1,
                    'state': 'FULL/BDR',
                    'dead_time': '00:00:36',
                    'address': 15,
                    'interface': 'GigabitEthernet0/0/3.11'
                }
            }
        }
    }
}
