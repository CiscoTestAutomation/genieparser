

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4 unicast': {
                    'ip': {
                        '10.36.3.3/32': {
                            'ubest_num': '2',
                            'mbest_num': '0',
                            'attach': 'attached',
                            'best_route': {
                                'unicast': {
                                    'nexthop': {
                                        '10.36.3.3': {
                                            'protocol': {
                                                'local': {
                                                    'interface': 'Loopback0',
                                                    'preference': '0',
                                                    'metric': '0',
                                                    'uptime': '1w4d',
                                                },
                                                'direct': {
                                                    'interface': 'Loopback0',
                                                    'preference': '0',
                                                    'metric': '0',
                                                    'uptime': '1w4d',
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
