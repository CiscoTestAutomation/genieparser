expected_output = {
    'vrf': {
		'default': {
			'total': '5',
			'established': '2',
			'peers': {
				'201.201.201.201': [{
					'port': '22400',
					'state': 'Up',
					'time': '00:05:12',
					'in': '14',
					'out': '16',
					'users': '4',
					'rtt': '125'
				}],
				'202:202:202:202::': [{
					'port': '13541',
					'state': 'Up',
					'time': '00:05:12',
					'in': '12',
					'out': '13',
					'users': '4',
					'rtt': '125'
				}]
			}
		}
	}
}
