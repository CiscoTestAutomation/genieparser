expected_output = {
    'vrf': {
        'default': {
            'local_label': {
                17: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '13.1.1.2-A': {
                                    'outgoing_interface': {
                                        'Ethernet0/2': {
                                            'next_hop': '13.1.1.2',
                                            'bytes_label_switched': 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                19: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '12.1.1.2-A': {
                                    'outgoing_interface': {
                                        'Ethernet0/1': {
                                            'next_hop': '12.1.1.2',
                                            'bytes_label_switched': 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16021: {
                    'outgoing_label_or_vc': {
                        'No Label': {
                            'prefix_or_tunnel_id': {
                                '2.2.2.2/32': {
                                    'outgoing_interface': {
                                        'drop': {
                                            'bytes_label_switched': 0,
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16022: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '0-2.2.2.2/32-2': {
                                    'outgoing_interface': {
                                        'Ethernet0/1': {
                                            'next_hop': '12.1.1.2',
                                            'bytes_label_switched': 0,
                                            'flexalgo_info': {
                                                'pdb_index': 1,
                                                'metric': 100,
                                                'algo': 1,
                                                'via_srms': 0
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16023: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '0-2.2.2.2/32-32772': {
                                    'outgoing_interface': {
                                        'Ethernet0/1': {
                                            'next_hop': '12.1.1.2',
                                            'bytes_label_switched': 0,
                                            'flexalgo_info': {
                                                'pdb_index': 2,
                                                'metric': 100,
                                                'algo': 128,
                                                'via_srms': 0
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16025: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '0-2.2.2.2/32-38404': {
                                    'outgoing_interface': {
                                        'Ethernet0/1': {
                                            'next_hop': '12.1.1.2',
                                            'bytes_label_switched': 0,
                                            'flexalgo_info': {
                                                'pdb_index': 3,
                                                'metric': 200,
                                                'algo': 128,
                                                'via_srms': 0
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16031: {
                    'outgoing_label_or_vc': {
                        'No Label': {
                            'prefix_or_tunnel_id': {
                                '3.3.3.3/32': {
                                    'outgoing_interface': {
                                        'drop': {
                                            'bytes_label_switched': 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16032: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '0-3.3.3.3/32-2': {
                                    'outgoing_interface': {
                                        'Ethernet0/2': {
                                            'next_hop': '13.1.1.2',
                                            'bytes_label_switched': 0,
                                            'flexalgo_info': {
                                                'pdb_index': 4,
                                                'metric': 100,
                                                'algo': 1,
                                                'via_srms': 0
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16033: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '0-3.3.3.3/32-32772': {
                                    'outgoing_interface': {
                                        'Ethernet0/2': {
                                            'next_hop': '13.1.1.2',
                                            'bytes_label_switched': 0,
                                            'flexalgo_info': {
                                                'pdb_index': 5,
                                                'metric': 100,
                                                'algo': 128,
                                                'via_srms': 0
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16035: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '0-3.3.3.3/32-38404': {
                                    'outgoing_interface': {
                                        'Ethernet0/2': {
                                            'next_hop': '13.1.1.2',
                                            'bytes_label_switched': 0,
                                            'flexalgo_info': {
                                                'pdb_index': 6,
                                                'metric': 220,
                                                'algo': 128,
                                                'via_srms': 0
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