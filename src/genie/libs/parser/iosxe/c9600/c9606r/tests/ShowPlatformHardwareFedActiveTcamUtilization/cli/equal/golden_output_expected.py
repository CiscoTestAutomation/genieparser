expected_output = {
    'asic': {
        '0': {
            'table': {
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
                                    'v6': 0
                                 }
                            }
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
                                    'v6': 0
                                }
                            }
                        }
                    }
               },
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
                                   'v6': 0
                               }
                           }
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
                                'v6': 0
                            }
                        }
                    }
               }
            },
            'control_plane': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1024,
                                'mpls': 0,
                                'other': 45,
                                'used': 281,
                                'used_percent': '27.44%',
                                'v4': 130,
                                'v6': 106
                            }
                        }
                    }
                }
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
                                'v6': 2
                            },
                           'o': {'max': 512,
                                 'mpls': 0,
                                 'other': 1,
                                 'used': 4,
                                 'used_percent': '0.78%',
                                 'v4': 1,
                                 'v6': 2
                           }
                        }
                    }
                }
            },
            'ip_route_table': {
                'subtype': {
                    'em_lpm': {
                        'dir': {
                            'i': {
                                'max': 212992,
                                'mpls': 1,
                                'other': 0,
                                'used': 14,
                                'used_percent': '0.01%',
                                'v4': 13,
                                'v6': 0
                            }
                        }
                    },
                   'tcam': {
                       'dir': {
                           'i': {
                               'max': 1536,
                               'mpls': 2,
                               'other': 0,
                               'used': 11,
                               'used_percent': '0.72%',
                               'v4': 6,
                               'v6': 3
                           }
                       }
                   }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
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
                                'v6': 4
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
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
                               'v6': 3
                           }
                       }
                   }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'mac_address_table': {
                'subtype': {
                    'em': {
                        'dir': {
                            'i': { 
                                'max': 32768,
                                'mpls': 0,
                                'other': 128,
                                'used': 128,
                                'used_percent': '0.39%',
                                'v4': 0,
                                'v6': 0
                            }
                        }
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
                                'v6': 0
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'netflow_acl': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1024,
                                'mpls': 0,
                                'other': 2,
                                'used': 6,
                                'used_percent': '0.59%',
                                'v4': 2,
                                'v6': 2
                            },
                           'o': {
                               'max': 1024,
                               'mpls': 0,
                               'other': 2,
                               'used': 7,
                               'used_percent': '0.68%',
                               'v4': 3,
                               'v6': 2
                           }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'pbr_acl': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 15872,
                                'mpls': 0,
                                'other': 0,
                                'used': 32,
                                'used_percent': '0.20%',
                                'v4': 26,
                                'v6': 6
                            }
                        }
                    }
                }
            },
            'qos_acl_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 2560,
                                'mpls': 0,
                                'other': 0,
                                'used': 15,
                                'used_percent': '0.59%',
                                'v4': 15,
                                'v6': 0
                            },
                            'o': {
                                'max': 3072,
                                'mpls': 0,
                                'other': 0,
                                'used': 13,
                                'used_percent': '0.42%',
                                'v4': 13,
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'qos_acl_non_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1536,
                                'mpls': 0,
                                'other': 10,
                                'used': 30,
                                'used_percent': '1.95%',
                                'v4': 0,
                                'v6': 20
                            },
                            'o': {'max': 1024,
                                  'mpls': 0,
                                  'other': 9,
                                  'used': 27,
                                  'used_percent': '2.64%',
                                  'v4': 0,
                                  'v6': 18
                            }
                        }
                    }
                }
            },
            'security_acl_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 7168,
                                'mpls': 0,
                                'other': 0,
                                'used': 12,
                                'used_percent': '0.17%',
                                'v4': 12,
                                'v6': 0
                            },
                           'o': {'max': 3072,
                                 'mpls': 0,
                                 'other': 0,
                                 'used': 14,
                                 'used_percent': '0.46%',
                                 'v4': 14,
                                 'v6': 0
                           }
                        }
                    }
                }
            },
            'security_acl_non_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 5120,
                                'mpls': 0,
                                'other': 40,
                                'used': 76,
                                'used_percent': '1.48%',
                                'v4': 0,
                                'v6': 36
                            },
                            'o': {
                                'max': 5120,
                                'mpls': 0,
                                'other': 5,
                                'used': 29,
                                'used_percent': '0.57%',
                                'v4': 0,
                                'v6': 24
                            }
                        }
                    }
                }
            },
            'tunnel_termination': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1792,
                                'mpls': 0,
                                'other': 0,
                                'used': 29,
                                'used_percent': '1.62%',
                                'v4': 11,
                                'v6': 18
                            }
                        }
                    }
                }
            }
        }
    },
    '1': {
        'table': {
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
                                'v6': 0
                            }
                        }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
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
                                'v6': 0
                            }
                        }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'control_plane': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1024,
                                'mpls': 0,
                                'other': 45,
                                'used': 281,
                                'used_percent': '27.44%',
                                'v4': 130,
                                'v6': 106
                            }
                        }
                    }
                }
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
                                'v6': 2
                            },
                            'o': {
                                'max': 512,
                                'mpls': 0,
                                'other': 1,
                                'used': 4,
                                'used_percent': '0.78%',
                                'v4': 1,
                                'v6': 2
                            }
                        }
                    }
                }
            },
            'ip_route_table': {
                'subtype': {
                    'em_lpm': {
                        'dir': {
                            'i': {
                                'max': 212992,
                                'mpls': 1,
                                'other': 0,
                                'used': 14,
                                'used_percent': '0.01%',
                                'v4': 13,
                                'v6': 0
                            }
                        }
                    },
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1536,
                                'mpls': 2,
                                'other': 0,
                                'used': 11,
                                'used_percent': '0.72%',
                                'v4': 6,
                                'v6': 3
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
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
                                'v6': 4
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
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
                                'v6': 3
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'mac_address_table': {
                'subtype': {
                    'em': {
                        'dir': {
                            'i': {
                                'max': 32768,
                                'mpls': 0,
                                'other': 128,
                                'used': 128,
                                'used_percent': '0.39%',
                                'v4': 0,
                                'v6': 0
                            }
                        }
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
                                'v6': 0
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'netflow_acl': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1024,
                                'mpls': 0,
                                'other': 2,
                                'used': 6,
                                'used_percent': '0.59%',
                                'v4': 2,
                                'v6': 2
                            },
                            'o': {
                                'max': 1024,
                                'mpls': 0,
                                'other': 2,
                                'used': 7,
                                'used_percent': '0.68%',
                                'v4': 3,
                                'v6': 2
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'pbr_acl': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 15872,
                                'mpls': 0,
                                'other': 0,
                                'used': 32,
                                'used_percent': '0.20%',
                                'v4': 26,
                                'v6': 6
                            }
                        }
                    }
                }
            },
            'qos_acl_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 2560,
                                'mpls': 0,
                                'other': 0,
                                'used': 15,
                                'used_percent': '0.59%',
                                'v4': 15,
                                'v6': 0
                            },
                            'o': {'max': 3072,
                                  'mpls': 0,
                                  'other': 0,
                                  'used': 12,
                                  'used_percent': '0.39%',
                                  'v4': 12,
                                  'v6': 0
                            }
                        }
                    }
                }
            },
            'qos_acl_non_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1536,
                                'mpls': 0,
                                'other': 10,
                                'used': 30,
                                'used_percent': '1.95%',
                                'v4': 0,
                                'v6': 20
                             },
                            'o': {
                                'max': 1024,
                                'mpls': 0,
                                'other': 8,
                                'used': 24,
                                'used_percent': '2.34%',
                                'v4': 0,
                                'v6': 16
                            }
                        }
                    }
                }
            },
            'security_acl_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 7168,
                                'mpls': 0,
                                'other': 0,
                                'used': 12,
                                'used_percent': '0.17%',
                                'v4': 12,
                                'v6': 0
                            },
                            'o': {
                                'max': 3072,
                                'mpls': 0,
                                'other': 0,
                                'used': 14,
                                'used_percent': '0.46%',
                                'v4': 14,
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'security_acl_non_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 5120,
                                'mpls': 0,
                                'other': 40,
                                'used': 76,
                                'used_percent': '1.48%',
                                'v4': 0,
                                'v6': 36
                            },
                            'o': {
                                'max': 5120,
                                'mpls': 0,
                                'other': 5,
                                'used': 29,
                                'used_percent': '0.57%',
                                'v4': 0,
                                'v6': 24
                            }
                        }
                    }
                }
            },
            'tunnel_termination': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1792,
                                'mpls': 0,
                                'other': 0,
                                'used': 29,
                                'used_percent': '1.62%',
                                'v4': 11,
                                'v6': 18
                            }
                        }
                    }
                }
            }
        }
    },
    '2': {
        'table': {
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
                                'v6': 0
                            }
                        }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
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
                                'v6': 0
                            }
                        }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'control_plane': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1024,
                                'mpls': 0,
                                'other': 45,
                                'used': 281,
                                'used_percent': '27.44%',
                                'v4': 130,
                                'v6': 106
                            }
                        }
                    }
                }
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
                                'v6': 2},
                            'o': {
                                'max': 512,
                                'mpls': 0,
                                'other': 1,
                                'used': 4,
                                'used_percent': '0.78%',
                                'v4': 1,
                                'v6': 2
                            }
                        }
                    }
                }
            },
            'ip_route_table': {
                'subtype': {
                    'em_lpm': {
                        'dir': {
                            'i': {
                                'max': 212992,
                                'mpls': 1,
                                'other': 0,
                                'used': 14,
                                'used_percent': '0.01%',
                                'v4': 13,
                                'v6': 0
                            }
                        }
                    },
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1536,
                                'mpls': 2,
                                'other': 0,
                                'used': 11,
                                'used_percent': '0.72%',
                                'v4': 6,
                                'v6': 3
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
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
                                'v6': 4
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
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
                                'v6': 3
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'mac_address_table': {
                'subtype': {
                    'em': {
                        'dir': {
                            'i': {
                                'max': 32768,
                                'mpls': 0,
                                'other': 128,
                                'used': 128,
                                'used_percent': '0.39%',
                                'v4': 0,
                                'v6': 0
                            }
                        }
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
                                'v6': 0
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'netflow_acl': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1024,
                                'mpls': 0,
                                'other': 2,
                                'used': 6,
                                'used_percent': '0.59%',
                                'v4': 2,
                                'v6': 2
                            },
                            'o': {
                                'max': 1024,
                                'mpls': 0,
                                'other': 2,
                                'used': 7,
                                'used_percent': '0.68%',
                                'v4': 3,
                                'v6': 2
                            }
                        }
                    }
                }
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
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'pbr_acl': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 15872,
                                'mpls': 0,
                                'other': 0,
                                'used': 32,
                                'used_percent': '0.20%',
                                'v4': 26,
                                'v6': 6
                            }
                        }
                    }
                }
            },
            'qos_acl_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 2560,
                                'mpls': 0,
                                'other': 0,
                                'used': 15,
                                'used_percent': '0.59%',
                                'v4': 15,
                                'v6': 0
                            },
                            'o': {
                                'max': 3072,
                                'mpls': 0,
                                'other': 0,
                                'used': 12,
                                'used_percent': '0.39%',
                                'v4': 12,
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'qos_acl_non_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1536,
                                'mpls': 0,
                                'other': 10,
                                'used': 30,
                                'used_percent': '1.95%',
                                'v4': 0,
                                'v6': 20
                            },
                            'o': {
                                'max': 1024,
                                'mpls': 0,
                                'other': 8,
                                'used': 24,
                                'used_percent': '2.34%',
                                'v4': 0,
                                'v6': 16
                            }
                        }
                    }
                }
            },
            'security_acl_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 7168,
                                'mpls': 0,
                                'other': 0,
                                'used': 12,
                                'used_percent': '0.17%',
                                'v4': 12,
                                'v6': 0
                            },
                            'o': {
                                'max': 3072,
                                'mpls': 0,
                                'other': 0,
                                'used': 14,
                                'used_percent': '0.46%',
                                'v4': 14,
                                'v6': 0
                            }
                        }
                    }
                }
            },
            'security_acl_non_ipv4': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 5120,
                                'mpls': 0,
                                'other': 40,
                                'used': 76,
                                'used_percent': '1.48%',
                                'v4': 0,
                                'v6': 36
                            },
                            'o': {
                                'max': 5120,
                                'mpls': 0,
                                'other': 5,
                                'used': 29,
                                'used_percent': '0.57%',
                                'v4': 0,
                                'v6': 24
                            }
                        }
                    }
                }
            },
            'tunnel_termination': {
                'subtype': {
                    'tcam': {
                        'dir': {
                            'i': {
                                'max': 1792,
                                'mpls': 0,
                                'other': 0,
                                'used': 29,
                                'used_percent': '1.62%',
                                'v4': 11,
                                'v6': 18
                            }
                        }
                    }
                }
            }
        }
    }
}
}