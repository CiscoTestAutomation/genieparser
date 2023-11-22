expected_output = {
'tag': {
         '1': {
             'flex_algo': {
                 128: {
                     'prefix': {
                         '6.6.6.6': {
                             'algo': {
                                 0: {
                                     'bound': True,
                                     'sid_index': 623,
                                 },
                                 1: {
                                 },
                             },
                             'prefix_attr': {
                                 'n_flag': True,
                                 'r_flag': True,
                                 'x_flag': False,
                             },
                             'source_router_id': '6.6.6.6',
                             'subnet': '32',
                             'via_interface': {
                                 'Ethernet0/1': {
                                     'level': {
                                         'ia': {
                                             'source_ip': {
                                                 '2.2.2.2': {
                                                     'algo': {
                                                         0: {
                                                             'flags': {
                                                                 'e_flag': False,
                                                                 'l_flag': False,
                                                                 'n_flag': True,
                                                                 'p_flag': True,
                                                                 'r_flag': True,
                                                                 'v_flag': False,
                                                             },
                                                             'label': '16623',
                                                             'sid_index': 623,
                                                         },
                                                         1: {
                                                         },
                                                     },
                                                     'distance': 115,
                                                     'filtered_out': False,
                                                     'host': 'R2.00-00',
                                                     'lsp': {
                                                     },
                                                     'metric': 40,
                                                     'prefix_attr': {
                                                         'n_flag': True,
                                                         'r_flag': True,
                                                         'x_flag': False,
                                                     },
                                                     'tag': '0',
                                                     'via_ip': '12.1.1.2',
                                                 },
                                             },
                                         },
                                     },
                                 },
                                 'Ethernet0/2': {
                                     'level': {
                                         'ia': {
                                             'source_ip': {
                                                 '3.3.3.3': {
                                                     'algo': {
                                                         0: {
                                                             'flags': {
                                                                 'e_flag': False,
                                                                 'l_flag': False,
                                                                 'n_flag': True,
                                                                 'p_flag': True,
                                                                 'r_flag': True,
                                                                 'v_flag': False,
                                                             },
                                                             'label': '16623',
                                                             'sid_index': 623,
                                                         },
                                                         1: {
                                                         },
                                                     },
                                                     'distance': 115,
                                                     'filtered_out': False,
                                                     'host': 'R3.00-00',
                                                     'lsp': {
                                                     },
                                                     'metric': 40,
                                                     'prefix_attr': {
                                                         'n_flag': True,
                                                         'r_flag': True,
                                                         'x_flag': False,
                                                     },
                                                     'tag': '0',
                                                     'via_ip': '13.1.1.2',
                                                 },
                                             },
                                         },
                                     },
                                 },
                             },
                         },
                     },
                 },
             },
             'tid': 0,
             'topo_id': '0x0',
             'topo_name': 'base',
             'topo_type': 'unicast',
         },
     },
 }

