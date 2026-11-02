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
                        }
                    }
                }
            }
        }
    }
}
