expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '0.0.0.0/0': {
                            'active': True,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '5.4.0.1',
                                        'updated': '1w1d',
                                    },
                                },
                            },
                            'route': '0.0.0.0/0',
                            'route_preference': 1,
                            'source_protocol': 'static',
                            'source_protocol_codes': 'S*',
                        },
                        '5.255.253.6/32': {
                            'active': True,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '5.4.0.1',
                                        'updated': '1w1d',
                                    },
                                },
                            },
                            'route': '5.255.253.6/32',
                            'route_preference': 1,
                            'source_protocol': 'static',
                            'source_protocol_codes': 'S',
                        },
                        '5.4.0.0/16': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'MgmtEth0/RP0/CPU0/0': {
                                        'outgoing_interface': 'MgmtEth0/RP0/CPU0/0',
                                        'updated': '1w1d',
                                    },
                                    'MgmtEth0/RP1/CPU0/0': {
                                        'outgoing_interface': 'MgmtEth0/RP1/CPU0/0',
                                        'updated': '1w1d',
                                    },
                                },
                            },
                            'route': '5.4.0.0/16',
                            'source_protocol': 'connected',
                            'source_protocol_codes': 'C',
                        },
                        '5.4.23.20/32': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'MgmtEth0/RP0/CPU0/0': {
                                        'outgoing_interface': 'MgmtEth0/RP0/CPU0/0',
                                        'updated': '1w1d',
                                    },
                                },
                            },
                            'route': '5.4.23.20/32',
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                        },
                        '5.4.23.22/32': {
                            'active': True,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '5.4.23.22',
                                        'outgoing_interface': 'MgmtEth0/RP0/CPU0/0',
                                        'updated': '1w1d',
                                    },
                                },
                            },
                            'route': '5.4.23.22/32',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                        },
                    },
                },
            },
            'last_resort': {
                'gateway': '5.4.0.1',
                'to_network': '0.0.0.0',
            },
        },
    },
}