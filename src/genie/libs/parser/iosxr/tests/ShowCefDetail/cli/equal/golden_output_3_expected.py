expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'prefix': {
                        '::ffff:10.0.0.1/128': {
                            'version': 32,
                            'internal': '0x1000001 0x0 (ptr 0x78d3fe50) [1], 0x0 (0x0), 0x0 (0x7a0cfaf8)',
                            'updated': 'Jun  2 10:49:26.121',
                            'length': 128,
                            'traffic_index': 0,
                            'precedence': 'n/a',
                            'priority': 0,
                            'gateway_array': {
                                'reference_count': 2,
                                'source_rib': 7,
                                'backups': 0,
                                'flags': {
                                    'flag_count': 1,
                                    'flag_type': 3,
                                    'flag_internal': '0x40441 (0x78c13b78) ext 0x0 (0x0)]'
                                },
                                'LW-LDI': {
                                    'type': 0,
                                    'refc': 0,
                                    'ptr': '0x0',
                                    'sh_ldi': '0x0'
                                },
                                'update': {
                                    'type_time': 1,
                                    'updated_at': 'Jun  2 10:49:26.120'
                                }
                            },
                            'ldi_update_time': 'Jun 15 10:49:52.373',
                            'LW-LDI-TS': {
                                'datetime': 'Jun 15 10:49:52.373',
                                'via_entries': {
                                    '0': {
                                        'via_address': 'fc00:c000:2003::/128',
                                        'dependencies': 9,
                                        'via_flags': 'recursive',
                                        'path': {
                                            'path_idx': 0,
                                            'nhid': '0x0',
                                            'nhid_hex': '0x7914c6bc 0x0',
                                            'path_idx_nh': {
                                                'path_idx_address': 'fc00:c000:2003::/128',
                                                'path_idx_via': 'fc00:c000:2003::/48'
                                            }
                                        },
                                        'next_hop_vrf': 'default',
                                        'next_hop_table': '0xe0800000',
                                        'sid_list': 'fc00:c000:2003:e005::'
                                    }
                                },
                                'level': {
                                    1: {
                                        'level': 1,
                                        'load_distribution': '0',
                                        'load': {
                                            0: {
                                                'load': 0,
                                                'via_address': 'fc00:c000:2003::/128',
                                                'via_flags': 'recursive'
                                            }
                                        }
                                    }
                                },
                                'load_distribution': {
                                    'distribution': '0',
                                    'refcount': 1,
                                    '0': {
                                        'hash': 0,
                                        'ok': 'Y',
                                        'interface': 'Bundle-Ether111',
                                        'address': 'fe80::96ae:f0ff:fe8e:c0da'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
