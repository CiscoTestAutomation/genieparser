expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'count_multicast_starg': 2,
                    'count_multicast_sg': 4,
                    'count_multicast_starg_prefix': 0,
                    'count_multicast_total': 6,
                    'group_count': 2,
                    'avg_source_per_group': 2.0,
                    'groups': {
                        '225.0.0.1/32': {
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
                                '100.100.100.5': {
                                    'packets': 1704,
                                    'bytes': 86904,
                                    'aps': 51,
                                    'pps': 0,
                                    'bitrate': 1500000.0,
                                    'bitrate_unit': 'bps',
                                    'oifs': 2
                                },
                                '100.100.100.6': {
                                    'packets': 1700,
                                    'bytes': 86700,
                                    'aps': 51,
                                    'pps': 0,
                                    'bitrate': 500000.0,
                                    'bitrate_unit': 'bps',
                                    'oifs': 1
                                }
                            }
                        },
                        '225.0.0.2/32': {
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
                                '100.100.100.7': {
                                    'packets': 1743,
                                    'bytes': 88893,
                                    'aps': 51,
                                    'pps': 0,
                                    'bitrate': 2000000000.0,
                                    'bitrate_unit': 'bps',
                                    'oifs': 1
                                },
                                '100.100.100.8': {
                                    'packets': 1891,
                                    'bytes': 100806,
                                    'aps': 53,
                                    'pps': 0,
                                    'bitrate': 1000000000000.0,
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
