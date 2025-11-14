expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'count_multicast_starg': 2,
                    'count_multicast_sg': 4,
                    'count_multicast_starg_prefix': 0,
                    'count_multicast_total': 6,
                    'group_count': 2,
                    'avg_source_per_group': 2.0,
                    'groups': {
                        'ff32::/32': {
                            'source_count': 2,
                            'source': {
                                '(*,G)': {
                                    'packets': 0,
                                    'bytes': 0,
                                    'aps': 0,
                                    'pps': 0,
                                    'bitrate': 0.0,
                                    'bitrate_unit': 'bps',
                                    'oifs': 2
                                },
                                '2001:180:1:57::1181': {
                                    'packets': 968,
                                    'bytes': 49478,
                                    'aps': 51,
                                    'pps': 0,
                                    'bitrate': 1500000.0,
                                    'bitrate_unit': 'bps',
                                    'oifs': 1
                                },
                                '2001:180:1:57::1182': {
                                    'packets': 970,
                                    'bytes': 49580,
                                    'aps': 51,
                                    'pps': 0,
                                    'bitrate': 750000.0,
                                    'bitrate_unit': 'bps',
                                    'oifs': 1
                                }
                            }
                        },
                        'ff33:0:0:1197::1/128': {
                            'source_count': 2,
                            'source': {
                                '(*,G)': {
                                    'packets': 0,
                                    'bytes': 0,
                                    'aps': 0,
                                    'pps': 0,
                                    'bitrate': 0.0,
                                    'bitrate_unit': 'bps',
                                    'oifs': 2
                                },
                                '2001:180:1:57::1183': {
                                    'packets': 1000,
                                    'bytes': 51000,
                                    'aps': 52,
                                    'pps': 0,
                                    'bitrate': 3000000000.0,
                                    'bitrate_unit': 'bps',
                                    'oifs': 1
                                },
                                '2001:180:1:57::1184': {
                                    'packets': 1100,
                                    'bytes': 56100,
                                    'aps': 53,
                                    'pps': 0,
                                    'bitrate': 2000000000000.0,
                                    'bitrate_unit': 'bps',
                                    'oifs': 2
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
