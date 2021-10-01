

expected_output = {
    'mstag': {
        'risc': {
            'domain': 'risc',
            'interfaces': {
                'Bundle-Ether10.0': {
                    'interface': 'Bundle-Ether10.0',
                    'preempt_delay': False,
                    'name': 'risc',
                    'revision': 1,
                    'max_age': 20,
                    'provider_bridge': False,
                    'bridge_id': '0000.00ff.0002',
                    'port_id': 1,
                    'external_cost': 0,
                    'hello_time': 2,
                    'active': True,
                    'counters': {
                        'bdpu_sent': 39921,
                        },
                    },
                'instances': {
                    '0': {
                        'instance': 0,
                        'vlans': '1-2,4-4094',
                        'priority': 8192,
                        'port_priority': 128,
                        'cost': 0,
                        'root_bridge': '0000.00ff.0001',
                        'root_priority': 4096,
                        'counters': {
                            'topology_changes': 31,
                            },
                        },
                    '1': {
                        'instance': 1,
                        'vlans': '3',
                        'priority': 4096,
                        'port_priority': 128,
                        'cost': 0,
                        'root_bridge': '0000.00ff.0002',
                        'root_priority': 4096,
                        'counters': {
                            'topology_changes': 51,
                            },
                        },
                    },
                },
            },
        },
    }
