expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        'fc00:a000:1000:101::2/128': {
                            'route': 'fc00:a000:1000:101::2/128',
                            'ip': 'fc00:a000:1000:101::2',
                            'mask': '128',
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
                                        'metric': 0,
                                        'label': 'None',
                                        'tunnel_id': 'None',
                                        'binding_label': 'None',
                                        'extended_communites_count': 0,
                                        'nhid': '0x0(Ref:0)',
                                        'path_grouping_id': 100,
                                        'srv6_headend': 'H.Encaps.Red [f3216]',
                                        'sid_list': 'fc00:c000:1002:e003::'
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
