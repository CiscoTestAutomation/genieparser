

expected_output = {
    'interfaces': {
        'TenGigE0/0/0/28/0': {
            'port_id': {
                'xe-0/1/2': {
                    'neighbors': {
                        'switch1': {
                            'capabilities': {
                                'bridge': {
                                    'enabled': True,
                                    'system': True,
                                },
                                'router': {
                                    'enabled': True,
                                    'system': True,
                                },
                            },
                            'chassis_id': '6464.9bff.6e31',
                            'hold_time': 120,
                            'neighbor_id': 'switch1',
                            'peer_mac': '64:64:9b:ff:6e:66',
                            'port_description': 'port description',
                            'system_description': '',
                            'system_name': 'switch1',
                            'time_remaining': 108,
                        },
                    },
                },
            },
        },
    },
    'total_entries': 1,
}
