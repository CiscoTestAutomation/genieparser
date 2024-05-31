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
                                                    '100.1.1.1 100.1.1.1': {
                                                        'adv_router': '100.1.1.1',
                                                        'lsa_id': '100.1.1.1',
                                                        'ospfv2': {
                                                            'body': {
                                                                'router': {
                                                                    'links': {
                                                                        '1.1.1.1': {
                                                                            'link_data': '255.255.255.255',
                                                                            'link_id': '1.1.1.1',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'stub network',
                                                                        },
                                                                        '192.168.12.2': {
                                                                            'link_data': '192.168.12.1',
                                                                            'link_id': '192.168.12.2',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '192.168.13.3': {
                                                                            'link_data': '192.168.13.1',
                                                                            'link_id': '192.168.13.3',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '192.168.14.4': {
                                                                            'link_data': '192.168.14.1',
                                                                            'link_id': '192.168.14.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                    },
                                                                    'num_of_links': 4,
                                                                },
                                                            },
                                                            'header': {
                                                                'adv_router': '100.1.1.1',
                                                                'age': 618,
                                                                'checksum': '0xF197',
                                                                'length': 72,
                                                                'lsa_id': '100.1.1.1',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '800000D3',
                                                                'type': 1,
                                                            },
                                                        },
                                                    },
                                                    '100.1.1.2 100.1.1.2': {
                                                        'adv_router': '100.1.1.2',
                                                        'lsa_id': '100.1.1.2',
                                                        'ospfv2': {
                                                            'body': {
                                                                'router': {
                                                                    'links': {
                                                                        '192.168.12.2': {
                                                                            'link_data': '192.168.12.2',
                                                                            'link_id': '192.168.12.2',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '192.168.23.3': {
                                                                            'link_data': '192.168.23.2',
                                                                            'link_id': '192.168.23.3',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '192.168.24.4': {
                                                                            'link_data': '192.168.24.2',
                                                                            'link_id': '192.168.24.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '2.2.2.2': {
                                                                            'link_data': '255.255.255.255',
                                                                            'link_id': '2.2.2.2',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'stub network',
                                                                        },
                                                                    },
                                                                    'num_of_links': 4,
                                                                },
                                                            },
                                                            'header': {
                                                                'adv_router': '100.1.1.2',
                                                                'age': 277,
                                                                'checksum': '0x2532',
                                                                'length': 72,
                                                                'lsa_id': '100.1.1.2',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '800000D4',
                                                                'type': 1,
                                                            },
                                                        },
                                                    },
                                                    '100.1.1.3 100.1.1.3': {
                                                        'adv_router': '100.1.1.3',
                                                        'lsa_id': '100.1.1.3',
                                                        'ospfv2': {
                                                            'body': {
                                                                'router': {
                                                                    'links': {
                                                                        '192.168.13.3': {
                                                                            'link_data': '192.168.13.3',
                                                                            'link_id': '192.168.13.3',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '192.168.23.3': {
                                                                            'link_data': '192.168.23.3',
                                                                            'link_id': '192.168.23.3',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '192.168.34.4': {
                                                                            'link_data': '192.168.34.3',
                                                                            'link_id': '192.168.34.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '3.3.3.3': {
                                                                            'link_data': '255.255.255.255',
                                                                            'link_id': '3.3.3.3',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'stub network',
                                                                        },
                                                                    },
                                                                    'num_of_links': 4,
                                                                },
                                                            },
                                                            'header': {
                                                                'adv_router': '100.1.1.3',
                                                                'age': 2017,
                                                                'checksum': '0xFE3A',
                                                                'length': 72,
                                                                'lsa_id': '100.1.1.3',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '800000D2',
                                                                'type': 1,
                                                            },
                                                        },
                                                    },
                                                    '100.1.1.4 100.1.1.4': {
                                                        'adv_router': '100.1.1.4',
                                                        'lsa_id': '100.1.1.4',
                                                        'ospfv2': {
                                                            'body': {
                                                                'router': {
                                                                    'links': {
                                                                        '192.168.14.4': {
                                                                            'link_data': '192.168.14.4',
                                                                            'link_id': '192.168.14.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '192.168.24.4': {
                                                                            'link_data': '192.168.24.4',
                                                                            'link_id': '192.168.24.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '192.168.34.4': {
                                                                            'link_data': '192.168.34.4',
                                                                            'link_id': '192.168.34.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '4.4.4.4': {
                                                                            'link_data': '255.255.255.255',
                                                                            'link_id': '4.4.4.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'stub network',
                                                                        },
                                                                    },
                                                                    'num_of_links': 4,
                                                                },
                                                            },
                                                            'header': {
                                                                'adv_router': '100.1.1.4',
                                                                'age': 224,
                                                                'checksum': '0x1D0B',
                                                                'length': 72,
                                                                'lsa_id': '100.1.1.4',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '800000D4',
                                                                'type': 1,
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
                                                    '200.1.1.1 200.1.1.1': {
                                                        'adv_router': '200.1.1.1',
                                                        'lsa_id': '200.1.1.1',
                                                        'ospfv2': {
                                                            'body': {
                                                                'router': {
                                                                    'links': {
                                                                        '1.1.1.1': {
                                                                            'link_data': '255.255.255.255',
                                                                            'link_id': '1.1.1.1',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'stub network',
                                                                        },
                                                                        '10.0.12.2': {
                                                                            'link_data': '10.0.12.1',
                                                                            'link_id': '10.0.12.2',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '10.0.13.3': {
                                                                            'link_data': '10.0.13.1',
                                                                            'link_id': '10.0.13.3',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '10.0.14.4': {
                                                                            'link_data': '10.0.14.1',
                                                                            'link_id': '10.0.14.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                    },
                                                                    'num_of_links': 4,
                                                                },
                                                            },
                                                            'header': {
                                                                'adv_router': '200.1.1.1',
                                                                'age': 103,
                                                                'area_border_router': True,
                                                                'checksum': '0x9C5F',
                                                                'length': 72,
                                                                'lsa_id': '200.1.1.1',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '800000D3',
                                                                'type': 1,
                                                            },
                                                        },
                                                    },
                                                    '200.1.1.2 200.1.1.2': {
                                                        'adv_router': '200.1.1.2',
                                                        'lsa_id': '200.1.1.2',
                                                        'ospfv2': {
                                                            'body': {
                                                                'router': {
                                                                    'links': {
                                                                        '10.0.12.2': {
                                                                            'link_data': '10.0.12.2',
                                                                            'link_id': '10.0.12.2',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '10.0.23.3': {
                                                                            'link_data': '10.0.23.2',
                                                                            'link_id': '10.0.23.3',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '10.0.24.4': {
                                                                            'link_data': '10.0.24.2',
                                                                            'link_id': '10.0.24.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '2.2.2.2': {
                                                                            'link_data': '255.255.255.255',
                                                                            'link_id': '2.2.2.2',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'stub network',
                                                                        },
                                                                    },
                                                                    'num_of_links': 4,
                                                                },
                                                            },
                                                            'header': {
                                                                'adv_router': '200.1.1.2',
                                                                'age': 237,
                                                                'area_border_router': True,
                                                                'checksum': '0xCFF9',
                                                                'length': 72,
                                                                'lsa_id': '200.1.1.2',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '800000D4',
                                                                'type': 1,
                                                            },
                                                        },
                                                    },
                                                    '200.1.1.3 200.1.1.3': {
                                                        'adv_router': '200.1.1.3',
                                                        'lsa_id': '200.1.1.3',
                                                        'ospfv2': {
                                                            'body': {
                                                                'router': {
                                                                    'links': {
                                                                        '10.0.13.3': {
                                                                            'link_data': '10.0.13.3',
                                                                            'link_id': '10.0.13.3',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '10.0.23.3': {
                                                                            'link_data': '10.0.23.3',
                                                                            'link_id': '10.0.23.3',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '10.0.34.4': {
                                                                            'link_data': '10.0.34.3',
                                                                            'link_id': '10.0.34.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '3.3.3.3': {
                                                                            'link_data': '255.255.255.255',
                                                                            'link_id': '3.3.3.3',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'stub network',
                                                                        },
                                                                    },
                                                                    'num_of_links': 4,
                                                                },
                                                            },
                                                            'header': {
                                                                'adv_router': '200.1.1.3',
                                                                'age': 1738,
                                                                'area_border_router': True,
                                                                'checksum': '0xAB01',
                                                                'length': 72,
                                                                'lsa_id': '200.1.1.3',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '800000D1',
                                                                'type': 1,
                                                            },
                                                        },
                                                    },
                                                    '200.1.1.4 200.1.1.4': {
                                                        'adv_router': '200.1.1.4',
                                                        'lsa_id': '200.1.1.4',
                                                        'ospfv2': {
                                                            'body': {
                                                                'router': {
                                                                    'links': {
                                                                        '10.0.14.4': {
                                                                            'link_data': '10.0.14.4',
                                                                            'link_id': '10.0.14.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '10.0.24.4': {
                                                                            'link_data': '10.0.24.4',
                                                                            'link_id': '10.0.24.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '10.0.34.4': {
                                                                            'link_data': '10.0.34.4',
                                                                            'link_id': '10.0.34.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'transit network',
                                                                        },
                                                                        '4.4.4.4': {
                                                                            'link_data': '255.255.255.255',
                                                                            'link_id': '4.4.4.4',
                                                                            'num_mtid_metrics': 0,
                                                                            'topologies': {
                                                                                0: {
                                                                                    'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0,
                                                                                },
                                                                            },
                                                                            'type': 'stub network',
                                                                        },
                                                                    },
                                                                    'num_of_links': 4,
                                                                },
                                                            },
                                                            'header': {
                                                                'adv_router': '200.1.1.4',
                                                                'age': 144,
                                                                'area_border_router': True,
                                                                'checksum': '0xCBD0',
                                                                'length': 72,
                                                                'lsa_id': '200.1.1.4',
                                                                'option': 'None',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '800000D2',
                                                                'type': 1,
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
