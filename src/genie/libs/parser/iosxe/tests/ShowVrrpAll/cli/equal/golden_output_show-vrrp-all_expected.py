expected_output = {
    'interfaces': {
        'GigabitEthernet3.420': {
            'group_number': 10,
            'advertise_interval_secs': 1.0,
            'master_advertisement_interval_secs': 1.0,
            'master_down_interval_secs': 3.609,
            'master_router_ip': '10.13.120.1',
            'master_router': 'local',
            'master_router_priority': 100,
            'preemption': 'enabled',
            'priority': 100,
            'virtual_ip_address': '10.13.120.254',
            'virtual_mac_address': '0000.5e00.010a',
            'state': 'Master',
            'track_object': { 
                1: {
                    'decrement': 15,
                    'state': 'Up',
                    }                        
            },
            'flags': '1/1'   
        },
        'GigabitEthernet3.415': {
            'group_number': 13,
            'advertise_interval_secs': 1.0,
            'master_advertisement_interval_secs': 1.0,
            'master_down_interval_secs': 3.609,
            'master_router_ip': '10.13.115.1',
            'master_router': 'local',
            'master_router_priority': 100,
            'preemption': 'enabled',
            'priority': 100,
            'virtual_ip_address': '10.13.115.254',
            'virtual_mac_address': '0000.5e00.010d',
            'state': 'Master',
            'flags': '1/1' 
        }
    }
}

