expected_output = {
    'protocols': 
        {'bgp': 
            {'address_family': 
                {'vpnv4 unicast': 
                    {'distance': 
                        {'external': 20,
                        'internal': 200,
                        'local': 200},
                    'neighbors': 
                        {'10.64.4.4': 
                            {'gr_enable': 'No',
                            'last_update': '00:01:28',
                            'nsr_state': 'None'}}},
                'vpnv6 unicast': 
                    {'distance': 
                        {'external': 20,
                        'internal': 200,
                        'local': 200},
                    'neighbors': 
                        {'10.64.4.4': 
                            {'gr_enable': 'No',
                            'last_update': '00:01:28',
                            'nsr_state': 'None'}}}},
            'bgp_pid': 100,
            'graceful_restart': 
                {'enable': False},
            'nsr': 
                {'current_state': 'active ready',
                'enable': True}},
        'ospf': 
            {'vrf': 
                {'default': 
                    {'address_family': 
                        {'ipv4': 
                            {'instance': 
                                {'1': 
                                    {'areas': 
                                        {'0.0.0.0': 
                                            {'interfaces': ['Loopback0', 'GigabitEthernet0/0/0/0', 'GigabitEthernet0/0/0/2'],
                                            'mpls': 
                                                {'te': 
                                                    {'enable': True}}}},
                                            'nsf': False,
                                    'preference': 
                                        {'multi_values': 
                                            {'external': 114,
                                            'granularity': 
                                                {'detail': 
                                                    {'inter_area': 113,
                                                    'intra_area': 112}}},
                                        'single_value': 
                                            {'all': 110}},
                                    'redistribution': 
                                        {'bgp': 
                                            {'bgp_id': 100,
                                            'metric': 111},
                                        'connected': 
                                            {'enabled': True},
                                        'isis': 
                                            {'isis_pid': '10',
                                            'metric': 3333},
                                        'static': 
                                            {'enabled': True,
                                            'metric': 10}},
                                    'router_id': '10.36.3.3'}}}}}}}}}
