expected_output = {
    'asic': {
        '0': {
            'table': {
                'client_table': {
                    'subtype': {
                        'em': {
                            'dir': {
                                'i': {
                                    'max': 8192,
                                    'mpls': 0,
                                    'other': 0,
                                    'used': 0,
                                    'used_percent': '0.00%',
                                    'v4': 0,
                                    'v6': 0,
                                },
                            },
                        },
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 512,
                                    'mpls': 0,
                                    'other': 0,
                                    'used': 0,
                                    'used_percent': '0.00%',
                                    'v4': 0,
                                    'v6': 0,
                                },
                            },
                        },
                    },
                },
                'control_plane': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 512,
                                    'mpls': 0,
                                    'other': 47,
                                    'used': 283,
                                    'used_percent': '55.27%',
                                    'v4': 130,
                                    'v6': 106,
                                },
                            },
                        },
                    },
                },
                'cts_cell_matrix_vpn_label': {
                    'subtype': {
                        'em': {
                            'dir': {
                                'o': {
                                    'max': 32768,
                                    'mpls': 0,
                                    'other': 0,
                                    'used': 0,
                                    'used_percent': '0.00%',
                                    'v4': 0,
                                    'v6': 0,
                                },
                            },
                        },
                        'tcam': {
                            'dir': {
                                'o': {
                                    'max': 768,
                                    'mpls': 0,
                                    'other': 1,
                                    'used': 1,
                                    'used_percent': '0.13%',
                                    'v4': 0,
                                    'v6': 0,
                                },
                            },
                        },
                    },
                },
                'flow_span_acl': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 512,
                                    'mpls': 0,
                                    'other': 1,
                                    'used': 4,
                                    'used_percent': '0.78%',
                                    'v4': 1,
                                    'v6': 2,
                                },
                                'o': {
                                    'max': 512,
                                    'mpls': 0,
                                    'other': 1,
                                    'used': 4,
                                    'used_percent': '0.78%',
                                    'v4': 1,
                                    'v6': 2,
                                },
                            },
                        },
                    },
                },
                'input_group_le': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 1024,
                                    'mpls': 0,
                                    'other': 0,
                                    'used': 0,
                                    'used_percent': '0.00%',
                                    'v4': 0,
                                    'v6': 0,
                                },
                            },
                        },
                    },
                },
                'ip_route_table': {
                    'subtype': {
                        'em_lpm': {
                            'dir': {
                                'i': {
                                    'max': 212992,
                                    'mpls': 0,
                                    'other': 0,
                                    'used': 17,
                                    'used_percent': '0.01%',
                                    'v4': 17,
                                    'v6': 0,
                                },
                            },
                        },
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 1536,
                                    'mpls': 3,
                                    'other': 0,
                                    'used': 16,
                                    'used_percent': '1.04%',
                                    'v4': 10,
                                    'v6': 3,
                                },
                            },
                        },
                    },
                },
                'l2_multicast': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 2304,
                                    'mpls': 0,
                                    'other': 0,
                                    'used': 7,
                                    'used_percent': '0.30%',
                                    'v4': 3,
                                    'v6': 4,
                                },
                            },
                        },
                    },
                },
                'l3_multicast': {
                    'subtype': {
                        'em': {
                            'dir': {
                                'i': {
                                    'max': 32768,
                                    'mpls': 0,
                                    'other': 0,
                                    'used': 0,
                                    'used_percent': '0.00%',
                                    'v4': 0,
                                    'v6': 0,
                                },
                            },
                        },
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 768,
                                    'mpls': 0,
                                    'other': 0,
                                    'used': 6,
                                    'used_percent': '0.78%',
                                    'v4': 3,
                                    'v6': 3,
                                },
                            },
                        },
                    },
                },
                'lisp_inst_mapping': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 1024,
                                    'mpls': 0,
                                    'other': 1,
                                    'used': 1,
                                    'used_percent': '0.10%',
                                    'v4': 0,
                                    'v6': 0,
                                },
                            },
                        },
                    },
                },
                'mac_address_table': {
                    'subtype': {
                        'em': {
                            'dir': {
                                'i': {
                                    'max': 32768,
                                    'mpls': 0,
                                    'other': 53,
                                    'used': 53,
                                    'used_percent': '0.16%',
                                    'v4': 0,
                                    'v6': 0,
                                },
                            },
                        },
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 768,
                                    'mpls': 0,
                                    'other': 22,
                                    'used': 22,
                                    'used_percent': '2.86%',
                                    'v4': 0,
                                    'v6': 0,
                                },
                            },
                        },
                    },
                },
                'macsec_spd': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 256,
                                    'mpls': 0,
                                    'other': 2,
                                    'used': 2,
                                    'used_percent': '0.78%',
                                    'v4': 0,
                                    'v6': 0,
                                },
                            },
                        },
                    },
                },
                'netflow_acl': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 512,
                                    'mpls': 0,
                                    'other': 2,
                                    'used': 6,
                                    'used_percent': '1.17%',
                                    'v4': 2,
                                    'v6': 2,
                                },
                                'o': {
                                    'max': 512,
                                    'mpls': 0,
                                    'other': 2,
                                    'used': 6,
                                    'used_percent': '1.17%',
                                    'v4': 2,
                                    'v6': 2,
                                },
                            },
                        },
                    },
                },
                'output_group_le': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'o': {
                                    'max': 1024,
                                    'mpls': 0,
                                    'other': 0,
                                    'used': 0,
                                    'used_percent': '0.00%',
                                    'v4': 0,
                                    'v6': 0,
                                },
                            },
                        },
                    },
                },
                'pbr_acl': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 27648,
                                    'mpls': 0,
                                    'other': 0,
                                    'used': 53,
                                    'used_percent': '0.19%',
                                    'v4': 37,
                                    'v6': 16,
                                },
                            },
                        },
                    },
                },
                'qos_acl': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 1024,
                                    'mpls': 0,
                                    'other': 10,
                                    'used': 45,
                                    'used_percent': '4.39%',
                                    'v4': 15,
                                    'v6': 20,
                                },
                                'o': {
                                    'max': 1024,
                                    'mpls': 0,
                                    'other': 9,
                                    'used': 40,
                                    'used_percent': '3.91%',
                                    'v4': 13,
                                    'v6': 18,
                                },
                            },
                        },
                    },
                },
                'security_acl': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 4096,
                                    'mpls': 0,
                                    'other': 40,
                                    'used': 88,
                                    'used_percent': '2.15%',
                                    'v4': 12,
                                    'v6': 36,
                                },
                                'o': {
                                    'max': 4096,
                                    'mpls': 0,
                                    'other': 5,
                                    'used': 43,
                                    'used_percent': '1.05%',
                                    'v4': 14,
                                    'v6': 24,
                                },
                            },
                        },
                    },
                },
                'security_association': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 512,
                                    'mpls': 0,
                                    'other': 0,
                                    'used': 4,
                                    'used_percent': '0.78%',
                                    'v4': 2,
                                    'v6': 2,
                                },
                            },
                        },
                    },
                },
                'tunnel_termination': {
                    'subtype': {
                        'tcam': {
                            'dir': {
                                'i': {
                                    'max': 768,
                                    'mpls': 0,
                                    'other': 1,
                                    'used': 33,
                                    'used_percent': '4.30%',
                                    'v4': 12,
                                    'v6': 20,
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}