

expected_output = {
    'mstag': {
        'A': {
            'domain': 'A',
            'interfaces': {
                'GigabitEthernet0/0/0/1': {
                    'interface': 'GigabitEthernet0/0/0/1',
                    'preempt_delay': False,
                    'name': '6161:6161:6161',
                    'revision': 0,
                    'max_age': 20,
                    'provider_bridge': False,
                    'bridge_id': '6161.61ff.c2c2',
                    'port_id': 1,
                    'external_cost': 0,
                    'hello_time': 2,
                    'active': False,
                    'counters': {
                        'bdpu_sent': 0,
                        },
                    },
                'instances': {
                    '0': {
                        'instance': 0,
                        'vlans': '1-9,32-39,41-4094',
                        'priority': 32768,
                        'port_priority': 128,
                        'cost': 0,
                        'root_bridge': '6161.61ff.c2c2',
                        'root_priority': 32768,
                        'counters': {
                            'topology_changes': 123,
                            },
                        },
                    '2': {
                        'instance': 2,
                        'vlans': '10-31',
                        'priority': 32768,
                        'port_priority': 128,
                        'cost': 0,
                        'root_bridge': '6161.61ff.c2c2',
                        'root_priority': 32768,
                        'counters': {
                            'topology_changes': 123,
                            },
                        },
                    '10': {
                        'instance': 10,
                        'vlans': '40',
                        'priority': 32768,
                        'port_priority': 128,
                        'cost': 200000000,
                        'root_bridge': '6161.61ff.c2c2',
                        'root_priority': 61440,
                        'counters': {
                            'topology_changes': 0,
                            },
                        },
                    },
                },
            },
        },
    }
