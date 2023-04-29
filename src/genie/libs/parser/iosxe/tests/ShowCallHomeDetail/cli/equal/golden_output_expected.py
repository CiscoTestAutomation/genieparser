expected_output = {
    'settings': {
        'available_alert_groups': {
            'Keyword': {
                'Keyword': {
                    'description': 'Description',
                    'state': 'State',
                },
                'configuration': {
                    'description': 'configuration info',
                    'state': 'Enable',
                },
                'crash': {
                    'description': 'crash and traceback info',
                    'state': 'Enable',
                },
                'diagnostic': {
                    'description': 'diagnostic info',
                    'state': 'Enable',
                },
                'environment': {
                    'description': 'environmental info',
                    'state': 'Enable',
                },
                'inventory': {
                    'description': 'inventory info',
                    'state': 'Enable',
                },
                'snapshot': {
                    'description': 'snapshot info',
                    'state': 'Enable',
                },
                'syslog': {
                    'description': 'syslog info',
                    'state': 'Enable',
                },
            },
        },
        'current_call_home_settings': {
            'aaa_authorization': 'disable',
            'aaa_authorization_username': 'callhome (default)',
            'call_home_feature': 'disable',
            'call_home_message_from_address': 'Not yet set up',
            'call_home_message_reply_to_address': 'Not yet set up',
            'contact_person_email_address': 'Not yet set up',
            'contact_person_phone_number': 'Not yet set up',
            'contract_id': 'Not yet set up',
            'customer_id': 'Not yet set up',
            'data_privacy': 'normal',
            'diagnostic_signature': {
                'mode': 'enabled',
                'profile': 'CiscoTAC-1',
                'status': 'INACTIVE',
            },
            'http_proxy': 'Not yet set up',
            'http_resolve_hostname': 'default',
            'mail_server': 'Not yet set up',
            'rate_limit': '20 message(s) per minute',
            'server_identity_check': 'enabled',
            'site_id': 'Not yet set up',
            'smart_licensing_messages': {
                'mode': 'disabled',
            },
            'snapshot_command': 'Not yet set up',
            'source_interface': 'Not yet set up',
            'source_ip_address': 'Not yet set up',
            'street_address': 'Not yet set up',
            'syslog_throttling': 'enable',
            'vrf_for_call_home_messages': 'Not yet set up',
        },
        'profiles': {
            'CiscoTAC-1': {
                'alert_group': {
                    'crash': {
                        'severity': 'debugging',
                    },
                    'diagnostic': {
                        'severity': 'minor',
                    },
                    'environment': {
                        'severity': 'warning',
                    },
                    'inventory': {
                        'severity': 'normal',
                    },
                },
                'message_size_limit': '3145728 Bytes',
                'mode': 'Full Reporting',
                'periodic_configuration_info_message_is_scheduled': 'every 1 day of the month at 09:15',
                'periodic_inventory_info_message_is_scheduled': 'every 1 day of the month at 09:00',
                'preferred_message_format': 'xml',
                'reporting_Data': 'Smart Call Home, Smart Licensing',
                'status': 'INACTIVE',
                'syslog_pattern': {
                    '.*': {
                        'severity': 'major',
                    },
                    'APF-.-WLC_.*': {
                        'severity': 'warning',
                    },
                },
                'transport_method': 'email',
            },
        },
    },
}