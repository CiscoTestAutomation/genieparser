expected_output = {
	'config_request': {
		'cfg_request': {
			'received': 19340,
			'transmit': 83
		}
	},
	'error_notify': {
		'no_proposal_chosen': {
			'received_request': 0,
			'received_response': 0,
			'transmit_request': 0,
			'transmit_response': 53
		},
		'invalid_spi':{
			'received_request': 288,
			'received_response': 0,
			'transmit_request': 0,
			'transmit_response': 0			
		},
		'ts_unacceptable':{
			'received_request': 0,
			'received_response': 0,
			'transmit_request': 0,
			'transmit_response': 1				
		}
	},
	'exchanges': {
		'create_child_sa': {
			'received_request': 33035,
			'received_response': 1959,
			'transmit_request': 2014,
			'transmit_response': 32935
		},
		'create_child_sa_ike_rekey': {
			'received_request': 1,
			'received_response': 1500,
			'transmit_request': 1500,
			'transmit_response': 1
		},
		'create_child_sa_ipsec_rekey': {
			'received_request': 10364,
			'received_response': 456,
			'transmit_request': 514,
			'transmit_response': 10364
		},
		'ike_auth': {
			'received_request': 19340,
			'received_response': 83,
			'transmit_request': 83,
			'transmit_response': 19340
		},
		'ike_sa_init': {
			'received_request': 20740,
			'received_response': 83,
			'transmit_request': 84,
			'transmit_response': 19343
		},
		'informational': {
			'received_request': 188824,
			'received_response': 11691,
			'transmit_request': 27365,
			'transmit_response': 188162
		},
		'create_child_sa_ipsec':{
			'received_request': 22589,
			'received_response': 0,
			'transmit_request': 0,
			'transmit_response': 22570			
		}
	},

	'other_counters': {
		'no_nat': {
			'counter': 19426
		}
	},
	'other_notify': {
		'dpd': {
			'received_request': 177453,
			'received_response': 0,
			'transmit_request': 5146,
			'transmit_response': 177452
		},
		'http_cert_lookup_supported': {
			'received_request': 19340,
			'received_response': 83,
			'transmit_request': 83,
			'transmit_response': 19343
		},
		'initial_contact': {
			'received_request': 19340,
			'received_response': 0,
			'transmit_request': 82,
			'transmit_response': 0
		},
		'nat_detection_destination_ip': {
			'received_request': 19343,
			'received_response': 83,
			'transmit_request': 84,
			'transmit_response': 19343
		},
		'nat_detection_source_ip': {
			'received_request': 19343,
			'received_response': 83,
			'transmit_request': 84,
			'transmit_response': 19343
		},
		'rekey_sa': {
			'received_request': 10364,
			'received_response': 0,
			'transmit_request': 514,
			'transmit_response': 0
		},
		'set_window_size': {
			'received_request': 19341,
			'received_response': 1583,
			'transmit_request': 1583,
			'transmit_response': 19340
		}
	}
}
