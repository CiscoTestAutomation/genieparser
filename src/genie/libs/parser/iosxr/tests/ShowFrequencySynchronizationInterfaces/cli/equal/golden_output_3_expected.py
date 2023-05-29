expected_output = {
	'interfaces': {
		'TenGigE0/0/2/0': {
			'interface': 'TenGigE0/0/2/0',
			'interface_status': 'shutdown',
			'selection': 'input',
			'wait_to_restore_time': 0,
			'ssm': {
				'status': 'Enabled'
			},
			'input': {
				'status': 'Down',
				'last_received_ql': 'Failed',
				'effective_ql': 'Failed',
				'priority': 5,
				'time_of_day_priority': 99
			},
			'output': {
				'selected_source': 'TenGigE0/0/2/1',
				'selected_source_ql': 'Opt-I/PRC',
				'effective_ql': 'Opt-I/PRC'
			},
			'next_selection_points': 'SPA_RX_2'
		},
		'TenGigE0/0/2/1': {
			'interface': 'TenGigE0/0/2/1',
			'interface_status': 'up',
			'selection': 'input',
			'wait_to_restore_time': 0,
			'ssm': {
				'status': 'Enabled',
				'peer_time': '1d02h',
				'last_ssm_received': '0.837s ago',
				'esmc_ssms': {
					'sent': {
						'total': 96052,
						'information': 96050,
						'event': 2,
						'dnu_dus': 96034
					},
					'received': {
						'total': 96051,
						'information': 96051,
						'event': 0,
						'dnu_dus': 0
					}
				}
			},
			'input': {
				'status': 'Up',
				'last_received_ql': 'Opt-I/PRC',
				'effective_ql': 'Opt-I/PRC',
				'priority': 10,
				'time_of_day_priority': 100
			},
			'output': {
				'selected_source': 'TenGigE0/0/2/1',
				'selected_source_ql': 'Opt-I/PRC',
				'effective_ql': 'DNU'
			},
			'next_selection_points': 'SPA_RX_2'
		},
		'GigabitEthernet0/0/0/2': {
			'interface': 'GigabitEthernet0/0/0/2',
			'interface_status': 'up',
			'wait_to_restore_time': 5,
			'ssm': {
				'status': 'Enabled',
				'peer_time': '1d02h',
				'last_ssm_received': 'never',
				'esmc_ssms': {
					'sent': {
						'total': 96039,
						'information': 96037,
						'event': 2,
						'dnu_dus': 0
					},
					'received': {
						'total': 0,
						'information': 0,
						'event': 0,
						'dnu_dus': 0
					}
				}
			},
			'input': {
				'status': 'Down',
				'selection': 'not assigned'
			},
			'output': {
				'selected_source': 'TenGigE0/0/2/1',
				'selected_source_ql': 'Opt-I/PRC',
				'effective_ql': 'Opt-I/PRC'
			},
			'next_selection_points': 'SPA_RX_0'
		},
		'GigabitEthernet0/0/0/16': {
			'interface': 'GigabitEthernet0/0/0/16',
			'interface_status': 'up',
			'selection': 'input',
			'wait_to_restore_time': 0,
			'ssm': {
				'status': 'Enabled',
				'peer_time': '1d02h',
				'last_ssm_received': '0.838s ago',
				'esmc_ssms': {
					'sent': {
						'total': 96037,
						'information': 96035,
						'event': 2,
						'dnu_dus': 0
					},
					'received': {
						'total': 96035,
						'information': 96034,
						'event': 1,
						'dnu_dus': 0
					}
				}
			},
			'input': {
				'status': 'Up',
				'last_received_ql': 'Opt-I/PRC',
				'effective_ql': 'Opt-I/PRC',
				'priority': 15,
				'time_of_day_priority': 101
			},
			'output': {
				'selected_source': 'TenGigE0/0/2/1',
				'selected_source_ql': 'Opt-I/PRC',
				'effective_ql': 'Opt-I/PRC'
			},
			'next_selection_points': 'SPA_RX_0'
		},
		'GigabitEthernet0/0/0/17': {
			'interface': 'GigabitEthernet0/0/0/17',
			'interface_status': 'shutdown',
			'selection': 'input',
			'wait_to_restore_time': 0,
			'ssm': {
				'status': 'Enabled'
			},
			'input': {
				'status': 'Down',
				'last_received_ql': 'Failed',
				'effective_ql': 'Failed',
				'priority': 15,
				'time_of_day_priority': 101
			},
			'output': {
				'selected_source': 'TenGigE0/0/2/1',
				'selected_source_ql': 'Opt-I/PRC',
				'effective_ql': 'Opt-I/PRC'
			},
			'next_selection_points': 'SPA_RX_0'
		}
	}
}