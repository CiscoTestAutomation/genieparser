

expected_output = {
    'vrf': 
        {'VRF': 
            {'address_family': 
                {'ipv4': {}}},
        'VRF1': 
            {'address_family': 
                {'ipv4': 
                    {'multicast_group': 
                        {'232.0.0.0/8': 
                            {'source_address': 
                                {'*': 
                                    {'flags': 'ip pim',
                                    'incoming_interface_list': 
                                        {'Null': 
                                            {'rpf_nbr': '0.0.0.0'}},
                                    'oil_count': 0,
                                    'uptime': '3d11h'}}},
                        '239.5.5.5/32': 
                            {'source_address': 
                                {'*': 
                                    {'flags': 'igmp ip pim',
                                    'incoming_interface_list': 
                                        {'Null': 
                                            {'rpf_nbr': '0.0.0.0'}},
                                    'oil_count': 1,
                                    'outgoing_interface_list': 
                                        {'loopback1': 
                                            {'oil_flags': 'igmp',
                                            'oil_uptime': '3d11h'}},
                                    'uptime': '3d11h'}}}}}}},
        'VRF2': 
            {'address_family': 
                {'ipv4': 
                    {'multicast_group': 
                        {'224.192.1.10/32': 
                            {'source_address': 
                                {'*': 
                                    {'flags': 'igmp ip pim',
                                    'incoming_interface_list': 
                                        {'port-channel8': 
                                            {'rpf_nbr': '172.16.189.233'}},
                                   'oil_count': 3,
                                    'outgoing_interface_list': 
                                        {'Vlan803': 
                                            {'oil_flags': 'igmp',
                                            'oil_uptime': '09:15:11'},
                                        'Vlan812': 
                                            {'oil_flags': 'igmp',
                                            'oil_uptime': '09:14:42'},
                                        'Vlan864': 
                                            {'oil_flags': 'igmp',
                                            'oil_uptime': '09:11:22'}},
                                   'uptime': '09:15:11'},
                                '192.168.112.3/32': 
                                    {'flags': 'ip pim',
                                    'incoming_interface_list': 
                                        {'Vlan807': 
                                            {'rpf_nbr': '172.16.94.228'}},
                                    'oil_count': 1,
                                    'outgoing_interface_list': 
                                        {'port-channel9': 
                                            {'oil_flags': 'pim',
                                            'oil_uptime': '09:31:16'}},
                                    'uptime': '09:31:16'},
                                '192.168.112.4/32': 
                                    {'flags': 'ip pim',
                                    'incoming_interface_list': 
                                        {'Ethernet1/1.10': 
                                            {'rpf_nbr': '172.16.94.228'}},
                                    'oil_count': 1,
                                    'outgoing_interface_list': 
                                        {'Ethernet1/2.20': 
                                            {'oil_flags': 'pim',
                                            'oil_uptime': '09:31:16'}},
                                    'uptime': '09:31:16'}}}}}}},
        'default': 
            {'address_family': 
                {'ipv4': 
                    {'multicast_group': 
                        {'232.0.0.0/8': 
                            {'source_address': 
                                {'*': 
                                    {'flags': 'ip '
                                              'pim',
                                    'incoming_interface_list': 
                                        {'Null': 
                                            {'rpf_nbr': '0.0.0.0'}},
                                    'oil_count': 0,
                                    'uptime': '00:41:05'}}},
                        '239.1.1.1/32': 
                            {'source_address': 
                                {'*': 
                                    {'flags': 'igmp '
                                              'ip '
                                              'pim',
                                    'incoming_interface_list': 
                                        {'Ethernet9/13': 
                                            {'rpf_nbr': '10.2.3.2'}},
                                    'oil_count': 1,
                                    'outgoing_interface_list': 
                                        {'loopback2': 
                                            {'oil_flags': 'igmp',
                                            'oil_uptime': '3d11h'}},
                                    'uptime': '3d11h'}}}}}}}}}
