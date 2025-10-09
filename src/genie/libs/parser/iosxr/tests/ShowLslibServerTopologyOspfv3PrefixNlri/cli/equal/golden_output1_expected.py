expected_output = {
		'nlri': {
			'[T][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.0][r192.168.0.3]][P[o0x01][p34:34:1::/64]]/520': {
				'nlri_str': '[T][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.0][r192.168.0.3]][P[o0x01][p34:34:1::/64]]/520',
				'nlri_length_bytes': 65,
				'attribute_length_bytes': 8,
				'producers': {
					10: {
						'inst_id': 10,
						'producer': 'ospfv3',
						},
					},
				'nlri_type': 'prefix',
				'protocol': 'ospfv3',
				'identifier': '0xa',
				'local_node_descriptor': {
					'as_number': 0,
					'bgp_identifier': '0.0.0.0',
					'area_id': '0.0.0.0',
					'router_id_ipv4': '192.168.0.3',
					},
				'prefix_descriptor': {
					'ospf_route_type': '0x01',
					'prefix': '34:34:1::/64',
					},
				'attributes': {
					'metric': 10,
					},
				},
			'[T][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.1][r192.168.0.6]][P[o0x01][p192:168:1::6/128]]/584': {
				'nlri_str': '[T][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.1][r192.168.0.6]][P[o0x01][p192:168:1::6/128]]/584',
				'nlri_length_bytes': 73,
				'attribute_length_bytes': 8,
				'producers': {
					10: {
						'inst_id': 10,
						'producer': 'ospfv3',
						},
					},
				'nlri_type': 'prefix',
				'protocol': 'ospfv3',
				'identifier': '0xa',
				'local_node_descriptor': {
					'as_number': 0,
					'bgp_identifier': '0.0.0.0',
					'area_id': '0.0.0.1',
					'router_id_ipv4': '192.168.0.6',
					},
				'prefix_descriptor': {
					'ospf_route_type': '0x01',
					'prefix': '192:168:1::6/128',
					},
				'attributes': {
					'metric': 10,
					},
				},
			'[T][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.2][r192.168.0.3]][P[o0x01][p192:168:2::3/128]]/584': {
					'nlri_str': '[T][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.2][r192.168.0.3]][P[o0x01][p192:168:2::3/128]]/584',
					'nlri_length_bytes': 73,
					'attribute_length_bytes': 8,
					'producers': {
						10: {
							'inst_id': 10,
							'producer': 'ospfv3',
							},
						},
					'nlri_type': 'prefix',
					'protocol': 'ospfv3',
					'identifier': '0xa',
					'local_node_descriptor': {
						'as_number': 0,
						'bgp_identifier': '0.0.0.0',
						'area_id': '0.0.0.2',
						'router_id_ipv4': '192.168.0.3',
						},
					'prefix_descriptor': {
						'ospf_route_type': '0x01',
						'prefix': '192:168:2::3/128',
						},
					'attributes': {
						'metric': 10,
						},
					},
			},
		}
