

expected_output = {
    'vrf':
        {'VRF1':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'1':
                            {'areas':
                                {'0.0.0.1':
                                    {'sham_links':
                                        {'10.151.22.22 10.229.11.11':
                                            {'backbone_area_id': '0.0.0.0',
                                            'cost': 1,
                                            'dead_interval': 40,
                                            'destination': '10.229.11.11',
                                            'hello_interval': 10,
                                            'hello_timer': '00:00:02',
                                            'index': 6,
                                            'interface_type': 'point_to_point',
                                            'link_state': 'up',
                                            'local_id': '10.151.22.22',
                                            'name': 'SL1',
                                            'nbr_adjs': 1,
                                            'nbr_flood': 1,
                                            'nbr_total': 1,
                                            'neighbors':
                                                {'10.229.11.11':
                                                    {'address': '10.229.11.11',
                                                    'area': '0.0.0.1',
                                                    'backbone_area_id': '0.0.0.0',
                                                    'dbd_option': '0x72',
                                                    'dead_timer': '00:00:38',
                                                    'hello_option': '0x32',
                                                    'instance': '1',
                                                    'last_change': '08:10:01',
                                                    'last_non_hello_received': 'never',
                                                    'local': '10.151.22.22',
                                                    'neighbor_router_id': '10.229.11.11',
                                                    'remote': '10.229.11.11',
                                                    'state': 'full',
                                                    'statistics': {'nbr_event_count': 8}}},
                                            'remote_id': '10.229.11.11',
                                            'retransmit_interval': 5,
                                            'state': 'point_to_point',
                                            'statistics':
                                                {'link_scope_lsa_cksum_sum': 0,
                                                'link_scope_lsa_count': 0},
                                            'transit_area_id': '0.0.0.1',
                                            'transmit_delay': 1,
                                            'unnumbered_interface': 'loopback1',
                                            'unnumbered_ip_address': '10.151.22.22',
                                            'wait_interval': 40},
                                        '10.151.22.22 10.21.33.33':
                                            {'authentication':
                                                {'auth_trailer_key':
                                                    {'crypto_algorithm': 'simple'},
                                                'auth_trailer_key_chain':
                                                    {'key_chain': 'test',
                                                    'status': 'ready'}},
                                            'backbone_area_id': '0.0.0.0',
                                            'cost': 111,
                                            'dead_interval': 13,
                                            'destination': '10.21.33.33',
                                            'hello_interval': 3,
                                            'hello_timer': '00:00:01',
                                            'index': 7,
                                            'nbr_adjs': 0,
                                            'nbr_flood': 0,
                                            'nbr_total': 0,
                                            'interface_type': 'point_to_point',
                                            'link_state': 'up',
                                            'local_id': '10.151.22.22',
                                            'name': 'SL2',
                                            'remote_id': '10.21.33.33',
                                            'retransmit_interval': 5,
                                            'state': 'point_to_point',
                                            'statistics':
                                                {'link_scope_lsa_cksum_sum': 0,
                                                'link_scope_lsa_count': 0},
                                            'transit_area_id': '0.0.0.1',
                                            'transmit_delay': 7,
                                            'unnumbered_interface': 'loopback1',
                                            'unnumbered_ip_address': '10.151.22.22',
                                            'wait_interval': 13}}}}}}}}}}}
