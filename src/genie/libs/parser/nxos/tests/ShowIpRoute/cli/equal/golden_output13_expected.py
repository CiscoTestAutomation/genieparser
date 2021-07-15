expected_output = {
    'vrf': {
        'User-VLAN': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '0.0.0.0/0': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '192.168.1.1',
                                        'next_hop_vrf': 'Internet_VLAN',
                                        'route_preference': 20,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'external',
                                        'updated': '38w2d',                                            
                                    },
                                },
                            },
                            'process_id': '64512',
                            'route': '0.0.0.0/0',
                            'route_preference': 20,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'external',
                            'tag': 65000,
                            'ubest': 1,
                        },
                        '10.0.0.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '169.254.0.1',
                                        'next_hop_vrf': 'Server*VLAN',
                                        'route_preference': 20,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'external',
                                        'updated': '38w2d',                                            
                                    },
                                },
                            },
                            'process_id': '64512',
                            'route': '10.0.0.0/24',
                            'route_preference': 20,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'external',
                            'tag': 65001,
                            'ubest': 1,
                        },
                        '10.0.0.10/32': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '169.254.1.1',
                                        'next_hop_af': '{101}',
                                        'next_hop_vrf': 'LegacyLAN',
                                        'route_preference': 20,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'external',
                                        'updated': '38w2d',                                            
                                    },
                                },
                            },
                            'process_id': '64512',
                            'route': '10.0.0.10/32',
                            'route_preference': 20,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'external',
                            'tag': 65002,
                            'ubest': 1,
                        },
                        '10.2.0.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 0,
                                        'next_hop': '172.16.0.1',
                                        'next_hop_vrf': 'default-VLAN',
                                        'route_preference': 200,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '02:46:06',
                                        'mpls_vpn': True,                                            
                                    },
                                },
                            },
                            'process_id': '64512',
                            'route': '10.2.0.0/24',
                            'route_preference': 200,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'internal',
                            'tag': 64513,
                            'ubest': 1,
                        },
                        '10.1.111.0/24': {
                            'active': True,
                            'mbest': 0,
                            'metric': 2000,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'best_ucast_nexthop': True,
                                        'index': 1,
                                        'metric': 2000,
                                        'next_hop': '10.84.66.66',
                                        'next_hop_vrf': 'default',
                                        'route_preference': 200,
                                        'source_protocol': 'bgp',
                                        'source_protocol_status': 'internal',
                                        'updated': '00:20:43',
                                        'segid': 601011,
                                        'asymmetric': True,
                                        'tunnelid': '0x64646401',
                                        'encap': 'vxlan',
                                    },
                                },
                            },
                            'process_id': '100',
                            'route': '10.1.111.0/24',
                            'route_preference': 200,
                            'source_protocol': 'bgp',
                            'source_protocol_status': 'internal',
                            'tag': 200,
                            'ubest': 1,
                        },                        
                    }
                }
            }
        }
    }
}
