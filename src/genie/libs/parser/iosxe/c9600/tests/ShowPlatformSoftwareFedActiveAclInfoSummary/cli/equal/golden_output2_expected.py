expected_output={
    'acl_name': {
        'SG_RESERVED_V4_DROP_ALL': {
            'cg_id': -15,
            'direction_egress': 'Y',
            'direction_ingress': 'N',
            'feature': 'Sgacl',
            'no_of_aces': 1,
            'protocol': 'IPv4',
        },
        'ipv6_ogacl_1': {
            'cg_id': 11,
            'direction_egress': 'N',
            'direction_ingress': 'Y',
            'feature': 'Racl',
            'no_of_aces': 3,
            'protocol': 'IPv6',
        },
    },
}