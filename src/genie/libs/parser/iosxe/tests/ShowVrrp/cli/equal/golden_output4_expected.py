expected_output = {
    'interface': {
        'GigabitEthernet0/0/3.129': {
            'group': {
                4: {
                    'state': 'BACKUP',
                    'description': 'State duration 2 weeks 2 days 14 hours',
                    'virtual_ip_address': '173.29.2.200',
                    'virtual_mac_address': '0000.5E00.0104',
                    'advertise_interval_secs': 1.0,
                    'preemption': 'enabled',
                    'priority': 70,
                    'track_object': {
                        55: {
                            'decrement': 20,
                            'state': 'DOWN'
                        }
                    },
                    'master_router_ip': '173.29.2.6',
                    'master_router_priority': 85,
                    'master_advertisement_interval_secs': 1.0,
                    'master_down_interval_secs': 3726.0,
                    'master_down_expiration_secs': 3.326,
                    'flags': '0/1'
                }
            }
        }
    }
}
