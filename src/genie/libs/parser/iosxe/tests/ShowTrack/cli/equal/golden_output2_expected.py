expected_output = {
	'tracks': {
		2: {
			'type': 'IP route',
			'ip_address': '10.21.12.0',
            'subnet_mask': '255.255.255.0',
			'parameter': 'reachability',
			'reachability': {
				'parameter_state': 'Down',
                'issue': 'no ip route',
                'delayed': {
                    'delayed_state': 'Up',
                    'seconds_remaining': 1.0,
                    'connection_state': 'connected',
                },
				'change_count': 1,
				'last_change': '00:00:24',
			},
            'delay_up_seconds': 20.0,
            'delay_down_seconds': 10.0,
            'first_hop_interface_state': 'unknown',
            'prev_first_hop_interface': 'Ethernet1/0',
			'tracked_by': {
				1: {
					'name': 'HSRP',
					'interface': 'Ethernet0/0',
					'group_id': '3'
				},
                2: {
					'name': 'HSRP',
					'interface': 'Ethernet0/1',
					'group_id': '3'
				}
			}
		}
	}
}          