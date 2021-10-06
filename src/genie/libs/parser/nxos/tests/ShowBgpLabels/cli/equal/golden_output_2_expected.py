

expected_output = {
    'vrf': 
        {'VRF1': 
            {'address_family': 
                {'ipv4 unicast': 
                    {'prefix': 
                        {'10.85.0.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': '492288',
                                    'nexthop': '10.76.1.101',
                                    'out_label': 'nolabel',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e',
                                    'vpn': 'VRF1'}}},
                        '10.85.1.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': '492288',
                                    'nexthop': '10.76.1.101',
                                    'out_label': 'nolabel',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e',
                                    'vpn': 'VRF1'}}},
                        '10.85.2.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': '492288',
                                    'nexthop': '10.76.1.101',
                                    'out_label': 'nolabel',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e',
                                    'vpn': 'VRF1'}}},
                        '10.85.3.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': '492288',
                                    'nexthop': '10.76.1.101',
                                    'out_label': 'nolabel',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e',
                                    'vpn': 'VRF1'}}},
                        '10.85.4.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': '492288',
                                    'nexthop': '10.76.1.101',
                                    'out_label': 'nolabel',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e',
                                    'vpn': 'VRF1'}}},
                        '10.94.0.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': '16',
                                    'nexthop': '10.51.1.101',
                                    'out_label': '16',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e',
                                    'vpn': 'VRF1'}}},
                        '10.94.1.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': '17',
                                    'nexthop': '10.51.1.101',
                                    'out_label': '17',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e',
                                    'vpn': 'VRF1'}}},
                        '10.94.2.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': '18',
                                    'nexthop': '10.51.1.101',
                                    'out_label': '18',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e',
                                    'vpn': 'VRF1'}}},
                        '10.94.3.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': '19',
                                    'nexthop': '10.51.1.101',
                                    'out_label': '19',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e',
                                    'vpn': 'VRF1'}}},
                        '10.94.4.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': '20',
                                    'nexthop': '10.51.1.101',
                                    'out_label': '20',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e',
                                    'vpn': 'VRF1'}}}},
                    'router_id': '10.81.1.1',
                    'table_version': 18}}},
        'default': 
            {'address_family': 
                {'ipv4 unicast': 
                    {'prefix': 
                        {'10.4.0.0/16': 
                            {'index': 
                                {0: 
                                    {'best_path': False,
                                    'in_label': 'nolabel',
                                    'nexthop': '0.0.0.0',
                                    'out_label': 'nolabel',
                                    'status': 'invalid',
                                    'type': 'aggregate',
                                    'type_code': 'a'}}},
                        '10.171.0.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': 'nolabel',
                                    'nexthop': '10.51.1.101',
                                    'out_label': 'nolabel',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e'}}},
                        '10.171.1.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': 'nolabel',
                                    'nexthop': '10.51.1.101',
                                    'out_label': 'nolabel',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e'}}},
                        '10.171.2.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': 'nolabel',
                                    'nexthop': '10.51.1.101',
                                    'out_label': 'nolabel',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'external',
                                    'type_code': 'e'}}},
                        '10.85.0.0/24': 
                            {'index': 
                                {0: 
                                    {'best_code': '>',
                                    'best_path': True,
                                    'in_label': 'nolabel',
                                    'nexthop': '0.0.0.0',
                                    'out_label': 'nolabel',
                                    'status': 'valid',
                                    'status_code': '*',
                                    'type': 'redist',
                                    'type_code': 'r'}}}},
                    'router_id': '10.1.1.1',
                    'table_version': 17}}}}}
