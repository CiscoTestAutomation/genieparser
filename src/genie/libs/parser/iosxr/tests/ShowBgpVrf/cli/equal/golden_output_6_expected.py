expected_output = {
	'vrf': {
		'srv6_l3vpn_be': {
			'address_family': {
				'ipv6_unicast': {
					'bgp_vrf': 'srv6_l3vpn_be',
					'vrf_state': 'active',
					'bgp_route_distinguisher': '100:1',
					'vrf_id': '0x60000002',
					'router_identifier': '10.0.0.1',
					'local_as': 100,
					'non_stop_routing': True,
					'table_state': 'active',
					'table_id': '0xe0800002',
					'rd_version': 86,
					'bgp_table_version': 86,
					'nsr_initial_initsync_version': '5',
					'nsr_initial_init_ver_status': 'reached',
					'nsr_issu_sync_group_versions': '0/0',
					'route_distinguisher': '100:1',
					'default_vrf': 'srv6_l3vpn_be',
					'prefix': {
						'fc00:a000:1000:100::1/128': {
							'index': {
								1: {
									'status_codes': '*>',
									'local_sid': 'fc00:c000:1001:e001::',
									'alloc_mode': 'per-vrf',
									'locator': 'main'
								}
							}
						},
						'fc00:a000:1000:100::2/128': {
							'index': {
								1: {
									'status_codes': '*>i',
									'local_sid': 'NO SRv6 Sid',
									'alloc_mode': '-',
									'locator': '-'
								},
								2: {
									'local_sid': 'NO SRv6 Sid',
									'status_codes': '*i',
									'alloc_mode': '-',
									'locator': '-'
								}
							}
						},
						'fc00:a000:2000:200::3/128': {
							'index': {
								1: {
									'status_codes': '*>i',
									'local_sid': 'NO SRv6 Sid',
									'alloc_mode': '-',
									'locator': '-'
								},
								2: {
									'local_sid': 'NO SRv6 Sid',
									'status_codes': '*i',
									'alloc_mode': '-',
									'locator': '-'
								}
							}
						},
						'fd00::1/128': {
							'index': {
								1: {
									'local_sid': 'fc00:c000:1001:e001::',
									'status_codes': '*>',
									'alloc_mode': 'per-vrf',
									'locator': 'main'
								}
							}
						},
						'fd00::3/128': {
							'index': {
								1: {
									'local_sid': 'NO SRv6 Sid',
									'status_codes': '*>i',
									'alloc_mode': '-',
									'locator': '-'
								},
								2: {
									'local_sid': 'NO SRv6 Sid',
									'status_codes': '*i',
									'alloc_mode': '-',
									'locator': '-'
								}
							}
						},
						'fd00:ffff:100:11::/64': {
							'index': {
								1: {
									'status_codes': '*>',
									'local_sid': 'fc00:c000:1001:e001::',
									'alloc_mode': 'per-vrf',
									'locator': 'main'
								}
							}
						},
						'fd00:ffff:100:12::/64': {
							'index': {
								1: {
									'status_codes': '*>i',
									'local_sid': 'NO SRv6 Sid',
									'alloc_mode': '-',
									'locator': '-'
								},
								2: {
									'local_sid': 'NO SRv6 Sid',
									'status_codes': '*i',
									'alloc_mode': '-',
									'locator': '-'
								}
							}
						},
						'fd00:ffff:200:13::/64': {
							'index': {
								1: {
									'status_codes': '*>i',
									'local_sid': 'NO SRv6 Sid',
									'alloc_mode': '-',
									'locator': '-'
								},
								2: {
									'local_sid': 'NO SRv6 Sid',
									'status_codes': '*i',
									'alloc_mode': '-',
									'locator': '-'
								}
							}
						}
					},
					'processed_prefix': 8,
					'processed_paths': 13
				}
			}
		}
	}
}