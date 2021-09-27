

expected_output = {
    'evi': {
        1: {
            'ethernet_segment_id': {
                '0055.55ff.aaaa.5555.5555': {
                    'index': {
                        1: {
                            'ether_tag': '0',
                            'label': 'None',
                            'encap': 'MPLS',
                        },
                        2: {
                            'ether_tag': '1',
                            'label': '29348',
                            'encap': 'MPLS',
                            'summary_pathlist': {
                                'index': {
                                    1: {
                                        'tep_id': '0xffffffff',
                                        'df_role': '(P)',
                                        'nexthop': '192.168.0.3',
                                        'label': '29213',
                                    },
                                },
                            },
                        },
                        3: {
                            'ether_tag': '3',
                            'label': '29352',
                            'encap': 'MPLS',
                            'summary_pathlist': {
                                'index': {
                                    2: {
                                        'tep_id': '0xffffffff',
                                        'df_role': '(P)',
                                        'nexthop': '192.168.0.3',
                                        'label': '29224',
                                    },
                                },
                            },
                        },
                    },
                },
                '0088.88ff.1111.8888.8888': {
                    'index': {
                        1: {
                            'ether_tag': '0',
                            'label': 'None',
                            'encap': 'MPLS',
                        },
                        2: {
                            'ether_tag': '1',
                            'label': '29350',
                            'encap': 'MPLS',
                            'summary_pathlist': {
                                'index': {
                                    3: {
                                        'tep_id': '0xffffffff',
                                        'df_role': '(P)',
                                        'nexthop': '192.168.0.4',
                                        'label': '29340',
                                    },
                                },
                            },
                        },
                        3: {
                            'ether_tag': '2',
                            'label': '29349',
                            'encap': 'MPLS',
                            'summary_pathlist': {
                                'index': {
                                    4: {
                                        'tep_id': '0xffffffff',
                                        'df_role': '(P)',
                                        'nexthop': '192.168.0.3',
                                        'label': '29216',
                                    },
                                    5: {
                                        'tep_id': '0x00000000',
                                        'df_role': '(B)',
                                        'nexthop': '192.168.0.4',
                                        'label': '29341',
                                    },
                                },
                            },
                        },
                        4: {
                            'ether_tag': '3',
                            'label': '29355',
                            'encap': 'MPLS',
                            'summary_pathlist': {
                                'index': {
                                    6: {
                                        'tep_id': '0xffffffff',
                                        'df_role': '(P)',
                                        'nexthop': '192.168.0.4',
                                        'label': '29352',
                                    },
                                },
                            },
                        },
                        5: {
                            'ether_tag': '4',
                            'label': '29354',
                            'encap': 'MPLS',
                            'summary_pathlist': {
                                'index': {
                                    7: {
                                        'tep_id': '0xffffffff',
                                        'df_role': '(P)',
                                        'nexthop': '192.168.0.3',
                                        'label': '29226',
                                    },
                                    8: {
                                        'tep_id': '0x00000000',
                                        'df_role': '(B)',
                                        'nexthop': '192.168.0.4',
                                        'label': '29353',
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
