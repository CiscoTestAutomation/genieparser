expected_output = {
    'vrf': {
        'VRF_1': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        '2000:90:11:1::/64': {
                            'route': '2000:90:11:1::/64',
                            'ip': '2000:90:11:1::',
                            'mask': '64',
                            'active': True,
                            'known_via': 'bgp 100',
                            'metric': 0,
                            'distance': 200,
                            'type': 'internal',
                            'installed': {
                                'date': 'Jan 13 11:31:20.102',
                                'for': '07:44:34'
                            },
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'from': '::ffff:50.1.1.8',
                                        'next_hop': '::ffff:50.1.1.1',
                                        'metric': 0
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
