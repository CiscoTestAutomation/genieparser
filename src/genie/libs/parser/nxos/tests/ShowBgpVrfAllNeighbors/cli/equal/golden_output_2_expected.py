

expected_output = {
    'neighbor':
        {'10.16.2.2':
            {'address_family':
                {'vpnv4 unicast':
                    {'bgp_table_version': 11,
                    'session_state': 'established',
                    'maximum_prefix_max_prefix_no': 300000,
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 1,
                        'memory_usage': 48,
                        'total_entries': 2},
                    'route_map_name_in': 'genie_redistribution',
                    'route_map_name_out': 'genie_redistribution',
                    'neighbor_version': 11,
                    'send_community': 'both'},
                'vpnv6 unicast':
                    {'bgp_table_version': 10,
                    'session_state': 'established',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 1,
                        'memory_usage': 48,
                        'total_entries': 2},
                    'neighbor_version': 10,
                    'send_community': 'both'}},
            'bfd_live_detection': True,
            'bgp_negotiated_capabilities':
                {'dynamic_capability': 'advertised '
                                       '(mp, '
                                       'refresh, '
                                       'gr) '
                                       'received '
                                       '(mp, '
                                       'refresh, '
                                       'gr)',
                'dynamic_capability_old': 'advertised '
                                          'received',
                'graceful_restart': 'advertised '
                                    'received',
                'route_refresh': 'advertised '
                                 'received',
                'route_refresh_old': 'advertised '
                                     'received',
                'vpnv4_unicast': 'advertised '
                                 'received',
                'vpnv6_unicast': 'advertised '
                                 'received',
                'ipv4_mvpn': 'advertised '
                                  'received'},
            'bgp_negotiated_keepalive_timers':
                {'hold_time': 99,
                'keepalive_interval': 33,
                'keepalive_timer': 'expiry '
                                 'due '
                                 '00:00:19',
                'last_read': '00:00:15',
                'last_written': '00:00:13'},
            'bgp_neighbor_counters':
                {'messages':
                    {'received':
                        {'bytes_in_queue': 0,
                        'capability': 0,
                        'keepalives': 256,
                        'notifications': 0,
                        'opens': 1,
                        'route_refresh': 0,
                        'total': 261,
                        'total_bytes': 5139,
                        'updates': 4},
                    'sent':
                        {'bytes_in_queue': 0,
                        'capability': 0,
                        'keepalives': 256,
                        'notifications': 0,
                        'opens': 1,
                        'route_refresh': 0,
                        'total': 263,
                        'total_bytes': 5311,
                        'updates': 6}}},
            'bgp_session_transport':
                {'connection':
                    {'dropped': 0,
                    'established': 1,
                    'last_reset': 'never',
                    'reset_by': 'peer',
                    'reset_reason': 'no '
                                    'error'},
                'transport':
                    {'fd': '44',
                    'foreign_host': '10.16.2.2',
                    'foreign_port': '179',
                    'local_host': '10.4.1.1',
                    'local_port': '57144'}},
            'bgp_version': 4,
            'description': 'nei_desc',
            'graceful_restart_paramters':
                {'restart_time_advertised_by_peer_seconds': 120,
                'restart_time_advertised_to_peer_seconds': 240,
                'stale_time_advertised_by_peer_seconds': 600},
            'link': 'ibgp',
            'local_as': 'None',
            'nbr_local_as_cmd': 'not active',
            'peer_index': 1,
            'received_bytes_queue': 0,
            'received_messages': 261,
            'received_notifications': 0,
            'remote_as': 100,
            'retry_time': 'None',
            'router_id': '10.16.2.2',
            'sent_bytes_queue': 0,
            'sent_messages': 263,
            'sent_notifications': 0,
            'session_state': 'established',
            'shutdown': False,
            'suppress_four_byte_as_capability': True,
            'up_time': '02:20:02',
            'update_source': 'loopback0'},
        '10.16.2.25':
            {'bgp_negotiated_keepalive_timers':
                {'hold_time': 45,
                'keepalive_interval': 15,
                'keepalive_timer': 'not '
                                  'running',
                'last_read': 'never',
                'last_written': 'never'},
            'bgp_neighbor_counters':
                {'messages':
                    {'received':
                        {'bytes_in_queue': 0,
                        'capability': 0,
                        'keepalives': 0,
                        'notifications': 0,
                        'opens': 0,
                        'route_refresh': 0,
                        'total': 0,
                        'total_bytes': 0,
                        'updates': 0},
                    'sent':
                        {'bytes_in_queue': 0,
                        'capability': 0,
                        'keepalives': 0,
                        'notifications': 0,
                        'opens': 0,
                        'route_refresh': 0,
                        'total': 0,
                        'total_bytes': 0,
                        'updates': 0}}},
            'bgp_session_transport':
                {'connection':
                    {'dropped': 0,
                    'established': 0,
                    'last_reset': 'never',
                    'reset_by': 'peer',
                    'reset_reason': 'no '
                                    'error'}},
            'bgp_version': 4,
            'link': 'unknown',
            'local_as': 'None',
            'peer_index': 3,
            'received_bytes_queue': 0,
            'received_messages': 0,
            'received_notifications': 0,
            'remote_as': 0,
            'retry_time': '0.000000',
            'router_id': '0.0.0.0',
            'sent_bytes_queue': 0,
            'sent_messages': 0,
            'sent_notifications': 0,
            'session_state': 'idle',
            'shutdown': False,
            'up_time': '02:20:08'},
        '10.16.2.5':
            {'address_family':
                {'ipv4 unicast':
                    {'as_override': True,
                    'as_override_count': 9,
                    'bgp_table_version': 2,
                    'session_state': 'shut',
                    'state_reason': 'admin',
                    'inherit_peer_policy':
                        {'PEER-POLICY':
                            {'inherit_peer_seq': 10},
                        'PEER-POLICY2':
                            {'inherit_peer_seq': 20}},
                    'maximum_prefix_max_prefix_no': 300,
                    'default_originate': True,
                    'next_hop_self': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0,
                        'total_entries': 0},
                    'route_map_name_in': 'test-map',
                    'route_map_name_out': 'test-map',
                    'neighbor_version': 0,
                    'send_community': 'both',
                    'soft_configuration': True}},
            'bfd_live_detection': True,
            'bfd_enabled': True,
            'bfd_state': 'up',
            'remove_private_as': True,
            'bgp_negotiated_keepalive_timers':
                {'hold_time': 45,
                'keepalive_interval': 15,
                'keepalive_timer': 'not '
                'running',
                'last_read': 'never',
                'last_written': 'never'},
            'bgp_neighbor_counters':
                {'messages':
                    {'received':
                        {'bytes_in_queue': 0,
                        'capability': 0,
                        'keepalives': 0,
                        'notifications': 0,
                        'opens': 0,
                        'route_refresh': 0,
                        'total': 0,
                        'total_bytes': 0,
                        'updates': 0},
                    'sent':
                        {'bytes_in_queue': 0,
                        'capability': 0,
                        'keepalives': 0,
                        'notifications': 0,
                        'opens': 0,
                        'route_refresh': 0,
                        'total': 0,
                        'total_bytes': 0,
                        'updates': 0}}},
            'bgp_session_transport':
                {'connection':
                    {'dropped': 0,
                    'established': 0,
                    'last_reset': 'never',
                    'mode': 'passive',
                    'reset_by': 'peer',
                    'reset_reason': 'no '
                                    'error'}},
            'bgp_version': 4,
            'disable_connected_check': True,
            'description': 'PEER-SESSION',
            'inherit_peer_session': 'PEER-SESSION',
            'link': 'ebgp',
            'local_as': '333',
            'peer_index': 2,
            'ebgp_multihop': True,
            'ebgp_multihop_max_hop': 255,
            'received_bytes_queue': 0,
            'received_messages': 0,
            'received_notifications': 0,
            'remote_as': 200,
            'retry_time': 'None',
            'router_id': '0.0.0.0',
            'sent_bytes_queue': 0,
            'sent_messages': 0,
            'sent_notifications': 0,
            'session_state': 'shut',
            'state_reason': 'admin',
            'shutdown': True,
            'tcp_md5_auth': 'enabled',
            'tcp_md5_auth_config': 'TCP MD5 authentication '
                                   'is enabled',
            'up_time': '02:20:09',
            'update_source': 'loopback0'}}}
