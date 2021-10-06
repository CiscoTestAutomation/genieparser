
expected_output = {
    'AWS-DNB-AppSharedServices-PROD': {
        'address_family': {
            'ipv4 unicast': {
                'route_target': {
                    '201627:373': {
                        'route_target': '201627:373',
                        'rt_type': 'both',
                    },
                },
            },
            'ipv6 unicast': {
            },
        },
        'description': 'not set',
        'interfaces': ['Bundle-Ether15.244'],
        'route_distinguisher': '201627:373',
        'vrf_mode': 'regular',
    },
    'Administrasjon': {
        'address_family': {
            'ipv4 unicast': {
                'route_target': {
                    '65100:30': {
                        'route_target': '65100:30',
                        'rt_type': 'both',
                    },
                },
            },
            'ipv6 unicast': {
            },
        },
        'description': 'not set',
        'vrf_mode': 'regular',
    },
    'BT-HCL-DNB': {
        'address_family': {
            'ipv4 unicast': {
                'route_target': {
                    '201627:600': {
                        'route_target': '201627:600',
                        'rt_type': 'both',
                    },
                },
            },
            'ipv6 unicast': {
            },
        },
        'description': 'not set',
        'interfaces': ['Bundle-Ether15.2942'],
        'route_distinguisher': '201627:600',
        'vrf_mode': 'regular',
    },
    'DNB-TATA': {
        'address_family': {
            'ipv4 unicast': {
                'route_target': {
                    '201627:241': {
                        'route_target': '201627:241',
                        'rt_type': 'both',
                    },
                },
            },
            'ipv6 unicast': {
            },
        },
        'description': 'not set',
        'interfaces': ['Bundle-Ether15.514', 'Bundle-Ether15.1285', 'TenGigE0/0/2/1.600'],
        'route_distinguisher': '201627:241',
        'vrf_mode': 'regular',
    },
}
