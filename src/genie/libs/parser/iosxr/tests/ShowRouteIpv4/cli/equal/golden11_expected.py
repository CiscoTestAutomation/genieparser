expected_output = {
        'vrf': {
            'qattwd': {
                'address_family': {
                    'ipv4': {
                        'routes': {
                            '0.0.0.0/0': {
                                'active': True,
                                'distance': 200,
                                'installed': {
                                    'date': 'Nov 20 07:00:25.367',
                                    'for': '7w5d'
                                },
                                'ip': '0.0.0.0',
                                'known_via': 'bgp '
                                '65001',
                                'mask': '0',
                                'metric': 10,
                                'next_hop': {
                                    'next_hop_list': {
                                        1: {
                                            'from': '172.23.15.196',
                                            'index': 1,
                                            'address_family': 'IPv4 Unicast',
                                            'metric': 10,
                                            'next_hop': '172.23.6.96',
                                            'nexthop_in_vrf': 'default',
                                            'table': 'default',
                                            'table_id': '0xe0000000'
                                        }
                                    }
                                },
                                'route': '0.0.0.0/0',
                                'tag': '10584',
                                'type': 'internal'
                            }
                        }
                    }
                }
            }
        }
    }
