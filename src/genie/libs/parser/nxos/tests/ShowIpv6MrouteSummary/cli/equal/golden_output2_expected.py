expected_output = {
    'vrf': {
        'vxlan-1007': {
            'address_family': {
                'ipv6': {
                    'count_multicast_starg': 9,
                    'count_multicast_sg': 2,
                    'count_multicast_total': 24,
                    'count_multicast_starg_prefix': 13,
                    'group_count': 11,
                    'avg_source_per_group': 0.1,
                    'groups': {
                        'ff33:0:0:1197::1/128': {
                            'source_count': 1,
                            'source': {
                                '2001:180:1:57::1181': {
                                    'packets': 968,
                                    'bytes': 49478,
                                    'aps': 51,
                                    'pps': 0,
                                    'bitrate': 0.000,
                                    'bitrate_unit': 'bps',
                                    'oifs': 1,
                                }
                            }
                        },
                        'ff33:0:0:11d7::1/128': {
                            'source_count': 1,
                            'source': {
                                '2001:1:1:57::1141': {
                                    'packets': 1027,
                                    'bytes': 52377,
                                    'aps': 51,
                                    'pps': 0,
                                    'bitrate': 0.000,
                                    'bitrate_unit': 'bps',
                                    'oifs': 1,
                                },
                            },
                        }
                    }
                }
            }
        }
    }
}
