expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'routes': {
                        '0.0.0.0/0': {
                            'route': '0.0.0.0/0',
                            'ip': '0.0.0.0',
                            'mask': '0',
                            'active': True,
                            'known_via': 'isis RAN',
                            'metric': 101,
                            'distance': 115,
                            'type': 'level-2',
                            'installed': {
                                'date': 'May 20 15:09:21.072',
                                'for': '5w1d'
                            }, 'next_hop':
                                {'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'outgoing_interface': 'Bundle-Ether1',
                                        'from': '10.252.78.130',
                                        'next_hop': '10.252.135.154',
                                        'metric': 101
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
