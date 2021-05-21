expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'instance': {
                        'mpls1': {
                            'router_id': '25.97.1.1',
                            'area': {
                                '0.0.0.0': {
                                    'area_id': 0,
                                    'database': {
                                        'lsa_types': {
                                            1: {
                                                'lsa_type': 1,
                                                'lsas': {
                                                    '0 25.97.1.1': {
                                                        'adv_router': '25.97.1.1',
                                                        'fragment_id': 0,
                                                        'ospfv3': {
                                                            'header': {
                                                                'age': 2019,
                                                                'seq_num': '0x8000007d',
                                                                'bits': 'E',
                                                                'link_count': 2
                                                            }
                                                        }
                                                    },
                                                    '0 95.95.95.95': {
                                                        'adv_router': '95.95.95.95',
                                                        'fragment_id': 0,
                                                        'ospfv3': {
                                                            'header': {
                                                                'age': 607,
                                                                'seq_num': '0x80000097',
                                                                'bits': 'E',
                                                                'link_count': 2
                                                            }
                                                        }
                                                    },
                                                    '0 100.100.100.100': {
                                                        'adv_router': '100.100.100.100',
                                                        'fragment_id': 0,
                                                        'ospfv3': {
                                                            'header': {
                                                                'age': 1595,
                                                                'seq_num': '0x8000007d',
                                                                'bits': 'E',
                                                                'link_count': 2
                                                            }
                                                        }
                                                    }
                                                }
                                            },
                                            8: {
                                                'lsa_type': 8,
                                                'lsas': {
                                                    '7 25.97.1.1': {
                                                        'adv_router': '25.97.1.1',
                                                        'link_id': 7,
                                                        'ospfv3': {
                                                            'header': {
                                                                'age': 1518,
                                                                'seq_num': '0x80000086',
                                                                'interface': 'Gi0/0/0/0'
                                                            }
                                                        }
                                                    },
                                                    '6 100.100.100.100': {
                                                        'adv_router': '100.100.100.100',
                                                        'link_id': 6,
                                                        'ospfv3': {
                                                            'header': {
                                                                'age': 1841,
                                                                'seq_num': '0x80000079',
                                                                'interface': 'Gi0/0/0/0'
                                                            }
                                                        }
                                                    },
                                                    '8 25.97.1.1': {
                                                        'adv_router': '25.97.1.1',
                                                        'link_id': 8,
                                                        'ospfv3': {
                                                            'header': {
                                                                'age': 2019,
                                                                'seq_num': '0x80000078',
                                                                'interface': 'Gi0/0/0/1'
                                                            }
                                                        }
                                                    },
                                                    '5 95.95.95.95': {
                                                        'adv_router': '95.95.95.95',
                                                        'link_id': 5,
                                                        'ospfv3': {
                                                            'header': {
                                                                'age': 1583,
                                                                'seq_num': '0x80000086',
                                                                'interface': 'Gi0/0/0/1'
                                                            }
                                                        }
                                                    }
                                                }
                                            },
                                            9: {
                                                'lsa_type': 9,
                                                'lsas': {
                                                    '0 25.97.1.1': {
                                                        'adv_router': '25.97.1.1',
                                                        'link_id': 0,
                                                        'ospfv3': {
                                                            'header': {
                                                                'age': 2019,
                                                                'seq_num': '0x80000078',
                                                                'ref_lstype': '0x2001',
                                                                'ref_lsid': 0
                                                            }
                                                        }
                                                    },
                                                    '0 95.95.95.95': {
                                                        'adv_router': '95.95.95.95',
                                                        'link_id': 0,
                                                        'ospfv3': {
                                                            'header': {
                                                                'age': 1583,
                                                                'seq_num': '0x80000086',
                                                                'ref_lstype': '0x2001',
                                                                'ref_lsid': 0
                                                            }
                                                        }
                                                    },
                                                    '0 100.100.100.100': {
                                                        'adv_router': '100.100.100.100',
                                                        'link_id': 0,
                                                        'ospfv3': {
                                                            'header': {
                                                                'age': 1595,
                                                                'seq_num': '0x80000079',
                                                                'ref_lstype': '0x2001',
                                                                'ref_lsid': 0
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
            }
        }
    }
}