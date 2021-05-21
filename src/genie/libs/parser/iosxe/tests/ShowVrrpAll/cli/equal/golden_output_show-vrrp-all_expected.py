expected_output = {
    'interface': {
        'GigabitEthernet3.420': {
            'group': {
                10: {
                    'state': 'Master',
                    'virtual_ip_address': '10.13.120.254',
                    'virtual_mac_address': '0000.5e00.010a',
                    'advertise_interval_secs': 1.0,
                    'preemption': 'enabled',
                    'priority': 100,
                    'track_object': {
                        1: {
                            'state': 'Up',
                            'decrement': 15,
                            }
                    },
                    'master_router_ip': '10.13.120.1',
                    'master_router': 'local',
                    'master_router_priority': 100,
                    'master_advertisement_interval_secs': 1.0,
                    'master_down_interval_secs': 3.609,
                    'flags': '1/1'
                }
            }
        },
        'GigabitEthernet3.415': {
            'group': {
                13: {
                    'state': 'Master',
                    'virtual_ip_address': '10.13.115.254',
                    'virtual_mac_address': '0000.5e00.010d',
                    'advertise_interval_secs': 1.0,
                    'preemption': 'enabled',
                    'priority': 100,
                    'master_router_ip': '10.13.115.1',
                    'master_router': 'local',
                    'master_router_priority': 100,
                    'master_advertisement_interval_secs': 1.0,
                    'master_down_interval_secs': 3.609,
                    'flags': '1/1'
                }
            }
        }
    }
}

