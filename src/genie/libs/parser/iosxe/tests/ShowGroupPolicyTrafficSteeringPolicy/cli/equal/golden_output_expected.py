expected_output = {
	'traffic_steering_policy': {
		3053: { 
			"sgt_policy_flag": '0x41400001',
			"source_sgt": 3053,
			"destination_sgt": 4003,
			"steer_type": 80,
			"steer_index": 1,
			"contract_name": 'Contract2',
			"ip_version": 'IPV4',
			"refcnt": 1,
			"flag": '0x41400000',
			"stale": False,
			"traffic_steering_ace": {
				1: {
					"protocol_number": 6,
					"source_port": 'any',
					"destination_port": '16000',
					"service_name": 'service_INFRA_VN',
				},
				2: {
					"protocol_number": 17,
					"source_port": 'any',
					"destination_port": '12000',
					"service_name": 'service_INFRA_VN',
				}
			},
			"traffic_steering_destination_list": 'Not exist',
			"traffic_steering_multicast_list": 'Not exist',
			"traffic_steering_policy_lifetime_secs": 86400,
			"policy_last_update_time": '05:51:21 UTC Wed Sep 29 2021',
			"policy_expires_in": '0:23:58:12',
			"policy_refreshes_in": '0:23:58:12'
		}
	}
}

