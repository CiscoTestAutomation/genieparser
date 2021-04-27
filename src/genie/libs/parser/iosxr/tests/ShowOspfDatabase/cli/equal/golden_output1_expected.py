expected_output= {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
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
                                                    '25.97.1.1 25.97.1.1': {
                                                        'adv_router': '25.97.1.1',
                                                        'link_id': '25.97.1.1',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 86,
                                                                'seq_num': '0x800080ff',
                                                                'checksum': '0x0043de',
                                                                'link_count': 5
                                                            }
                                                        }
                                                    },
                                                    '95.95.95.95 95.95.95.95': {
                                                        'adv_router': '95.95.95.95',
                                                        'link_id': '95.95.95.95',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 98,
                                                                'seq_num': '0x8000a441',
                                                                'checksum': '0x006677',
                                                                'link_count': 5
                                                            }
                                                        }
                                                    },
                                                    '96.96.96.96 96.96.96.96': {
                                                        'adv_router': '96.96.96.96',
                                                        'link_id': '96.96.96.96',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 1045,
                                                                'seq_num': '0x80008c65',
                                                                'checksum': '0x004f09',
                                                                'link_count': 4
                                                            }
                                                        }
                                                    },
                                                    '100.100.100.100 100.100.100.100': {
                                                        'adv_router': '100.100.100.100',
                                                        'link_id': '100.100.100.100',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 102,
                                                                'seq_num': '0x80001b04',
                                                                'checksum': '0x004061',
                                                                'link_count': 5
                                                            }
                                                        }
                                                    }
                                                }
                                            },
                                            10: {
                                                'lsa_type': 10,
                                                'lsas': {
                                                    '1.0.0.0 25.97.1.1': {
                                                        'adv_router': '25.97.1.1',
                                                        'link_id': '1.0.0.0',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 54,
                                                                'seq_num': '0x8003b136',
                                                                'checksum': '0x009cb2',
                                                                'opaque_id': 0
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.0 95.95.95.95': {
                                                        'adv_router': '95.95.95.95',
                                                        'link_id': '1.0.0.0',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 90,
                                                                'seq_num': '0x8000f3ee',
                                                                'checksum': '0x001a3b',
                                                                'opaque_id': 0
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.0 96.96.96.96': {
                                                        'adv_router': '96.96.96.96',
                                                        'link_id': '1.0.0.0',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 1045,
                                                                'seq_num': '0x80045c8f',
                                                                'checksum': '0x0093ac',
                                                                'opaque_id': 0
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.0 100.100.100.100': {
                                                        'adv_router': '100.100.100.100',
                                                        'link_id': '1.0.0.0',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 541,
                                                                'seq_num': '0x80000079',
                                                                'checksum': '0x006c3a',
                                                                'opaque_id': 0
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.5 95.95.95.95': {
                                                        'adv_router': '95.95.95.95',
                                                        'link_id': '1.0.0.5',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 97,
                                                                'seq_num': '0x800040af',
                                                                'checksum': '0x00019a',
                                                                'opaque_id': 5
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.6 25.97.1.1': {
                                                        'adv_router': '25.97.1.1',
                                                        'link_id': '1.0.0.6',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 3600,
                                                                'seq_num': '0x80055266',
                                                                'checksum': '0x0033a9',
                                                                'opaque_id': 6
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.6 95.95.95.95': {
                                                        'adv_router': '95.95.95.95',
                                                        'link_id': '1.0.0.6',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 98,
                                                                'seq_num': '0x80000001',
                                                                'checksum': '0x000da0',
                                                                'opaque_id': 6
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.6 96.96.96.96': {
                                                        'adv_router': '96.96.96.96',
                                                        'link_id': '1.0.0.6',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 1045,
                                                                'seq_num': '0x80044e2c',
                                                                'checksum': '0x0023f8',
                                                                'opaque_id': 6
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.6 100.100.100.100': {
                                                        'adv_router': '100.100.100.100',
                                                        'link_id': '1.0.0.6',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 26,
                                                                'seq_num': '0x80000079',
                                                                'checksum': '0x000b06',
                                                                'opaque_id': 6
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.7 25.97.1.1': {
                                                        'adv_router': '25.97.1.1',
                                                        'link_id': '1.0.0.7',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 54,
                                                                'seq_num': '0x8003b05e',
                                                                'checksum': '0x006f08',
                                                                'opaque_id': 7
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.7 100.100.100.100': {
                                                        'adv_router': '100.100.100.100',
                                                        'link_id': '1.0.0.7',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 98,
                                                                'seq_num': '0x80000006',
                                                                'checksum': '0x00ced8',
                                                                'opaque_id': 7
                                                            }
                                                        }
                                                    },
                                                    '1.0.0.8 25.97.1.1': {
                                                        'adv_router': '25.97.1.1',
                                                        'link_id': '1.0.0.8',
                                                        'ospf': {
                                                            'header': {
                                                                'age': 79,
                                                                'seq_num': '0x8000f551',
                                                                'checksum': '0x00a29e',
                                                                'opaque_id': 8
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