expected_output = {
	'policy_name': {
		'default': {
			'match_address_local': 'any',
			'match_fvrf': 'any',
			'proposal': 'default'
		},
		'ikev2policy': {
			'match_address_local': 'any',
			'match_fvrf': 'global',
			'proposal': 'ikev2proposal'
		}
	}
}
