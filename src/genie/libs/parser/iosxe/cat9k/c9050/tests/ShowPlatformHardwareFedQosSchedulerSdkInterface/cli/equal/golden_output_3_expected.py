expected_output = {
    'interface': {
        'FiftyGigE3/1/1': {
            'cstse_scheduler': {
            },
            'interface_id': '0x4DA',
            'interface_scheduler': {
                'oid': {
                    '2647': {
                        'ct_r': {
                            'C-R': {
                                'cir': 11000000512,
                                'eir_pir': 11000000512,
                                'hw_id': 2647,
                                'is_eir': 'PIR',
                                'wfq_weights': 'C(1   ) E(1   )',
                            },
                            'T-R': {
                                'cir': 11000000512,
                                'eir_pir': 11000000512,
                                'hw_id': 2647,
                                'is_eir': 'PIR',
                                'wfq_weights': 'C(1   ) E(1   )',
                            },
                        },
                    },
                },
            },
            'logical_port': 'Disabled',
            'oqhse_scheduler': {
                'oid': {
                    '2653': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 100,
                                'link_point': 'OQPG-1',
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 63,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 100,
                                'link_point': 'OQPG-0',
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 63,
                            },
                        },
                        'child_group': {
                            0: {
                                'branch': 'Left',
                                'child': {
                                    0: {
                                        'hse_oid': 1026,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 0,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 1026,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 2,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'SP': {
                                        'c': 2,
                                        's': 0,
                                    },
                                    'WFQ': {
                                        'c': 2,
                                        's': 2,
                                    },
                                },
                                'weights': [0, 0, 255, 255, 0, 0, 0, 0],
                            },
                            1: {
                                'branch': 'Right',
                                'child': {
                                    0: {
                                        'hse_oid': 1025,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 4,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 1025,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 6,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'SP': {
                                        'c': 2,
                                        's': 4,
                                    },
                                    'WFQ': {
                                        'c': 2,
                                        's': 6,
                                    },
                                },
                                'weights': [0, 0, 255, 255, 0, 0, 0, 0],
                            },
                        },
                        'mode': '2-I',
                    },
                    '2654': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 101,
                                'link_point': 'OQPG-3',
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 63,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 101,
                                'link_point': 'OQPG-2',
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 63,
                            },
                        },
                        'child_group': {
                            0: {
                                'branch': 'Left',
                                'child': {
                                    0: {
                                        'hse_oid': 1321,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 0,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 1321,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 2,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'SP': {
                                        'c': 2,
                                        's': 0,
                                    },
                                    'WFQ': {
                                        'c': 2,
                                        's': 2,
                                    },
                                },
                                'weights': [0, 0, 255, 255, 0, 0, 0, 0],
                            },
                            1: {
                                'branch': 'Right',
                                'child': {
                                    0: {
                                        'hse_oid': 1027,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 4,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 1027,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 6,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'SP': {
                                        'c': 2,
                                        's': 4,
                                    },
                                    'WFQ': {
                                        'c': 2,
                                        's': 6,
                                    },
                                },
                                'weights': [0, 0, 255, 255, 0, 0, 0, 0],
                            },
                        },
                        'mode': '2-I',
                    },
                    '2655': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 102,
                                'link_point': 'OQPG-5',
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 63,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 102,
                                'link_point': 'OQPG-4',
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 63,
                            },
                        },
                        'child_group': {
                            0: {
                                'branch': 'Left',
                                'child': {
                                    0: {
                                        'hse_oid': 1334,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 0,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 1334,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 2,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'SP': {
                                        'c': 2,
                                        's': 0,
                                    },
                                    'WFQ': {
                                        'c': 2,
                                        's': 2,
                                    },
                                },
                                'weights': [0, 0, 255, 255, 0, 0, 0, 0],
                            },
                            1: {
                                'branch': 'Right',
                                'child': {
                                    0: {
                                        'hse_oid': 1333,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 4,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 1333,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 6,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'SP': {
                                        'c': 2,
                                        's': 4,
                                    },
                                    'WFQ': {
                                        'c': 2,
                                        's': 6,
                                    },
                                },
                                'weights': [0, 0, 255, 255, 0, 0, 0, 0],
                            },
                        },
                        'mode': '2-I',
                    },
                    '2656': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 103,
                                'link_point': 'OQPG-7',
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 63,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 103,
                                'link_point': 'OQPG-6',
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 63,
                            },
                        },
                        'child_group': {
                            0: {
                                'branch': 'Left',
                                'child': {
                                    0: {
                                        'hse_oid': 1336,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 0,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 1336,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 2,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'SP': {
                                        'c': 2,
                                        's': 0,
                                    },
                                    'WFQ': {
                                        'c': 2,
                                        's': 2,
                                    },
                                },
                                'weights': [0, 0, 255, 255, 0, 0, 0, 0],
                            },
                            1: {
                                'branch': 'Right',
                                'child': {
                                    0: {
                                        'hse_oid': 1335,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 4,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 1335,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 6,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'SP': {
                                        'c': 2,
                                        's': 4,
                                    },
                                    'WFQ': {
                                        'c': 2,
                                        's': 6,
                                    },
                                },
                                'weights': [0, 0, 255, 255, 0, 0, 0, 0],
                            },
                        },
                        'mode': '2-I',
                    },
                },
            },
            'priority_propagation': 'Disabled',
            'sub_interface_q_mode': 'Disabled - No Priority Propagation',
            'svcse_scheduler': {
                'oid': {
                    '1025': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2653,
                                'hse_type': 'OQHSE',
                                'hw_id': 8554,
                                'link_point': 4,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2653,
                                'hse_type': 'OQHSE',
                                'hw_id': 8554,
                                'link_point': 6,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '720': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 720,
                                },
                            },
                        },
                    },
                    '1026': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2653,
                                'hse_type': 'OQHSE',
                                'hw_id': 8555,
                                'link_point': 0,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2653,
                                'hse_type': 'OQHSE',
                                'hw_id': 8555,
                                'link_point': 2,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '721': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 721,
                                },
                            },
                        },
                    },
                    '1027': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2654,
                                'hse_type': 'OQHSE',
                                'hw_id': 8556,
                                'link_point': 4,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2654,
                                'hse_type': 'OQHSE',
                                'hw_id': 8556,
                                'link_point': 6,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '722': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 722,
                                },
                            },
                        },
                    },
                    '1321': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2654,
                                'hse_type': 'OQHSE',
                                'hw_id': 8557,
                                'link_point': 0,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2654,
                                'hse_type': 'OQHSE',
                                'hw_id': 8557,
                                'link_point': 2,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '723': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 723,
                                },
                            },
                        },
                    },
                    '1333': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2655,
                                'hse_type': 'OQHSE',
                                'hw_id': 8558,
                                'link_point': 4,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2655,
                                'hse_type': 'OQHSE',
                                'hw_id': 8558,
                                'link_point': 6,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '724': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 724,
                                },
                            },
                        },
                    },
                    '1334': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2655,
                                'hse_type': 'OQHSE',
                                'hw_id': 8559,
                                'link_point': 0,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2655,
                                'hse_type': 'OQHSE',
                                'hw_id': 8559,
                                'link_point': 2,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '725': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 725,
                                },
                            },
                        },
                    },
                    '1335': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2656,
                                'hse_type': 'OQHSE',
                                'hw_id': 8560,
                                'link_point': 4,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2656,
                                'hse_type': 'OQHSE',
                                'hw_id': 8560,
                                'link_point': 6,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '726': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 726,
                                },
                            },
                        },
                    },
                    '1336': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2656,
                                'hse_type': 'OQHSE',
                                'hw_id': 8561,
                                'link_point': 0,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2656,
                                'hse_type': 'OQHSE',
                                'hw_id': 8561,
                                'link_point': 2,
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '727': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 727,
                                },
                            },
                        },
                    },
                },
            },
            'system_port_scheduler': {
                'oid': {
                    '2652': {
                        'c_pb': {
                            'M-B/W': {
                                'act_wfq': 63,
                                'burst': 0,
                                'child_oid': {
                                    '2653': {
                                        'child_type': 'OQHSE',
                                    },
                                    '2654': {
                                        'child_type': 'OQHSE',
                                    },
                                    '2655': {
                                        'child_type': 'OQHSE',
                                    },
                                    '2656': {
                                        'child_type': 'OQHSE',
                                    },
                                },
                                'cir': 122070,
                                'eir_wfq': 1,
                                'pg_type': 'OQPG-0',
                                'tx_burst': 0,
                                'tx_cir': 122070,
                            },
                        },
                    },
                },
            },
            'tc_profile': {
                'sdk_oid': 77,
                'tc': {
                    'tc0': {
                        'voq_offset': 0,
                    },
                    'tc1': {
                        'voq_offset': 1,
                    },
                    'tc2': {
                        'voq_offset': 2,
                    },
                    'tc3': {
                        'voq_offset': 3,
                    },
                    'tc4': {
                        'voq_offset': 4,
                    },
                    'tc5': {
                        'voq_offset': 5,
                    },
                    'tc6': {
                        'voq_offset': 6,
                    },
                    'tc7': {
                        'voq_offset': 7,
                    },
                },
            },
        },
    },
}