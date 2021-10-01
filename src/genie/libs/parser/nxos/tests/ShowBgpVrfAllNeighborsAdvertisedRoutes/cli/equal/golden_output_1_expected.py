

expected_output = {
    'vrf':
        {'default':
            {'neighbor':
                {'10.16.2.10':
                    {'address_family':
                        {'ipv4 label unicast':
                            {'bgp_table_version': 28,
                            'local_router_id': '10.186.101.1',
                            'advertised': {}},
                        'ipv4 multicast':
                            {'advertised':
                                {'10.4.1.0/24':
                                    {'index':
                                        {1:
                                            {'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 3333,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}},
                                '10.9.1.0/24':
                                    {'index':
                                        {1:
                                            {'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 3333,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}},
                                '10.204.0.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 3333,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}},
                                '10.4.0.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 3333,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}},
                                '192.168.4.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 3333,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}}},
                            'bgp_table_version': 19,
                            'local_router_id': '10.186.101.1'},
                        'ipv4 mvpn':
                            {'bgp_table_version': 2,
                            'local_router_id': '10.186.101.1',
                            'advertised': {}},
                        'ipv4 unicast':
                            {'advertised':
                                {'10.4.1.0/24':
                                    {'index':
                                        {1:
                                            {'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'origin_codes': 'i',
                                            'path_type': 'l',
                                            'status_codes': '*>',
                                            'weight': 32768}}},
                                '10.16.1.0/24':
                                    {'index':
                                        {1:
                                            {'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 4444,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}},
                                '10.16.2.0/24':
                                    {'index':
                                        {1:
                                            {'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 4444,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}},
                                '10.106.0.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 4444,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}},
                                '192.168.51.0/8':
                                    {'index':
                                        {1:
                                            {'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 4444,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}}},
                            'bgp_table_version': 25,
                            'local_router_id': '10.186.101.1'},
                        'ipv6 multicast':
                            {'bgp_table_version': 2,
                            'local_router_id': '10.186.101.1',
                            'advertised': {}},
                        'ipv6 mvpn':
                            {'bgp_table_version': 2,
                            'local_router_id': '10.186.101.1',
                            'advertised': {}},
                        'ipv6 unicast':
                            {'bgp_table_version': 7,
                            'local_router_id': '10.186.101.1',
                            'advertised': {}},
                        'link-state':
                            {'bgp_table_version': 2,
                            'local_router_id': '10.186.101.1',
                            'advertised': {}},
                        'vpnv4 unicast':
                            {'bgp_table_version': 23,
                            'local_router_id': '10.186.101.1',
                            'advertised': {}},
                        'vpnv4 unicast RD 1:100': {
                            'bgp_table_version': 23,
                            'default_vrf': 'vpn1',
                            'local_router_id': '10.186.101.1',
                            'route_distinguisher': '1:100',
                            'advertised': {
                                '10.4.1.0/24':{
                                    'index': {
                                        1: {
                                            'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 3333,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}},
                                '10.9.1.0/24':{
                                    'index': {
                                        1: {
                                            'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 3333,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}}}},
                        'vpnv4 unicast RD 2:100': {
                            'bgp_table_version': 23,
                            'default_vrf': 'vpn2',
                            'local_router_id': '10.186.101.1',
                            'route_distinguisher': '2:100',
                            'advertised': {
                                '10.4.1.0/24':{
                                    'index': {
                                        1: {
                                            'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 3333,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}},
                                '10.9.1.0/24':{
                                    'index': {
                                        1: {
                                            'next_hop': '0.0.0.0',
                                            'locprf': 100,
                                            'metric': 3333,
                                            'origin_codes': '?',
                                            'path_type': 'r',
                                            'status_codes': '*>',
                                            'weight': 32768}}}}},
                        'vpnv6 unicast':
                            {'bgp_table_version': 7,
                            'local_router_id': '10.186.101.1',
                            'advertised': {}},
                        'vpnv6 unicast RD 1:100':
                            {'bgp_table_version': 7,
                            'default_vrf': 'vpn1',
                            'local_router_id': '10.186.101.1',
                            'route_distinguisher': '1:100',
                            'advertised': {}},
                        'vpnv6 unicast RD 2:100':
                            {'bgp_table_version': 7,
                            'default_vrf': 'vpn2',
                            'local_router_id': '10.186.101.1',
                            'route_distinguisher': '2:100',
                            'advertised': {}}}}}}}}
