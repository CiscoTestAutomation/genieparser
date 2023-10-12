expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'prefix': {
                        'fd00::3/128': {
                            'version': 103,
                            'internal': '0x5000001 0x30 (ptr 0xeb4f580) [1], 0x400 (0xda89410), 0x0 (0xf580648)',
                            'updated': 'Mar 29 18:12:57.209',
                            'length': 128,
                            'traffic_index': 0,
                            'precedence': 'n/a',
                            'priority': 3,
                            'gateway_array': {
                                'reference_count': 3,
                                'source_rib': 7,
                                'backups': 0,
                                'flags': {
                                    'flag_count': 4,
                                    'flag_type': 3,
                                    'flag_internal': '0x441 (0xd9a23c8) ext 0x0 (0x0)]'
                                },
                                'LW-LDI': {
                                    'type': 3,
                                    'refc': 1,
                                    'ptr': '0xda89410',
                                    'sh_ldi': '0xd9a23c8'
                                },
                                'update': {
                                    'type_time': 1,
                                    'updated_at': 'Mar 13 12:39:03.184'
                                }
                            },
                            'ldi_update_time': 'Mar 29 18:11:51.158',
                            'LW-LDI-TS': {
                                'datetime': 'Mar 29 18:11:51.158',
                                'via_entries': {
                                    '0': {
                                        'via_address': 'fc00:c000:2003::/128',
                                        'dependencies': 5,
                                        'via_flags': 'recursive',
                                        'path': {
                                            'path_idx': 0,
                                            'nhid': '0x0',
                                            'nhid_hex': '0xeb502b0 0x0',
                                            'path_idx_nh': {
                                                'path_idx_address': 'fc00:c000:2003::/128',
                                                'path_idx_via': 'fc00:c000:2003::/48'
                                            }
                                        },
                                        'next_hop_vrf': 'default',
                                        'next_hop_table': '0xe0800000',
                                        'sid_list': 'fc00:c000:2003:e003::'
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
                                    'refcount': 4,
                                    '0': {
                                        'hash': 0,
                                        'ok': 'Y',
                                        'interface': 'GigabitEthernet0/0/0/2',
                                        'address': 'remote'
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
