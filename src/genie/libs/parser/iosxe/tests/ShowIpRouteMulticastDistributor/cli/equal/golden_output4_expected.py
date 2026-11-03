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
                        }
                    }
                }
            }
        }
    }
}
