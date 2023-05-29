expected_output = {
	'interfaces': {
		'TenGigE0/0/2/0': {
			'interface': 'TenGigE0/0/2/0',
			'interface_status': 'down',
			'wait_to_restore_time': 5,
			'ssm': {
				'status': 'Enabled'
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
			'next_selection_points': 'SPA_RX_2'
		},
		'TenGigE0/0/2/1': {
			'interface': 'TenGigE0/0/2/1',
			'interface_status': 'up',
			'wait_to_restore_time': 5,
			'ssm': {
				'status': 'Enabled',
				'peer_time': '1d05h',
				'last_ssm_received': '0.650s ago',
				'esmc_ssms': {
					'sent': {
						'total': 106793,
						'information': 106792,
						'event': 1,
						'dnu_dus': 0
					},
					'received': {
						'total': 106788,
						'information': 106786,
						'event': 2,
						'dnu_dus': 106773
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
			'next_selection_points': 'SPA_RX_2'
		},
		'GigabitEthernet0/0/0/16': {
			'interface': 'GigabitEthernet0/0/0/16',
			'interface_status': 'up',
			'wait_to_restore_time': 5,
			'ssm': {
				'status': 'Enabled',
				'peer_time': '1d05h',
				'last_ssm_received': '0.651s ago',
				'esmc_ssms': {
					'sent': {
						'total': 106775,
						'information': 106774,
						'event': 1,
						'dnu_dus': 0
					},
					'received': {
						'total': 106775,
						'information': 106774,
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
		},
		'GigabitEthernet0/0/0/17': {
			'interface': 'GigabitEthernet0/0/0/17',
			'interface_status': 'down',
			'wait_to_restore_time': 5,
			'ssm': {
				'status': 'Enabled'
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