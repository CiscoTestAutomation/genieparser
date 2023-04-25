expected_output = {
    'vrf': {
        'ce1': {
            'rd': '2:2',
            'address_family': {
                'ipv4': {
                    'route_target': [
                        {
                            'rt': '1:1',
                            'type': 'export'
                        },
                        {
                            'rt': '1:1',
                            'type': 'import'
                        },
                    ]
                },
                'ipv6': {
                    'route_target': [
                        {
                            'rt': '1:1',
                            'type': 'export'
                        },
                        {
                            'rt': '1:1',
                            'type': 'import'
                        },
                    ]
                }
            }
        }
    }
}
