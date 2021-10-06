

expected_output = {
    'vrf':
        {'default':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'1':
                            {'areas':
                                {'0.0.0.1':
                                    {'virtual_links':
                                        {'0.0.0.1 10.64.4.4':
                                            {'backbone_area_id': '0.0.0.0',
                                            'cost': 40,
                                            'dead_interval': 40,
                                            'hello_interval': 10,
                                            'hello_timer': '00:00:05',
                                            'index': 7,
                                            'interface': 'Ethernet1/5',
                                            'interface_type': 'point_to_point',
                                            'link_state': 'up',
                                            'name': 'VL1',
                                            'nbr_adjs': 1,
                                            'nbr_flood': 1,
                                            'nbr_total': 1,
                                            'neighbors':
                                                {'10.64.4.4':
                                                    {'address': '10.19.4.4',
                                                    'dbd_option': '0x72',
                                                    'dead_timer': '00:00:33',
                                                    'hello_option': '0x32',
                                                    'last_change': '00:07:51',
                                                    'last_non_hello_received': '00:07:49',
                                                    'neighbor_router_id': '10.64.4.4',
                                                    'state': 'full',
                                                    'statistics':
                                                        {'nbr_event_count': 5}}},
                                            'remote_addr': '10.19.4.4',
                                            'retransmit_interval': 5,
                                            'router_id': '10.64.4.4',
                                            'state': 'point_to_point',
                                            'statistics':
                                                {'link_scope_lsa_cksum_sum': 0,
                                                'link_scope_lsa_count': 0},
                                            'transit_area_id': '0.0.0.1',
                                            'transmit_delay': 1,
                                            'unnumbered_interface': 'Ethernet1/5',
                                            'unnumbered_ip_address': '10.19.4.3',
                                            'wait_interval': 40}}}}}}}}}}}
