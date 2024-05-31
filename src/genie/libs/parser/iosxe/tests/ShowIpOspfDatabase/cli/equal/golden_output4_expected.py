expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        '1': {
                            'areas': {
                                '0.0.0.0': {
                                    'database': {
                                        'lsa_types': {
                                            1: {
                                                'lsa_type': 1,
                                                'lsas': {
                                                    '100.1.1.1': {
                                                        'adv_router': '100.1.1.1',
                                                        'lsa_id': '100.1.1.1',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '100.1.1.1',
                                                                'age': 1573,
                                                                'checksum': '0x00F396',
                                                                'link_count': 4,
                                                                'lsa_id': '100.1.1.1',
                                                                'seq_num': '0x800000D2',
                                                            },
                                                        },
                                                    },
                                                    '100.1.1.2': {
                                                        'adv_router': '100.1.1.2',
                                                        'lsa_id': '100.1.1.2',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '100.1.1.2',
                                                                'age': 1229,
                                                                'checksum': '0x002731',
                                                                'link_count': 4,
                                                                'lsa_id': '100.1.1.2',
                                                                'seq_num': '0x800000D3',
                                                            },
                                                        },
                                                    },
                                                    '100.1.1.3': {
                                                        'adv_router': '100.1.1.3',
                                                        'lsa_id': '100.1.1.3',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '100.1.1.3',
                                                                'age': 937,
                                                                'checksum': '0x00FE3A',
                                                                'link_count': 4,
                                                                'lsa_id': '100.1.1.3',
                                                                'seq_num': '0x800000D2',
                                                            },
                                                        },
                                                    },
                                                    '100.1.1.4': {
                                                        'adv_router': '100.1.1.4',
                                                        'lsa_id': '100.1.1.4',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '100.1.1.4',
                                                                'age': 1148,
                                                                'checksum': '0x001F0A',
                                                                'link_count': 4,
                                                                'lsa_id': '100.1.1.4',
                                                                'seq_num': '0x800000D3',
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            2: {
                                                'lsa_type': 2,
                                                'lsas': {
                                                    '192.168.12.2': {
                                                        'adv_router': '100.1.1.2',
                                                        'lsa_id': '192.168.12.2',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '100.1.1.2',
                                                                'age': 1229,
                                                                'checksum': '0x007A46',
                                                                'lsa_id': '192.168.12.2',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                    '192.168.13.3': {
                                                        'adv_router': '100.1.1.3',
                                                        'lsa_id': '192.168.13.3',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '100.1.1.3',
                                                                'age': 937,
                                                                'checksum': '0x006953',
                                                                'lsa_id': '192.168.13.3',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                    '192.168.14.4': {
                                                        'adv_router': '100.1.1.4',
                                                        'lsa_id': '192.168.14.4',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '100.1.1.4',
                                                                'age': 1148,
                                                                'checksum': '0x005860',
                                                                'lsa_id': '192.168.14.4',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                    '192.168.23.3': {
                                                        'adv_router': '100.1.1.3',
                                                        'lsa_id': '192.168.23.3',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '100.1.1.3',
                                                                'age': 937,
                                                                'checksum': '0x0009A8',
                                                                'lsa_id': '192.168.23.3',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                    '192.168.24.4': {
                                                        'adv_router': '100.1.1.4',
                                                        'lsa_id': '192.168.24.4',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '100.1.1.4',
                                                                'age': 1148,
                                                                'checksum': '0x00F7B5',
                                                                'lsa_id': '192.168.24.4',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                    '192.168.34.4': {
                                                        'adv_router': '100.1.1.4',
                                                        'lsa_id': '192.168.34.4',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '100.1.1.4',
                                                                'age': 1148,
                                                                'checksum': '0x00970B',
                                                                'lsa_id': '192.168.34.4',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        '2': {
                            'areas': {
                                '0.0.0.0': {
                                    'database': {
                                        'lsa_types': {
                                            1: {
                                                'lsa_type': 1,
                                                'lsas': {
                                                    '200.1.1.1': {
                                                        'adv_router': '200.1.1.1',
                                                        'lsa_id': '200.1.1.1',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '200.1.1.1',
                                                                'age': 1025,
                                                                'checksum': '0x009E5E',
                                                                'link_count': 4,
                                                                'lsa_id': '200.1.1.1',
                                                                'seq_num': '0x800000D2',
                                                            },
                                                        },
                                                    },
                                                    '200.1.1.2': {
                                                        'adv_router': '200.1.1.2',
                                                        'lsa_id': '200.1.1.2',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '200.1.1.2',
                                                                'age': 1203,
                                                                'checksum': '0x00D1F8',
                                                                'link_count': 4,
                                                                'lsa_id': '200.1.1.2',
                                                                'seq_num': '0x800000D3',
                                                            },
                                                        },
                                                    },
                                                    '200.1.1.3': {
                                                        'adv_router': '200.1.1.3',
                                                        'lsa_id': '200.1.1.3',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '200.1.1.3',
                                                                'age': 659,
                                                                'checksum': '0x00AB01',
                                                                'link_count': 4,
                                                                'lsa_id': '200.1.1.3',
                                                                'seq_num': '0x800000D1',
                                                            },
                                                        },
                                                    },
                                                    '200.1.1.4': {
                                                        'adv_router': '200.1.1.4',
                                                        'lsa_id': '200.1.1.4',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '200.1.1.4',
                                                                'age': 1112,
                                                                'checksum': '0x00CDCF',
                                                                'link_count': 4,
                                                                'lsa_id': '200.1.1.4',
                                                                'seq_num': '0x800000D1',
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            2: {
                                                'lsa_type': 2,
                                                'lsas': {
                                                    '10.0.12.2': {
                                                        'adv_router': '200.1.1.2',
                                                        'lsa_id': '10.0.12.2',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '200.1.1.2',
                                                                'age': 1203,
                                                                'checksum': '0x0031C1',
                                                                'lsa_id': '10.0.12.2',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                    '10.0.13.3': {
                                                        'adv_router': '200.1.1.3',
                                                        'lsa_id': '10.0.13.3',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '200.1.1.3',
                                                                'age': 659,
                                                                'checksum': '0x0020CE',
                                                                'lsa_id': '10.0.13.3',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                    '10.0.14.4': {
                                                        'adv_router': '200.1.1.4',
                                                        'lsa_id': '10.0.14.4',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '200.1.1.4',
                                                                'age': 1112,
                                                                'checksum': '0x000FDB',
                                                                'lsa_id': '10.0.14.4',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                    '10.0.23.3': {
                                                        'adv_router': '200.1.1.3',
                                                        'lsa_id': '10.0.23.3',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '200.1.1.3',
                                                                'age': 659,
                                                                'checksum': '0x00BF24',
                                                                'lsa_id': '10.0.23.3',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                    '10.0.24.4': {
                                                        'adv_router': '200.1.1.4',
                                                        'lsa_id': '10.0.24.4',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '200.1.1.4',
                                                                'age': 1112,
                                                                'checksum': '0x00AE31',
                                                                'lsa_id': '10.0.24.4',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                    '10.0.34.4': {
                                                        'adv_router': '200.1.1.4',
                                                        'lsa_id': '10.0.34.4',
                                                        'ospfv2': {
                                                            'header': {
                                                                'adv_router': '200.1.1.4',
                                                                'age': 1112,
                                                                'checksum': '0x004E86',
                                                                'lsa_id': '10.0.34.4',
                                                                'seq_num': '0x800000CA',
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
