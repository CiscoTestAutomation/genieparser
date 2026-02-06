expected_output =  {
    'fqdn': {
        '*.atoz.msn.com': {
            'acl_clients': 1,
            'clients': {
                1: {
                    'ace': 4,
                    'acl': 'FQDN_v6ACL_WEBAUTH_REDIRECT',
                    'next_resolved_ace_seq': 40000,
                    'position': 'destination',
                },
            },
            'ip_version': 'IPv6',
        },
        '*.cisco.com': {
            'acl_clients': 1,
            'clients': {
                1: {
                    'ace': 2,
                    'acl': 'FQDN_v6ACL_WEBAUTH_REDIRECT',
                    'next_resolved_ace_seq': 20000,
                    'position': 'destination',
                },
            },
            'ip_version': 'IPv6',
        },
        '*.csc.net': {
            'acl_clients': 1,
            'clients': {
                1: {
                    'ace': 6,
                    'acl': 'FQDN_v6ACL_WEBAUTH_REDIRECT',
                    'next_resolved_ace_seq': 60000,
                    'position': 'destination',
                },
            },
            'ip_version': 'IPv6',
        },
        '*.demo1.msft.com': {
            'acl_clients': 1,
            'clients': {
                1: {
                    'ace': 3,
                    'acl': 'FQDN_v6ACL_WEBAUTH_REDIRECT',
                    'next_resolved_ace_seq': 30000,
                    'position': 'destination',
                },
            },
            'ip_version': 'IPv6',
        },
        'www.ab.*.*.*.test.com': {
            'acl_clients': 1,
            'clients': {
                1: {
                    'ace': 5,
                    'acl': 'FQDN_v6ACL_WEBAUTH_REDIRECT',
                    'next_resolved_ace_seq': 50000,
                    'position': 'destination',
                },
            },
            'ip_version': 'IPv6',
        },
    },
}
