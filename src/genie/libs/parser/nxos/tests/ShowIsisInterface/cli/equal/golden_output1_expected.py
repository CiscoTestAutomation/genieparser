expected_output = {
	'instance': {
		'1': {
			'vrf': {
				'default': {
					'interfaces': {
						'Ethernet1/1': {
							'name': 'Ethernet1/1',
							'status': 'protocol-up/link-up/admin-up',
							'ipv4': '9.9.9.1',
							'ipv4_subnet': '9.9.9.0/24',
							'authentication': {
								'level_1': {
									'auth_check': 'set'
								},
								'level_2': {
									'auth_check': 'set'
								}
							},
							'index': '0x0001',
							'local_circuit_id': '0x01',
							'circuit_type': 'L1-2',
							'bfd_ipv4': 'locally disabled',
							'bfd_ipv6': 'locally disabled',
							'mtr': 'disabled',
							'mtu': 1500,
							'lsp_interval_ms': 33,
							'levels': {
								'1': {
									'designated_is': 'uut1'
								},
								'2': {
									'designated_is': 'uut1'
								}
							},
							'topologies': {
								'0': {
									'level': {
										'1': {
											'metric': '40',
											'metric_cfg': 'no',
											'fwdng': 'UP',
											'ipv4_mt': 'UP',
											'ipv4_cfg': 'yes',
											'ipv6_mt': 'DN',
											'ipv6_cfg': 'no'
										},
										'2': {
											'metric': '40',
											'metric_cfg': 'no',
											'fwdng': 'UP',
											'ipv4_mt': 'UP',
											'ipv4_cfg': 'yes',
											'ipv6_mt': 'DN',
											'ipv6_cfg': 'no'
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}