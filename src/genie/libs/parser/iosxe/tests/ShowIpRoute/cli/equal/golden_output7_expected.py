expected_output = {
    'vrf': 
        {'red': 
            {'address_family': 
                {'ipv4': 
                    {'routes': 
                        {'192.168.1.0/24': 
                            {'active': True,
                             'next_hop': 
                                {'outgoing_interface': 
                                    {'Vlan1500': 
                                        {
                                            'outgoing_interface': 'Vlan1500'
                                        }
                                    }
                                },
                             'route': '192.168.1.0/24',
                             'source_protocol': 'connected',
                             'source_protocol_codes': 'C'
                            },
                         '192.168.1.1/32': 
                            {'active': True,
                             'next_hop': 
                                {'outgoing_interface': 
                                    {'Vlan1500': 
                                        {
                                            'outgoing_interface': 'Vlan1500'
                                        }
                                    }
                                },
                             'route': '192.168.1.1/32',
                             'source_protocol': 'local',
                             'source_protocol_codes': 'L'},
                         '192.168.1.20/32': 
                            {'active': True,
                             'metric': 0,
                             'next_hop': 
                                {'next_hop_list': 
                                    {1: 
                                        {'index': 1,
                                         'next_hop': '2109:1::2',
                                         'outgoing_interface': 'Vlan500',
                                         'updated': '00:03:46',
                                         'vrf': 'red:ipv6'
                                        }
                                    }
                                },
                             'route': '192.168.1.20/32',
                             'route_preference': 200,
                             'source_protocol': 'bgp',
                             'source_protocol_codes': 'B'
                            },
                         '192.168.1.40/32': 
                            {'active': True,
                             'metric': 0,
                             'next_hop': 
                                {'next_hop_list': 
                                    {1: {'index': 1,
                                         'next_hop': '2109:1::4',
                                         'outgoing_interface': 'Vlan500',
                                         'updated': '00:03:20',
                                         'vrf': 'red:ipv6'
                                        }
                                    }
                                },
                             'route': '192.168.1.40/32',
                             'route_preference': 200,
                             'source_protocol': 'bgp',
                             'source_protocol_codes': 'B'
                            }
                        }
                    }
                }
            }
        }
    }
