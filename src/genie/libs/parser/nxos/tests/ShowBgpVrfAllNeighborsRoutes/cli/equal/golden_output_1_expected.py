

expected_output = {
    'vrf':
        {'default':
            {'neighbor':
                {'10.186.0.2':
                    {'address_family':
                        {'ipv4 label unicast':
                            {'bgp_table_version': 28,
                            'local_router_id': '10.186.101.1',
                            'routes':
                                {'10.106.0.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '10.186.0.2',
                                            'locprf': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'path_type': 'i',
                                            'status_codes': '* ',
                                            'weight': 0}}},
                                '192.168.51.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '10.186.0.2',
                                            'locprf': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'path_type': 'i',
                                            'status_codes': '* ',
                                            'weight': 0}}},
                                        '10.16.0.0/8':
                                            {'index':
                                                {1:
                                                    {'next_hop': '10.186.0.2',
                                                    'locprf': 100,
                                                    'metric': 0,
                                                    'origin_codes': '?',
                                                    'path_type': 'i',
                                                    'status_codes': '*>',
                                                    'weight': 0}}}}},
                        'ipv4 multicast':
                            {'bgp_table_version': 19,
                            'local_router_id': '10.186.101.1',
                            'routes':
                                {'10.106.0.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '10.186.0.2',
                                            'locprf': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'path_type': 'i',
                                            'status_codes': '*>',
                                            'weight': 0}}},
                                '192.168.51.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '10.186.0.2',
                                            'locprf': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'path_type': 'i',
                                            'status_codes': '*>',
                                            'weight': 0}}},
                                '10.16.0.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '10.186.0.2',
                                            'locprf': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'path_type': 'i',
                                            'status_codes': '*>',
                                            'weight': 0}}}}},
                        'ipv4 mvpn':
                            {'bgp_table_version': 2,
                            'local_router_id': '10.186.101.1',
                            'routes': {}},
                        'ipv4 unicast':
                            {'bgp_table_version': 25,
                            'local_router_id': '10.186.101.1',
                            'routes':
                                {'10.106.0.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '10.186.0.2',
                                            'locprf': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'path_type': 'i',
                                            'status_codes': '* ',
                                            'weight': 0}}},
                                '192.168.51.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '10.186.0.2',
                                            'locprf': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'path_type': 'i',
                                            'status_codes': '* ',
                                            'weight': 0}}},
                                '10.16.0.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '10.186.0.2',
                                            'locprf': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'path_type': 'i',
                                            'status_codes': '*>',
                                            'weight': 0}}}}},
                        'ipv6 multicast':
                            {'bgp_table_version': 2,
                            'local_router_id': '10.186.101.1',
                            'routes': {}},
                        'ipv6 mvpn':
                            {'bgp_table_version': 2,
                            'local_router_id': '10.186.101.1',
                            'routes': {}},
                        'ipv6 unicast':
                            {'bgp_table_version': 7,
                            'local_router_id': '10.186.101.1',
                            'routes': {}},
                        'link-state':
                            {'bgp_table_version': 2,
                            'local_router_id': '10.186.101.1',
                            'routes': {}},
                        'vpnv4 unicast':
                            {'bgp_table_version': 23,
                            'local_router_id': '10.186.101.1',
                            'routes': {}},
                        'vpnv4 unicast RD 2:100':
                            {'bgp_table_version': 23,
                            'default_vrf': 'vpn2',
                            'local_router_id': '10.186.101.1',
                            'route_distinguisher': '2:100',
                            'routes':
                                {'10.16.0.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '10.186.0.2',
                                            'locprf': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'path_type': 'i',
                                            'status_codes': '*>',
                                            'weight': 0}}}}},
                        'vpnv4 unicast RD 1:100':
                            {'bgp_table_version': 23,
                            'default_vrf': 'vpn1',
                            'local_router_id': '10.186.101.1',
                            'route_distinguisher': '1:100',
                            'routes':
                                {'10.16.0.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '10.186.0.2',
                                            'locprf': 100,
                                            'metric': 0,
                                            'origin_codes': '?',
                                            'path_type': 'i',
                                            'status_codes': '*>',
                                            'weight': 0}}}}},
                        'vpnv6 unicast':
                            {'bgp_table_version': 7,
                            'local_router_id': '10.186.101.1',
                            'routes': {}},
                        'vpnv6 unicast RD 1:100':
                            {'bgp_table_version': 7,
                            'default_vrf': 'vpn1',
                            'local_router_id': '10.186.101.1',
                            'route_distinguisher': '1:100',
                            'routes': {}},
                        'vpnv6 unicast RD 2:100':
                            {'bgp_table_version': 7,
                            'default_vrf': 'vpn2',
                            'local_router_id': '10.186.101.1',
                            'route_distinguisher': '2:100',
                            'routes': {}}}}}}}}
