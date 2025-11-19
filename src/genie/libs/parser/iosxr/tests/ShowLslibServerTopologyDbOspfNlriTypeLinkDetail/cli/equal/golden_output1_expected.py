expected_output = {
		'links': {
			'[E][O][I0x0][N[c0][b0.0.0.0][a0.0.0.0][r1.1.1.1]][R[c0][b0.0.0.0][a0.0.0.0][r1.1.1.2]][L[i99.1.2.1][n99.1.2.2]]/792': {
				'nlri_length': 99,
				'attribute_length': 51,
				'producers': {
					0: {
						'inst_id': 0,
						'producer': 'ospf',
						},
					},
				'nlri_type': 'link',
				'protocol': 'ospf',
				'identifier': '0x0',
				'local_node_descriptor': {
					'as_number': 0,
					'bgp_identifier': '0.0.0.0',
					'area_id': '0.0.0.0',
					'router_id_ipv4': '1.1.1.1',
					},
				'remote_node_descriptor': {
					'as_number': 0,
					'bgp_identifier': '0.0.0.0',
					'area_id': '0.0.0.0',
					'router_id_ipv4': '1.1.1.2',
					},
				'link_descriptor': {
					'local_interface_address_ipv4': '99.1.2.1',
					'neighbor_interface_address_ipv4': '99.1.2.2',
					},
				'attributes': {
					'local_link_id': 109,
					'remote_link_id': 16,
					'metric': 1,
					'opaque_link_attr': '800200180000000976312e30302d4f4c542d435f305f305f30202020',
					},
				},
			},
		}
