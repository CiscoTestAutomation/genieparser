expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        '1:2:3::/64': {
                            'route': '1:2:3::/64',
                            'active': True,
                            'metric': 0,
                            'route_preference': 0,
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
                        '1:2:3::4/128': {
                            'route': '1:2:3::4/128',
                            'active': True,
                            'metric': 0,
                            'route_preference': 0,
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
                        '10:1:1::/64': {
                            'route': '10:1:1::/64',
                            'active': True,
                            'metric': 0,
                            'route_preference': 1,
                            'source_protocol': 'static',
                            'source_protocol_codes': 'S',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '1:2:3::5',
                                        'outgoing_interface': 'Ethernet0/0',
                                        'vrf': 'default'
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
