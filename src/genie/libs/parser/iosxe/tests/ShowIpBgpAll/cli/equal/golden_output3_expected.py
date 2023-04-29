expected_output = {
	'vrf': {
		'default': {
			'address_family': {
				'l2vpn evpn RD 1.1.1.1:1': {
					'bgp_table_version': 24595, 
					'route_identifier': '1.1.1.1', 
					'route_distinguisher': '1.1.1.1:1', 
					'default_vrf': 'default', 
					'routes': {
						'[2][1.1.1.1:1][0][48][000C293B2157][0][*]/20': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][000C293B2157][128][2000::22]/36': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][000C293B22A8][128][2000::21]/36': {
							'index': {
								1: {
									'status_codes': '*>', 
									'next_hop': '::', 
									'weight': 32768, 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][000C293B2F21][0][*]/20': {
							'index': {
								1: {
									'status_codes': '*>', 
									'next_hop': '::', 
									'weight': 32768, 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][000C293B2F22][0][*]/20': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][000C29ED4A12][0][*]/20': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][000C29ED4A12][32][20.20.20.22]/24': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][000C29ED4A26][0][*]/20': {
							'index': {
								1: {
									'status_codes': '*>', 
									'next_hop': '::', 
									'weight': 32768, 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][000C29ED4A26][32][20.20.20.21]/24': {
							'index': {
								1: {
									'status_codes': '*>', 
									'next_hop': '::', 
									'weight': 32768, 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][780CF0E11D61][32][20.20.20.1]/24': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][780CF0E11D61][128][2000::1]/36': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][780CF0E11EE1][32][20.20.20.1]/24': {
							'index': {
								1: {
									'status_codes': '*>', 
									'next_hop': '::', 
									'weight': 32768, 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][780CF0E11EE1][128][2000::1]/36': {
							'index': {
								1: {
									'status_codes': '*>', 
									'next_hop': '::', 
									'weight': 32768, 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][7C210DD9D3D1][32][20.20.20.1]/24': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][7C210DD9D3D1][128][2000::1]/36': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][A03D6E7D2140][0][*]/20': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][A03D6E7D2140][32][20.20.20.23]/24': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][A03D6E7D2140][128][2000::23]/36': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][1.1.1.1:1][0][48][A03D6E7D2140][128][FE80::A23D:6EFF:FE7D:2140]/36': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}
					}
				}, 
				'l2vpn evpn RD 2.2.2.2:1': {
					'bgp_table_version': 24595, 
					'route_identifier': '1.1.1.1', 
					'route_distinguisher': '2.2.2.2:1', 
					'default_vrf': 'default', 
					'routes': {
						'[2][2.2.2.2:1][0][48][000C293B2157][0][*]/20': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][2.2.2.2:1][0][48][000C293B2157][128][2000::22]/36': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
										'status_codes': '*>', 
										'next_hop': '2000::2:2', 
										'weight': 0, 
										'metric': 0, 
										'path': '1001', 
										'origin_codes': '?'
								}
							}
						}, 
						'[2][2.2.2.2:1][0][48][000C293B2F22][0][*]/20': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][2.2.2.2:1][0][48][000C29ED4A12][0][*]/20': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][2.2.2.2:1][0][48][000C29ED4A12][32][20.20.20.22]/24': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][2.2.2.2:1][0][48][7C210DD9D3D1][32][20.20.20.1]/24': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][2.2.2.2:1][0][48][7C210DD9D3D1][128][2000::1]/36': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'metric': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}
					}
				}, 
				'l2vpn evpn RD 3.3.3.3:1': {
					'bgp_table_version': 24595, 
					'route_identifier': '1.1.1.1', 
					'route_distinguisher': '3.3.3.3:1', 
					'default_vrf': 'default', 
					'routes': {
						'[2][3.3.3.3:1][0][48][780CF0E11D61][32][20.20.20.1]/24': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][3.3.3.3:1][0][48][780CF0E11D61][128][2000::1]/36': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][3.3.3.3:1][0][48][A03D6E7D2140][0][*]/20': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][3.3.3.3:1][0][48][A03D6E7D2140][32][20.20.20.23]/24': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][3.3.3.3:1][0][48][A03D6E7D2140][128][2000::23]/36': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[2][3.3.3.3:1][0][48][A03D6E7D2140][128][FE80::A23D:6EFF:FE7D:2140]/36': {
							'index': {
								1: {
									'status_codes': '*m', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'metric': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}
					}
				}, 
				'l2vpn evpn RD 1001:1': {
					'bgp_table_version': 24595, 
					'route_identifier': '1.1.1.1', 
					'route_distinguisher': '1001:1', 
					'default_vrf': 'default', 
					'routes': {
						'[5][1001:1][0][24][20.20.20.0]/17': {
							'index': {
								1: {
									'status_codes': '*', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[5][1001:1][0][24][100.100.100.0]/17': {
							'index': {
								1: {
									'status_codes': '*', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}, 
						'[5][1001:1][0][32][7.7.7.7]/17': {
							'index': {
								1: {
									'status_codes': '*', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000 1001', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001', 
									'origin_codes': '?'
								}
							}
						}
					}
				}
			}
		}, 
		'red': {
			'address_family': {
				'l2vpn evpn RD 1002:1': {
					'bgp_table_version': 24595, 
					'route_identifier': '1.1.1.1', 
					'route_distinguisher': '1002:1', 
					'default_vrf': 'red', 
					'routes': {
						'[5][1002:1][0][24][20.20.20.0]/17': {
							'index': {
								1: {
									'status_codes': '*>', 
									'next_hop': '0.0.0.0', 
									'weight': 32768, 
									'metric': 0, 
									'origin_codes': '?'
								}
							}
						}, 
						'[5][1002:1][0][24][100.100.100.0]/17': {
							'index': {
								1: {
									'status_codes': '*>', 
									'next_hop': '0.0.0.0', 
									'weight': 32768, 
									'metric': 0, 
									'origin_codes': '?'
								}
							}
						}, 
						'[5][1002:1][0][32][6.6.6.6]/17': {
								'index': {
										1: {
												'status_codes': '*>', 
												'next_hop': '0.0.0.0', 
												'weight': 32768, 
												'metric': 0, 
												'origin_codes': '?'
										}
								}
						}
					}
				}, 
				'l2vpn evpn RD 1003:1': {
					'bgp_table_version': 24595, 
					'route_identifier': '1.1.1.1', 
					'route_distinguisher': '1003:1', 
					'default_vrf': 'red', 
					'routes': {
						'[5][1003:1][0][24][20.20.20.0]/17': {
							'index': {
								1: {
									'status_codes': '*', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[5][1003:1][0][24][100.100.100.0]/17': {
							'index': {
								1: {
									'status_codes': '*', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}, 
						'[5][1003:1][0][32][9.9.9.9]/17': {
							'index': {
								1: {
									'status_codes': '*', 
									'next_hop': '2000::2:2', 
									'weight': 0, 
									'path': '1001 1000', 
									'origin_codes': '?'
								}, 
								2: {
									'status_codes': '*>', 
									'next_hop': '2000::3:3', 
									'weight': 0, 
									'path': '1000', 
									'origin_codes': '?'
								}
							}
						}
					}
				}
			}
		}
	}
}