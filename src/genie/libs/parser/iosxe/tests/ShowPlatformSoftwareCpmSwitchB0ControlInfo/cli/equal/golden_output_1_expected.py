expected_output = {
    'system_port': 1052, 
    'svl_control_interface': {
	    'FourHundredGigE2/0/19': {
		    '0x85': {
			    'ec_if_id': '0x85', 
				'system_port': 31, 
				'if_type': 'etherchannel'
				}, 
			'0x15': {
			    'ec_if_id': '0x85', 
				'system_port': 1052, 
				'if_type': 'member'
				}, 
			'0x16': {
			    'ec_if_id': '0x85',
				'system_port': 1053, 
				'if_type': 'member'
				}, 
			'0x18': {
			    'ec_if_id': '0x85', 
				'system_port': 1054,
				'if_type': 'member'
				},
			'0x12': {
			    'ec_if_id': '0', 
				'system_port': 1050, 
				'if_type': 'dad'
				}, 
			'0x14': {
			    'ec_if_id': '0', 
				'system_port': 1051,
				'if_type': 'dad'
				}
			}
		}
	}
