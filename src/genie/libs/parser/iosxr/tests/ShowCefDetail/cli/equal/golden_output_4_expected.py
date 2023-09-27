expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'prefix': {
                        'fc00:a000:1000:101::2/128': {
                            'version': 83,
                            'internal': '0x5000001 0x40 (ptr 0x7914cf2c) [1], 0x0 (0x0), 0x0 (0x7a0cf918)',
                            'updated': 'May 31 13:26:22.019',
                            'length': 128,
                            'traffic_index': 0,
                            'precedence': 'n/a',
                            'priority': 4,
                            'gateway_array': {
                                'reference_count': 1,
                                'source_rib': 7,
                                'backups': 0,
                                'flags': {
                                    'flag_count': 1,
                                    'flag_type': 3,
                                    'flag_internal': '0x48441 (0x78c13a40) ext 0x0 (0x0)]'
                                },
                                'LW-LDI': {
                                    'type': 0,
                                    'refc': 0,
                                    'ptr': '0x0',
                                    'sh_ldi': '0x0'
                                },
                                'update': {
                                    'type_time': 1,
                                    'updated_at': 'May 31 13:26:22.019'
                                }
                            },
                            'ldi_update_time': 'May 31 13:26:22.019',
                            'LW-LDI-TS': {
                                'datetime': 'May 31 13:26:22.019',
                                'via_entries': {
                                    '0': {
                                        'via_address': 'fc00:c000:1002::/128',
                                        'dependencies': 11,
                                        'via_flags': 'recursive',
                                        'path': {
                                            'path_idx': 0,
                                            'nhid': '0x0',
                                            'nhid_hex': '0x7914c1ac 0x0',
                                            'path_idx_nh': {
                                                'path_idx_address': 'fc00:c000:1002::/128',
                                                'path_idx_via': 'fc00:c000:1002::/48'
                                            }
                                        },
                                        'sid_list': 'fc00:c000:1002:e003::'
                                    }
                                },
                                'level': {
                                    1: {
                                        'level': 1,
                                        'load_distribution': '0',
                                        'load': {
                                            0: {
                                                'load': 0,
                                                'via_address': 'fc00:c000:1002::/128',
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
                                        'interface': 'Bundle-Ether12',
                                        'address': 'fe80::bee7:12ff:fe1f:abb5'
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
