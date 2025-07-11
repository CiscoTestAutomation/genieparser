expected_output = {
    'test2': {
        'statements': {
            '20': {
                'actions': {
                    'recursive': True,
                    'route_disposition': 'permit',
                    'set_metric': -20,
                    'set_next_hop': ['10.36.3.3'],
                    'set_next_hop_self': False,
                    'set_next_hop_v6': ['2001:DB8:3::1'],
                    'set_ospf_metric_type': 'type-1',
                    'set_recursive_next_hop': {
                        'force': True,
                        'ip_version': 'ipv6',
                        'next_hop': '12::0',
                        'vrf': 'Mgmt-vrf',
                    },
                    'set_route_origin': 'igp',
                    'set_verify_availability_next_hops': {
                        '10': {
                            'ip_version': 'ipv6',
                            'next_hop': '10:24::00',
                            'seq_no': 10,
                            'track': 150,
                            'track_state': 'up',
                            'vrf': 'default',
                        },
                        '11': {
                            'ip_version': 'ipv6',
                            'next_hop': '10:23::00',
                            'seq_no': 11,
                            'track': 140,
                            'track_state': 'down',
                            'vrf': 'default',
                        },
                        '12': {
                            'ip_version': 'ipv6',
                            'next_hop': '10:22::00',
                            'seq_no': 12,
                            'track': 130,
                            'track_state': 'undefined',
                            'vrf': 'red',
                        },
                        '17': {
                            'ip_version': 'ip',
                            'next_hop': '12.0.0.0',
                            'seq_no': 17,
                            'track': 150,
                            'track_state': 'down',
                            'vrf': 'default',
                        },
                        '15': {
                            'ip_version': 'ip',
                            'next_hop': '12.0.0.10',
                            'seq_no': 15,
                            'track': 150,
                            'track_state': 'down',
                            'vrf': 'red',
                        },
                    },
                    'verify_availability': True,
                },
                'conditions': {
                    'match_as_path_list': '100',
                    'match_community_list': 'test',
                    'match_ext_community_list': 'test',
                    'match_interface': 'GigabitEthernet1 GigabitEthernet2',
                    'match_level_eq': 'level-1-2',
                    'match_prefix_list': 'test test_2 test&3',
                },
                'policy_routing_matches': {
                    'bytes': 0,
                    'packets': 0,
                },
            },
        },
    },
}