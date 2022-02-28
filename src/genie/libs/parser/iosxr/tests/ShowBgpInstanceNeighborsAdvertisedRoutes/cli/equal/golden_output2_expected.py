expected_output = {
    'instance': {
        'default': {
            'vrf': {
                'default': {
                    'address_family': {
                        'l2vpn evpn RD 192.168.1.11:40000': {
                            'advertised': {
                                '[5][0][24][1.0.0.0]/80': {
                                    'index': {
                                        1: {
                                            'froms': '192.168.1.2',
                                            'next_hop': '192.168.1.11',
                                            'origin_code': '?',
                                        },
                                    },
                                },
                                '[5][0][64][2002:60:60:60::]/176': {
                                    'index': {
                                        1: {
                                            'froms': '192.168.1.2',
                                            'next_hop': '192.168.1.11',
                                            'origin_code': '?',
                                        },
                                    },
                                },
                            },
                            'default_vrf': 'default',
                            'processed_paths': '269',
                            'processed_prefixes': '269',
                            'route_distinguisher': '192.168.1.11:40000',
                        },
                        'l2vpn evpn RD 192.168.1.1:40000': {
                            'advertised': {
                                '[5][0][16][150.0.0.0]/80': {
                                    'index': {
                                        1: {
                                            'froms': '192.168.1.2',
                                            'next_hop': '192.168.1.1',
                                            'origin_code': '?',
                                        },
                                    },
                                },
                            },
                            'default_vrf': 'default',
                            'route_distinguisher': '192.168.1.1:40000',
                        },
                        'l2vpn evpn RD 192.168.1.2:40000': {
                            'advertised': {
                                '[5][0][31][192.0.101.0]/80': {
                                    'index': {
                                        1: {
                                            'froms': '192.168.1.2',
                                            'next_hop': '192.168.2.2',
                                            'origin_code': '?',
                                        },
                                    },
                                },
                            },
                            'default_vrf': 'default',
                            'route_distinguisher': '192.168.1.2:40000',
                        },
                        'vpnv4 unicast RD 192.168.2.2:40000': {
                            'advertised': {
                                '192.0.201.0/31': {
                                    'index': {
                                        1: {
                                            'froms': 'Local',
                                            'next_hop': '192.168.2.2',
                                            'origin_code': '?',
                                        },
                                    },
                                },
                                '3.2.12.0/24': {
                                    'index': {
                                        1: {
                                            'froms': '192.168.2.11',
                                            'next_hop': '192.168.2.11',
                                            'origin_code': '?',
                                        },
                                    },
                                },
                                '3.2.21.0/24': {
                                    'index': {
                                        1: {
                                            'froms': '192.168.2.11',
                                            'next_hop': '192.168.1.13',
                                            'origin_code': '?',
                                        },
                                    },
                                },
                                '3.3.13.0/24': {
                                    'index': {
                                        1: {
                                            'froms': '192.168.2.11',
                                            'next_hop': '192.168.1.13',
                                            'origin_code': '?',
                                        },
                                    },
                                },
                            },
                            'default_vrf': 'default',
                            'processed_paths': '19',
                            'processed_prefixes': '19',
                            'route_distinguisher': '192.168.2.2:40000',
                        },
                        'vpnv6 unicast RD 192.168.2.2:40000': {
                            'advertised': {
                                '192.168.1.1/32': {
                                    'index': {
                                        1: {
                                            'froms': '192.168.1.2',
                                            'next_hop': '192.168.2.2',
                                            'origin_code': 'i',
                                        },
                                    },
                                },
                                '192.168.2.2/32': {
                                    'index': {
                                        1: {
                                            'froms': 'Local',
                                            'next_hop': '192.168.2.2',
                                            'origin_code': 'i',
                                        },
                                    },
                                },
                                '2002:3:2:21::/64': {
                                    'index': {
                                        1: {
                                            'froms': '192.168.2.11',
                                            'next_hop': '192.168.2.11',
                                            'origin_code': '?',
                                        },
                                    },
                                },
                                '2003:192:3:1::13/128': {
                                    'index': {
                                        1: {
                                            'froms': '192.168.2.11',
                                            'next_hop': '192.168.1.13',
                                            'origin_code': '?',
                                        },
                                    },
                                },
                            },
                            'default_vrf': 'default',
                            'processed_paths': '17',
                            'processed_prefixes': '17',
                            'route_distinguisher': '192.168.2.2:40000',
                        },
                    },
                },
            },
        },
    },
}
