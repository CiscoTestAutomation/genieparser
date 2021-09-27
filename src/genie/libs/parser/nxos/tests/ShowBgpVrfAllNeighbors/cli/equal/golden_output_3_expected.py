

expected_output = {
    'neighbor':
        {'10.186.101.1':
            {'address_family':
                {'ipv4 multicast':
                    {'bgp_table_version': 55,
                    'session_state': 'established',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 5,
                        'memory_usage': 660},
                    'route_reflector_client': True,
                    'neighbor_version': 55,
                    'send_community': 'both'},
                'ipv4 unicast':
                    {'bgp_table_version': 6765004,
                    'session_state': 'established',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 5,
                        'memory_usage': 660},
                    'route_reflector_client': True,
                    'neighbor_version': 6765004,
                    'send_community': 'both'},
                'ipv6 multicast':
                    {'bgp_table_version': 2,
                    'session_state': 'established',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'route_reflector_client': True,
                    'neighbor_version': 0,
                    'send_community': 'both'},
                'ipv6 unicast':
                    {'bgp_table_version': 2,
                    'session_state': 'established',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'route_reflector_client': True,
                    'neighbor_version': 0,
                    'send_community': 'both'},
                'vpnv4 unicast':
                    {'bgp_table_version': 12863408,
                     'session_state': 'established',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'route_reflector_client': True,
                    'neighbor_version': 0,
                    'send_community': 'both'},
                'vpnv6 unicast':
                    {'bgp_table_version': 2,
                     'session_state': 'established',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'route_reflector_client': True,
                    'neighbor_version': 0,
                    'send_community': 'both'}},
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
                'vpnv4_unicast': 'advertised',
                'vpnv6_unicast': 'advertised'},
            'bgp_negotiated_keepalive_timers':
                {'hold_time': 180,
                'keepalive_interval': 60,
                'keepalive_timer': 'expiry '
                                   'due '
                                   '00:00:14',
                'last_read': '00:00:45',
                'last_written': '00:00:45'},
            'bgp_neighbor_counters':
                {'messages':
                    {'received':
                        {'bytes_in_queue': 0,
                        'capability': 17,
                        'keepalives': 17,
                        'notifications': 0,
                        'opens': 5,
                        'route_refresh': 0,
                        'total': 67,
                        'total_bytes': 2261,
                        'updates': 28},
                    'sent':
                        {'bytes_in_queue': 0,
                        'capability': 17,
                        'keepalives': 17,
                        'notifications': 0,
                        'opens': 5,
                        'route_refresh': 0,
                        'total': 50,
                        'total_bytes': 1940,
                        'updates': 23}}},
            'bgp_session_transport':
                {'connection':
                    {'dropped': 4,
                    'established': 5,
                    'last_reset': 'never',
                    'reset_by': 'us',
                    'reset_reason': 'no '
                    'error'},
                'transport':
                    {'fd': '81',
                    'foreign_host': '10.186.101.1',
                    'foreign_port': '179',
                    'local_host': '10.186.0.2',
                    'local_port': '55337'}},
            'bgp_version': 4,
            'graceful_restart_paramters':
                {'restart_time_advertised_by_peer_seconds': 120,
                'restart_time_advertised_to_peer_seconds': 120,
                'stale_time_advertised_by_peer_seconds': 300},
            'link': 'ibgp',
            'local_as': 'None',
            'peer_index': 6,
            'received_bytes_queue': 0,
            'received_messages': 67,
            'received_notifications': 0,
            'remote_as': 333,
            'retry_time': 'None',
            'router_id': '10.186.101.1',
            'session_state': 'established',
            'shutdown': False,
            'up_time': '00:07:46'},
        '10.186.102.1':
            {'address_family':
                {'ipv4 multicast':
                    {'bgp_table_version': 55,
                    'session_state': 'idle',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'route_reflector_client': True,
                    'neighbor_version': 0,
                    'send_community': 'both'},
                'ipv4 unicast':
                    {'bgp_table_version': 6765004,
                     'session_state': 'idle',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'route_reflector_client': True,
                    'neighbor_version': 0,
                    'send_community': 'both'},
                'ipv6 multicast':
                    {'bgp_table_version': 2,
                     'session_state': 'idle',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'route_reflector_client': True,
                    'neighbor_version': 0,
                    'send_community': 'both'},
                'ipv6 unicast':
                    {'bgp_table_version': 2,
                     'session_state': 'idle',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'route_reflector_client': True,
                    'neighbor_version': 0,
                    'send_community': 'both'},
                'vpnv4 unicast':
                    {'bgp_table_version': 12863408,
                     'session_state': 'idle',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'neighbor_version': 0,
                    'send_community': 'both'},
                'vpnv6 unicast':
                    {'bgp_table_version': 2,
                     'session_state': 'idle',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'route_reflector_client': True,
                    'neighbor_version': 0,
                    'send_community': 'both'}},
            'bgp_negotiated_keepalive_timers':
                {'hold_time': 180,
                'keepalive_interval': 60,
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
            'link': 'ibgp',
            'local_as': 'None',
            'peer_index': 7,
            'received_bytes_queue': 0,
            'received_messages': 0,
            'received_notifications': 0,
            'remote_as': 333,
            'retry_time': '00:00:55',
            'router_id': '0.0.0.0',
            'session_state': 'idle',
            'shutdown': False,
            'up_time': '01:27:53'},
        '10.186.201.1':
            {'address_family':
                {'ipv4 multicast':
                    {'bgp_table_version': 55,
                    'session_state': 'idle',
                    'neighbor_version': 0,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'send_community': 'both'},
                'ipv4 unicast':
                    {'bgp_table_version': 6765004,
                     'session_state': 'idle',
                    'neighbor_version': 0,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'send_community': 'both'},
                'ipv6 multicast':
                    {'bgp_table_version': 2,
                     'session_state': 'idle',
                    'neighbor_version': 0,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'send_community': 'both'},
                'ipv6 unicast':
                    {'bgp_table_version': 2,
                     'session_state': 'idle',
                    'neighbor_version': 0,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'send_community': 'both'},
                'vpnv4 unicast':
                    {'bgp_table_version': 12863408,
                     'session_state': 'idle',
                    'neighbor_version': 0,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'send_community': 'both'},
                'vpnv6 unicast':
                    {'bgp_table_version': 2,
                     'session_state': 'idle',
                    'neighbor_version': 0,
                    'path':
                        {'accepted_paths': 0,
                       'memory_usage': 0},
                    'send_community': 'both'}},
            'bgp_negotiated_keepalive_timers':
                {'hold_time': 180,
                'keepalive_interval': 60,
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
            'link': 'ebgp',
            'local_as': 'None',
            'peer_index': 8,
            'received_bytes_queue': 0,
            'received_messages': 0,
            'received_notifications': 0,
            'remote_as': 888,
            'retry_time': '00:01:12',
            'router_id': '0.0.0.0',
            'session_state': 'idle',
            'shutdown': False,
            'up_time': '01:27:52'},
        '10.64.4.4':
            {'bgp_negotiated_keepalive_timers':
                {'hold_time': 180,
                'keepalive_interval': 60,
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
            'peer_index': 5,
            'received_bytes_queue': 0,
            'received_messages': 0,
            'received_notifications': 0,
            'remote_as': 0,
            'retry_time': '0.000000',
            'router_id': '0.0.0.0',
            'session_state': 'idle',
            'shutdown': False,
            'up_time': '01:27:54'},
        '2001:db8:8b05::1002':
            {'address_family':
                {'ipv4 unicast':
                    {'bgp_table_version': 6765004,
                    'session_state': 'established',
                    'neighbor_version': 6765004,
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 5,
                        'memory_usage': 660},
                    'route_reflector_client': True,
                    'send_community': 'both'}},
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
                                     'received'},
            'bgp_negotiated_keepalive_timers':
                {'hold_time': 180,
                'keepalive_interval': 60,
                'keepalive_timer': 'expiry '
                                   'due '
                                   '00:00:20',
                'last_read': '00:00:39',
                'last_written': '00:00:39'},
            'bgp_neighbor_counters':
                {'messages':
                    {'received':
                        {'bytes_in_queue': 0,
                        'capability': 6,
                        'keepalives': 17,
                        'notifications': 0,
                        'opens': 5,
                        'route_refresh': 0,
                        'total': 43,
                        'total_bytes': 1420,
                        'updates': 15},
                    'sent':
                        {'bytes_in_queue': 0,
                        'capability': 6,
                        'keepalives': 17,
                        'notifications': 0,
                        'opens': 5,
                        'route_refresh': 0,
                        'total': 33,
                        'total_bytes': 1739,
                        'updates': 20}}},
            'bgp_session_transport':
                {'connection':
                    {'dropped': 4,
                    'established': 5,
                    'last_reset': 'never',
                    'reset_by': 'us',
                    'reset_reason': 'no '
                    'error'},
                'transport':
                    {'fd': '88'}},
            'bgp_version': 4,
            'graceful_restart_paramters':
                {'restart_time_advertised_by_peer_seconds': 120,
                'restart_time_advertised_to_peer_seconds': 120,
                'stale_time_advertised_by_peer_seconds': 300},
            'link': 'ibgp',
            'local_as': 'None',
            'peer_index': 3,
            'received_bytes_queue': 0,
            'received_messages': 43,
            'received_notifications': 0,
            'remote_as': 333,
            'retry_time': 'None',
            'router_id': '10.186.101.1',
            'session_state': 'established',
            'shutdown': False,
            'up_time': '00:07:40'},
        '2001:db8:8b05::2002':
            {'address_family':
                {'ipv4 unicast':
                    {'bgp_table_version': 6765004,
                    'session_state': 'idle',
                    'state_reason': 'connect failure',
                    'neighbor_version': 0,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'send_community': 'both'},
                'ipv6 multicast':
                    {'bgp_table_version': 2,
                    'session_state': 'idle',
                    'state_reason': 'connect failure',
                    'neighbor_version': 0,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'send_community': 'both'},
                'ipv6 unicast':
                    {'bgp_table_version': 2,
                    'session_state': 'idle',
                    'state_reason': 'connect failure',
                    'neighbor_version': 0,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0},
                    'send_community': 'both'}},
            'bgp_negotiated_keepalive_timers':
                {'hold_time': 180,
                'keepalive_interval': 60,
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
            'link': 'ebgp',
            'local_as': 'None',
            'peer_index': 4,
            'received_bytes_queue': 0,
            'received_messages': 0,
            'received_notifications': 0,
            'remote_as': 888,
            'retry_time': '00:00:29',
            'router_id': '0.0.0.0',
            'session_state': 'idle',
            'state_reason': 'connect failure',
            'shutdown': False,
            'up_time': '01:27:55'}}}
