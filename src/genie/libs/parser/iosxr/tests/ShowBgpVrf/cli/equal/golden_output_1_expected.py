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
					'route_distinguisher': '50.1.1.4:1',
					'default_vrf': '2hub',
					'prefix': {
						'90.11.1.0/30': {
							'index': {
								1: {
									'next_hop': '90.33.1.2',
									'status_codes': '*>',
									'origin_codes': '?',
									'weight': '0',
									'path': '7000 100'
								}
							}
						},
						'90.12.1.0/30': {
							'index': {
								1: {
									'next_hop': '90.33.1.2',
									'status_codes': '*>',
									'origin_codes': '?',
									'weight': '0',
									'path': '7000 100'
								}
							}
						},
						'90.22.1.0/30': {
							'index': {
								1: {
									'next_hop': '90.33.1.2',
									'status_codes': '*>',
									'origin_codes': '?',
									'weight': '0',
									'path': '7000 100'
								}
							}
						},
						'90.33.1.0/30': {
							'index': {
								1: {
									'next_hop': '0.0.0.0',
									'status_codes': '*>',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '32768'
								}
							}
						},
						'90.33.1.4/30': {
							'index': {
								1: {
									'next_hop': '90.33.1.2',
									'status_codes': '*>',
									'origin_codes': '?',
									'weight': '0',
									'path': '7000 100'
								}
							}
						}
					},
					'processed_prefix': 5,
					'processed_paths': 5
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
					'route_distinguisher': '50.1.1.4:2',
					'default_vrf': '2spk',
					'prefix': {
						'90.11.1.0/30': {
							'index': {
								1: {
									'next_hop': '50.1.1.1',
									'status_codes': '*>i',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '100',
									'path': '0'
								}
							}
						},
						'90.12.1.0/30': {
							'index': {
								1: {
									'next_hop': '50.1.1.1',
									'status_codes': '*>i',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '100',
									'path': '0'
								}
							}
						},
						'90.22.1.0/30': {
							'index': {
								1: {
									'next_hop': '50.1.1.5',
									'status_codes': '*>i',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '100',
									'path': '0'
								}
							}
						},
						'90.33.1.4/30': {
							'index': {
								1: {
									'next_hop': '0.0.0.0',
									'status_codes': '*>',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '32768'
								}
							}
						}
					},
					'processed_prefix': 4,
					'processed_paths': 4
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
					'route_distinguisher': '50.1.1.4:0',
					'default_vrf': 'vrf_1',
					'prefix': {
						'50.0.0.1/32': {
							'index': {
								1: {
									'next_hop': '50.1.1.1',
									'status_codes': '*>i',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '100',
									'path': '0'
								}
							}
						},
						'70.3.3.3/32': {
							'index': {
								1: {
									'next_hop': '90.33.1.2',
									'status_codes': '*>',
									'origin_codes': 'i',
									'metric': '0',
									'weight': '0',
									'path': '7000'
								}
							}
						},
						'90.11.1.0/30': {
							'index': {
								1: {
									'next_hop': '50.1.1.1',
									'status_codes': '*>i',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '100',
									'path': '0'
								}
							}
						},
						'90.12.1.0/30': {
							'index': {
								1: {
									'next_hop': '50.1.1.1',
									'status_codes': '*>i',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '100',
									'path': '0'
								}
							}
						},
						'90.21.1.0/30': {
							'index': {
								1: {
									'next_hop': '50.1.1.5',
									'status_codes': '*>i',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '100',
									'path': '0'
								}
							}
						},
						'90.22.1.0/30': {
							'index': {
								1: {
									'next_hop': '50.1.1.5',
									'status_codes': '*>i',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '100',
									'path': '0'
								}
							}
						},
						'90.33.1.0/30': {
							'index': {
								1: {
									'next_hop': '0.0.0.0',
									'status_codes': '*>',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '32768'
								}
							}
						},
						'200.1.1.0/24': {
							'index': {
								1: {
									'next_hop': '50.1.1.1',
									'status_codes': '*>i',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '100',
									'path': '0'
								},
								2: {
									'next_hop': '50.1.1.5',
									'status_codes': '*i',
									'origin_codes': '?',
									'locprf': '0',
									'weight': '100',
									'path': '0'
								}
							}
						}
					},
					'processed_prefix': 8,
					'processed_paths': 9
				}
			}
		}
	}
}