expected_output = {
    'interface': {
        'TenGigabitEthernet1/0/25': {
            'cstse_scheduler': {
                'oid': {
                    '763': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 760,
                                'hse_type': 'OQHSE',
                                'hw_id': 262,
                                'link_point': '0',
                                'rate': '2000000000',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 760,
                                'hse_type': 'OQHSE',
                                'hw_id': 262,
                                'link_point': '2',
                                'rate': '2000000000',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child_group': {
                            0: {
                                'branch': 'Left',
                                'child': {
                                    0: {
                                        'hse_oid': 772,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 0,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'RR': {
                                        'c': 1,
                                        's': 7,
                                    },
                                    'SP': {
                                        'c': 7,
                                        's': 0,
                                    },
                                },
                            },
                            1: {
                                'branch': 'Right',
                                'child': {
                                    0: {
                                        'hse_oid': 772,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 8,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'SP': {
                                        'c': 7,
                                        's': 8,
                                    },
                                    'WFQ': {
                                        'c': 1,
                                        's': 15,
                                    },
                                },
                                'weights': [0, 0, 0, 0, 0, 0, 0, 255],
                            },
                        },
                        'mode': 'PP-S',
                    },
                    '764': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 760,
                                'hse_type': 'OQHSE',
                                'hw_id': 263,
                                'link_point': '4',
                                'rate': '2000000000',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 760,
                                'hse_type': 'OQHSE',
                                'hw_id': 263,
                                'link_point': '6',
                                'rate': '2000000000',
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child_group': {
                            0: {
                                'branch': 'Left',
                                'child': {
                                    0: {
                                        'hse_oid': 771,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 1,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 770,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 2,
                                            },
                                        },
                                    },
                                    2: {
                                        'hse_oid': 769,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 3,
                                            },
                                        },
                                    },
                                    3: {
                                        'hse_oid': 768,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 4,
                                            },
                                        },
                                    },
                                    4: {
                                        'hse_oid': 767,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 5,
                                            },
                                        },
                                    },
                                    5: {
                                        'hse_oid': 766,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 6,
                                            },
                                        },
                                    },
                                    6: {
                                        'hse_oid': 765,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 7,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'RR': {
                                        'c': 8,
                                        's': 0,
                                    },
                                    'SP': {
                                        'c': 0,
                                        's': 0,
                                    },
                                },
                            },
                            1: {
                                'branch': 'Right',
                                'child': {
                                    0: {
                                        'hse_oid': 771,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 9,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 770,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 10,
                                            },
                                        },
                                    },
                                    2: {
                                        'hse_oid': 769,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 11,
                                            },
                                        },
                                    },
                                    3: {
                                        'hse_oid': 768,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 12,
                                            },
                                        },
                                    },
                                    4: {
                                        'hse_oid': 767,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 13,
                                            },
                                        },
                                    },
                                    5: {
                                        'hse_oid': 766,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 14,
                                            },
                                        },
                                    },
                                    6: {
                                        'hse_oid': 765,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'RR/WFQ-Link': {
                                                'link_point': 15,
                                            },
                                        },
                                    },
                                },
                                'load_balance_type': {
                                    'SP': {
                                        'c': 0,
                                        's': 8,
                                    },
                                    'WFQ': {
                                        'c': 8,
                                        's': 8,
                                    },
                                },
                                'weights': [255, 255, 255, 255, 255, 255, 255, 255],
                            },
                        },
                        'mode': 'PP-S',
                    },
                },
            },
            'interface_id': '0x420',
            'interface_scheduler': {
                'oid': {
                    '755': {
                        'ct_r': {
                            'C-R': {
                                'cir': 11000000512,
                                'eir_pir': 11000000512,
                                'hw_id': 755,
                                'is_eir': 'PIR',
                                'wfq_weights': 'C(1   ) E(1   )',
                            },
                            'T-R': {
                                'cir': 11000000512,
                                'eir_pir': 11000000512,
                                'hw_id': 755,
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
                    '760': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 7,
                                'link_point': 'OQPG-7',
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 7,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 7,
                                'link_point': 'OQPG-7',
                                'rate': 'UNLIMITED',
                                'type': 'PARENT',
                                'weight': 7,
                            },
                        },
                        'child_group': {
                            0: {
                                'branch': 'Left',
                                'child': {
                                    0: {
                                        'hse_oid': 763,
                                        'hse_type': 'CSTSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 0,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 763,
                                        'hse_type': 'CSTSE',
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
                                        'hse_oid': 764,
                                        'hse_type': 'CSTSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 4,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 764,
                                        'hse_type': 'CSTSE',
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
                    '765': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 48,
                                'link_point': 7,
                                'rate': 0,
                                'type': 'PARENT',
                                'weight': 0,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 48,
                                'link_point': 15,
                                'rate': 2000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '320': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 320,
                                },
                            },
                        },
                    },
                    '766': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 49,
                                'link_point': 6,
                                'rate': 0,
                                'type': 'PARENT',
                                'weight': 0,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 49,
                                'link_point': 14,
                                'rate': 2000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '321': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 321,
                                },
                            },
                        },
                    },
                    '767': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 50,
                                'link_point': 5,
                                'rate': 0,
                                'type': 'PARENT',
                                'weight': 0,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 50,
                                'link_point': 13,
                                'rate': 2000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '322': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 322,
                                },
                            },
                        },
                    },
                    '768': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 51,
                                'link_point': 4,
                                'rate': 0,
                                'type': 'PARENT',
                                'weight': 0,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 51,
                                'link_point': 12,
                                'rate': 2000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '323': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 323,
                                },
                            },
                        },
                    },
                    '769': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 52,
                                'link_point': 3,
                                'rate': 0,
                                'type': 'PARENT',
                                'weight': 0,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 52,
                                'link_point': 11,
                                'rate': 2000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '324': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 324,
                                },
                            },
                        },
                    },
                    '770': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 53,
                                'link_point': 2,
                                'rate': 0,
                                'type': 'PARENT',
                                'weight': 0,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 53,
                                'link_point': 10,
                                'rate': 2000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '325': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 325,
                                },
                            },
                        },
                    },
                    '771': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 54,
                                'link_point': 1,
                                'rate': 0,
                                'type': 'PARENT',
                                'weight': 0,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 764,
                                'hse_type': 'CSTSE',
                                'hw_id': 54,
                                'link_point': 9,
                                'rate': 2000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '326': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 326,
                                },
                            },
                        },
                    },
                    '772': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 763,
                                'hse_type': 'CSTSE',
                                'hw_id': 55,
                                'link_point': 0,
                                'rate': 2000000000,
                                'type': 'PARENT',
                                'weight': 0,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 763,
                                'hse_type': 'CSTSE',
                                'hw_id': 55,
                                'link_point': 8,
                                'rate': 0,
                                'type': 'PARENT',
                                'weight': 0,
                            },
                        },
                        'child': {
                            'hse_oid': {
                                '327': {
                                    'hse_type': 'VSC',
                                    'in_device': 0,
                                    'in_slice': 0,
                                    'voq_id': 327,
                                },
                            },
                        },
                    },
                },
            },
            'system_port_scheduler': {
                'oid': {
                    '759': {
                        'c_pb': {
                            'P-CIR': {
                                'act_wfq': 7,
                                'burst': 12,
                                'child_oid': {
                                    '760': {
                                        'child_type': 'OQHSE',
                                    },
                                },
                                'cir': 11000000512,
                                'eir_wfq': 1,
                                'pg_type': 'OQPG-7',
                                'tx_burst': 12,
                                'tx_cir': 11000000512,
                            },
                        },
                    },
                },
            },
            'tc_profile': {
                'sdk_oid': 76,
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