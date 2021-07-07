expected_output = {
    'process_id': {
        '10000': {
            'address_family': 'ipv6',
            'router_id': '10.2.2.21',
            'null_route': {
                '10:2::/96': {
                    'null_metric': '<unreachable>'
                },
            },
            'summary': {
                '10:2:2::/96': {
                    'sum_type': '2',
                    'sum_tag': 111,
                    'sum_metric': 123
                    ,
                },
            },
        },
    },
}

