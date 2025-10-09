expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'rp': {
                        'bsr': {
                            'bsr': {
                                'address': '2000::2',
                                'expires': '00:00:02',
                                'hash_mask_length': 126,
                                'priority': 254,
                                'rpf_address': 'FE80::CE7F:76FF:FE3D:9A76',
                                'rpf_interface': 'Tw1/0/25',
                                'scope_range_list': 'ff00::/8',
                                'up_time': '00:01:58',
                            },
                            'bsr_candidate': {
                                'address': '2000::2',
                                'hash_mask_length': 126,
                                'priority': 254,
                            },
                        },
                    },
                },
            },
        },
    },
}