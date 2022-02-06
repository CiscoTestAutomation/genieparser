expected_output = {
    'system_port': 28,
	'svl_control_interface': {
	    'FourHundredGigE1/0/19': {
		    '0x85': {
			    'ec_if_id': '0x85',
				'system_port': 31,
				'if_type': 'etherchannel'
				},
			'0x15': {
			    'ec_if_id': '0x85', 
				'system_port': 28, 
				'if_type': 'member'
				},
			'0x16': {
			    'ec_if_id': '0x85', 
				'system_port': 29, 
				'if_type': 'member'
				},
			'0x18': {
			    'ec_if_id': '0x85', 
				'system_port': 30, 
				'if_type': 'member'
				},
			'0x11': {
			    'ec_if_id': '0', 
				'system_port': 26, 
				'if_type': 'dad'
				},
			'0x13': {
			    'ec_if_id': '0', 
				'system_port': 27, 
				'if_type': 'dad'
			    }
		    }
	    }
    }
