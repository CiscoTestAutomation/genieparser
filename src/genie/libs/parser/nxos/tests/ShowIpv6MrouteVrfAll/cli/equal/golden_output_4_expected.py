

expected_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv6': {
                        'multicast_group': {
                            'ff05::32/128': {
                                'source_address': {
                                    '2001:db8:dd::1/128': {
                                        'uptime': '00:10:17',
                                        'flags': 'ipv6 pim6 static',
                                        'oil_count': '1',
                                        'incoming_interface_list': {
                                            'Ethernet1/2': {
                                                'rpf_nbr': 'fe80::21e:14ff:fe79:1b08',
                                                'internal': True,
                                                'router_id': '2.2.2.2'
                                            }
                                        },
                                        'outgoing_interface_list': {
                                            'loopback0': {
                                                'oil_uptime': '00:10:17',
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