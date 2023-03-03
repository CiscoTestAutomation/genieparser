

expected_output = {
'vrf': {
    'VRF_Flow1_1': {
        'address_family': {
            'ipv6': {
                'routes': {
                    '100:1:1::1/128': {
                        'active': True,
                        'mbest': 0,
                        'metric': 2219,
                        'next_hop': {
                            'next_hop_list': {
                                1: {
                                    'best_ucast_nexthop': True,
                                    'encap': 'vxlan',
                                    'index': 1,
                                    'metric': 2219,
                                    'next_hop': '::ffff:1.1.1.2',
                                    'next_hop_af': 'ipv4',
                                    'next_hop_vrf': 'default',
                                    'route_preference': 200,
                                    'segid': 501001,
                                    'source_protocol': 'bgp',
                                    'source_protocol_status': 'internal',
                                    'tunnelid': '0x5c5c5c5c',
                                    'updated': '01:46:21'
                                }
                            }
                        },
                        'process_id': '1',
                        'route': '100:1:1::1/128',
                        'route_preference': 200,
                        'source_protocol': 'bgp',
                        'source_protocol_status': 'internal',
                        'tag': 10,
                        'ubest': 1
                    }
                }
            }
        }
    }
}
}