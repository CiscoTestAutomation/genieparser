

expected_output = {
    'neighbor':
        {'10.16.2.10':
            {'address_family':
                {'ipv4 unicast':
                    {'bgp_table_version': 21,
                    'session_state': 'idle',
                    'default_originate': True,
                    'default_originate_route_map': 'SOMENAME',
                    'third_party_nexthop': True,
                    'path':
                        {'accepted_paths': 0,
                        'memory_usage': 0,
                        'total_entries': 0},
                    'neighbor_version': 0,
                    'soo': 'SOO:100:100'}},
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
            'link': 'unknown',
            'local_as': 'None',
            'peer_index': 1,
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
            'up_time': '02:19:37'}}}
