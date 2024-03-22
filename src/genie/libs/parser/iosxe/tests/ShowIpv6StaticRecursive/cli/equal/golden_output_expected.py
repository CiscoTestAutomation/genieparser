expected_output={
	'2001::/64': {
		'distance': 1,
		'installed': False,
		'via': [
			'2005::'
		]
	},
	'2005::/64': {
		'distance': 1,
		'installed': True,
		'via': [
			'2001::2'
		]
	},
	'4200::/64': {
		'distance': 1,
		'installed': True,
		'via': [
			'4102::',
			'4101::'
		]
	}
}