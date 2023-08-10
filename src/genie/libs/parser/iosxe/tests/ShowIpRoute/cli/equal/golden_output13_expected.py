expected_output = {
    'vrf': {
        'ce1': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '1.1.1.1/32': {
                            'route': '1.1.1.1/32',
                            'active': True,
                            'metric': 0,
                            'route_preference': 20,
                            'source_protocol_codes': 'B',
                            'source_protocol': 'bgp',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '99.1.2.1',
                                        'updated': '16:49:22'
                                    }
                                }
                            }
                        },
                        '1.1.1.10/32': {
                            'route': '1.1.1.10/32',
                            'active': True,
                            'metric': 0,
                            'route_preference': 200,
                            'source_protocol_codes': 'B',
                            'source_protocol': 'bgp',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'FC01:101:8:E007::',
                                        'updated': '16:48:31',
                                        'vrf': 'default:ipv6'
                                    }
                                }
                            }
                        },
                        '99.1.2.0/24': {
                            'route': '99.1.2.0/24',
                            'active': True,
                            'source_protocol_codes': 'C',
                            'source_protocol': 'connected',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Ethernet1/0': {
                                        'outgoing_interface': 'Ethernet1/0'
                                    }
                                }
                            }
                        },
                        '99.1.2.2/32': {
                            'route': '99.1.2.2/32',
                            'active': True,
                            'source_protocol_codes': 'L',
                            'source_protocol': 'local',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Ethernet1/0': {
                                        'outgoing_interface': 'Ethernet1/0'
                                    }
                                }
                            }
                        },
                        '100.1.2.0/24': {
                            'route': '100.1.2.0/24',
                            'active': True,
                            'source_protocol_codes': 'C',
                            'source_protocol': 'connected',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Ethernet1/1': {
                                        'outgoing_interface': 'Ethernet1/1'
                                    }
                                }
                            }
                        },
                        '100.1.2.2/32': {
                            'route': '100.1.2.2/32',
                            'active': True,
                            'source_protocol_codes': 'L',
                            'source_protocol': 'local',
                            'next_hop': {
                                'outgoing_interface': {
                                    'Ethernet1/1': {
                                        'outgoing_interface': 'Ethernet1/1'
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