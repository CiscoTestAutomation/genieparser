expected_output = {
    'address_family': {
        'ipv4': {
            'process_id': 100, 
            'vrf_id': 'WAN-VRF', 
            'router_id': '10.0.2.38', 
            'FiveGigabitEthernet1/0/24': {
                'neighbor_id': '101.1.1.2', 
                'priority': 1, 
                'state': 'FULL/BDR', 
                'dead_time': '00:00:38', 
                'int_id': 167
            }
        }, 
        'ipv6': {
            'process_id': 100, 
            'vrf_id': 'WAN-VRF', 
            'router_id': '10.0.2.38', 
            'FiveGigabitEthernet1/0/24': {
                'neighbor_id': '101.1.1.2', 
                'priority': 1, 
                'state': 'FULL/BDR', 
                'dead_time': '00:00:33', 
                'int_id': 167
            }
        }
    }
}