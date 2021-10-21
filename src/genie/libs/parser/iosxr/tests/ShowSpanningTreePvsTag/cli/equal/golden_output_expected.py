

expected_output = {
    'pvstag': {
        'foo': {
            'domain': 'foo',
            'interfaces': {
                'Bundle-Ether1000': {
                    'interface': 'Bundle-Ether1000',
                    'vlans': {
                        '2100': {
                            'preempt_delay': False,
                            'sub_interface': 'Bundle-Ether1000.2100',
                            'sub_interface_state': 'Up',
                            'max_age': 20,
                            'root_priority': 0,
                            'root_bridge': '0000.0000.0000',
                            'root_cost': 0,
                            'bridge_priority': 32768,
                            'bridge_id': '6c9c.edff.8d95',
                            'port_priority': 128,
                            'port_id': 1,
                            'hello_time': 2,
                            'active': True,
                            'counters': {
                                'bdpu_sent': 10,
                                'topology_changes': 0,
                                },
                            },
                        },
                    },
                },
            },
        },
    }
