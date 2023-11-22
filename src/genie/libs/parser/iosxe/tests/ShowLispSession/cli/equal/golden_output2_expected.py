expected_output = {
    'vrf': {
		'default': {
			'total': '7',
			'established': '4',
			'peers': {
				'201.201.201.201': [{
					'port': '22400',
					'state': 'Up',
					'time': '00:02:18',
					'in': '13',
					'out': '15',
					'users': '4',
					'rtt': '125'
				}],
				'202.202.202.202': [{
					'port': '13541',
					'state': 'Up',
					'time': '00:02:18',
					'in': '11',
					'out': '12',
					'users': '4',
					'rtt': '125'
				}],
				'203.203.203.203': [{
					'port': '4342',
					'state': 'Up',
					'time': '00:03:15',
					'in': '10',
					'out': '5',
					'users': '4',
					'rtt': '0'
				}, {
					'port': '42424',
					'state': 'Up',
					'time': '00:03:15',
					'in': '5',
					'out': '10',
					'users': '3',
					'rtt': '125'
				}]
			}
		}
	}
}