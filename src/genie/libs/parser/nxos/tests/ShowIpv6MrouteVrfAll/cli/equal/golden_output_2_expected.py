

expected_output = {
    'vrf': 
        {'VRF1': 
            {'address_family': 
                {'ipv6': {}}},
        'blue': 
            {'address_family': 
                {'ipv6': 
                    {'multicast_group': 
                        {'ff30::/12': 
                            {'source_address': 
                                {'*': 
                                    {'flags': 'ipv6 pim6',
                                    'incoming_interface_list': 
                                        {'Null': 
                                            {'rpf_nbr': '0::'}},
                                    'oil_count': '0',
                                    'uptime': '10w5d'}}}}}}},
        'default': 
            {'address_family': 
                {'ipv6': 
                    {'multicast_group': 
                        {'ff03:3::/64': 
                            {'source_address': 
                                {'*': 
                                    {'bidir': True,
                                    'flags': 'pim6',
                                    'incoming_interface_list': 
                                        {'Null': 
                                            {'rpf_nbr': '0::'}},
                                    'oil_count': '0',
                                    'uptime': '10w5d'}}},
                        'ff30::/12': 
                            {'source_address': 
                                {'*': 
                                    {'flags': 'ipv6 pim6',
                                    'incoming_interface_list': 
                                        {'Null': 
                                            {'rpf_nbr': '0::'}},
                                    'oil_count': '0',
                                    'uptime': '10w5d'}}}}}}}}}
