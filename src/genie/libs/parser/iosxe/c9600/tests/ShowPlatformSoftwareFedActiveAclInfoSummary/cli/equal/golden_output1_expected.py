expected_output={
	'acl_name': {
		'v4denytest': {
			'cg_id': 20,
			'no_of_aces': 23,
			'protocol': 'IPv4',
			'direction_ingress': 'Y',
			'direction_egress': 'N'
		},
		'auto-egress': {
			'cg_id': 30,
			'no_of_aces': 3,
			'protocol': 'IPv6',
			'direction_ingress': 'N',
			'direction_egress': 'Y'
		},
		'bfd1': {
			'cg_id': 31,
			'no_of_aces': 7,
			'protocol': 'IPv6',
			'direction_ingress': 'Y',
			'direction_egress': 'N'
		}
	}
}
