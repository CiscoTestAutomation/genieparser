

expected_output = {
    'bgp_pid': 100,
    'total_paths': 0,
    'total_prefixes': 0,
    'vrf': 
        {'default': 
            {'address_family': 
                {'idx:l3vpn-ipv4-unicast': 
                    {'enabled': True,
                    'total_paths': 0,
                    'total_prefixes': 0},
                'idx:l3vpn-ipv6-unicast': 
                    {'enabled': True,
                    'total_paths': 0,
                    'total_prefixes': 0}},
            'neighbor': 
                {'10.16.2.2': 
                    {'address_family': 
                        {'idx:l3vpn-ipv4-unicast': 
                            {'active': False,
                            'enabled': True,
                            'prefixes_received': 0,
                            'prefixes_sent': 0},
                        'idx:l3vpn-ipv6-unicast': 
                            {'active': False,
                            'enabled': True,
                            'prefixes_received': 0,
                            'prefixes_sent': 0}},
                    'bgp_neighbor_counters': 
                        {'messages': 
                            {'received': 
                                {'notifications': 0,
                                'updates': 0},
                            'sent': 
                                {'notifications': 0,
                                'updates': 0}}},
                    'bgp_session_transport': 
                        {'transport': 
                            {'foreign_host': '0',
                            'foreign_port': '10.16.2.2',
                            'local_host': 'Loopback0',
                            'local_port': '0'}},
                    'graceful_restart_restart_time': 120,
                    'holdtime': 180,
                    'input_queue': 0,
                    'output_queue': 0,
                    'remote_as': 100,
                    'session_state': 'idle'},
                '10.36.3.3': 
                    {'address_family': 
                        {'idx:l3vpn-ipv4-unicast': 
                            {'active': False,
                            'enabled': True,
                            'prefixes_received': 0,
                            'prefixes_sent': 0},
                        'idx:l3vpn-ipv6-unicast': 
                            {'active': False,
                            'enabled': True,
                            'prefixes_received': 0,
                            'prefixes_sent': 0}},
                    'bgp_neighbor_counters': 
                        {'messages': 
                            {'received': 
                                {'notifications': 0,
                                'updates': 0},
                            'sent': 
                                {'notifications': 0,
                                'updates': 0}}},
                    'bgp_session_transport': 
                        {'transport': 
                            {'foreign_host': '0',
                            'foreign_port': '10.36.3.3',
                            'local_host': 'Loopback0',
                            'local_port': '0'}},
                    'graceful_restart_restart_time': 120,
                    'holdtime': 180,
                    'input_queue': 0,
                    'output_queue': 0,
                    'remote_as': 100,
                    'session_state': 'idle'}},
            'router_id': '10.4.1.1'}}}
