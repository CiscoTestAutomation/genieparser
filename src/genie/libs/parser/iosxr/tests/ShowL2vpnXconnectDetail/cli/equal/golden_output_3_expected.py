

expected_output = {
    'group': {
        'CLIENT': {
            'xc': {
                'C1': {
                    'state': 'up',
                    'interworking': 'none',
                    'ac': {
                        'GigabitEthernet200/0/0/1.3109': {
                            'state': 'up, active in RG-ID 10',
                            'type': 'VLAN',
                            'num_ranges': 1,
                            'rewrite_tags': '',
                            'vlan_ranges': ['3109', '3109'],
                            'mtu': 1500,
                            'xc_id': '0x120000e',
                            'interworking': 'none',
                            'statistics': {
                                'packet_totals': {
                                    'receive': 3711214,
                                    'send': 3707556
                                },
                                'byte_totals': {
                                    'receive': 566159136,
                                    'send': 793161693
                                },
                                'drops': {
                                    'illegal_vlan': 0,
                                    'illegal_length': 0
                                }
                            }
                        }
                    },
                    'pw': {
                        'neighbor': {
                            '192.168.1.1': {
                                'id': {
                                    1384496: {
                                        'state': 'up ( established )',
                                        'pw_class': 'not set',
                                        'xc_id': '0xa0000003',
                                        'encapsulation': 'MPLS',
                                        'protocol': 'LDP',
                                        'source_address': '192.168.0.47',
                                        'type': 'Ethernet',
                                        'control_word': 'disabled',
                                        'interworking': 'none',
                                        'backup_disable_delay': 0,
                                        'sequencing': 'not set',
                                        'lsp': 'Up',
                                        'status_tlv': 'not set',
                                        'mpls': {
                                            'label': {
                                                'local': '24047',
                                                'remote': '1784'
                                            },
                                            'group_id': {
                                                'local': '0x4002580',
                                                'remote': '0x7'
                                            },
                                            'interface': {
                                                'local': 'GigabitEthernet200/0/0/1.3109',
                                                'remote': 'C1'
                                            },
                                            'mtu': {
                                                'local': '1500',
                                                'remote': '1500'
                                            },
                                            'control_word': {
                                                'local': 'disabled',
                                                'remote': 'disabled'
                                            },
                                            'pw_type': {
                                                'local': 'Ethernet',
                                                'remote': 'Ethernet'
                                            },
                                            'vccv_cv_type': {
                                                'local': '0x2',
                                                'remote': '0x2',
                                                'local_type': ['LSP ping verification'],
                                                'remote_type': ['LSP ping verification']
                                            },
                                            'vccv_cc_type': {
                                                'local': '0x6',
                                                'remote': '0x2',
                                                'local_type': ['router alert label', 'TTL expiry'],
                                                'remote_type': ['router alert label']
                                            }
                                        },
                                        'create_time': '08/12/2020 01:02:44 (2w0d ago)',
                                        'last_time_status_changed': '12/12/2020 14:05:44 (1w3d ago)',
                                        'last_time_pw_went_down': '12/12/2020 14:00:30 (1w3d ago)',
                                        'statistics': {
                                            'packet_totals': {
                                                'receive': 3707556,
                                                'send': 3711214
                                            },
                                            'byte_totals': {
                                                'receive': 793161693,
                                                'send': 566159136
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'C2': {
                    'state': 'up',
                    'interworking': 'none',
                    'ac': {
                        'GigabitEthernet100/0/0/5.3100': {
                            'state': 'up, active in RG-ID 10',
                            'type': 'VLAN',
                            'num_ranges': 1,
                            'rewrite_tags': '',
                            'vlan_ranges': ['3100', '3100'],
                            'mtu': 9198,
                            'xc_id': '0x1200008',
                            'interworking': 'none',
                            'statistics': {
                                'packet_totals': {
                                    'receive': 0,
                                    'send': 225798
                                },
                                'byte_totals': {
                                    'receive': 0,
                                    'send': 13547880
                                },
                                'drops': {
                                    'illegal_vlan': 0,
                                    'illegal_length': 0
                                }
                            }
                        }
                    },
                    'pw': {
                        'neighbor': {
                            '192.168.0.51': {
                                'id': {
                                    1542017: {
                                        'state': 'up ( established )',
                                        'pw_class': 'not set',
                                        'xc_id': '0xa0000005',
                                        'encapsulation': 'MPLS',
                                        'protocol': 'LDP',
                                        'source_address': '192.168.0.47',
                                        'type': 'Ethernet',
                                        'control_word': 'disabled',
                                        'interworking': 'none',
                                        'backup_disable_delay': 0,
                                        'sequencing': 'not set',
                                        'lsp': 'Up',
                                        'status_tlv': 'not set',
                                        'mpls': {
                                            'label': {
                                                'local': '24043',
                                                'remote': '26256'
                                            },
                                            'group_id': {
                                                'local': '0x4001980',
                                                'remote': '0x4002b40'
                                            },
                                            'monitor_interface': {
                                                'local': 'GigabitEthernet100/0/0/5.3100',
                                                'remote': 'GigabitEthernet300/0/0/23.571'
                                            },
                                            'mtu': {
                                                'local': '9198',
                                                'remote': '9198'
                                            },
                                            'control_word': {
                                                'local': 'disabled',
                                                'remote': 'disabled'
                                            },
                                            'pw_type': {
                                                'local': 'Ethernet',
                                                'remote': 'Ethernet'
                                            },
                                            'vccv_cv_type': {
                                                'local': '0x2',
                                                'remote': '0x2',
                                                'local_type': ['LSP ping verification'],
                                                'remote_type': ['LSP ping verification']
                                            },
                                            'vccv_cc_type': {
                                                'local': '0x6',
                                                'remote': '0x6',
                                                'local_type': ['router alert label', 'TTL expiry'],
                                                'remote_type': ['router alert label', 'TTL expiry']
                                            }
                                        },
                                        'create_time': '08/12/2020 01:02:44 (2w0d ago)',
                                        'last_time_status_changed': '11/12/2020 12:45:30 (1w4d ago)',
                                        'last_time_pw_went_down': '11/12/2020 12:44:41 (1w4d ago)',
                                        'statistics': {
                                            'packet_totals': {
                                                'receive': 225798,
                                                'send': 0
                                            },
                                            'byte_totals': {
                                                'receive': 13547880,
                                                'send': 0
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'backup_pw': {
                        'neighbor': {
                            '192.168.0.52': {
                                'id': {
                                    1542017: {
                                        'state': 'standby ( all ready )',
                                        'pw_class': 'not set',
                                        'xc_id': '0xa0000007',
                                        'encapsulation': 'MPLS',
                                        'protocol': 'LDP',
                                        'source_address': '192.168.0.47',
                                        'type': 'Ethernet',
                                        'control_word': 'disabled',
                                        'interworking': 'none',
                                        'sequencing': 'not set',
                                        'lsp': 'Up',
                                        'status_tlv': 'not set',
                                        'mpls': {
                                            'label': {
                                                'local': '24044',
                                                'remote': '25981'
                                            },
                                            'group_id': {
                                                'local': '0x4001980',
                                                'remote': '0x4002b00'
                                            },
                                            'interface': {
                                                'local': 'GigabitEthernet100/0/0/5.3100',
                                                'remote': 'GigabitEthernet300/0/0/23.571'
                                            },
                                            'mtu': {
                                                'local': '9198',
                                                'remote': '9198'
                                            },
                                            'control_word': {
                                                'local': 'disabled',
                                                'remote': 'disabled'
                                            },
                                            'pw_type': {
                                                'local': 'Ethernet',
                                                'remote': 'Ethernet'
                                            },
                                            'vccv_cv_type': {
                                                'local': '0x2',
                                                'remote': '0x2',
                                                'local_type': ['LSP ping verification'],
                                                'remote_type': ['LSP ping verification']
                                            },
                                            'vccv_cc_type': {
                                                'local': '0x6',
                                                'remote': '0x6',
                                                'local_type': ['router alert label', 'TTL expiry'],
                                                'remote_type': ['router alert label', 'TTL expiry']
                                            }
                                        },
                                        'create_time': '08/12/2020 01:02:44 (2w0d ago)',
                                        'last_time_status_changed': '08/12/2020 01:06:55 (2w0d ago)'
                                    }
                                }
                            }
                        }
                    }
                },
                'C3': {
                    'state': 'up',
                    'interworking': 'none',
                    'ac': {
                        'GigabitEthernet100/0/0/6.3100': {
                            'state': 'up, active in RG-ID 10',
                            'type': 'VLAN',
                            'num_ranges': 1,
                            'rewrite_tags': '',
                            'vlan_ranges': ['3100', '3100'],
                            'mtu': 9198,
                            'xc_id': '0x120000a',
                            'interworking': 'none',
                            'statistics': {
                                'packet_totals': {
                                    'receive': 50709266,
                                    'send': 81925195
                                },
                                'byte_totals': {
                                    'receive': 20472200681,
                                    'send': 29487822535
                                },
                                'drops': {
                                    'illegal_vlan': 0,
                                    'illegal_length': 0
                                }
                            }
                        }
                    },
                    'pw': {
                        'neighbor': {
                            '192.168.0.51': {
                                'id': {
                                    1542550: {
                                        'state': 'up ( established )',
                                        'pw_class': 'not set',
                                        'xc_id': '0xa0000009',
                                        'encapsulation': 'MPLS',
                                        'protocol': 'LDP',
                                        'source_address': '192.168.0.47',
                                        'type': 'Ethernet',
                                        'control_word': 'disabled',
                                        'interworking': 'none',
                                        'backup_disable_delay': 0,
                                        'sequencing': 'not set',
                                        'lsp': 'Up',
                                        'status_tlv': 'not set',
                                        'mpls': {
                                            'label': {
                                                'local': '24045',
                                                'remote': '24029'
                                            },
                                            'group_id': {
                                                'local': '0x4001940',
                                                'remote': '0x4000180'
                                            },
                                            'monitor_interface': {
                                                'local': 'GigabitEthernet100/0/0/6.3100',
                                                'remote': 'TenGigE0/0/0/3.214'
                                            },
                                            'mtu': {
                                                'local': '9198',
                                                'remote': '9198'
                                            },
                                            'control_word': {
                                                'local': 'disabled',
                                                'remote': 'disabled'
                                            },
                                            'pw_type': {
                                                'local': 'Ethernet',
                                                'remote': 'Ethernet'
                                            },
                                            'vccv_cv_type': {
                                                'local': '0x2',
                                                'remote': '0x2',
                                                'local_type': ['LSP ping verification'],
                                                'remote_type': ['LSP ping verification']
                                            },
                                            'vccv_cc_type': {
                                                'local': '0x6',
                                                'remote': '0x6',
                                                'local_type': ['router alert label', 'TTL expiry'],
                                                'remote_type': ['router alert label', 'TTL expiry']
                                            }
                                        },
                                        'create_time': '08/12/2020 01:02:44 (2w0d ago)',
                                        'last_time_status_changed': '08/12/2020 01:12:15 (2w0d ago)',
                                        'statistics': {
                                            'packet_totals': {
                                                'receive': 81925195,
                                                'send': 50709266
                                            },
                                            'byte_totals': {
                                                'receive': 29487822535,
                                                'send': 20472200681
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
