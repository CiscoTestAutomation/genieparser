

expected_output = {
    'vrf':
        {'VRF1':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'1':
                            {'areas':
                                {'0.0.0.1':
                                    {'interfaces':
                                        {'Ethernet2/1':
                                            {'neighbors':
                                                {'10.84.66.66':
                                                    {'address': '10.229.6.6',
                                                    'bdr_ip_addr': '10.229.6.2',
                                                    'dbd_options': '0x52',
                                                    'dead_timer': '00:00:38',
                                                    'dr_ip_addr': '10.229.6.6',
                                                    'hello_options': '0x12',
                                                    'last_non_hello_packet_received': 'never',
                                                    'last_state_change': '08:38:39',
                                                    'priority': 1,
                                                    'neighbor_router_id': '10.84.66.66',
                                                    'state': 'full',
                                                    'statistics':
                                                        {'nbr_event_count': 6}}}}},
                                    'sham_links':
                                        {'10.151.22.22 10.229.11.11':
                                            {'neighbors':
                                                {'10.229.11.11':
                                                    {'address': '10.229.11.11',
                                                    'dbd_options': '0x72',
                                                    'dead_timer': '00:00:41',
                                                    'hello_options': '0x32',
                                                    'last_non_hello_packet_received': 'never',
                                                    'last_state_change': '08:16:20',
                                                    'neighbor_router_id': '10.229.11.11',
                                                    'state': 'full',
                                                    'statistics':
                                                        {'nbr_event_count': 8}}}}}}}}}}}},
        'default':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'1':
                            {'areas':
                                {'0.0.0.0':
                                    {'interfaces':
                                        {'Ethernet1/2':
                                            {'neighbors':
                                                {'10.4.1.1':
                                                    {'address': '10.1.3.1',
                                                    'bdr_ip_addr': '10.1.3.3',
                                                    'dbd_options': '0x52',
                                                    'dead_timer': '00:00:36',
                                                    'dr_ip_addr': '10.1.3.1',
                                                    'hello_options': '0x12',
                                                    'last_non_hello_packet_received': '00:00:15',
                                                    'last_state_change': '11:04:28',
                                                    'priority': 1,
                                                    'neighbor_router_id': '10.4.1.1',
                                                    'state': 'full',
                                                    'statistics':
                                                        {'nbr_event_count': 5}}}},
                                        'Ethernet2/2':
                                            {'neighbors':
                                                {'10.36.3.3':
                                                    {'address': '10.2.3.3',
                                                    'bdr_ip_addr': '10.2.3.2',
                                                    'dbd_options': '0x52',
                                                    'dead_timer': '00:00:39',
                                                    'dr_ip_addr': '10.2.3.3',
                                                    'hello_options': '0x12',
                                                    'last_non_hello_packet_received': 'never',
                                                    'last_state_change': '08:38:40',
                                                    'priority': 1,
                                                    'neighbor_router_id': '10.36.3.3',
                                                    'state': 'full',
                                                    'statistics':
                                                        {'nbr_event_count': 5}}}},
                                        'Ethernet2/3':
                                            {'neighbors':
                                                {'10.64.4.4':
                                                    {'address': '10.2.4.4',
                                                    'bdr_ip_addr': '10.2.4.2',
                                                    'dbd_options': '0x52',
                                                    'dead_timer': '00:00:33',
                                                    'dr_ip_addr': '10.2.4.4',
                                                    'hello_options': '0x12',
                                                    'last_non_hello_packet_received': 'never',
                                                    'last_state_change': '08:38:42',
                                                    'priority': 1,
                                                    'neighbor_router_id': '10.64.4.4',
                                                    'state': 'full',
                                                    'statistics':
                                                        {'nbr_event_count': 6}}}},
                                        'Ethernet2/4':
                                            {'neighbors':
                                                {'10.4.1.1':
                                                    {'address': '10.1.2.1',
                                                    'bdr_ip_addr': '10.1.2.2',
                                                    'dbd_options': '0x52',
                                                    'dead_timer': '00:00:35',
                                                    'dr_ip_addr': '10.1.2.1',
                                                    'hello_options': '0x12',
                                                    'last_non_hello_packet_received': 'never',
                                                    'last_state_change': '08:38:41',
                                                    'priority': 1,
                                                    'neighbor_router_id': '10.4.1.1',
                                                    'state': 'full',
                                                    'statistics':
                                                        {'nbr_event_count': 5}}}}},
                                    'virtual_links':
                                        {'0.0.0.1 10.64.4.4':
                                            {'neighbors':
                                                {'10.64.4.4':
                                                    {'address': '10.19.4.4',
                                                    'dbd_options': '0x72',
                                                    'dead_timer': '00:00:43',
                                                    'hello_options': '0x32',
                                                    'last_non_hello_packet_received': '00:00:18',
                                                    'last_state_change': '00:00:23',
                                                    'neighbor_router_id': '10.64.4.4',
                                                    'state': 'full',
                                                    'statistics':
                                                        {'nbr_event_count': 5}}}}}},
                                '0.0.0.1':
                                    {'interfaces':
                                        {'Ethernet1/3':
                                            {'neighbors':
                                                {'10.100.2.2':
                                                    {'address': '10.229.3.2',
                                                    'bdr_ip_addr': '10.229.3.3',
                                                    'dbd_options': '0x52',
                                                    'dead_timer': '00:00:36',
                                                    'dr_ip_addr': '10.229.3.2',
                                                    'hello_options': '0x12',
                                                    'last_non_hello_packet_received': '00:00:18',
                                                    'last_state_change': '11:04:25',
                                                    'priority': 1,
                                                    'neighbor_router_id': '10.100.2.2',
                                                    'state': 'full',
                                                    'statistics':
                                                        {'nbr_event_count': 5}}}},
                                        'Ethernet1/5':
                                            {'neighbors':
                                                {'10.64.4.4':
                                                    {'address': '10.19.4.4',
                                                    'bdr_ip_addr': '10.19.4.3',
                                                    'dbd_options': '0x52',
                                                    'dead_timer': '00:00:36',
                                                    'dr_ip_addr': '10.19.4.4',
                                                    'hello_options': '0x12',
                                                    'last_non_hello_packet_received': '00:00:18',
                                                    'last_state_change': '11:04:28',
                                                    'priority': 1,
                                                    'neighbor_router_id': '10.64.4.4',
                                                    'state': 'full',
                                                    'statistics':
                                                        {'nbr_event_count': 6}}}}}}}}}}}}}}
