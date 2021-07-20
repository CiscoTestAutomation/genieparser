expected_output = {
    'vrf': {
        'vxlan-1009': {
            'address_family': {
                'ipv4': {
                    'count_multicast_starg': 11,
                    'count_multicast_sg': 18,
                    'count_multicast_total': 29,
                    'count_multicast_starg_prefix': 0,
                    'group_count': 18,
                    'avg_source_per_group': 1.0,
                    'groups': {
                        '225.1.1.17/32': {
                            'source_count': 1,
                            'source': {
                                '(*,G)': {
                                    'packets': 6,
                                    'bytes': 636,
                                    'aps': 106,
                                    'pps': 0,
                                    'bitrate': 0.000,
                                    'bitrate_unit': 'bps',
                                    'oifs': 1,
                                },
                                '1.1.91.67': {
                                    'packets': 145,
                                    'bytes': 7505,
                                    'aps': 51,
                                    'pps': 0,
                                    'bitrate': 27.200,
                                    'bitrate_unit': 'bps',
                                    'oifs': 1,
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
