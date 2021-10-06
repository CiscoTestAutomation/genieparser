

expected_output = {
    'vpn_id': {
        1000: {
            'encap': 'MPLS',
            'esi': '0001.00ff.0102.0000.0011',
            'eth_tag': 0,
            'label': 100001,
            'mp_info': 'Remote all-active, ECMP Disable',
            'mp_resolved': True,
            'pathlists': {
                'ead_es': {
                    'nexthop': {
                        '172.16.2.89': {
                            'label': 0,
                        },
                    },
                },
                'ead_evi': {
                    'nexthop': {
                        '172.16.2.89': {
                            'label': 100001,
                        },
                    },
                },
                'mac': {
                    'nexthop': {
                        '172.16.2.89': {
                            'label': 100001,
                        },
                    },
                },
                'summary': {
                    'nexthop': {
                        '172.16.2.89': {
                            'df_role': '(P)',
                            'label': 100001,
                            'value': '0xffffffff',
                        },
                    },
                },
            },
            'vpn_id': 1000,
        },
    },
}
