expected_output = {
	'proposal_name': {
		'default': {
			'dh_group': [
				'DH_GROUP_256_ECP/Group 19',
				'DH_GROUP_2048_MODP/Group 14',
				'DH_GROUP_521_ECP/Group 21',
				'DH_GROUP_1536_MODP/Group 5'
			],
			'encryption': 'AES-CBC-256',
			'integrity': 'SHA512 SHA384',
			'prf': 'SHA512 SHA384'
		},
		'ikev2proposal': {
			'dh_group': ['DH_GROUP_4096_MODP/Group 16'],
			'encryption': 'AES-CBC-128',
			'integrity': 'SHA96',
			'prf': 'SHA1'
		}
	}
}
