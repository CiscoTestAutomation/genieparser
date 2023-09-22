expected_output = {
    'group': {
        'SRv6_VPWS': {
            'xc': {
                'SRv6_VPWS_Dual_Homing_AA': {
                    'state': 'up',
                    'interworking': 'none',
                    'ac': {
                        'Bundle-Ether36.1001': {
                            'state': 'up',
                            'type': 'VLAN',
                            'num_ranges': 1,
                            'rewrite_tags': '',
                            'vlan_ranges': ['1001', '1001'],
                            'mtu': 1500,
                            'xc_id': '0xa0000001',
                            'interworking': 'none',
                            'statistics': {
                                'packet_totals': {
                                    'receive': 2358,
                                    'send': 2359
                                },
                                'byte_totals': {
                                    'receive': 273372,
                                    'send': 273772
                                },
                                'drops': {
                                    'illegal_vlan': 0,
                                    'illegal_length': 0
                                }
                            }
                        }
                    },
                    'evpn': {
                        'neighbor': {
                            '::ffff:10.0.0.1': {
                                'id': {
                                    'evi 1001': {
                                        'state': 'up ( established )',
                                        'ac_id': 10001,
                                        'xc_id': '0xc0000001',
                                        'encapsulation': 'SRv6',
                                        'encap_type': 'Ethernet',
                                        'ignore_mtu_mismatch': 'Enabled',
                                        'transmit_mtu_zero': 'Enabled',
                                        'reachability': 'Up',
                                        'srv6': {
                                            'udx2': {
                                                'local': 'fc00:c000:2003:e005::',
                                                'remote': 'fc00:c000:1001:e006::',
                                                'local_type': [],
                                                'remote_type': ['fc00:c000:1002:e006::']
                                            },
                                            'ac_id': {
                                                'local': '10001',
                                                'remote': '10001'
                                            },
                                            'mtu': {
                                                'local': '1514',
                                                'remote': '0'
                                            },
                                            'locator': {
                                                'local': 'MAIN',
                                                'remote': 'N/A'
                                            },
                                            'locator_resolved': {
                                                'local': 'Yes',
                                                'remote': 'N/A'
                                            },
                                            'srv6_headend': {
                                                'local': 'H.Encaps.L2.Red',
                                                'remote': 'N/A'
                                            }
                                        },
                                        'statistics': {
                                            'packet_totals': {
                                                'receive': 2359,
                                                'send': 2358
                                            },
                                            'byte_totals': {
                                                'receive': 273772,
                                                'send': 273372
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
    }
}
