expected_output = {
	'instance': {
		'SRv6': {
			'level': {
				2: {
					'lspid': {
						'A-AN1.00-00': {
							'lsp': {
								'seq_num': '0x000006a2',
								'checksum': '0x2105',
								'local_router': True,
								'holdtime': 336,
								'attach_bit': 0,
								'p_bit': 0,
								'overload_bit': 0
							},
							'area_address': '49.0001.0010',
							'mt_srv6_locator': {
								'locator_prefix': 'fc00:c000:1001::',
								'locator_prefix_length': 48,
								'd_flag': 0,
								'metric': 0,
								'algorithm': 0
							},
							'nlpid': ['0x8e'],
							'hostname': 'A-AN1',
							'ipv6_address': 'fc00:a000:1000::1',
							'mt_ipv6_reachability': {
								'fc00:a000:1000::1/128': {
									'ip_prefix': 'fc00:a000:1000::1',
									'prefix_length': '128',
									'metric': 0
								},
								'fc00:b000::1:2:0/126': {
									'ip_prefix': 'fc00:b000::1:2:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::1:11:0/126': {
									'ip_prefix': 'fc00:b000::1:11:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:c000:1001::/48': {
									'ip_prefix': 'fc00:c000:1001::',
									'prefix_length': '48',
									'metric': 1
								}
							},
							'router_cap': '0.0.0.0 D:0 S:0',
							'mt_entries': {
								'IPv6 Unicast': {
									'attach_bit': 0,
									'p_bit': 0,
									'overload_bit': 0
								}
							},
							'mt_is_neighbor': {
								'A-AN2.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'A-AG1.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								}
							}
						},
						'A-AN2.00-00': {
							'lsp': {
								'seq_num': '0x0000069e',
								'checksum': '0xbf5a',
								'local_router': False,
								'holdtime': 681,
								'received': 1200,
								'attach_bit': 0,
								'p_bit': 0,
								'overload_bit': 0
							},
							'area_address': '49.0001.0010',
							'mt_srv6_locator': {
								'locator_prefix': 'fc00:c000:1002::',
								'locator_prefix_length': 48,
								'd_flag': 0,
								'metric': 0,
								'algorithm': 0
							},
							'nlpid': ['0x8e'],
							'hostname': 'A-AN2',
							'ipv6_address': 'fc00:a000:1000::2',
							'mt_ipv6_reachability': {
								'fc00:a000:1000::2/128': {
									'ip_prefix': 'fc00:a000:1000::2',
									'prefix_length': '128',
									'metric': 0
								},
								'fc00:b000::1:2:0/126': {
									'ip_prefix': 'fc00:b000::1:2:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::2:12:0/126': {
									'ip_prefix': 'fc00:b000::2:12:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:c000:1002::/48': {
									'ip_prefix': 'fc00:c000:1002::',
									'prefix_length': '48',
									'metric': 1
								}
							},
							'router_cap': '0.0.0.0 D:0 S:0',
							'mt_entries': {
								'IPv6 Unicast': {
									'attach_bit': 0,
									'p_bit': 0,
									'overload_bit': 0
								}
							},
							'mt_is_neighbor': {
								'A-AG2.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'A-AN1.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								}
							}
						},
						'B-AN1.00-00': {
							'lsp': {
								'seq_num': '0x000006a3',
								'checksum': '0xfc41',
								'local_router': False,
								'holdtime': 620,
								'received': 1200,
								'attach_bit': 0,
								'p_bit': 0,
								'overload_bit': 0
							},
							'area_address': '49.0001.0010',
							'mt_srv6_locator': {
								'locator_prefix': 'fc00:c000:2003::',
								'locator_prefix_length': 48,
								'd_flag': 0,
								'metric': 0,
								'algorithm': 0
							},
							'nlpid': ['0x8e'],
							'hostname': 'B-AN1',
							'ipv6_address': 'fc00:a000:2000::3',
							'mt_ipv6_reachability': {
								'fc00:a000:2000::3/128': {
									'ip_prefix': 'fc00:a000:2000::3',
									'prefix_length': '128',
									'metric': 0
								},
								'fc00:b000::3:13:0/126': {
									'ip_prefix': 'fc00:b000::3:13:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::3:14:0/126': {
									'ip_prefix': 'fc00:b000::3:14:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:c000:2003::/48': {
									'ip_prefix': 'fc00:c000:2003::',
									'prefix_length': '48',
									'metric': 1
								}
							},
							'router_cap': '0.0.0.0 D:0 S:0',
							'mt_entries': {
								'IPv6 Unicast': {
									'attach_bit': 0,
									'p_bit': 0,
									'overload_bit': 0
								}
							},
							'mt_is_neighbor': {
								'B-AG1.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'B-AG2.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								}
							}
						},
						'A-AG1.00-00': {
							'lsp': {
								'seq_num': '0x000006a0',
								'checksum': '0xb23d',
								'local_router': False,
								'holdtime': 429,
								'received': 1200,
								'attach_bit': 0,
								'p_bit': 0,
								'overload_bit': 0
							},
							'area_address': '49.0001.0010',
							'mt_srv6_locator': {
								'locator_prefix': 'fc00:c000:1011::',
								'locator_prefix_length': 48,
								'd_flag': 0,
								'metric': 0,
								'algorithm': 0
							},
							'nlpid': ['0x8e'],
							'hostname': 'A-AG1',
							'ipv6_address': 'fc00:a000:1000::11',
							'mt_ipv6_reachability': {
								'fc00:a000:1000::11/128': {
									'ip_prefix': 'fc00:a000:1000::11',
									'prefix_length': '128',
									'metric': 0
								},
								'fc00:b000::1:11:0/126': {
									'ip_prefix': 'fc00:b000::1:11:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::11:12:0/126': {
									'ip_prefix': 'fc00:b000::11:12:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::11:13:0/126': {
									'ip_prefix': 'fc00:b000::11:13:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::11:15:0/126': {
									'ip_prefix': 'fc00:b000::11:15:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:c000:1011::/48': {
									'ip_prefix': 'fc00:c000:1011::',
									'prefix_length': '48',
									'metric': 1
								}
							},
							'router_cap': '0.0.0.0 D:0 S:0',
							'mt_entries': {
								'IPv6 Unicast': {
									'attach_bit': 0,
									'p_bit': 0,
									'overload_bit': 0
								}
							},
							'mt_is_neighbor': {
								'A-AN1.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'B-AG1.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'A-AG2.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								}
							}
						},
						'A-AG2.00-00': {
							'lsp': {
								'seq_num': '0x000000f3',
								'checksum': '0xc763',
								'local_router': False,
								'holdtime': 976,
								'received': 1200,
								'attach_bit': 0,
								'p_bit': 0,
								'overload_bit': 0
							},
							'area_address': '49.0001.0010',
							'mt_srv6_locator': {
								'locator_prefix': 'fc00:c000:1012::',
								'locator_prefix_length': 48,
								'd_flag': 0,
								'metric': 0,
								'algorithm': 0
							},
							'nlpid': ['0x8e'],
							'hostname': 'A-AG2',
							'ipv6_address': 'fc00:a000:1000::12',
							'mt_ipv6_reachability': {
								'fc00:a000:1000::12/128': {
									'ip_prefix': 'fc00:a000:1000::12',
									'prefix_length': '128',
									'metric': 0
								},
								'fc00:b000::2:12:0/126': {
									'ip_prefix': 'fc00:b000::2:12:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::11:12:0/126': {
									'ip_prefix': 'fc00:b000::11:12:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::12:14:0/126': {
									'ip_prefix': 'fc00:b000::12:14:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:c000:1012::/48': {
									'ip_prefix': 'fc00:c000:1012::',
									'prefix_length': '48',
									'metric': 1
								}
							},
							'router_cap': '0.0.0.0 D:0 S:0',
							'mt_entries': {
								'IPv6 Unicast': {
									'attach_bit': 0,
									'p_bit': 0,
									'overload_bit': 0
								}
							},
							'mt_is_neighbor': {
								'A-AN2.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'B-AG2.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'A-AG1.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								}
							}
						},
						'B-AG1.00-00': {
							'lsp': {
								'seq_num': '0x000006a9',
								'checksum': '0x8643',
								'local_router': False,
								'holdtime': 681,
								'received': 1200,
								'attach_bit': 0,
								'p_bit': 0,
								'overload_bit': 0
							},
							'area_address': '49.0001.0010',
							'mt_srv6_locator': {
								'locator_prefix': 'fc00:c000:2013::',
								'locator_prefix_length': 48,
								'd_flag': 0,
								'metric': 0,
								'algorithm': 0
							},
							'nlpid': ['0x8e'],
							'hostname': 'B-AG1',
							'ipv6_address': 'fc00:a000:2000::13',
							'mt_ipv6_reachability': {
								'fc00:a000:2000::13/128': {
									'ip_prefix': 'fc00:a000:2000::13',
									'prefix_length': '128',
									'metric': 0
								},
								'fc00:b000::3:13:0/126': {
									'ip_prefix': 'fc00:b000::3:13:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::11:13:0/126': {
									'ip_prefix': 'fc00:b000::11:13:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::13:14:0/126': {
									'ip_prefix': 'fc00:b000::13:14:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:c000:2013::/48': {
									'ip_prefix': 'fc00:c000:2013::',
									'prefix_length': '48',
									'metric': 1
								}
							},
							'router_cap': '0.0.0.0 D:0 S:0',
							'mt_entries': {
								'IPv6 Unicast': {
									'attach_bit': 0,
									'p_bit': 0,
									'overload_bit': 0
								}
							},
							'mt_is_neighbor': {
								'A-AG1.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'B-AG2.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'B-AN1.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								}
							}
						},
						'B-AG2.00-00': {
							'lsp': {
								'seq_num': '0x000006ab',
								'checksum': '0xe7f4',
								'local_router': False,
								'holdtime': 776,
								'received': 1200,
								'attach_bit': 0,
								'p_bit': 0,
								'overload_bit': 0
							},
							'area_address': '49.0001.0010',
							'mt_srv6_locator': {
								'locator_prefix': 'fc00:c000:2014::',
								'locator_prefix_length': 48,
								'd_flag': 0,
								'metric': 0,
								'algorithm': 0
							},
							'nlpid': ['0x8e'],
							'hostname': 'B-AG2',
							'ipv6_address': 'fc00:a000:2000::14',
							'mt_ipv6_reachability': {
								'fc00:a000:2000::14/128': {
									'ip_prefix': 'fc00:a000:2000::14',
									'prefix_length': '128',
									'metric': 0
								},
								'fc00:b000::3:14:0/126': {
									'ip_prefix': 'fc00:b000::3:14:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::12:14:0/126': {
									'ip_prefix': 'fc00:b000::12:14:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::13:14:0/126': {
									'ip_prefix': 'fc00:b000::13:14:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:b000::14:16:0/126': {
									'ip_prefix': 'fc00:b000::14:16:0',
									'prefix_length': '126',
									'metric': 10
								},
								'fc00:c000:2014::/48': {
									'ip_prefix': 'fc00:c000:2014::',
									'prefix_length': '48',
									'metric': 1
								}
							},
							'router_cap': '0.0.0.0 D:0 S:0',
							'mt_entries': {
								'IPv6 Unicast': {
									'attach_bit': 0,
									'p_bit': 0,
									'overload_bit': 0
								}
							},
							'mt_is_neighbor': {
								'RR2.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'B-AN1.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'A-AG2.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								},
								'B-AG1.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								}
							}
						},
						'RR2.00-00': {
							'lsp': {
								'seq_num': '0x000002d1',
								'checksum': '0x9191',
								'local_router': False,
								'holdtime': 716,
								'received': 1200,
								'attach_bit': 0,
								'p_bit': 0,
								'overload_bit': 0
							},
							'area_address': '49.0001.0010',
							'nlpid': ['0xcc', '0x8e'],
							'mt_entries': {
								'Standard (IPv4 Unicast)': {},
								'IPv6 Unicast': {
									'attach_bit': 0,
									'p_bit': 0,
									'overload_bit': 0
								}
							},
							'hostname': 'RR2',
							'mt_is_neighbor': {
								'B-AG2.00': {
									'metric': 10,
									'mt_id': 'MT (IPv6 Unicast)'
								}
							},
							'ip_address': '10.0.0.16',
							'extended_ipv4_reachability': {
								'10.0.0.16/32': {
									'ip_prefix': '10.0.0.16',
									'prefix_length': '32',
									'metric': 0
								}
							},
							'ipv6_address': 'fc00:a000:2000::16',
							'mt_ipv6_reachability': {
								'fc00:a000:2000::16/128': {
									'ip_prefix': 'fc00:a000:2000::16',
									'prefix_length': '128',
									'metric': 0
								}
							}
						}
					},
					'total_lsp_count': 8,
					'local_lsp_count': 1
				}
			}
		}
	}
}