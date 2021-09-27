

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        '2001:0:10:204:0:30:0:2/128': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'Bundle-Ether10': {
                                        'outgoing_interface': 'Bundle-Ether10',
                                        'updated': '00:05:36'
                                    }
                                }
                            },
                            'route': '2001:0:10:204:0:30:0:2/128',
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L'
                        },
                        '2001:0:10:204:0:30::/126': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'Bundle-Ether10': {
                                        'outgoing_interface': 'Bundle-Ether10',
                                        'updated': '00:05:36'
                                    }
                                }
                            },
                            'route': '2001:0:10:204:0:30::/126',
                            'source_protocol': 'connected',
                            'source_protocol_codes': 'C'
                        },
                        '2001:0:10:204:0:33::/126': {
                            'active': True,
                            'metric': 20,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::21c:73ff:fed7:2ead',
                                        'outgoing_interface': 'Bundle-Ether10',
                                        'updated': '00:01:58'
                                    },
                                    2: {
                                        'index': 2,
                                        'next_hop': 'fe80::226:88ff:fe55:6f17',
                                        'outgoing_interface': 'TenGigE0/0/0/1',
                                        'updated': '00:01:58'
                                    }
                                }
                            },
                            'route': '2001:0:10:204:0:33::/126',
                            'route_preference': 115,
                            'source_protocol': 'isis',
                            'source_protocol_codes': 'i L2'
                        },
                        '2001:db8:1b7f:8e5c::8/128': {
                            'active': True,
                            'metric': 10,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::226:88ff:fe55:6f17',
                                        'outgoing_interface': 'TenGigE0/0/0/1',
                                        'updated': '00:01:58'
                                    }
                                }
                            },
                            'route': '2001:db8:1b7f:8e5c::8/128',
                            'route_preference': 115,
                            'source_protocol': 'isis',
                            'source_protocol_codes': 'i L2'
                        },
                        '2001:db8:4:4::1/128': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'Loopback60': {
                                        'outgoing_interface': 'Loopback60',
                                        'updated': '00:05:52'
                                    }
                                }
                            },
                            'route': '2001:db8:4:4::1/128',
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L'
                        },
                        '::ffff:127.0.0.0/104': {
                            'active': True,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '::',
                                        'updated': '00:03:29'
                                    }
                                }
                            },
                            'route': '::ffff:127.0.0.0/104',
                            'route_preference': 0,
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L'
                        },
                        'fc00:a0:1:216::1/128': {
                            'active': True,
                            'metric': 20,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::21c:73ff:fed7:2ead',
                                        'outgoing_interface': 'Bundle-Ether10',
                                        'updated': '00:05:23'
                                    }
                                }
                            },
                            'route': 'fc00:a0:1:216::1/128',
                            'route_preference': 115,
                            'source_protocol': 'isis',
                            'source_protocol_codes': 'i L2'
                        },
                        'fc00:a0:1::/64': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'TenGigE0/0/0/0': {
                                        'outgoing_interface': 'TenGigE0/0/0/0',
                                        'updated': '00:05:52'
                                    }
                                }
                            },
                            'route': 'fc00:a0:1::/64',
                            'source_protocol': 'connected',
                            'source_protocol_codes': 'C'
                        },
                        'fc00:a0:1::2/128': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'TenGigE0/0/0/0': {
                                        'outgoing_interface': 'TenGigE0/0/0/0',
                                        'updated': '00:05:52'
                                    }
                                }
                            },
                            'route': 'fc00:a0:1::2/128',
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L'
                        },
                        'fc00:a0:5::/64': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'TenGigE0/0/0/1': {
                                        'outgoing_interface': 'TenGigE0/0/0/1',
                                        'updated': '00:02:10'
                                    }
                                }
                            },
                            'route': 'fc00:a0:5::/64',
                            'source_protocol': 'connected',
                            'source_protocol_codes': 'C'
                        },
                        'fc00:a0:5::2/128': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'TenGigE0/0/0/1': {
                                        'outgoing_interface': 'TenGigE0/0/0/1',
                                        'updated': '00:02:10'
                                    }
                                }
                            },
                            'route': 'fc00:a0:5::2/128',
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L'
                        }
                    }
                }
            },
            'last_resort': {
                'gateway': 'not set'
            },
        },
    }
}
