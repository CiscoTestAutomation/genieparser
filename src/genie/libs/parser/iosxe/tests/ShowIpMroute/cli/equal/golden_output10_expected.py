expected_output = {
	'vrf': {
		'red': {
			'address_family': {
				'ipv4': {
					'multicast_group': {
						'239.1.1.1': {
							'source_address': {
								'*': {
									'uptime': '1d06h', 
									'expire': 'stopped', 
									'flags': 'SPF', 
									'msdp_learned': False, 
									'rp_bit': False, 'rp': 
									'6.6.6.6', 'rpf_nbr': 
									'0.0.0.0'
								}, 
								'20.20.20.21': {
									'uptime': '1d06h', 
									'expire': '00:01:30', 
									'flags': 'FTGqx', 
									'msdp_learned': False, 
									'rp_bit': False, 
									'rpf_nbr': '0.0.0.0', 
									'incoming_interface_list': {
										'Vlan100': {
											'rpf_nbr': '0.0.0.0'
										}
									}, 
									'outgoing_interface_list': {
										'Vlan500': {
											'uptime': '00:03:24', 
											'expire': 'stopped', 
											'state_mode': 'forward/sparse', 
											'vxlan_version': 'v6', 
											'vxlan_vni': '50000', 
											'vxlan_nxthop': 'FF55::2'
										}
									}
								}
							}
						}, 
						'239.1.1.30': {
							'source_address': {
								'*': {
									'uptime': '3d14h', 
									'expire': 'stopped', 
									'flags': 'SJC', 
									'msdp_learned': False, 
									'rp_bit': False, 
									'rp': '6.6.6.6', 
									'rpf_nbr': '0.0.0.0', 
									'outgoing_interface_list': {
										'Vlan100': {
											'uptime': '3d14h', 
											'expire': '00:00:23', 
											'state_mode': 'forward/sparse'
										}
									}
								}, 
								'20.20.20.22': {
									'uptime': '13:45:36', 
									'expire': '00:02:35', 
									'flags': 'Tgq', 
									'msdp_learned': False, 
									'rp_bit': False, 
									'rpf_nbr': '2000::2:2', 
									'incoming_interface_list': {
										'Vlan500': {
											'rpf_nbr': '2000::2:2'
										}
									}, 
									'outgoing_interface_list': {
										'Vlan100': {
											'uptime': '00:03:33', 
											'expire': '00:02:26', 
											'state_mode': 'forward/sparse'
										}
									}
								}
							}
						}, 
						'232.1.1.5': {
							'source_address': {
								'20.20.20.21': {
									'uptime': '1d06h', 
									'expire': 'stopped', 
									'flags': 'sTGx', 
									'msdp_learned': False, 
									'rp_bit': False, 
									'rpf_nbr': '0.0.0.0', 
									'incoming_interface_list': {
										'Vlan100': {
											'rpf_nbr': '0.0.0.0'
										}
									}, 
									'outgoing_interface_list': {
										'Vlan500': {
										'uptime': '00:03:24', 
										'expire': 'stopped', 
										'state_mode': 'forward/sparse', 
										'vxlan_version': 'v6', 
										'vxlan_vni': '50000', 
										'vxlan_nxthop': 'FF55::2'
										}
									}
								}
							}
					   }, 
					   '232.1.1.6': {
							'source_address': {
								'20.20.20.22': {
									'uptime': '3d14h', 
									'expire': 'stopped', 
									'flags': 'sLTIg', 
									'msdp_learned': False, 
									'rp_bit': False, 
									'rpf_nbr': '2000::2:2', 
									'incoming_interface_list': {
										'Vlan500': {
											'rpf_nbr': '2000::2:2'
										}
									}, 
									'outgoing_interface_list': {
										'Vlan100': {
											'uptime': '00:03:33', 
											'expire': '00:02:26', 
											'state_mode': 'forward/sparse'
										}
									}
								}
							}
						}, 
						'224.0.1.40': {
							'source_address': {
								'*': {
									'uptime': '3d14h', 
									'expire': '00:02:41', 
									'flags': 'SJCL', 
									'msdp_learned': False, 
									'rp_bit': False, 
									'rp': '6.6.6.6', 
									'rpf_nbr': '0.0.0.0', 
									'outgoing_interface_list': {
										'Loopback2': {
											'uptime': '3d14h', 
											'expire': '00:02:41', 
											'state_mode': 'forward/sparse'
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

