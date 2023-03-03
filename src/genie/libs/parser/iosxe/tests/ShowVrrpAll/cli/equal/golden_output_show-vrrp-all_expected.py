expected_output = {
    'interface': {
        'GigabitEthernet3.420': {
            'group': {
                10: {
                    'state': 'Master',
                    'virtual_ip_address': '10.13.120.254',
                    'virtual_mac_address': '0000.5eff.010a',
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
                    'virtual_mac_address': '0000.5eff.010d',
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
        },
        'GigabitEthernet1/0/19': {
            'group': {
                1: {
                    'description': 'single_Vrrp', 
                    'state': 'MASTER',
                    'state_duration': {
                        'minutes': 0, 
                        'seconds': 23.134
                    }, 
                    'virtual_ip_address': '10.50.10.104', 
                    'virtual_mac_address': '0000.5E00.0101', 
                    'advertise_interval_secs': 1.0, 
                    'preemption': 'enabled', 
                    'priority': 100, 
                    'master_router_ip': '10.50.10.106', 
                    'master_router': 'local', 
                    'master_router_priority': 100, 
                    'master_advertisement_interval_secs': 1.0, 
                    'master_advertisement_expiration_secs': 0.441, 
                    'master_down_interval_secs': 'unknown', 
                    'flags': '1/1'
                }
            }
        },
        'GigabitEthernet1/0/20': {
                'group': {
                    1: {
                        'description': 'single_Vrrp', 
                        'state': 'INIT', 
                        'state_duration': {
                            'minutes': 20, 
                            'seconds': 5.224
                            }, 
                        'virtual_ip_address': 'no address', 
                        'virtual_mac_address': '0000.5E00.0101', 
                        'advertise_interval_secs': 40.95, 
                        'preemption': 'enabled', 
                        'priority': 200, 
                        'master_router_ip': 'unknown', 
                        'master_router_priority': 'unknown', 
                        'master_advertisement_interval_secs': 'unknown', 
                        'master_down_interval_secs': 'unknown', 
                        'flags': '0/0'
                }
            }
        }
    }
}

