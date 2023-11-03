expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '101.0.0.2/32': {
                            'route': '101.0.0.2/32',
                            'ip': '101.0.0.2',
                            'mask': '32',
                            'active': True,
                            'known_via': 'bgp 100',
                            'metric': 0,
                            'distance': 200,
                            'type': 'internal',
                            'installed': {
                                'date': 'May 31 13:26:22.013',
                                'for': '3w0d'
                            },
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'from': 'fc00:a000:1000::11',
                                        'next_hop': 'fc00:a000:1000::2',
                                        'nexthop_in_vrf': 'default',
                                        'table': 'default',
                                        'address_family': 'IPv6 Unicast',
                                        'table_id': '0xe0800000',
                                        'metric': 0,
                                        'label': 'None',
                                        'tunnel_id': 'None',
                                        'binding_label': 'None',
                                        'extended_communites_count': 0,
                                        'nhid': '0x0(Ref:0)',
                                        'path_grouping_id': 100,
                                        'srv6_headend': 'H.Encaps.Red [f3216]',
                                        'sid_list': 'fc00:c000:1002:e002::'
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
