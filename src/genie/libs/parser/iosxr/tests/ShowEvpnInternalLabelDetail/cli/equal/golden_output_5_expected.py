

expected_output = {
    'vpn_id': {
        1000: {
            'vpn_id': 1000,
            'encap': 'MPLS',
            'esi': '0001.00ff.0102.0000.0011',
            'eth_tag': 0,
            'mp_resolved': True,
            'mp_info': 'Remote all-active, ECMP Disable',
            'pathlists': {
                'ead_evi': {
                    'nexthop': {
                        '10.94.2.88': {
                            'label': 100010,
                        },
                    },
                },
            },
        },
    },
}
