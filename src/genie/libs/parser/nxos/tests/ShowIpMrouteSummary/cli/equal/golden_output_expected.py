expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'count_multicast_starg': 41,
                    'count_multicast_sg': 123,
                    'count_multicast_total': 165,
                    'count_multicast_starg_prefix': 1,
                    'group_count': 41,
                    'avg_source_per_group': 3.0,
                    'groups': {
                        '225.0.0.1/32': {
                            'source_count': 3,
                            'source': {
                                '(*,G)': {
                                    'packets': 0,
                                    'bytes': 0,
                                    'aps': 0,
                                    'pps': 0,
                                    'bitrate': 0.000,
                                    'bitrate_unit': 'bps',
                                    'oifs': 2,
                                },
                                '100.100.100.11': {
                                    'packets': 1879,
                                    'bytes': 101104,
                                    'aps': 53,
                                    'pps': 0,
                                    'bitrate': 27.200,
                                    'bitrate_unit': 'bps',
                                    'oifs': 0,
                                },
                                '100.100.100.5': {
                                    'packets': 1704,
                                    'bytes': 86904,
                                    'aps': 51,
                                    'pps': 0,
                                    'bitrate': 27.200,
                                    'bitrate_unit': 'bps',
                                    'oifs': 2,
                                },
                                '100.100.100.6': {
                                    'packets': 1700,
                                    'bytes': 86700,
                                    'aps': 51,
                                    'pps': 0,
                                    'bitrate': 27.200,
                                    'bitrate_unit': 'bps',
                                    'oifs': 1,
                                }
                            },
                        },
                        '225.0.0.2/32': {
                            'source_count': 3,
                            'source': {
                                '(*,G)': {
                                    'packets': 0,
                                    'bytes': 0,
                                    'aps': 0,
                                    'pps': 0,
                                    'bitrate': 0.000,
                                    'bitrate_unit': 'bps',
                                    'oifs': 2,
                                },
                                '100.100.100.11': {
                                    'packets': 1891,
                                    'bytes': 100806,
                                    'aps': 53,
                                    'pps': 0,
                                    'bitrate': 27.200,
                                    'bitrate_unit': 'bps',
                                    'oifs': 2,
                                },
                                '100.100.100.5': {
                                    'packets': 1743,
                                    'bytes': 88893,
                                    'aps': 51,
                                    'pps': 0,
                                    'bitrate': 27.200,
                                    'bitrate_unit': 'bps',
                                    'oifs': 1,
                                },
                                '100.100.100.6': {
                                    'packets': 1743,
                                    'bytes': 88893,
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
        },
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
