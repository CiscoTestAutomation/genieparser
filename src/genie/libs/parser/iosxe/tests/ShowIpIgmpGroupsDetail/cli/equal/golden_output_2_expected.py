expected_output =  {
     'vrf': {
         'default': {
             'interface': {
                 'GigabitEthernet0/0/2': {
                     'group': {
                         '232.10.10.10': {
                             'flags': 'SSM',
                             'group_mode': 'include',
                             'last_reporter': '10.1.0.200',
                             'up_time': '00:00:05',
                             'source': {
                                 '10.1.1.1': {
                                     'up_time': '00:00:05',
                                     'v3_exp': '00:02:54',
                                     'csr_exp': 'stopped',
                                     'forward': True,
                                     'flags': 'R',
                                 },
                             },
                         },
                     },
                     'join_group': {
                         '232.10.10.10 10.1.1.1': {
                             'v3_exp': '00:02:54',
                             'csr_exp': 'stopped',
                             'forward': True,
                             'flags': 'SSM',
                             'group': '232.10.10.10',
                             'source': '10.1.1.1',
                             'up_time': '00:00:05',
                             'last_reporter': '10.1.0.200',
                         },
                     },
                 },
             },
         },
     },
 }
