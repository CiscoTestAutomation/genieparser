expected_output = {
    'vrf': {
        'foo:multicast:test': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '5.0.0.0/8': {
                            'route': '5.0.0.0/8',
                            'active': True,
                            'source_protocol': 'connected',
                            'source_protocol_codes': 'C +',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Loopback20': {
                                        'outgoing_interface': 'Loopback20'
                                    }
                                }
                            }
                        },
                        '5.5.5.1/32': {
                            'route': '5.5.5.1/32',
                            'active': True,
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L +',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Loopback20': {
                                        'outgoing_interface': 'Loopback20'
                                    }
                                }
                            }
                        },
                        '10.0.0.0/8': {
                            'route': '10.0.0.0/8',
                            'active': True,
                            'route_preference': 1,
                            'metric': 0,
                            'source_protocol': 'static',
                            'source_protocol_codes': 'S +',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '5.5.5.2',
                                        'outgoing_interface': 'Loopback20'
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
