expected_output = {
	'interface': {
		'Tunnel2': {
			'peer': {
				'2001:101:0:1::2': {
					'port': {
						'500': {
							'desc': 'none',
							'fvrf': 'none',
							'ike_sa': {
								'1': {
									'capabilities': 'NU',
									'conn_id': '1',
									'lifetime': '23:29:35',
									'local': '2001:101:0:1::1',
									'local_port': '500',
									'remote': '2001:101:0:1::2',
									'remote_port': '500',
									'sa_status': 'Active',
									'session_id': '395',
									'version': 'IKEv2'
								}
							},
							'ipsec_flow': {
								'permit ip   0.0.0.0/0.0.0.0 0.0.0.0/0.0.0.0': {
									'active_sas': 2,
									'inbound_life_kb': '7',
									'inbound_life_secs': '233',
									'inbound_pkts_decrypted': 47,
									'inbound_pkts_drop': 0,
									'origin': 'crypto '
									'map',
									'outbound_life_kb': '3',
									'outbound_life_secs': '233',
									'outbound_pkts_drop': 0,
									'outbound_pkts_encrypted': 12
								}
							},
							'ivrf': 'none',
							'phase1_id': '2001:101:0:1::2'
						}
					}
				}
			},
			'profile': 'nil_ike_prof',
			'session_status': 'UP-ACTIVE',
			'uptime': '00:30:25'
		}
	}
}