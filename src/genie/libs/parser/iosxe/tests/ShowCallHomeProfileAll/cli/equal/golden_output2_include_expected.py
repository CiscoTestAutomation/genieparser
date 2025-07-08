expected_output = {
    'profile': {
         'name': {
             'CiscoTAC-1': {
                 'email_address': 'callhome@cisco.com',
                 'group_pattern': {
                     '.*': {
                         'severity': 'major',
                     },
                     'Alert-group': {
                         'severity': 'Severity',
                     },
                     'Syslog-Pattern': {
                         'severity': 'Severity',
                     },
                     'crash': {
                         'severity': 'debug',
                     },
                     'diagnostic': {
                         'severity': 'minor',
                     },
                     'environment': {
                         'severity': 'minor',
                     },
                     'inventory': {
                         'severity': 'normal',
                     },
                 },
                 'message_size_limit_in_bytes': 3145728,
                 'mode': 'Full Reporting',
                 'other_address': 'default',
                 'periodic_info': {
                     'configuration': {
                         'scheduled': 'every 17 day of the month',
                         'time': '10:11',
                     },
                     'inventory': {
                         'scheduled': 'every 17 day of the month',
                         'time': '09:56',
                     },
                 },
                 'preferred_message_format': 'xml',
                 'reporting_data': 'Smart Call Home, Smart Licensing',
                 'status': 'ACTIVE',
                 'transport_method': 'email',
             },
         },
     },
 }
