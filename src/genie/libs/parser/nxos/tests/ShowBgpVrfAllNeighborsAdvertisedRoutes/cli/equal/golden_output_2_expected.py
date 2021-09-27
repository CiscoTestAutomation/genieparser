

expected_output = {
    'vrf':
        {'default':
            {'neighbor':
                {'10.106.102.3':
                    {'address_family':
                        {'ipv4 multicast':
                            {'advertised':
                                {'10.9.1.0/24': {'index': {1: {'locprf': 100,
                                                           'next_hop': '10.106.101.1',
                                                           'origin_codes': 'i',
                                                           'path': '2 '
                                                                   '3 '
                                                                   '4',
                                                           'path_type': 'i',
                                                           'status_codes': '*>',
                                                           'weight': 0}}},
                                '10.9.2.0/24': {'index': {1: {'locprf': 100,
                                                           'next_hop': '10.106.101.1',
                                                           'origin_codes': 'i',
                                                           'path': '2 '
                                                                   '3 '
                                                                   '4',
                                                           'path_type': 'i',
                                                           'status_codes': '*>',
                                                           'weight': 0}}},
                                '10.25.1.0/24': {'index': {1: {'locprf': 100,
                                                           'next_hop': '10.106.102.4',
                                                           'origin_codes': 'i',
                                                           'path': '2 '
                                                                   '3 '
                                                                   '4',
                                                           'path_type': 'i',
                                                           'status_codes': '*>',
                                                           'weight': 0}}},
                                '10.25.2.0/24': {'index': {1: {'locprf': 100,
                                                           'next_hop': '10.106.102.4',
                                                           'origin_codes': 'i',
                                                           'path': '2 '
                                                                   '3 '
                                                                   '4',
                                                           'path_type': 'i',
                                                           'status_codes': '*>',
                                                           'weight': 0}}},
                                '10.36.2.0/24': {'index': {1: {'locprf': 500,
                                                           'metric': 5555,
                                                           'next_hop': '10.106.102.4',
                                                           'origin_codes': 'i',
                                                           'path': '2 '
                                                                   '3 '
                                                                   '4 '
                                                                   '5 '
                                                                   '6 '
                                                                   '7 '
                                                                   '8 '
                                                                   '9 '
                                                                   '10 '
                                                                   '11 '
                                                                   '12',
                                                           'path_type': 'i',
                                                           'status_codes': '*>',
                                                           'weight': 32788}}}},
                            'bgp_table_version': 175,
                            'local_router_id': '10.145.0.6'},
                        'ipv4 unicast':
                            {'advertised':
                                {'10.4.1.0/24': {'index': {1: {'locprf': 100,
                                                             'next_hop': '10.106.102.4',
                                                             'origin_codes': 'i',
                                                             'path': '{62112 '
                                                                     '33492 '
                                                                     '4872 '
                                                                     '41787 '
                                                                     '13166 '
                                                                     '50081 '
                                                                     '21461 '
                                                                     '58376 '
                                                                     '29755 '
                                                                     '1135}',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}},
                                '10.4.2.0/24': {'index': {1: {'locprf': 100,
                                                             'next_hop': '10.106.102.4',
                                                             'origin_codes': 'i',
                                                             'path': '{62112 '
                                                                     '33492 '
                                                                     '4872 '
                                                                     '41787 '
                                                                     '13166 '
                                                                     '50081 '
                                                                     '21461 '
                                                                     '58376 '
                                                                     '29755 '
                                                                     '1135}',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}},
                                '10.36.0.0/24': {'index': {1: {'metric': 100,
                                                             'next_hop': '10.106.102.3',
                                                             'origin_codes': 'i',
                                                             'path': '10 '
                                                                     '20 '
                                                                     '30 '
                                                                     '40 '
                                                                     '50 '
                                                                     '60 '
                                                                     '70 '
                                                                     '80 '
                                                                     '90',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}},
                                '10.49.0.0/16': {'index': {1: {'locprf': 100,
                                                             'next_hop': '10.106.101.1',
                                                             'origin_codes': 'i',
                                                             'path': '10 '
                                                                     '20 '
                                                                     '30 '
                                                                     '40 '
                                                                     '50 '
                                                                     '60 '
                                                                     '70 '
                                                                     '80 '
                                                                     '90',
                                                             'path_type': 'i',
                                                             'status_codes': '*>',
                                                             'weight': 0}}}},
                            'bgp_table_version': 174,
                            'local_router_id': '10.145.0.6'},
                        'ipv6 multicast':
                            {'bgp_table_version': 6,
                            'local_router_id': '10.145.0.6',
                            'advertised': {}},
                        'ipv6 unicast':
                            {'bgp_table_version': 173,
                            'local_router_id': '10.145.0.6',
                            'advertised': {}},
                        'link-state':
                            {'advertised':
                                {'[2]:[77][7,0][10.69.9.9,1,151587081][10.135.1.1,22][10.106.101.1,10.76.1.30]/616':
                                    {'index':
                                        {1:
                                            {'locprf': 100,
                                            'metric': 4444,
                                            'next_hop': '10.106.101.1',
                                            'origin_codes': 'i',
                                            'path': '3 '
                                                    '10 '
                                                    '20 '
                                                    '30 '
                                                    '40 '
                                                    '50 '
                                                    '60 '
                                                    '70 '
                                                    '80 '
                                                    '90',
                                            'path_type': 'i',
                                            'status_codes': '*>',
                                            'weight': 0},
                                        2:
                                            {'locprf': 100,
                                            'metric': 4444,
                                            'next_hop': '10.106.102.3',
                                            'origin_codes': 'i',
                                            'path': '3 '
                                                    '10 '
                                                    '20 '
                                                    '30 '
                                                    '40 '
                                                    '50 '
                                                    '60 '
                                                    '70 '
                                                    '80 '
                                                    '90',
                                            'path_type': 'i',
                                            'status_codes': '*>',
                                            'weight': 0}}},
                                '[2]:[77][7,0][10.69.9.9,2,151587081][10.135.1.1,22][10.106.101.1,10.76.1.31]/616':
                                    {'index':
                                        {1:
                                            {'locprf': 200,
                                            'metric': 555,
                                            'next_hop': '10.106.103.2',
                                            'origin_codes': 'i',
                                            'path': '3 '
                                                    '10 '
                                                    '20 '
                                                    '30 '
                                                    '40 '
                                                    '50 '
                                                    '60 '
                                                    '70 '
                                                    '80 '
                                                    '90',
                                            'path_type': 'i',
                                            'status_codes': '*>',
                                            'weight': 0}}}},
                            'bgp_table_version': 173,
                            'local_router_id': '10.145.0.6'},
                        'vpnv4 unicast':
                            {'bgp_table_version': 183,
                            'local_router_id': '10.145.0.6',
                            'advertised': {}},
                        'vpnv4 unicast RD 0:0':
                            {'bgp_table_version': 183,
                            'local_router_id': '10.145.0.6',
                            'route_distinguisher': '0:0',
                            'advertised': {}},
                        'vpnv4 unicast RD 101:100':
                            {'bgp_table_version': 183,
                            'local_router_id': '10.145.0.6',
                            'route_distinguisher': '101:100',
                            'advertised': {}},
                        'vpnv4 unicast RD 102:100':
                            {'bgp_table_version': 183,
                            'local_router_id': '10.145.0.6',
                            'route_distinguisher': '102:100',
                            'advertised': {}},
                        'vpnv6 unicast':
                            {'bgp_table_version': 13,
                            'local_router_id': '10.145.0.6',
                            'advertised': {}},
                        'vpnv6 unicast RD 0xbb00010000000000':
                            {'bgp_table_version': 13,
                            'local_router_id': '10.145.0.6',
                            'route_distinguisher': '0xbb00010000000000',
                            'advertised': {}},
                        'vpnv6 unicast RD 100:200':
                            {'bgp_table_version': 13,
                            'local_router_id': '10.145.0.6',
                            'route_distinguisher': '100:200',
                            'advertised': {}}}}}}}}
