

expected_output = {
    'vrf': 
        {'VRF1': 
            {'address_family': 
                {'ipv4': {}}},
        'blue': 
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
                                    'uptime': '10w5d'}}}}}}},
        'default': 
            {'address_family': 
                {'ipv4': 
                    {'multicast_group': 
                        {'228.0.0.0/8': 
                            {'source_address': 
                                {'*': 
                                    {'bidir': True,
                                    'flags': 'ip pim',
                                    'incoming_interface_list': 
                                        {'Null': 
                                            {'rpf_nbr': '0.0.0.0'}},
                                    'oil_count': 0,
                                    'uptime': '10w5d'}}},
                        '232.0.0.0/8': 
                            {'source_address': 
                                {'*': 
                                    {'flags': 'ip pim',
                                    'incoming_interface_list': 
                                        {'Null': 
                                            {'rpf_nbr': '0.0.0.0'}},
                                    'oil_count': 0,
                                    'uptime': '10w5d'}}}}}}}}}
