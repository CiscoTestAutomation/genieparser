expected_output = {
	'mpls_tp': {
	    '0::101.1.1.1': {
		'endpoints': {
		    'down': 0,
		    'protect': {
			'down': 0,
			'total': 500,
			'up': 500,
		    },
		    'shut': 0,
		    'total': 500,
		    'up': 500,
		    'working': {
			'down': 0,
			'total': 500,
			'up': 500,
		    },
		},
		'midpoints': {
		    'protect': 0,
		    'total': 0,
		    'working': 0,
		},
		'path_protection_mode': '1:1 revertive',
		'platform_max_tp_interfaces': 65536,
		'psc': 'Disabled',
		'timers': {
		    'fault_oam': '20 seconds',
		    'psc': {
			'fast_timer': '1000',
			'messages': 3,
			'slow_timer': '5 seconds',
		    },
		    'wait_to_restore': '10 seconds',
		}, 
	    },
	}, 
}
