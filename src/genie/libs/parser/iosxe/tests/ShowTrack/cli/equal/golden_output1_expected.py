expected_output = {
    'tracks': {
        1: {
            'type': 'Interface',
            'name': 'GigabitEthernet3.420',
            'parameter': 'line-protocol',
            'line_protocol': {
                'parameter_state': 'Up',
                'change_count': 1,
                'last_change': '00:00:27',
            },
            'tracked_by': {
                1: {
                    'name': 'VRRP',
                    'interface': 'GigabitEthernet3.420',
                    'group_id': '10'
                }
            }
        }
    }
}
