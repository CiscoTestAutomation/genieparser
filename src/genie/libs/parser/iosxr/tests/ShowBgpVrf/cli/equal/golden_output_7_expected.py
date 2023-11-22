expected_output = {
	'vrf': {
		'srv6_l3vpn_be': {
			'address_family': {
				'ipv4_unicast': {
					'bgp_vrf': 'srv6_l3vpn_be',
					'vrf_state': 'active',
					'bgp_route_distinguisher': '100:1',
					'vrf_id': '0x60000002',
					'router_identifier': '10.0.0.1',
					'local_as': 100,
					'non_stop_routing': True,
					'table_state': 'active',
					'table_id': '0xe0000002',
					'rd_version': 89,
					'bgp_table_version': 89,
					'nsr_initial_initsync_version': '4',
					'nsr_initial_init_ver_status': 'reached',
					'nsr_issu_sync_group_versions': '0/0',
					'route_distinguisher': '100:1',
					'default_vrf': 'srv6_l3vpn_be',
					'prefix': {
						'1.1.1.1/32': {
							'index': {
								1: {
									'local_sid': 'fc00:c000:1001:e000::',
									'status_codes': '*>',
									'alloc_mode': 'per-vrf',
									'locator': 'main'
								}
							}
						},
						'3.3.3.3/32': {
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
						'100.0.0.1/32': {
							'index': {
								1: {
									'local_sid': 'fc00:c000:1001:e000::',
									'status_codes': '*>',
									'alloc_mode': 'per-vrf',
									'locator': 'main'
								}
							}
						},
						'100.0.0.2/32': {
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
						'192.168.111.0/24': {
							'index': {
								1: {
									'local_sid': 'fc00:c000:1001:e000::',
									'status_codes': '*>',
									'alloc_mode': 'per-vrf',
									'locator': 'main'
								}
							}
						},
						'192.168.112.0/24': {
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
						'192.168.213.0/24': {
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
						'200.0.0.3/32': {
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
						}
					},
					'processed_prefix': 8,
					'processed_paths': 13
				}
			}
		}
	}
}