expected_output = {
    'vrf': {
        'multicast': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '1.2.3.0/24': {
                            'route': '1.2.3.0/24',
                            'active': True,
                            'source_protocol': 'connected',
                            'source_protocol_codes': 'C',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Ethernet0/0': {
                                        'outgoing_interface': 'Ethernet0/0'
                                    }
                                }
                            }
                        },
                        '1.2.3.4/32': {
                            'route': '1.2.3.4/32',
                            'active': True,
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Ethernet0/0': {
                                        'outgoing_interface': 'Ethernet0/0'
                                    }
                                }
                            }
                        },
                        '10.1.1.0/24': {
                            'route': '10.1.1.0/24',
                            'active': True,
                            'route_preference': 1,
                            'metric': 0,
                            'source_protocol': 'static',
                            'source_protocol_codes': 'S +',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '1.2.3.5',
                                        'outgoing_interface': 'Ethernet0/0'
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
