

expected_output = {
    'vrf':
        {'VRF1':
            {'address_family':
                {'ipv4 unicast':
                    {'aggregate_address_as_set': True,
                    'aggregate_address_ipv4_address': '10.84.0.0',
                    'aggregate_address_ipv4_mask': '8',
                    'aggregate_address_summary_only': True,
                    'bgp_table_version': 35,
                    'local_router_id': '10.229.11.11',
                    'prefixes':
                        {'10.121.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'a',
                                    'status_codes': '*>',
                                    'weight': 32768},
                                2:
                                    {'next_hop': '10.144.6.6',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': 'e',
                                    'path_type': 'a',
                                    'status_codes': '*>',
                                    'weight': 32768},
                                3:
                                    {'next_hop': '10.64.4.4',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': 'e',
                                    'path_type': 'a',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                                '10.229.11.11/32':
                                    {'index':
                                        {1:
                                        {'next_hop': '0.0.0.0',
                                        'localprf': 100,
                                        'metric': 0,
                                        'origin_codes': '?',
                                        'path_type': 'r',
                                        'status_codes': '*>',
                                        'weight': 32768}}},
                        '10.84.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'a',
                                    'status_codes': ' ',
                                    'weight': 32768}}},
                        '10.21.33.33/32':
                            {'index':
                                {1:
                                    {'next_hop': '10.36.3.3',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '*>',
                                    'weight': 0}}},
                        '10.34.34.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'l',
                                    'status_codes': ' ',
                                    'weight': 32768}}}}},
                'ipv6 unicast':
                    {'bgp_table_version': 28,
                    'local_router_id': '10.229.11.11',
                    'prefixes':
                        {'2001:db8:400::/8':
                            {'index':
                                {1:
                                    {'next_hop': '0::',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'a',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '2001:111:222::/64':
                            {'index':
                                {1:
                                    {'next_hop': '0::',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'l',
                                    'status_codes': ' ',
                                    'weight': 32768}}},
                        '2001::11/128':
                            {'index':
                                {1:
                                    {'next_hop': '0::',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '2001::33/128':
                            {'index':
                                {1:
                                    {'next_hop': '::ffff:10.36.3.3',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '*>',
                                    'weight': 0}}}},
                    'v6_aggregate_address_as_set': True,
                    'v6_aggregate_address_ipv6_address': '2001:db8:400::/8',
                    'v6_aggregate_address_summary_only': True}}},
        'default':
            {'address_family':
                {'vpnv4 unicast':
                    {'bgp_table_version': 48,
                    'local_router_id': '10.4.1.1'},
                'vpnv4 unicast RD 100:100':
                    {'aggregate_address_as_set': True,
                    'aggregate_address_ipv4_address': '10.84.0.0',
                    'aggregate_address_ipv4_mask': '8',
                    'aggregate_address_summary_only': True,
                    'bgp_table_version': 48,
                    'default_vrf': 'VRF1',
                    'local_router_id': '10.4.1.1',
                    'prefixes':
                        {'10.121.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'a',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.229.11.11/32':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '10.84.0.0/8':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'a',
                                    'status_codes': ' ',
                                    'weight': 32768}}},
                        '10.21.33.33/32':
                            {'index':
                                {1:
                                    {'next_hop': '10.36.3.3',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '*>',
                                    'weight': 0}}},
                        '10.34.34.0/24':
                            {'index':
                                {1:
                                    {'next_hop': '0.0.0.0',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'l',
                                    'status_codes': ' ',
                                    'weight': 32768}}}},
                    'route_distinguisher': '100:100'},
                'vpnv6 unicast':
                    {'bgp_table_version': 41,
                    'local_router_id': '10.4.1.1'},
                'vpnv6 unicast RD 100:100':
                    {'bgp_table_version': 41,
                    'default_vrf': 'VRF1',
                    'local_router_id': '10.4.1.1',
                    'prefixes':
                        {'2001:db8:400::/8':
                            {'index':
                                {1:
                                    {'next_hop': '0::',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'a',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '2001:111:222::/64':
                            {'index':
                                {1:
                                    {'next_hop': '0::',
                                    'localprf': 100,
                                    'origin_codes': 'i',
                                    'path_type': 'l',
                                    'status_codes': ' ',
                                    'weight': 32768}}},
                        '2001::11/128':
                            {'index':
                                {1:
                                    {'next_hop': '0::',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'r',
                                    'status_codes': '*>',
                                    'weight': 32768}}},
                        '2001::33/128':
                            {'index':
                                {1:
                                    {'next_hop': '::ffff:10.36.3.3',
                                    'localprf': 100,
                                    'metric': 0,
                                    'origin_codes': '?',
                                    'path_type': 'i',
                                    'status_codes': '*>',
                                    'weight': 0}}}},
                    'route_distinguisher': '100:100',
                    'v6_aggregate_address_as_set': True,
                    'v6_aggregate_address_ipv6_address': '2001:db8:400::/8',
                    'v6_aggregate_address_summary_only': True}}}}}
