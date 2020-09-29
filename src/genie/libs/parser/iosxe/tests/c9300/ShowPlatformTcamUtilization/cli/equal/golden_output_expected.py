expected_output = {
        'asic': {
            '0': {
                'table': {
                    'CTS Cell Matrix/VPN Label': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'O': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'O': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '1',
                                        'used': '1',
                                        'used_percent': '0.20%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Client Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '4096',
                                        'mpls': '0',
                                        'other': '5',
                                        'used': '5',
                                        'used_percent': '0.12%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Control Plane': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '43',
                                        'used': '263',
                                        'used_percent': '51.37%',
                                        'v4': '114',
                                        'v6': '106',
                                    },
                                },
                            },
                        },
                    },
                    'Flow SPAN ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '4',
                                        'used': '13',
                                        'used_percent': '1.27%',
                                        'v4': '3',
                                        'v6': '6',
                                    },
                                },
                            },
                        },
                    },
                    'IP Route Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '24576',
                                        'mpls': '11',
                                        'other': '0',
                                        'used': '40',
                                        'used_percent': '0.16%',
                                        'v4': '25',
                                        'v6': '4',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '2',
                                        'other': '1',
                                        'used': '76',
                                        'used_percent': '0.93%',
                                        'v4': '29',
                                        'v6': '44',
                                    },
                                },
                            },
                        },
                    },
                    'Input Group LE': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'L2 Multicast': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '11',
                                        'used_percent': '2.15%',
                                        'v4': '3',
                                        'v6': '8',
                                    },
                                },
                            },
                        },
                    },
                    'L3 Multicast': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '67',
                                        'used_percent': '13.09%',
                                        'v4': '3',
                                        'v6': '64',
                                    },
                                },
                            },
                        },
                    },
                    'Lisp Inst Mapping': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '2048',
                                        'mpls': '0',
                                        'other': '1',
                                        'used': '1',
                                        'used_percent': '0.05%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Mac Address Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '32768',
                                        'mpls': '0',
                                        'other': '33',
                                        'used': '33',
                                        'used_percent': '0.10%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '21',
                                        'used': '21',
                                        'used_percent': '2.05%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Macsec SPD': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '2',
                                        'used_percent': '0.78%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Netflow ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '6',
                                        'used_percent': '2.34%',
                                        'v4': '2',
                                        'v6': '2',
                                    },
                                    'O': {
                                        'max': '768',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '6',
                                        'used_percent': '0.78%',
                                        'v4': '2',
                                        'v6': '2',
                                    },
                                },
                            },
                        },
                    },
                    'Output Group LE': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'O': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'PBR ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '22',
                                        'used_percent': '2.15%',
                                        'v4': '16',
                                        'v6': '6',
                                    },
                                },
                            },
                        },
                    },
                    'QOS ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '5120',
                                        'mpls': '0',
                                        'other': '19',
                                        'used': '85',
                                        'used_percent': '1.66%',
                                        'v4': '28',
                                        'v6': '38',
                                    },
                                },
                            },
                        },
                    },
                    'Security ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '5120',
                                        'mpls': '0',
                                        'other': '45',
                                        'used': '129',
                                        'used_percent': '2.52%',
                                        'v4': '26',
                                        'v6': '58',
                                    },
                                },
                            },
                        },
                    },
                    'Security Association': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '4',
                                        'used_percent': '1.56%',
                                        'v4': '2',
                                        'v6': '2',
                                    },
                                },
                            },
                        },
                    },
                    'Tunnel Termination': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '51',
                                        'used_percent': '9.96%',
                                        'v4': '41',
                                        'v6': '10',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '1': {
                'table': {
                    'CTS Cell Matrix/VPN Label': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'O': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'O': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '1',
                                        'used': '1',
                                        'used_percent': '0.20%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Client Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '4096',
                                        'mpls': '0',
                                        'other': '11',
                                        'used': '11',
                                        'used_percent': '0.27%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Control Plane': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '43',
                                        'used': '263',
                                        'used_percent': '51.37%',
                                        'v4': '114',
                                        'v6': '106',
                                    },
                                },
                            },
                        },
                    },
                    'Flow SPAN ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '4',
                                        'used': '13',
                                        'used_percent': '1.27%',
                                        'v4': '3',
                                        'v6': '6',
                                    },
                                },
                            },
                        },
                    },
                    'IP Route Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '24576',
                                        'mpls': '11',
                                        'other': '0',
                                        'used': '40',
                                        'used_percent': '0.16%',
                                        'v4': '25',
                                        'v6': '4',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '2',
                                        'other': '1',
                                        'used': '76',
                                        'used_percent': '0.93%',
                                        'v4': '29',
                                        'v6': '44',
                                    },
                                },
                            },
                        },
                    },
                    'Input Group LE': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'L2 Multicast': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '11',
                                        'used_percent': '2.15%',
                                        'v4': '3',
                                        'v6': '8',
                                    },
                                },
                            },
                        },
                    },
                    'L3 Multicast': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '67',
                                        'used_percent': '13.09%',
                                        'v4': '3',
                                        'v6': '64',
                                    },
                                },
                            },
                        },
                    },
                    'Lisp Inst Mapping': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '2048',
                                        'mpls': '0',
                                        'other': '1',
                                        'used': '1',
                                        'used_percent': '0.05%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Mac Address Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '32768',
                                        'mpls': '0',
                                        'other': '33',
                                        'used': '33',
                                        'used_percent': '0.10%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '21',
                                        'used': '21',
                                        'used_percent': '2.05%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Macsec SPD': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '2',
                                        'used_percent': '0.78%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Netflow ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '7',
                                        'used_percent': '2.73%',
                                        'v4': '3',
                                        'v6': '2',
                                    },
                                    'O': {
                                        'max': '768',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '7',
                                        'used_percent': '0.91%',
                                        'v4': '3',
                                        'v6': '2',
                                    },
                                },
                            },
                        },
                    },
                    'Output Group LE': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'O': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'PBR ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '22',
                                        'used_percent': '2.15%',
                                        'v4': '16',
                                        'v6': '6',
                                    },
                                },
                            },
                        },
                    },
                    'QOS ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '5120',
                                        'mpls': '0',
                                        'other': '18',
                                        'used': '81',
                                        'used_percent': '1.58%',
                                        'v4': '27',
                                        'v6': '36',
                                    },
                                },
                            },
                        },
                    },
                    'Security ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '5120',
                                        'mpls': '0',
                                        'other': '45',
                                        'used': '129',
                                        'used_percent': '2.52%',
                                        'v4': '26',
                                        'v6': '58',
                                    },
                                },
                            },
                        },
                    },
                    'Security Association': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '3',
                                        'used_percent': '1.17%',
                                        'v4': '1',
                                        'v6': '2',
                                    },
                                },
                            },
                        },
                    },
                    'Tunnel Termination': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '51',
                                        'used_percent': '9.96%',
                                        'v4': '41',
                                        'v6': '10',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }