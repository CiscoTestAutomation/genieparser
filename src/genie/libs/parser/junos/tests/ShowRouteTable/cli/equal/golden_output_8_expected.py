expected_output = {
    'table_name': {
        'NF-TEST.inet6.0': {
            'active_route_count': 3,
            'destination_count': 3,
            'hidden_route_count': 0,
            'holddown_route_count': 0,
            'routes': {
                '2001:10:1:1::/64': {
                    'active_tag': '*',
                    'age': '00:26:06',
                    'next_hop': {
                        'next_hop_list': {
                            1: {
                                'best_route': '>',
                                'via': 'ge-0/0/4.11',
                            },
                        },
                    },
                    'preference': '0',
                    'protocol_name': 'Direct',
                },
                '2001:10:1:1::1/128': {
                    'active_tag': '*',
                    'age': '00:26:06',
                    'next_hop': {
                        'next_hop_list': {
                            1: {
                                'via': 'ge-0/0/4.11',
                            },
                        },
                    },
                    'preference': '0',
                    'protocol_name': 'Local',
                },
                'fe80::250:5600:b8d:fea3/128': {
                    'active_tag': '*',
                    'age': '00:26:06',
                    'next_hop': {
                        'next_hop_list': {
                            1: {
                                'via': 'ge-0/0/4.11',
                            },
                        },
                    },
                    'preference': '0',
                    'protocol_name': 'Local',
                },
            },
            'total_route_count': 3,
        },
    },
}
				