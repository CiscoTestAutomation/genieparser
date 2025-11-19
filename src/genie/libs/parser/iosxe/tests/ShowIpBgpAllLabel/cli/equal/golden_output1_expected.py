expected_output = {
    'route_distinguisher': {
        '10:10': {
            'vrf_name': 'vpn2',
            'prefix': {
                '3.3.3.0/24': {
                    'in_label': 'nolabel',
                    'next_hop': '100.0.0.3',
                    'out_label': '21',
                },
                '6.6.6.0/24': {
                    'in_label': '16',
                    'next_hop': '6.6.6.10',
                    'out_label': 'aggregate(vpn2)',
                },
                '33.33.33.11/32': {
                    'in_label': 'nolabel',
                    'next_hop': '100.0.0.3',
                    'out_label': '22',
                },
                '66.66.66.10/32': {
                    'in_label': '17',
                    'next_hop': '6.6.6.10',
                    'out_label': 'nolabel',
                },
                '74.0.0.0': {
                    'in_label': '18',
                    'next_hop': '6.6.6.10',
                    'out_label': 'nolabel',
                },
                '84.0.0.0': {
                    'in_label': 'nolabel',
                    'next_hop': '100.0.0.3',
                    'out_label': '23',
                },
                '100.0.0.10/32': {
                    'in_label': '19',
                    'next_hop': '6.6.6.10',
                    'out_label': 'nolabel',
                },
                '100.0.0.11/32': {
                    'in_label': 'nolabel',
                    'next_hop': '100.0.0.3',
                    'out_label': '24',
                },
            },
        },
        '21:21': {
            'prefix': {
                '0.0.0.0': {
                    'in_label': 'nolabel',
                    'next_hop': '100.0.0.3',
                    'out_label': '20',
                },
                '3.3.3.0/24': {
                    'in_label': 'nolabel',
                    'next_hop': '100.0.0.3',
                    'out_label': '21',
                },
                '33.33.33.11/32': {
                    'in_label': 'nolabel',
                    'next_hop': '100.0.0.3',
                    'out_label': '22',
                },
                '84.0.0.0': {
                    'in_label': 'nolabel',
                    'next_hop': '100.0.0.3',
                    'out_label': '23',
                },
                '100.0.0.11/32': {
                    'in_label': 'nolabel',
                    'next_hop': '100.0.0.3',
                    'out_label': '24',
                },
            },
        },
    },
}
