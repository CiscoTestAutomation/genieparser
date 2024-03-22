expected_output = {
	'vrf': {
		'2hub': {
			'address_family': {
				'ipv4_unicast': {
					'bgp_vrf': '2hub',
					'vrf_state': 'active',
					'bgp_route_distinguisher': '50.1.1.4:1',
					'vrf_id': '0x60000003',
					'router_identifier': '50.1.1.4',
					'local_as': 100,
					'non_stop_routing': True,
					'table_state': 'active',
					'table_id': '0xe0000012',
					'rd_version': 1882,
					'bgp_table_version': 1882,
					'nsr_initial_initsync_version': '6',
					'nsr_initial_init_ver_status': 'reached',
					'nsr_issu_sync_group_versions': '0/0',
					'process': {
						'Speaker': {
							'rcvtblver': 1882,
							'brib_rib': 1882,
							'labelver': 1882,
							'importver': 1882,
							'sendtblver': 1882,
							'standbyver': 0
						}
					},
					'neighbor': {
						'90.33.1.2': {
							'remote_as': 7000,
							'spk': 0,
							'msg_rcvd': 211371,
							'msg_sent': 194462,
							'tbl_ver': 1882,
							'input_queue': 0,
							'output_queue': 0,
							'up_down': '19w2d',
							'state_pfxrcd': '4'
						}
					}
				}
			}
		},
		'2spk': {
			'address_family': {
				'ipv4_unicast': {
					'bgp_vrf': '2spk',
					'vrf_state': 'active',
					'bgp_route_distinguisher': '50.1.1.4:2',
					'vrf_id': '0x60000004',
					'router_identifier': '50.1.1.4',
					'local_as': 100,
					'non_stop_routing': True,
					'table_state': 'active',
					'table_id': '0xe0000013',
					'rd_version': 1882,
					'bgp_table_version': 1882,
					'nsr_initial_initsync_version': '6',
					'nsr_initial_init_ver_status': 'reached',
					'nsr_issu_sync_group_versions': '0/0',
					'process': {
						'Speaker': {
							'rcvtblver': 1882,
							'brib_rib': 1882,
							'labelver': 1882,
							'importver': 1882,
							'sendtblver': 1882,
							'standbyver': 0
						}
					},
					'neighbor': {
						'90.33.1.6': {
							'remote_as': 7000,
							'spk': 0,
							'msg_rcvd': 211260,
							'msg_sent': 194475,
							'tbl_ver': 1882,
							'input_queue': 0,
							'output_queue': 0,
							'up_down': '19w2d',
							'state_pfxrcd': '0'
						}
					}
				}
			}
		},
		'vrf_1': {
			'address_family': {
				'ipv4_unicast': {
					'bgp_vrf': 'vrf_1',
					'vrf_state': 'active',
					'bgp_route_distinguisher': '50.1.1.4:0',
					'vrf_id': '0x60000002',
					'router_identifier': '50.1.1.4',
					'local_as': 100,
					'non_stop_routing': True,
					'table_state': 'active',
					'table_id': '0xe0000011',
					'rd_version': 1882,
					'bgp_table_version': 1882,
					'nsr_initial_initsync_version': '6',
					'nsr_initial_init_ver_status': 'reached',
					'nsr_issu_sync_group_versions': '0/0',
					'process': {
						'Speaker': {
							'rcvtblver': 1882,
							'brib_rib': 1882,
							'labelver': 1882,
							'importver': 1882,
							'sendtblver': 1882,
							'standbyver': 0
						}
					},
					'neighbor': {
						'90.33.1.2': {
							'remote_as': 7000,
							'spk': 0,
							'msg_rcvd': 207417,
							'msg_sent': 191239,
							'tbl_ver': 1882,
							'input_queue': 0,
							'output_queue': 0,
							'up_down': '11w3d',
							'state_pfxrcd': '1'
						}
					}
				}
			}
		}
	}
}