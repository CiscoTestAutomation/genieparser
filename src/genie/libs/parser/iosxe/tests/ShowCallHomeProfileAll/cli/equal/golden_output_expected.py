expected_output = {
    'profile': {
        'name': {
            'CiscoTAC-1': {
                'group_pattern': {
                    '.*': {
                        'severity': 'major'
                    },
                    'APF-.-WLC_.*': {
                        'severity': 'warning'
                    },
                    'Alert-group': {
                        'severity': 'Severity'
                    },
                    'Syslog-Pattern': {
                        'severity': 'Severity'
                    },
                    'crash': {
                        'severity': 'debugging'
                    },
                    'diagnostic': {
                        'severity': 'minor'
                    },
                    'environment': {
                        'severity': 'warning'
                    },
                    'inventory': {
                        'severity': 'normal'
                    }
                },
                'http_address': 'https://tools.cisco.com/its/service/oddce/services/DDCEService',
                'message_size_limit_in_bytes': 3145728,
                'mode': 'Full Reporting',
                'other_address': 'default',
                'periodic_info': {
                    'configuration': {
                        'scheduled': 'every '
                        '1 '
                        'day '
                        'of '
                        'the '
                        'month',
                        'time': '09:15'
                    },
                    'inventory': {
                        'scheduled': 'every '
                        '1 '
                        'day '
                        'of '
                        'the '
                        'month',
                        'time': '09:00'
                    }
                },
                'preferred_message_format': 'xml',
                'reporting_data': 'Smart Call Home, Smart '
                'Licensing',
                'status': 'ACTIVE',
                'transport_method': 'http'
            },
            'MohamedMuskan': {
                'email_address': 'Not yet set up',
                'group_pattern': {
                    'Alert-group': {
                        'severity': 'Severity'
                    },
                    'N/A': {
                        'severity': 'N/A'
                    },
                    'Syslog-Pattern': {
                        'severity': 'Severity'
                    },
                    '\\W+': {
                        'severity': 'catastrophic'
                    },
                    '\\W+\\S': {
                        'severity': 'disaster'
                    },
                    'abc': {
                        'severity': 'minor'
                    }
                },
                'message_size_limit_in_bytes': 3145728,
                'mode': 'Full Reporting',
                'periodic_info': {
                    'inventory': {
                        'scheduled': 'daily',
                        'time': '00:00'
                    }
                },
                'preferred_message_format': 'xml',
                'reporting_data': 'Smart Call Home, '
                'Smart Licensing',
                'status': 'INACTIVE',
                'transport_method': 'email'
            },
            'Shishir': {
                'email_address': 'shishir@cisco.com,Shisihir213@cisco.com',
                'group_pattern': {
                    'Alert-group': {
                        'severity': 'Severity'
                    },
                    'N/A': {
                        'severity': 'N/A'
                    },
                    'Syslog-Pattern': {
                        'severity': 'Severity'
                    }
                },
                'message_size_limit_in_bytes': 3145728,
                'mode': 'Full Reporting',
                'other_address': 'https://shishir.com/its/service/oddce/services/DDCEService',
                'preferred_message_format': 'xml',
                'reporting_data': 'Smart Call Home, Smart '
                'Licensing',
                'status': 'INACTIVE',
                'transport_method': 'email'
            },
            'muskan': {
                'email_address': 'Not yet set up',
                'group_pattern': {
                    'Alert-group': {
                        'severity': 'Severity'
                    },
                    'N/A': {
                        'severity': 'N/A'
                    },
                    'Syslog-Pattern': {
                        'severity': 'Severity'
                    }
                },
                'message_size_limit_in_bytes': 3145728,
                'mode': 'Full Reporting',
                'other_address': 'http://linkedin.com',
                'preferred_message_format': 'xml',
                'reporting_data': 'Smart Call Home, Smart '
                'Licensing',
                'status': 'INACTIVE',
                'transport_method': 'email'
            },
            'test': {
                'email_address': 'Not yet set up',
                'group_pattern': {
                    'Alert-group': {
                        'severity': 'Severity'
                    },
                    'N/A': {
                        'severity': 'N/A'
                    },
                    'Syslog-Pattern': {
                        'severity': 'Severity'
                    }
                },
                'message_size_limit_in_bytes': 3145728,
                'mode': 'Full Reporting',
                'preferred_message_format': 'xml',
                'reporting_data': 'Smart Call Home',
                'status': 'ACTIVE',
                'transport_method': 'email'
            }
        }
    }
}