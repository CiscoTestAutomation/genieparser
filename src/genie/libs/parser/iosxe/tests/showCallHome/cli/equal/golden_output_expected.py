expected_output= {
	'current_call_home_settings': {
		'call_home_feature': 'enable',
		'msg_from_address': 'Not yet set up',
		'msg_reply_to_address': 'Not yet set up',
		'vrf_for_msg': 'Not yet set up',
		'contact_person_email': 'sch-smart-licensing@cisco.com',
		'contact_person_phone': 'Not yet set up',
		'street_address': 'Not yet set up',
		'customer_id': 'Not yet set up',
		'contract_id': 'Not yet set up',
		'site_id': 'Not yet set up',
		'source_ip_address': 'Not yet set up',
		'source_interface': 'Not yet set up',
		'mail_server': {
			'Mail-server[1]': {
				'address': 'ott-ads-035',
				'priority': 1,
				'secure': 'none'
			},
			'Mail-server[2]': {
				'address': 'ott-ads-085',
				'priority': 2,
				'secure': 'tls'
			}
		},
		'http_proxy': 'Not yet set up',
		'http_secure': {
			'server_identity_check': 'enabled'
		},
		'http_resolve_hostname': 'default',
		'diagnostic_signature': 'enabled',
		'profile': {
			'muskan': {
				'status': 'INACTIVE'
			},
			'CiscoTAC-1': {
				'status': 'ACTIVE'
			}
		},
		'smart_licensing_msg': 'enabled',
		'aaa_authorization': 'disable',
		'aaa_authorization_username': 'callhome (default)',
		'data_privacy': 'normal',
		'syslog_throttling': 'enable',
		'Rate_limit_msg_per_min': 20,
		'snapshot_command': 'Not yet set up'
	},
	'available_alert_group': {
		'keyword': {
			'Keyword': {
				'state': 'State',
				'description': 'Description'
			},
			'configuration': {
				'state': 'Enable',
				'description': 'configuration info'
			},
			'crash': {
				'state': 'Enable',
				'description': 'crash and traceback info'
			},
			'diagnostic': {
				'state': 'Enable',
				'description': 'diagnostic info'
			},
			'environment': {
				'state': 'Enable',
				'description': 'environmental info'
			},
			'inventory': {
				'state': 'Enable',
				'description': 'inventory info'
			},
			'snapshot': {
				'state': 'Enable',
				'description': 'snapshot info'
			},
			'syslog': {
				'state': 'Enable',
				'description': 'syslog info'
			}
		}
	},
	'profiles': {
		'name': 'CiscoTAC-1, dummy, MohamedMuskan, muskan, Shishir, test'
	}
}