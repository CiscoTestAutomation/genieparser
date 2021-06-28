expected_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '0.0.0.0/0': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '172.16.0.88',
                                            'outgoing_interface': 'Bundle-Ether1',
                                            'updated': '3d00h',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '172.16.0.96',
                                            'outgoing_interface': 'Bundle-Ether2',
                                            'updated': '3d00h',
                                        },
                                    },
                                },
                                'route': '0.0.0.0/0',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O* E2',
                            },
                            '10.4.1.1/32': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback100': {
                                            'outgoing_interface': 'Loopback100',
                                            'updated': '5w6d',
                                        },
                                    },
                                },
                                'route': '10.4.1.1/32',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                            },
                            '10.1.1.0/24': {
                                'active': True,
                                'metric': 66036,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '172.16.0.88',
                                            'outgoing_interface': 'Bundle-Ether1',
                                            'updated': '2d23h',
                                        },
                                        2: {
                                            'index': 2,
                                            'next_hop': '172.16.0.96',
                                            'outgoing_interface': 'Bundle-Ether2',
                                            'updated': '2d23h',
                                        },
                                    },
                                },
                                'route': '10.1.1.0/24',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O',
                            },
                            '10.10.10.21/32': {
                                'active': True,
                                'metric': 1,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '172.16.0.88',
                                            'outgoing_interface': 'Bundle-Ether1',
                                            'updated': '3d04h',
                                        },
                                    },
                                },
                                'route': '10.10.10.21/32',
                                'route_preference': 110,
                                'source_protocol': 'ospf',
                                'source_protocol_codes': 'O E2',
                            },
                            '10.10.10.255/32': {
                                'active': True,
                                'next_hop': {
                                    'outgoing_interface': {
                                        'Loopback2112': {
                                            'outgoing_interface': 'Loopback2112',
                                            'updated': '5w6d',
                                        },
                                    },
                                },
                                'route': '10.10.10.255/32',
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                            },
                        },
                    },
                },
                'last_resort': {
                    'gateway': '172.16.0.88',
                    'to_network': '0.0.0.0'
                },
            },
        },
    }
