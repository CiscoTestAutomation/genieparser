

expected_output = {
    'vrf':
        {'default':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'100':
                            {'areas':
                                {'0.0.0.1':
                                    {'interfaces':
                                        {'loopback0':
                                            {'bfd':
                                                {'enable': False},
                                            'cost': 1,
                                            'enable': True,
                                            'if_cfg': True,
                                            'index': 3,
                                            'interface_type': 'loopback',
                                            'ip_address': '192.168.111.1/32',
                                            'line_protocol': 'up',
                                            'name': 'loopback0',
                                            'state': 'loopback'},
                                        'loopback21':
                                            {'bfd':
                                                {'enable': False},
                                            'cost': 1,
                                            'enable': True,
                                            'if_cfg': True,
                                            'index': 2,
                                            'interface_type': 'loopback',
                                            'ip_address': '192.168.136.1/32',
                                            'line_protocol': 'up',
                                            'name': 'loopback21',
                                            'state': 'loopback'},
                                        'port-channel1.100':
                                            {'bdr_ip_addr': '192.168.234.1',
                                            'bdr_router_id': '192.168.111.1',
                                            'bfd':
                                                {'enable': False},
                                            'cost': 1,
                                            'dead_interval': 40,
                                            'dr_ip_addr': '192.168.234.2',
                                            'dr_router_id': '192.168.246.1',
                                            'enable': True,
                                            'hello_interval': 10,
                                            'hello_timer': '00:00:04',
                                            'if_cfg': True,
                                            'index': 1,
                                            'interface_type': 'broadcast',
                                            'ip_address': '192.168.234.1/24',
                                            'line_protocol': 'up',
                                            'name': 'port-channel1.100',
                                            'passive': False,
                                            'priority': 1,
                                            'retransmit_interval': 5,
                                            'state': 'bdr',
                                            'statistics':
                                                {'link_scope_lsa_cksum_sum': 0,
                                                'link_scope_lsa_count': 0,
                                                'num_nbrs_adjacent': 1,
                                                'num_nbrs_flooding': 1,
                                                'total_neighbors': 1},
                                            'transmit_delay': 1,
                                            'wait_interval': 40}}}}},
                        '2':
                            {'areas':
                                {'0.0.0.1':
                                    {'interfaces':
                                        {'loopback3':
                                            {'bfd':
                                                {'enable': False},
                                            'cost': 1,
                                            'enable': True,
                                            'if_cfg': True,
                                            'index': 2,
                                            'interface_type': 'loopback',
                                            'ip_address': '192.168.51.1/32',
                                            'line_protocol': 'up',
                                            'name': 'loopback3',
                                            'state': 'loopback'},
                                        'port-channel1.103':
                                            {'bdr_ip_addr': '192.168.246.1',
                                            'bdr_router_id': '192.168.111.1',
                                            'bfd':
                                                {'enable': False},
                                            'cost': 1,
                                            'dead_interval': 40,
                                            'dr_ip_addr': '192.168.246.2',
                                            'dr_router_id': '192.168.4.1',
                                            'enable': True,
                                            'hello_interval': 10,
                                            'hello_timer': '00:00:05',
                                            'if_cfg': True,
                                            'index': 1,
                                            'interface_type': 'broadcast',
                                            'ip_address': '192.168.246.1/24',
                                            'line_protocol': 'up',
                                            'name': 'port-channel1.103',
                                            'passive': False,
                                            'priority': 1,
                                            'retransmit_interval': 5,
                                            'state': 'bdr',
                                            'statistics':
                                                {'link_scope_lsa_cksum_sum': 0,
                                                'link_scope_lsa_count': 0,
                                                'num_nbrs_adjacent': 1,
                                                'num_nbrs_flooding': 1,
                                                'total_neighbors': 1},
                                            'transmit_delay': 1,
                                            'wait_interval': 40}}}}}}}}}}}
