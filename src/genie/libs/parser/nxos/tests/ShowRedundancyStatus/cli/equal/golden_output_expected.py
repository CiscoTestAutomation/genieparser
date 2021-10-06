

expected_output = {'redundancy_mode':
                          {'administrative': 'HA',
                           'operational': 'HA'},
                        'supervisor_1':
                          {'redundancy_state': 'Active',
                           'supervisor_state': 'Active',
                           'internal_state':'Active with HA standby'},
                        'supervisor_2':
                          {'redundancy_state': 'Standby',
                           'supervisor_state': 'HA standby',
                           'internal_state':'HA standby'},
                        'system_start_time': 'Fri Apr 21 01:53:24 2017',
                        'system_uptime': '0 days, 7 hours, 57 minutes, 30 seconds',
                        'kernel_uptime': '0 days, 8 hours, 0 minutes, 56 seconds',
                        'active_supervisor_time': '0 days, 7 hours, 57 minutes, 30 seconds'}
