expected_output = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '0.0.0.0/0': {
                                'route': '0.0.0.0/0',
                                'active': True,
                                'route_preference': 200,
                                'metric': 0,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B*',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.4.4',
                                            'updated': '08:11:19',
                                        },
                                    },
                                },
                            },
                            '192.168.1.2/18': {
                                'route': '192.168.1.2/18',
                                'active': True,
                                'route_preference': 200,
                                'metric': 0,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.4.5',
                                            'updated': '1w5d',
                                        },
                                    },
                                },
                            },
                            '192.168.1.3/27': {
                                'route': '192.168.1.3/27',
                                'active': True,
                                'route_preference': 20,
                                'metric': 0,
                                'source_protocol': 'bgp',
                                'source_protocol_codes': 'B',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.4.6',
                                            'updated': '5d13h',
                                        },
                                    },
                                },
                            },
                            '192.168.1.4/32': {
                                'route': '192.168.1.4/32',
                                'active': True,
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/0/1/8': {
                                            'outgoing_interface': 'GigabitEthernet0/0/1/8',
                                            'updated': '36w5d',
                                        },
                                    },
                                },
                            },
                            '192.168.1.5/29': {
                                'route': '192.168.1.5/29',
                                'active': True,
                                'source_protocol': 'connected',
                                'source_protocol_codes': 'C',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'BVI3001': {
                                            'outgoing_interface': 'BVI3001',
                                            'updated': '36w5d',
                                        },
                                    },
                                },
                            },
                            '192.168.1.6/32': {
                                'route': '192.168.1.6/32',
                                'active': True,
                                'route_preference': 0,
                                'metric': 0,
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'index': 1,
                                            'next_hop': '192.168.4.7',
                                            'outgoing_interface': 'BVI3001',
                                            'updated': '36w5d',
                                        },
                                    },
                                },
                            },
                            '192.168.1.7/32': {
                                'route': '192.168.1.7/32',
                                'active': True,
                                'source_protocol': 'local',
                                'source_protocol_codes': 'L',
                                'next_hop': {
                                    'outgoing_interface': {
                                        'BVI3001': {
                                            'outgoing_interface': 'BVI3001',
                                            'updated': '36w5d',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                'last_resort': {
                    'gateway': '192.168.1.1',
                    'to_network': '0.0.0.0'
                },
            },
        },
    }
