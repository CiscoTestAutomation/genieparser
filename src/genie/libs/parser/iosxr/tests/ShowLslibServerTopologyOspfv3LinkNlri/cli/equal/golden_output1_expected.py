expected_output = {
		'nlri': {
			'[E][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.0][r192.168.0.3]][R[c0][b0.0.0.0][a0.0.0.0][r192.168.0.4]][L[l64.35]]/760': {
				'nlri_str': '[E][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.0][r192.168.0.3]][R[c0][b0.0.0.0][a0.0.0.0][r192.168.0.4]][L[l64.35]]/760',
				'nlri_length_bytes': 95,
				'attribute_length_bytes': 7,
				'producers': {
					10: {
						'inst_id': 10,
						'producer': 'ospfv3',
						},
					},
				'nlri_type': 'link',
				'protocol': 'ospfv3',
				'identifier': '0xa',
				'local_node_descriptor': {
					'as_number': 0,
					'bgp_identifier': '0.0.0.0',
					'area_id': '0.0.0.0',
					'router_id_ipv4': '192.168.0.3',
					},
				'remote_node_descriptor': {
					'as_number': 0,
					'bgp_identifier': '0.0.0.0',
					'area_id': '0.0.0.0',
					'router_id_ipv4': '192.168.0.4',
					},
				'link_descriptor': {
					'link_id': '64.35',
					},
				'attributes': {
					'metric': 10,
					},
				},

			'[E][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.1][r192.168.0.6]][R[c0][b0.0.0.0][a0.0.0.1][r192.168.0.5]][L[l65.62]]/760': {
				'nlri_str': '[E][O3][I0xa][N[c0][b0.0.0.0][a0.0.0.1][r192.168.0.6]][R[c0][b0.0.0.0][a0.0.0.1][r192.168.0.5]][L[l65.62]]/760',
				'nlri_length_bytes': 95,
				'attribute_length_bytes': 7,
				'producers': {
					10: {
						'inst_id': 10,
						'producer': 'ospfv3',
						},
					},
				'nlri_type': 'link',
				'protocol': 'ospfv3',
				'identifier': '0xa',
				'local_node_descriptor': {
					'as_number': 0,
					'bgp_identifier': '0.0.0.0',
					'area_id': '0.0.0.1',
					'router_id_ipv4': '192.168.0.6',
					},
				'remote_node_descriptor': {
					'as_number': 0,
					'bgp_identifier': '0.0.0.0',
					'area_id': '0.0.0.1',
					'router_id_ipv4': '192.168.0.5',
					},
				'link_descriptor': {
					'link_id': '65.62',
					},
				'attributes': {
					'metric': 10,
					},
				},
			},
		}

