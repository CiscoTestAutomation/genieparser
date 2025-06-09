expected_output = {
     'configuration_status': 'enabled',
     'initialization_state': 'Running',
     'interfaces': {
         'TenGigabitEthernet0/1/0': {
             'cef_based_output': {
                 'available': 'yes',
                 'configured': 'yes',
             },
             'status': 'up',
         },
         'TenGigabitEthernet0/1/1': {
             'cef_based_output': {
                 'available': 'yes',
                 'configured': 'yes',
             },
             'status': 'up',
         },
         'Tunnel0': {
             'cef_based_output': {
                 'available': 'no',
                 'configured': 'yes',
             },
             'status': 'up',
         },
         'Tunnel1': {
             'cef_based_output': {
                 'available': 'yes',
                 'configured': 'yes',
             },
             'status': 'up',
         },
         'Tunnel2': {
             'cef_based_output': {
                 'available': 'no',
                 'configured': 'yes',
             },
             'status': 'up',
         },
     },
     'operational_status': 'running',
     'process_status': 'may enable - 3 - pid 711',
     'tables': {
         'active': 1,
         'io': 0,
         'mrib': 1,
     },
     'total_signalling_packets_queued': 0,
 }
