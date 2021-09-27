

expected_output = {
    'vrf': 
        {'VRF1': 
            {'address_family': 
                {'ipv4': 
                    {'mroute': 
                        {'10.2.2.2/32': 
                            {'path': 
                                {'0.0.0.0/32%sanity1 Vlan2': 
                                    {'neighbor_address': '0.0.0.0/32%sanity1 '
                                                          'Vlan2',
                                    'urib': True,
                                    'vrf_id': '2'}}},
                        '10.2.2.3/32': 
                            {'path': 
                                {'0.0.0.0/32%sanity1 Vlan2': 
                                    {'neighbor_address': '0.0.0.0/32%sanity1 '
                                                         'Vlan2',
                                    'urib': True,
                                    'vrf_id': '2'}}}}}}},
        'default': 
            {'address_family': 
                {'ipv4': 
                    {'mroute': 
                        {'10.49.0.0/8': 
                            {'path': 
                                {'0.0.0.0/32 Null0': 
                                    {'interface_name': 'Null0',
                                    'neighbor_address': '0.0.0.0/32',
                                    'urib': True,
                                    'vrf_id': '1'}}},
                        '192.168.64.0/8': 
                            {'path': 
                                {'0.0.0.0/32 Null0': 
                                    {'interface_name': 'Null0',
                                    'neighbor_address': '0.0.0.0/32',
                                    'urib': True,
                                    'vrf_id': '1'}}}}}}},
        'management': 
            {'address_family': 
                {'ipv4': 
                    {'mroute': 
                        {'0.0.0.0/0': 
                            {'path': 
                                {'172.31.200.1/32': 
                                    {'neighbor_address': '172.31.200.1/32',
                                    'urib': True,
                                    'vrf_id': '3'}}}}}}},
        'sanity1': 
            {'address_family': 
                {'ipv4': 
                    {'mroute': 
                        {'10.2.2.2/32': 
                            {'path': 
                                {'0.0.0.0/32 Vlan2': 
                                    {'interface_name': 'Vlan2',
                                    'neighbor_address': '0.0.0.0/32',
                                    'urib': True,
                                    'vrf_id': '4'}}},
                        '10.2.2.3/32': 
                            {'path': 
                                {'0.0.0.0/32 Vlan2': 
                                    {'interface_name': 'Vlan2',
                                    'neighbor_address': '0.0.0.0/32',
                                    'urib': True,
                                    'vrf_id': '4'}}}}}}}}}
