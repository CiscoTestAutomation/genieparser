

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4 unicast': {
                    'ip': {
                        '10.4.1.1/32': {
                            'ubest_num': '1',
                            'mbest_num': '0',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '10.13.90.1': {
                                            'protocol': {
                                                'eigrp': {
                                                    'interface': 'Ethernet1/2.90',
                                                    'preference': '90',
                                                    'metric': '2848',
                                                    'uptime': '1w5d',
                                                    'protocol_id': 'test',
                                                    'attribute': 'internal',
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'routes': {
                                'nexthop': {
                                    '10.4.1.1': {
                                        'protocol': {
                                            'bgp': {
                                                'preference': '200',
                                                'metric': '0',
                                                'uptime': '1w5d',
                                                'protocol_id': '65000',
                                                'attribute': 'internal',
                                                'tag': '65000',
                                            },
                                        },
                                    },
                                    '10.13.110.1': {
                                        'protocol': {
                                            'ospf': {
                                                'interface': 'Ethernet1/2.110',
                                                'preference': '110',
                                                'metric': '41',
                                                'uptime': '1w5d',
                                                'protocol_id': '1',
                                                'attribute': 'intra',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'bgp_distance_internal_as': 200,
                },
            },
        },
    },
}
