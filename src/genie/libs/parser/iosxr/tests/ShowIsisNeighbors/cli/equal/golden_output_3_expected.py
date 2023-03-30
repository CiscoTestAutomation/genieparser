expected_output = {
	'isis': {
		'10': {
			'vrf': {
				'default': {
					'interfaces': {
						'Bundle-Ether10.10': {
							'neighbors': {
								'PE-9001-1': {
									'snpa': '5087.890d.27c3',
									'state': 'Up',
									'holdtime': '20',
									'type': 'L2',
									'ietf_nsf': 'Capable'
								}
							}
						},
						'GigabitEthernet0/0/0/1.19': {
							'neighbors': {
								'PE-9001-1': {
									'snpa': '28c7.cebd.7c23',
									'state': 'Up',
									'holdtime': '25',
									'type': 'L2',
									'ietf_nsf': 'Capable'
								}
							}
						}
					},
					'total_neighbor_count': 2
				}
			}
		}
	}
}