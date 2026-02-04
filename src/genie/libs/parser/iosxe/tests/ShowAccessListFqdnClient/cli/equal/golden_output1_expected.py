expected_output = {
    'fqdn': {
        '*.atoz.msn.com': {
            'acl_clients': 3,
            'clients': {
                1: {
                    'ace': 4,
                    'acl': 'Gi1/0/23#v4-redirect#1a6cb697',
                    'next_resolved_ace_seq': 40000,
                    'position': 'destination',
                },
                2: {
                    'ace': 4,
                    'acl': 'Gi2/0/23#v4-redirect#1630a389',
                    'next_resolved_ace_seq': 40000,
                    'position': 'destination',
                },
                3: {
                    'ace': 4,
                    'acl': 'Gi7/0/23#v4-redirect#11d307cf',
                    'next_resolved_ace_seq': 40000,
                    'position': 'destination',
                },
            },
        },
        '*.cisco.com': {
            'acl_clients': 3,
            'clients': {
                1: {
                    'ace': 2,
                    'acl': 'Gi1/0/23#v4-redirect#1a6cb697',
                    'next_resolved_ace_seq': 20000,
                    'position': 'destination',
                },
                2: {
                    'ace': 2,
                    'acl': 'Gi2/0/23#v4-redirect#1630a389',
                    'next_resolved_ace_seq': 20000,
                    'position': 'destination',
                },
                3: {
                    'ace': 2,
                    'acl': 'Gi7/0/23#v4-redirect#11d307cf',
                    'next_resolved_ace_seq': 20000,
                    'position': 'destination',
                },
            },
        },
        '*.csc.net': {
            'acl_clients': 3,
            'clients': {
                1: {
                    'ace': 6,
                    'acl': 'Gi1/0/23#v4-redirect#1a6cb697',
                    'next_resolved_ace_seq': 60000,
                    'position': 'destination',
                },
                2: {
                    'ace': 6,
                    'acl': 'Gi2/0/23#v4-redirect#1630a389',
                    'next_resolved_ace_seq': 60000,
                    'position': 'destination',
                },
                3: {
                    'ace': 6,
                    'acl': 'Gi7/0/23#v4-redirect#11d307cf',
                    'next_resolved_ace_seq': 60000,
                    'position': 'destination',
                },
            },
        },
        '*.demo1.msft.com': {
            'acl_clients': 3,
            'clients': {
                1: {
                    'ace': 3,
                    'acl': 'Gi1/0/23#v4-redirect#1a6cb697',
                    'next_resolved_ace_seq': 30000,
                    'position': 'destination',
                },
                2: {
                    'ace': 3,
                    'acl': 'Gi2/0/23#v4-redirect#1630a389',
                    'next_resolved_ace_seq': 30000,
                    'position': 'destination',
                },
                3: {
                    'ace': 3,
                    'acl': 'Gi7/0/23#v4-redirect#11d307cf',
                    'next_resolved_ace_seq': 30000,
                    'position': 'destination',
                },
            },
        },
        'www.ab.*.*.*.test.com': {
            'acl_clients': 3,
            'clients': {
                1: {
                    'ace': 5,
                    'acl': 'Gi1/0/23#v4-redirect#1a6cb697',
                    'next_resolved_ace_seq': 50000,
                    'position': 'destination',
                },
                2: {
                    'ace': 5,
                    'acl': 'Gi2/0/23#v4-redirect#1630a389',
                    'next_resolved_ace_seq': 50000,
                    'position': 'destination',
                },
                3: {
                    'ace': 5,
                    'acl': 'Gi7/0/23#v4-redirect#11d307cf',
                    'next_resolved_ace_seq': 50000,
                    'position': 'destination',
                },
            },
        },
        'www.msft10.com': {
            'acl_clients': 3,
            'clients': {
                1: {
                    'ace': 7,
                    'acl': 'Gi1/0/23#v4-redirect#1a6cb697',
                    'next_resolved_ace_seq': 70000,
                    'position': 'destination',
                },
                2: {
                    'ace': 7,
                    'acl': 'Gi2/0/23#v4-redirect#1630a389',
                    'next_resolved_ace_seq': 70000,
                    'position': 'destination',
                },
                3: {
                    'ace': 7,
                    'acl': 'Gi7/0/23#v4-redirect#11d307cf',
                    'next_resolved_ace_seq': 70000,
                    'position': 'destination',
                },
            },
        },
        'www.msft11.com': {
            'acl_clients': 3,
            'clients': {
                1: {
                    'ace': 8,
                    'acl': 'Gi1/0/23#v4-redirect#1a6cb697',
                    'next_resolved_ace_seq': 80000,
                    'position': 'destination',
                },
                2: {
                    'ace': 8,
                    'acl': 'Gi2/0/23#v4-redirect#1630a389',
                    'next_resolved_ace_seq': 80000,
                    'position': 'destination',
                },
                3: {
                    'ace': 8,
                    'acl': 'Gi7/0/23#v4-redirect#11d307cf',
                    'next_resolved_ace_seq': 80000,
                    'position': 'destination',
                },
            },
        },
        'www.msft12.com': {
            'acl_clients': 3,
            'clients': {
                1: {
                    'ace': 9,
                    'acl': 'Gi1/0/23#v4-redirect#1a6cb697',
                    'next_resolved_ace_seq': 90000,
                    'position': 'destination',
                },
                2: {
                    'ace': 9,
                    'acl': 'Gi2/0/23#v4-redirect#1630a389',
                    'next_resolved_ace_seq': 90000,
                    'position': 'destination',
                },
                3: {
                    'ace': 9,
                    'acl': 'Gi7/0/23#v4-redirect#11d307cf',
                    'next_resolved_ace_seq': 90000,
                    'position': 'destination',
                },
            },
        },
        'www.msft13.com': {
            'acl_clients': 3,
            'clients': {
                1: {
                    'ace': 10,
                    'acl': 'Gi1/0/23#v4-redirect#1a6cb697',
                    'next_resolved_ace_seq': 100000,
                    'position': 'destination',
                },
                2: {
                    'ace': 10,
                    'acl': 'Gi2/0/23#v4-redirect#1630a389',
                    'next_resolved_ace_seq': 100000,
                    'position': 'destination',
                },
                3: {
                    'ace': 10,
                    'acl': 'Gi7/0/23#v4-redirect#11d307cf',
                    'next_resolved_ace_seq': 100000,
                    'position': 'destination',
                },
            },
        },
    },
}
