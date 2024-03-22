expected_output = {
	'vrf': {
		'vrf_1': {
			'address_family': {
				'ipv6_unicast': {
					'bgp_vrf': 'vrf_1',
					'vrf_state': 'active',
					'bgp_route_distinguisher': '50.1.1.4:0',
					'vrf_id': '0x60000002',
					'router_identifier': '50.1.1.4',
					'local_as': 100,
					'non_stop_routing': True,
					'table_state': 'active',
					'table_id': '0xe0800011',
					'rd_version': 1412,
					'bgp_table_version': 1412,
					'nsr_initial_initsync_version': '6',
					'nsr_initial_init_ver_status': 'reached',
					'nsr_issu_sync_group_versions': '0/0',
					'process': {
						'Speaker': {
							'rcvtblver': 1412,
							'brib_rib': 1412,
							'labelver': 1412,
							'importver': 1412,
							'sendtblver': 1412,
							'standbyver': 0
						}
					},
					'neighbor': {
						'2000:90:33:1::2': {
							'remote_as': 7000,
							'spk': 0,
							'msg_rcvd': 243875,
							'msg_sent': 222416,
							'tbl_ver': 1412,
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