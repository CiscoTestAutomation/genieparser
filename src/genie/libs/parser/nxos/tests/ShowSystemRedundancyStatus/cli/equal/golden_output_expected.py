

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
                      }
