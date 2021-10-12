

expected_output = {
    'pvrstag': {
        'foo': {
            'domain': 'foo',
            'interfaces': {
                'GigabitEthernet0/0/0/0': {
                    'interface': 'GigabitEthernet0/0/0/0',
                    'vlans': {
                        '5': {
                            'preempt_delay': True,
                            'preempt_delay_state': 'Sending startup BPDU until 13:38:03',
                            'sub_interface': 'GigabitEthernet0/0/0/0.5',
                            'sub_interface_state': 'Up',
                            'max_age': 20,
                            'root_priority': 0,
                            'root_bridge': '0000.0000.0000',
                            'root_cost': 1,
                            'bridge_priority': 32768,
                            'bridge_id': '0255.1dff.3c70',
                            'port_priority': 128,
                            'port_id': 1,
                            'hello_time': 2,
                            'active': True,
                            'counters': {
                                'bdpu_sent': 6,
                                'topology_changes': 0,
                                },
                            },
                        },
                    },
                'GigabitEthernet0/0/0/1': {
                    'interface': 'GigabitEthernet0/0/0/1',
                    'vlans': {
                        '5': {
                            'preempt_delay': True,
                            'preempt_delay_state': 'Sending standard BPDU',
                            'sub_interface': 'GigabitEthernet0/0/0/1.5',
                            'sub_interface_state': 'Up',
                            'max_age': 20,
                            'root_priority': 0,
                            'root_bridge': '0000.0000.0000',
                            'root_cost': 0,
                            'bridge_priority': 32768,
                            'bridge_id': '021a.9eff.5645',
                            'port_priority': 128,
                            'port_id': 1,
                            'hello_time': 2,
                            'active': True,
                            'counters': {
                                'bdpu_sent': 7,
                                'topology_changes': 0,
                                },
                            },
                        },
                    },
                },
            },
        },
    }
