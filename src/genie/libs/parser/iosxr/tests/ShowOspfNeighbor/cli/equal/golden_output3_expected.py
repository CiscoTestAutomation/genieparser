expected_output = {
    'vrfs': {
        'default': {
            'neighbors': {
                '192.168.199.137': {
                    'priority': '1',
                    'state': 'FULL/DR',
                    'dead_time': '0:00:31',
                    'address': '172.31.80.37',
                    'interface': 'GigabitEthernet 0/3/0/2',
                    'up_time': '18:45:22'
                },
                '192.168.48.1': {
                    'priority': '1',
                    'state': 'FULL/DROTHER',
                    'dead_time': '0:00:33',
                    'address': '192.168.48.1',
                    'interface': 'GigabitEthernet 0/3/0/3',
                    'up_time': '18:45:30'
                },
                '192.168.48.200': {
                    'priority': '1',
                    'state': 'FULL/DROTHER',
                    'dead_time': '0:00:33',
                    'address': '192.168.48.200',
                    'interface': 'GigabitEthernet 0/3/0/3',
                    'up_time': '18:45:25'
                },
                '192.168.199.138': {
                    'priority': '5',
                    'state': 'FULL/DR',
                    'dead_time': '0:00:33',
                    'address': '192.168.48.189',
                    'interface': 'GigabitEthernet 0/3/0/3',
                    'up_time': '18:45:27'
                },
            },
        },
    },
}