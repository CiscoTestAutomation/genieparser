

expected_output = {
    'instance': {
        'Genie': {
            'level': {
                2: {
                    'lspid': {
                        'core1-genie.00-00': {
                            'lsp': {
                                'seq_num': '0x0000a302',
                                'checksum': '0x1a0e',
                                'local_router': False,
                                'holdtime': 58285,
                                'received': 65534,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                            },
                            'area_address': '49.0000',
                            'nlpid': ['0xcc'],
                            'ip_address': '10.154.219.57',
                            'hostname': 'core1-genie',
                            'router_cap': '10.154.219.57 D:0 S:0',
                            'extended_ipv4_reachability': {
                                '10.154.219.57/32': {
                                    'ip_prefix': '10.154.219.57',
                                    'prefix_length': '32',
                                    'metric': 0,
                                },
                            },
                            'extended_is_neighbor': {
                                'core2-genie.00': {
                                    'metric': 50,
                                },
                                'tcore4-genie.00': {
                                    'metric': 250,
                                },
                                'bl1-genie.00': {
                                    'metric': 1000,
                                },
                                'bl2-genie.00': {
                                    'metric': 1000,
                                },
                            },
                        },
                        'core2-genie.00-00': {
                            'lsp': {
                                'seq_num': '0x0000a15b',
                                'checksum': '0xfcfe',
                                'local_router': False,
                                'holdtime': 60939,
                                'received': 65534,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                            },
                            'area_address': '49.0000',
                            'nlpid': ['0xcc'],
                            'ip_address': '10.154.219.58',
                            'hostname': 'core2-genie',
                            'router_cap': '10.154.219.58 D:0 S:0',
                            'extended_ipv4_reachability': {
                                '10.154.219.58/32': {
                                    'ip_prefix': '10.154.219.58',
                                    'prefix_length': '32',
                                    'metric': 0,
                                },
                            },
                            'extended_is_neighbor': {
                                'core1-genie.00': {
                                    'metric': 50,
                                },
                                'bl2-genie.00': {
                                    'metric': 1000,
                                },
                                'bl1-genie.00': {
                                    'metric': 1000,
                                },
                                'tcore3-genie.00': {
                                    'metric': 250,
                                },
                            },
                        },
                        'dis17-genie_RE1.00-00': {
                            'lsp': {
                                'seq_num': '0x00000215',
                                'checksum': '0xf5f4',
                                'local_router': False,
                                'holdtime': 32551,
                                'received': 65535,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                            },
                            'area_address': '49.0000',
                            'tlv': 14,
                            'tlv_length': 2,
                            'nlpid': ['0xcc', '0x8e'],
                            'router_id': '10.154.219.102',
                            'ip_address': '10.154.219.102',
                            'hostname': 'dis17-genie_RE1',
                            'extended_is_neighbor': {
                                'tcore4-genie.00': {
                                    'metric': 100,
                                },
                                'tcore3-genie.00': {
                                    'metric': 100,
                                },
                            },
                            'extended_ipv4_reachability': {
                                '10.154.219.102/32': {
                                    'ip_prefix': '10.154.219.102',
                                    'prefix_length': '32',
                                    'metric': 0,
                                },
                            },
                            'router_cap': '10.154.219.102 D:0 S:0',
                        },
                    },
                },
            },
        },
    },
}
