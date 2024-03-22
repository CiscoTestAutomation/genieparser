expected_output = {
	'contract': {
		'Contract1-01': {
            'policy': {
			    1: {
			    	'dst_port': '30',
			    	'pdm_counters': 0,
			    	'protocol': 17,
			    	'service': 'service_red',
			    	'src_port': '20'
			    }
            }
		},
		'Contract2-01': {
            'policy': {
			    1: {
			    	'dst_port': '15000',
			    	'pdm_counters': 0,
			    	'protocol': 6,
			    	'service': 'service_INFRA_VN',
			    	'src_port': 'any'
			    },
			    2: {
			    	'dst_port': 'any',
			    	'pdm_counters': 70827,
			    	'protocol': 17,
			    	'service': 'service_INFRA_VN',
			    	'src_port': 'any'
			    }
            }
		}
	}
}