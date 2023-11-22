expected_output = {
	'ipsec_profile_name': {
		'default': {
			'mixed_mode': 'Disabled',
			'psf': 'N',
			'responder_only': 'N',
			'security_association_lifetime': '4608000 '
			'kilobytes/3600 '
			'seconds',
			'tranform_sets': {
				'default': {
					'transform_set_method': 'esp-sha-hmac',
					'transform_set_name': 'esp-aes'
				}
			}
		},
		'nil_ips': {
			'ikev2_profile_name': 'nil_ike_prof',
			'mixed_mode': 'Disabled',
			'psf': 'N',
			'responder_only': 'N',
			'security_association_lifetime': '4608000 '
			'kilobytes/3600 '
			'seconds',
			'tranform_sets': {
				'nil_tfs': {
					'transform_set_method': 'esp-sha-hmac',
					'transform_set_name': 'esp-aes'
				},
				'test': {
					'transform_set_method': 'esp-sha-hmac',
					'transform_set_name': 'esp-aes'
				}
			}
		}
	}
}
