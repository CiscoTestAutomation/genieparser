
expected_output = {
    'vrf':
        {'default':
            {'address_family':
                {'ipv4 label unicast':
                    {'bgp_table_version': 28,
                    'local_router_id': '10.186.101.1',
                    'prefixes':
                        {'10.4.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'l',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.2.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.106.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768},
                                2:
                                    {'next_hop': '10.186.0.2',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '* ',
                                    'weight': 0},
                                3:
                                    {'next_hop': '2001:db8:8b05::112',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '* ',
                                    'weight': 0}}},
                        '192.168.51.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768},
                                2:
                                    {'next_hop': '10.186.0.2',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '* ',
                                    'weight': 0},
                                3:
                                    {'next_hop': '2001:db8:8b05::112',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '* ',
                                    'weight': 0}}},
                        '10.16.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '10.186.0.2',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '*>',
                                    'weight': 0},
                                2:
                                    {'next_hop': '2001:db8:8b05::112',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '* ',
                                    'weight': 0}}}}},
                'ipv4 multicast':
                    {'bgp_table_version': 19,
                    'local_router_id': '10.186.101.1',
                    'prefixes':
                        {'10.4.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 3333,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.9.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 3333,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.204.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 3333,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.106.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '10.186.0.2',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '*>',
                                    'weight': 0}}},
                        '10.4.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 3333,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '192.168.4.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 3333,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '192.168.51.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '10.186.0.2',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '*>',
                                    'weight': 0}}},
                        '10.16.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '10.186.0.2',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '*>',
                                    'weight': 0}}}}},
                'ipv4 unicast':
                    {'bgp_table_version': 25,
                    'local_router_id': '10.186.101.1',
                    'prefixes':
                        {'10.4.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'l',
                                    'status_codes': '*>',
                                    'weight': 32768},
                                2:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'i',
                                    'status_codes': '* ',
                                    'weight': 32768}}},
                        '10.16.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.2.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.106.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768},
                                2:
                                    {'next_hop': '10.186.0.2',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '* ',
                                    'weight': 0},
                                3:
                                    {'next_hop': '2001:db8:8b05::112',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '* ',
                                    'weight': 0}}},
                        '192.168.51.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768},
                                2:
                                    {'next_hop': '10.186.0.2',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '* ',
                                    'weight': 0},
                                3:
                                    {'next_hop': '2001:db8:8b05::112',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '* ',
                                    'weight': 0}}},
                        '10.16.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '10.186.0.2',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '*>',
                                    'weight': 0},
                                2:
                                    {'next_hop': '2001:db8:8b05::112',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '* ',
                                    'weight': 0}}}}},
                'ipv6 unicast':
                    {'bgp_table_version': 7,
                    'local_router_id': '10.186.101.1',
                    'prefixes':
                        {'2001:11::1/128':
                            {'index':
                                {1:
                                    {'next_hop': '0::',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}}}},
                'vpnv4 unicast':
                    {'bgp_table_version': 23,
                    'local_router_id': '10.186.101.1'},
                'vpnv4 unicast RD 1:100':
                    {'bgp_table_version': 23,
                    'default_vrf': 'vpn1',
                    'local_router_id': '10.186.101.1',
                    'prefixes':
                        {'10.4.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'l',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.2.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.106.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '192.168.51.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '10.186.0.2',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '*>',
                                    'weight': 0}}}},
                    'route_distinguisher': '1:100'},
                'vpnv4 unicast RD 2:100':
                    {'bgp_table_version': 23,
                    'default_vrf': 'vpn2',
                    'local_router_id': '10.186.101.1',
                    'prefixes':
                        {'10.16.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.2.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.106.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '192.168.51.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}}},
                    'route_distinguisher': '2:100'},
                'vpnv6 unicast':
                    {'bgp_table_version': 7,
                    'local_router_id': '10.186.101.1'},
                'vpnv6 unicast RD 2:100':
                    {'bgp_table_version': 7,
                    'default_vrf': 'vpn2',
                    'local_router_id': '10.186.101.1',
                    'prefixes':
                        {'2001:11::1/128':
                            {'index':
                                {1:
                                    {'next_hop': '0::',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}}},
                    'route_distinguisher': '2:100'},
                'vpnv6 unicast RD 1:100':
                    {'bgp_table_version': 7,
                    'default_vrf': 'vpn1',
                    'local_router_id': '10.186.101.1',
                    'prefixes':
                        {'2001:11::1/128':
                            {'index':
                                {1:
                                    {'next_hop': '0::',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}}},
                    'route_distinguisher': '1:100'},
                }},
        'vpn1':
            {'address_family':
                {'ipv4 multicast':
                    {'bgp_table_version': 6,
                    'local_router_id': '10.229.11.11',
                    'prefixes':
                        {'10.16.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.2.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.106.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '192.168.51.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}}}},
                'ipv4 unicast':
                    {'bgp_table_version': 19,
                    'local_router_id': '10.229.11.11',
                    'prefixes':
                        {'10.4.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'l',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.2.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.106.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '192.168.51.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '10.186.0.2',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '*>',
                                    'weight': 0}}}}},
                'ipv6 unicast':
                    {'bgp_table_version': 6,
                    'local_router_id': '10.229.11.11',
                    'prefixes':
                        {'2001:11::1/128':
                            {'index':
                                {1:
                                    {'next_hop': '0::',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}}}}}},
        'vpn2':
            {'address_family':
                {'ipv4 unicast':
                    {'bgp_table_version': 6,
                    'local_router_id': '10.151.22.22',
                    'prefixes':
                        {'10.16.1.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.16.2.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.106.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '192.168.51.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 4444,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}}}},
                'ipv6 unicast':
                    {'bgp_table_version': 3,
                    'local_router_id': '10.151.22.22',
                    'prefixes':
                        {'2001:11::1/128':
                            {'index':
                                {1:
                                    {'next_hop': '0::',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}}}}}}}}
