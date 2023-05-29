expected_output = {
    'instance': {
        'default': {
            'interface': {
                'Bundle-Ether10.10': {
                    'state': 'Enabled',
                    'adjacency_formation': 'Enabled',
                    'prefix_advertisement': 'Enabled',
                    'ipv4_bfd': True,
                    'ipv6_bfd': True,
                    'bfd_min_interval': 100,
                    'bfd_multiplier': 3,
                    'rsi_srlg': 'Registered',
                    'bandwidth': 2000000,
                    'total_bandwidth': 2000000,
                    'circuit_type': 'level-2-only',
                    'media_type': 'LAN',
                    'circuit_number': 1,
                    'measured_delay': {
                        'min': '-',
                        'avg': '-',
                        'max': '-'
                    },
                    'delay_normalization': {
                        'interval': 0,
                        'offset': 0
                    },
                    'normalized_delay': {
                        'min': '-',
                        'avg': '-',
                        'max': '-'
                    },
                    'link_loss': '-',
                    'level': {
                        2: {
                            'adjacency_count': 1,
                            'lan_id': 'P-9001-1.01',
                            'priority': {
                                'local': '64',
                                'dis': '64'
                            },
                            'next_lan_iih_sec': 2,
                            'lsp_pacing_interval_ms': 33,
                            'psnp_entry_queue_size': 0,
                            'hello_interval_sec': 10,
                            'hello_multiplier': 3
                        }
                    },
                    'clns_io': {
                        'protocol_state': 'Up',
                        'mtu': 1497,
                        'snpa': '8478.ac6d.6c4a',
                        'layer2_mcast_groups_membership': {
                            'all_level_2_iss': 'Yes'
                        }
                    },
                    'topology': {
                        'ipv4 unicast': {
                            'state': 'Enabled',
                            'adjacency_formation': 'Running',
                            'prefix_advertisement': 'Running',
                            'metric': {
                                'level': {
                                    1: 0,
                                    2: 10
                                }
                            },
                            'metric_fallback': {
                                'bandwidth': {
                                    'level': {
                                        1: 'Inactive',
                                        2: 'Inactive'
                                    }
                                },
                                'anomaly': {
                                    'level': {
                                        1: 'Inactive',
                                        2: 'Inactive'
                                    }
                                }
                            },
                            'weight': {
                                'level': {
                                    1: 0,
                                    2: 0
                                }
                            },
                            'mpls': {
                                'mpls_max_label_stack': '1/3/10/10 (PRI/BKP/SRTE/SRAT)',
                                'ldp_sync': {
                                    'level': {
                                        1: 'Disabled',
                                        2: 'Disabled'
                                    }
                                }
                            },
                            'frr': {
                                'level': {
                                    1: {
                                        'state': 'Not Enabled',
                                        'type': 'None'
                                    },
                                    2: {
                                        'state': 'Not Enabled',
                                        'type': 'None'
                                    }
                                }
                            }
                        },
                        'ipv6 unicast': {
                            'state': 'Enabled',
                            'adjacency_formation': 'Running',
                            'prefix_advertisement': 'Running',
                            'metric': {
                                'level': {
                                    1: 0,
                                    2: 10
                                }
                            },
                            'metric_fallback': {
                                'bandwidth': {
                                    'level': {
                                        1: 'Inactive',
                                        2: 'Inactive'
                                    }
                                },
                                'anomaly': {
                                    'level': {
                                        1: 'Inactive',
                                        2: 'Inactive'
                                    }
                                }
                            },
                            'weight': {
                                'level': {
                                    1: 0,
                                    2: 0
                                }
                            },
                            'mpls': {
                                'mpls_max_label_stack': '1/3/10/10 (PRI/BKP/SRTE/SRAT)',
                                'ldp_sync': {
                                    'level': {
                                        1: 'Disabled',
                                        2: 'Disabled'
                                    }
                                }
                            },
                            'frr': {
                                'level': {
                                    1: {
                                        'state': 'Not Enabled',
                                        'type': 'None'
                                    },
                                    2: {
                                        'state': 'Not Enabled',
                                        'type': 'None'
                                    }
                                }
                            }
                        }
                    },
                    'address_family': {
                        'IPv4': {
                            'state': 'Enabled',
                            'protocol_state': 'Up',
                            'forwarding_address': ['192.168.17.1'],
                            'global_prefix': ['192.168.17.0/24']
                        },
                        'IPv6': {
                            'state': 'Enabled',
                            'protocol_state': 'Up',
                            'forwarding_address': ['fe80::8678:acff:fe6d:6c4a'],
                            'global_prefix': ['100:1:1::/64']
                        }
                    },
                    'lsp': {
                        'transmit_timer_expires_ms': 0,
                        'transmission_state': 'idle',
                        'lsp_transmit_back_to_back_limit_window_msec': 0,
                        'lsp_transmit_back_to_back_limit': 9
                    }
                }
            }
        }
    }
}