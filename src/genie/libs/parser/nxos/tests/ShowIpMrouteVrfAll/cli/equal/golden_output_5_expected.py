

expected_output = {
    'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'multicast_group': {
                            '225.0.0.249/32': {
                                'source_address': {
                                    '1.2.3.4/32': {
                                        'uptime': '01:07:11',
                                        'flags': 'ip pim static',
                                        'oil_count': 1,
                                        'incoming_interface_list': {
                                            'Ethernet1/2': {
                                                'rpf_nbr': '10.2.3.1',
                                                'internal': True,
                                                'router_id': '2.2.2.2'
                                            }
                                        },
                                        'outgoing_interface_list': {
                                            'loopback0': {
                                                'oil_uptime': '01:07:11',
                                                'oil_flags': 'static'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }