

expected_output = {
    'vrf':
        {'VRF1':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'UNDERLAY':
                            {'areas':
                                {'0.0.0.1':
                                    {'interfaces':
                                        {'Ethernet2/1':
                                            {'bdr_ip_addr': '10.229.6.2',
                                            'bdr_router_id': '10.151.22.22',
                                            'bfd':
                                                {'enable': False},
                                            'cost': 40,
                                            'dead_interval': 40,
                                            'dr_ip_addr': '10.229.6.6',
                                            'dr_router_id': '10.84.66.66',
                                            'enable': True,
                                            'hello_interval': 10,
                                            'hello_timer': '00:00:07',
                                            'if_cfg': True,
                                            'index': 2,
                                            'interface_type': 'broadcast',
                                            'ip_address': '10.229.6.2/24',
                                            'line_protocol': 'up',
                                            'name': 'Ethernet2/1',
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
                                            'wait_interval': 40}},
                                    'sham_links':
                                        {'10.151.22.22 10.229.11.11':
                                            {'bfd':
                                                {'enable': False},
                                            'cost': 1,
                                            'dead_interval': 40,
                                            'enable': True,
                                            'hello_interval': 10,
                                            'hello_timer': '00:00:07',
                                            'if_cfg': False,
                                            'index': 6,
                                            'interface_type': 'p2p',
                                            'ip_address': '10.151.22.22',
                                            'line_protocol': 'up',
                                            'name': 'SL1-0.0.0.0-10.151.22.22-10.229.11.11',
                                            'passive': False,
                                            'retransmit_interval': 5,
                                            'state': 'p2p',
                                            'statistics':
                                                {'link_scope_lsa_cksum_sum': 0,
                                                'link_scope_lsa_count': 0,
                                                'num_nbrs_adjacent': 1,
                                                'num_nbrs_flooding': 1,
                                                'total_neighbors': 1},
                                            'transmit_delay': 1,
                                            'wait_interval': 40},
                                        '10.151.22.22 10.21.33.33':
                                            {'authentication':
                                                {'auth_trailer_key':
                                                    {'crypto_algorithm': 'Simple'},
                                                    'auth_trailer_key_chain':
                                                        {'key_chain': 'test'}},
                                                'bfd':
                                                    {'enable': False},
                                                'cost': 111,
                                                'dead_interval': 13,
                                                'enable': True,
                                                'hello_interval': 3,
                                                'hello_timer': '00:00:00',
                                                'if_cfg': False,
                                                'index': 7,
                                                'interface_type': 'p2p',
                                                'ip_address': '10.151.22.22',
                                                'line_protocol': 'up',
                                                'name': 'SL2-0.0.0.0-10.151.22.22-10.21.33.33',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'state': 'p2p',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 0,
                                                    'num_nbrs_flooding': 0,
                                                    'total_neighbors': 0},
                                                'transmit_delay': 7,
                                                'wait_interval': 13}},
                                    'virtual_links':
                                        {'0.0.0.1 10.1.8.8':
                                            {'backbone_area_id': '0.0.0.0',
                                            'bfd':
                                                {'enable': False},
                                            'cost': 1,
                                            'dead_interval': 40,
                                            'enable': True,
                                            'hello_interval': 10,
                                            'hello_timer': '00:00:07',
                                            'if_cfg': False,
                                            'index': 6,
                                            'interface_type': 'p2p',
                                            'ip_address': '10.151.22.22',
                                            'line_protocol': 'up',
                                            'name': 'VL1-0.0.0.0-10.1.8.8-10.66.12.12',
                                            'passive': False,
                                            'retransmit_interval': 5,
                                            'state': 'p2p',
                                            'statistics':
                                                {'link_scope_lsa_cksum_sum': 0,
                                                'link_scope_lsa_count': 0,
                                                'num_nbrs_adjacent': 1,
                                                'num_nbrs_flooding': 1,
                                                'total_neighbors': 1},
                                            'transmit_delay': 1,
                                            'wait_interval': 40}}}}}}}}},
        'default':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'UNDERLAY':
                            {'areas':
                                {'0.0.0.0':
                                    {'interfaces':
                                        {'Ethernet2/2':
                                            {'bdr_ip_addr': '10.2.3.2',
                                            'bdr_router_id': '10.100.2.2',
                                            'bfd':
                                                {'enable': False},
                                            'cost': 1,
                                            'dead_interval': 40,
                                            'dr_ip_addr': '10.2.3.3',
                                            'dr_router_id': '10.36.3.3',
                                            'enable': True,
                                            'hello_interval': 10,
                                            'hello_timer': '00:00:02',
                                            'if_cfg': True,
                                            'index': 3,
                                            'interface_type': 'broadcast',
                                            'ip_address': '10.2.3.2/24',
                                            'line_protocol': 'up',
                                            'name': 'Ethernet2/2',
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
                                            'wait_interval': 40},
                                        'Ethernet2/3':
                                            {'bdr_ip_addr': '10.2.4.2',
                                            'bdr_router_id': '10.100.2.2',
                                            'bfd':
                                                {'enable': False},
                                            'cost': 1,
                                            'dead_interval': 40,
                                            'dr_ip_addr': '10.2.4.4',
                                            'dr_router_id': '10.64.4.4',
                                            'enable': True,
                                            'hello_interval': 10,
                                            'hello_timer': '00:00:00',
                                            'if_cfg': True,
                                            'index': 4,
                                            'interface_type': 'broadcast',
                                            'ip_address': '10.2.4.2/24',
                                            'line_protocol': 'up',
                                            'name': 'Ethernet2/3',
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
                                            'wait_interval': 40},
                                        'Ethernet2/4':
                                            {'bdr_ip_addr': '10.1.2.2',
                                            'bdr_router_id': '10.100.2.2',
                                            'bfd':
                                                {'enable': False},
                                            'cost': 1,
                                            'dead_interval': 40,
                                            'dr_ip_addr': '10.1.2.1',
                                            'dr_router_id': '10.4.1.1',
                                            'enable': True,
                                            'hello_interval': 10,
                                            'hello_timer': '00:00:00',
                                            'if_cfg': True,
                                            'index': 5,
                                            'interface_type': 'broadcast',
                                            'ip_address': '10.1.2.2/24',
                                            'line_protocol': 'up',
                                            'name': 'Ethernet2/4',
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
                                            'wait_interval': 40},
                                        'loopback0':
                                            {'bfd':
                                                {'enable': False},
                                            'cost': 1,
                                            'enable': True,
                                            'if_cfg': True,
                                            'index': 1,
                                            'interface_type': 'loopback',
                                            'ip_address': '10.100.2.2/32',
                                            'line_protocol': 'up',
                                            'name': 'loopback0',
                                            'state': 'loopback'}}}}}}}}}}}
