

expected_output = {
    'vrf': {
        'GENIE-CORE': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        '1000': {
                            'areas': {
                                '0.0.0.1': {
                                    'interfaces': {
                                        'Ethernet1/2': {
                                            'bfd': {
                                                'enable': False
                                            },
                                            'cost': 20,
                                            'dead_interval': 6,
                                            'enable': True,
                                            'hello_interval': 2,
                                            'hello_timer': '00:00:01',
                                            'if_cfg': True,
                                            'index': 1,
                                            'interface_type': 'p2p',
                                            'ip_address': '10.100.31.27/31',
                                            'line_protocol': 'up',
                                            'name': 'Ethernet1/2',
                                            'passive': False,
                                            'retransmit_interval': 5,
                                            'state': 'p2p',
                                            'statistics': {
                                                'link_scope_lsa_cksum_sum': 0,
                                                'link_scope_lsa_count': 0,
                                                'num_nbrs_adjacent': 1,
                                                'num_nbrs_flooding': 1,
                                                'total_neighbors': 1
                                            },
                                            'transmit_delay': 1,
                                            'wait_interval': 6
                                        },
                                        'Vlan959': {
                                            'bfd': {
                                                'enable': False
                                            },
                                            'cost': 10,
                                            'dead_interval': 6,
                                            'enable': True,
                                            'hello_interval': 2,
                                            'hello_timer': '00:00:00',
                                            'if_cfg': True,
                                            'index': 4,
                                            'interface_type': 'p2p',
                                            'ip_address': '10.100.31.217/30',
                                            'line_protocol': 'up',
                                            'name': 'Vlan959',
                                            'passive': False,
                                            'retransmit_interval': 5,
                                            'state': 'p2p',
                                            'statistics': {
                                                'link_scope_lsa_cksum_sum': 0,
                                                'link_scope_lsa_count': 0,
                                                'num_nbrs_adjacent': 1,
                                                'num_nbrs_flooding': 1,
                                                'total_neighbors': 1
                                            },
                                            'transmit_delay': 1,
                                            'wait_interval': 6
                                        },
                                        'loopback110': {
                                            'bfd': {
                                                'enable': False
                                            },
                                            'cost': 1,
                                            'enable': True,
                                            'if_cfg': True,
                                            'index': 3,
                                            'interface_type': 'loopback',
                                            'ip_address': '10.100.0.13/32',
                                            'line_protocol': 'up',
                                            'name': 'loopback110',
                                            'state': 'loopback'
                                        },
                                        'port-channel1001': {
                                            'bfd': {
                                                'enable': True
                                            },
                                            'cost': 10,
                                            'dead_interval': 6,
                                            'enable': True,
                                            'hello_interval': 2,
                                            'hello_timer': '00:00:01',
                                            'if_cfg': True,
                                            'index': 5,
                                            'interface_type': 'p2p',
                                            'ip_address': '10.100.31.197/30',
                                            'line_protocol': 'up',
                                            'name': 'port-channel1001',
                                            'passive': False,
                                            'retransmit_interval': 5,
                                            'state': 'p2p',
                                            'statistics': {
                                                'link_scope_lsa_cksum_sum': 0,
                                                'link_scope_lsa_count': 0,
                                                'num_nbrs_adjacent': 1,
                                                'num_nbrs_flooding': 1,
                                                'total_neighbors': 1
                                            },
                                            'transmit_delay': 1,
                                            'wait_interval': 6
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        '2000': {
                            'areas': {
                                '0.0.0.1': {
                                    'interfaces': {
                                        'Ethernet1/31': {
                                            'bfd': {
                                                'enable': False
                                            },
                                            'cost': 100,
                                            'dead_interval': 6,
                                            'enable': True,
                                            'hello_interval': 2,
                                            'hello_timer': '00:00:01',
                                            'if_cfg': True,
                                            'index': 3,
                                            'interface_type': 'p2p',
                                            'ip_address': '10.100.31.252/31',
                                            'line_protocol': 'up',
                                            'name': 'Ethernet1/31',
                                            'passive': False,
                                            'retransmit_interval': 5,
                                            'state': 'p2p',
                                            'statistics': {
                                                'num_nbrs_adjacent': 1,
                                                'num_nbrs_flooding': 1,
                                                'total_neighbors': 1
                                            },
                                            'transmit_delay': 1,
                                            'wait_interval': 6
                                        },
                                        'Ethernet1/45': {
                                            'bfd': {
                                                'enable': False
                                            },
                                            'cost': 100,
                                            'dead_interval': 40,
                                            'enable': True,
                                            'hello_interval': 10,
                                            'if_cfg': False,
                                            'index': 1,
                                            'interface_type': 'p2p',
                                            'ip_address': '10.111.3.2/30',
                                            'line_protocol': 'down',
                                            'name': 'Ethernet1/45',
                                            'passive': False,
                                            'retransmit_interval': 5,
                                            'state': 'down',
                                            'statistics': {
                                                'link_scope_lsa_cksum_sum': 0,
                                                'link_scope_lsa_count': 0,
                                                'num_nbrs_adjacent': 0,
                                                'num_nbrs_flooding': 0,
                                                'total_neighbors': 0
                                            },
                                            'transmit_delay': 1,
                                            'wait_interval': 40
                                        },
                                        'Vlan3030': {
                                            'bfd': {
                                                'enable': False
                                            },
                                            'cost': 1000,
                                            'enable': True,
                                            'if_cfg': True,
                                            'index': 118,
                                            'interface_type': 'broadcast',
                                            'ip_address': '10.115.128.4/24',
                                            'line_protocol': 'up',
                                            'name': 'Vlan3030',
                                            'passive': True,
                                            'state': 'dr'
                                        },
                                        'Vlan986': {
                                            'bfd': {
                                                'enable': False
                                            },
                                            'cost': 1000,
                                            'enable': True,
                                            'if_cfg': True,
                                            'index': 122,
                                            'interface_type': 'broadcast',
                                            'ip_address': '10.100.17.51/29',
                                            'line_protocol': 'up',
                                            'name': 'Vlan986',
                                            'passive': True,
                                            'state': 'dr'
                                        },
                                        'Vlan997': {
                                            'bfd': {
                                                'enable': False
                                            },
                                            'cost': 10,
                                            'dead_interval': 40,
                                            'enable': True,
                                            'hello_interval': 10,
                                            'hello_timer': '00:00:04',
                                            'if_cfg': True,
                                            'index': 137,
                                            'interface_type': 'p2p',
                                            'ip_address': '10.100.17.81/30',
                                            'line_protocol': 'up',
                                            'name': 'Vlan997',
                                            'passive': False,
                                            'retransmit_interval': 5,
                                            'state': 'p2p',
                                            'statistics': {
                                                'num_nbrs_adjacent': 1,
                                                'num_nbrs_flooding': 1,
                                                'total_neighbors': 1
                                            },
                                            'transmit_delay': 1,
                                            'wait_interval': 40
                                        },
                                        'loopback100': {
                                            'bfd': {
                                                'enable': False
                                            },
                                            'cost': 1,
                                            'enable': True,
                                            'if_cfg': True,
                                            'index': 50,
                                            'interface_type': 'loopback',
                                            'ip_address': '10.100.0.11/32',
                                            'line_protocol': 'up',
                                            'name': 'loopback100',
                                            'state': 'loopback'
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
