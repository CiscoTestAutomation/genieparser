expected_output = {
    'vrf': {
        'multicast': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '20.20.20.0/24': {
                            'route': '20.20.20.0/24',
                            'active': True,
                            'route_preference': 1,
                            'metric': 0,
                            'source_protocol': 'static',
                            'source_protocol_codes': 'S',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '1.2.3.5'
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
