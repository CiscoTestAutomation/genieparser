expected_output = {
	'interfaces': {
		'GigabitEthernet0/0/0/16': {
			'interface': 'GigabitEthernet0/0/0/16',
			'interface_status': 'up',
			'wait_to_restore_time': 5,
			'ssm': {
				'status': 'Enabled',
				'peer_time': '1d05h',
				'last_ssm_received': '0.549s ago',
				'esmc_ssms': {
					'sent': {
						'total': 107715,
						'information': 107714,
						'event': 1,
						'dnu_dus': 0
					},
					'received': {
						'total': 107715,
						'information': 107714,
						'event': 1,
						'dnu_dus': 0
					}
				}
			},
			'input': {
				'status': 'Down',
				'selection': 'not assigned'
			},
			'output': {
				'selected_source': 'PTP [0/RSP0/CPU0]',
				'selected_source_ql': 'Opt-I/PRC',
				'effective_ql': 'Opt-I/PRC'
			},
			'next_selection_points': 'SPA_RX_0'
		}
	}
}