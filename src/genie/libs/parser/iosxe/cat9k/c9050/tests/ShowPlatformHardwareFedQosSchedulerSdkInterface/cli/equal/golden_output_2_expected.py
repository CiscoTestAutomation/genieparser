expected_output = {
    'interface': {
        'TwentyFiveGigE2/1/1': {
            'cstse_scheduler': {
            },
            'interface_id': '0x4DF',
            'interface_scheduler': {
                'oid': {
                    '2630': {
                        'ct_r': {
                            'C-R': {
                                'cir': 11000000512,
                                'eir_pir': 11000000512,
                                'hw_id': 2630,
                                'is_eir': 'PIR',
                                'wfq_weights': 'C(1   ) E(1   )',
                            },
                            'T-R': {
                                'cir': 11000000512,
                                'eir_pir': 11000000512,
                                'hw_id': 2630,
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
                    '2636': {
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
                                'burst': '30',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 100,
                                'link_point': 'OQPG-0',
                                'rate': '1000000000',
                                'type': 'PARENT',
                                'weight': 63,
                            },
                        },
                        'child_group': {
                            0: {
                                'branch': 'Left',
                                'child': {
                                    0: {
                                        'hse_oid': 1260,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 0,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 1260,
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
                                        'hse_oid': 1254,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 4,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 1254,
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
                    '2637': {
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
                                        'hse_oid': 2641,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 0,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 2641,
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
                                        'hse_oid': 2572,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 4,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 2572,
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
                    '2638': {
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
                                        'hse_oid': 2643,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 0,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 2643,
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
                                        'hse_oid': 2642,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 4,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 2642,
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
                    '2639': {
                        'cep_ir': {
                            'CIR': {
                                'burst': '30',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 103,
                                'link_point': 'OQPG-7',
                                'rate': '1000000000',
                                'type': 'PARENT',
                                'weight': 63,
                            },
                            'PIR': {
                                'burst': '30',
                                'hse_oid': 0,
                                'hse_type': 'Sys-P SCH',
                                'hw_id': 103,
                                'link_point': 'OQPG-6',
                                'rate': '1000000000',
                                'type': 'PARENT',
                                'weight': 63,
                            },
                        },
                        'child_group': {
                            0: {
                                'branch': 'Left',
                                'child': {
                                    0: {
                                        'hse_oid': 2645,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 0,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 2645,
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
                                        'hse_oid': 2644,
                                        'hse_type': 'SVCSE',
                                        'link': {
                                            'SP-Link': {
                                                'link_point': 4,
                                            },
                                        },
                                    },
                                    1: {
                                        'hse_oid': 2644,
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
                    '1254': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2636,
                                'hse_type': 'OQHSE',
                                'hw_id': 8554,
                                'link_point': 4,
                                'rate': 2000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2636,
                                'hse_type': 'OQHSE',
                                'hw_id': 8554,
                                'link_point': 6,
                                'rate': 1000000000,
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
                    '1260': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2636,
                                'hse_type': 'OQHSE',
                                'hw_id': 8555,
                                'link_point': 0,
                                'rate': 1000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2636,
                                'hse_type': 'OQHSE',
                                'hw_id': 8555,
                                'link_point': 2,
                                'rate': 2000000000,
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
                    '2572': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2637,
                                'hse_type': 'OQHSE',
                                'hw_id': 8556,
                                'link_point': 4,
                                'rate': 1000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2637,
                                'hse_type': 'OQHSE',
                                'hw_id': 8556,
                                'link_point': 6,
                                'rate': 2000000000,
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
                    '2641': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2637,
                                'hse_type': 'OQHSE',
                                'hw_id': 8557,
                                'link_point': 0,
                                'rate': 1000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2637,
                                'hse_type': 'OQHSE',
                                'hw_id': 8557,
                                'link_point': 2,
                                'rate': 2000000000,
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
                    '2642': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2638,
                                'hse_type': 'OQHSE',
                                'hw_id': 8558,
                                'link_point': 4,
                                'rate': 1000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2638,
                                'hse_type': 'OQHSE',
                                'hw_id': 8558,
                                'link_point': 6,
                                'rate': 2000000000,
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
                    '2643': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2638,
                                'hse_type': 'OQHSE',
                                'hw_id': 8559,
                                'link_point': 0,
                                'rate': 1500000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2638,
                                'hse_type': 'OQHSE',
                                'hw_id': 8559,
                                'link_point': 2,
                                'rate': 2000000000,
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
                    '2644': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2639,
                                'hse_type': 'OQHSE',
                                'hw_id': 8560,
                                'link_point': 4,
                                'rate': 1000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2639,
                                'hse_type': 'OQHSE',
                                'hw_id': 8560,
                                'link_point': 6,
                                'rate': 2000000000,
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
                    '2645': {
                        'cep_ir': {
                            'CIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2639,
                                'hse_type': 'OQHSE',
                                'hw_id': 8561,
                                'link_point': 0,
                                'rate': 1000000000,
                                'type': 'PARENT',
                                'weight': 255,
                            },
                            'PIR': {
                                'burst': 'DEFLT',
                                'hse_oid': 2639,
                                'hse_type': 'OQHSE',
                                'hw_id': 8561,
                                'link_point': 2,
                                'rate': 2000000000,
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
                    '2635': {
                        'c_pb': {
                            'M-B/W': {
                                'act_wfq': 63,
                                'burst': 0,
                                'child_oid': {
                                    '2636': {
                                        'child_type': 'OQHSE',
                                    },
                                    '2637': {
                                        'child_type': 'OQHSE',
                                    },
                                    '2638': {
                                        'child_type': 'OQHSE',
                                    },
                                    '2639': {
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
                'sdk_oid': 141,
                'tc': {
                    'tc0': {
                        'voq_offset': 0,
                    },
                    'tc1': {
                        'voq_offset': 0,
                    },
                    'tc2': {
                        'voq_offset': 0,
                    },
                    'tc3': {
                        'voq_offset': 0,
                    },
                    'tc4': {
                        'voq_offset': 0,
                    },
                    'tc5': {
                        'voq_offset': 0,
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