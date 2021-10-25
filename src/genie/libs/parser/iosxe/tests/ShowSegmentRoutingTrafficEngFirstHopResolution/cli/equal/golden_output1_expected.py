expected_output = {
    26: {
        'old_route_entry': {
            'primary': {
                'ip': '1.2.3.4',
                'using': 'Et1/2',
                'labels': 'pop (implicit-null)',
            },
            'repair': {
                'ip': '110.1.1.4',
                'using': 'MP6',
                'labels': '20444'
            },
        },
        'route_entry': {
            'primary': {
                'ip': '1.2.3.4',
                'using': 'Et1/2',
                'labels': 'pop (implicit-null)',
            },
            'repair': {
                'ip': '110.1.1.4',
                'using': 'MP6',
                'labels': '20444'
            },
            'weight': 1,
        },
        'status': 'Resolved via fib'
    },
    16106: {
        'status': 'Unresolved via fib'
    },
    16230: {
        'old_route_entry': {
            'primary': {
                'ip': '110.1.1.4',
                'using': 'Et0/1',
                'labels': '16230'
            },
            'repair': {
                'ip': '1.2.3.4',
                'using': 'Et1/2',
                'labels': '16230'

            },
        },
        'route_entry': {
            'primary': {
                'ip': '110.1.1.4',
                'using': 'Et0/1',
                'labels': '16230'
            },
            'repair': {
                'ip': '1.2.3.4',
                'using': 'Et1/2',
                'labels': '16230'
            }
        },
        'status': 'Resolved via igp'
    },
    1640: {
        'old_route_entry': {
            'primary': {
                'ip': '2001:0db8:85a3:0000:0000:8a2e:0370:7334',
                'using': 'Et0/1',
                'labels': '1640'
            },
            'repair': {
                'ip': '::2',
                'using': 'Et1/2',
                'labels': '1640'

            },
        },
        'route_entry': {
            'primary': {
                'ip': '2001:0db8:85a3:0000:0000:8a2e:0370:7334',
                'using': 'Et0/1',
                'labels': '1640'
            },
            'repair': {
                'ip': '::2',
                'using': 'Et1/2',
                'labels': '1640'
            }
        },
        'status': 'Resolved via igp'
    }
}
