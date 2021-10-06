# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        1: {
            'bd_id': {
                11: {
                    'eth_tag': {
                        0: {
                            'ip_addr': {
                                '192.168.11.11': {
                                    'mac_addr': {
                                        'aabb.0011.0001': {
                                            'stale': False,
                                            'esi': '0000.0000.0000.0000.0000',
                                            'next_hops': [
                                                'L:17 Ethernet1/0 service instance 11',
                                            ],
                                            'seq_number': 0,
                                            'ip_dup_detection': {
                                                'status': 'Timer not running',
                                            },
                                            'label2_included': 'No',
                                        }
                                    }
                                },
                                '192.168.11.20': {
                                    'mac_addr': {
                                        'aabb.0011.0020': {
                                            'stale': False,
                                            'esi': '0000.0000.0000.0000.0000',
                                            'next_hops': [
                                                'L:17 Ethernet1/0 service instance 11',
                                            ],
                                            'seq_number': 5,
                                            'ip_dup_detection': {
                                                'status': 'Timer not running',
                                            },
                                            'label2_included': 'No',
                                        }
                                    }
                                },
                                '192.168.11.21': {
                                    'mac_addr': {
                                        'ccdd.0011.0022': {
                                            'stale': False,
                                            'esi': '0000.0000.0000.0000.0000',
                                            'next_hops': [
                                                'L:17 Ethernet1/0 service instance 11',
                                            ],
                                            'seq_number': 0,
                                            'ip_dup_detection': {
                                                'status': 'Duplicate IP address detected',
                                            },
                                            'last_local_mac_sent': 'aabb.0011.0022',
                                            'label2_included': 'No',
                                        }
                                    }
                                },
                                '2001:11::11': {
                                    'mac_addr': {
                                        'aabb.0011.0001': {
                                            'stale': False,
                                            'esi': '0000.0000.0000.0000.0000',
                                            'next_hops': [
                                                'L:17 Ethernet1/0 service instance 11',
                                            ],
                                            'seq_number': 0,
                                            'ip_dup_detection': {
                                                'status': 'Timer not running',
                                            },
                                            'label2_included': 'No',
                                        }
                                    }
                                },
                                '2001:11::20': {
                                    'mac_addr': {
                                        'aabb.0011.0021': {
                                            'stale': False,
                                            'esi': '0000.0000.0000.0000.0000',
                                            'next_hops': [
                                                'L:17 Ethernet1/0 service instance 11',
                                                'L:16 2.2.2.1',
                                            ],
                                            'local_addr': '1.1.1.1',
                                            'seq_number': 6,
                                            'ip_dup_detection': {
                                                'status': 'Timer not running',
                                            },
                                            'label2_included': 'No',
                                        }
                                    }
                                },
                                '2001:11::21': {
                                    'mac_addr': {
                                        'aabb.0011.0023': {
                                            'stale': False,
                                            'esi': '0000.0000.0000.0000.0000',
                                            'next_hops': [
                                                'L:17 Ethernet1/0 service instance 11',
                                            ],
                                            'seq_number': 0,
                                            'ip_dup_detection': {
                                                'status': 'IP moves 4, limit 5',
                                                'moves_count': 4,
                                                'moves_limit': 5,
                                                'expiry_time': '09:21:25',
                                            },
                                            'label2_included': 'No',
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        2: {
            'bd_id': {
                12: {
                    'eth_tag': {
                        0: {
                            'ip_addr': {
                                '192.168.12.11': {
                                    'mac_addr': {
                                        'aabb.0012.0001': {
                                            'stale': False,
                                            'esi': '0000.0000.0000.0000.0000',
                                            'next_hops': [
                                                'L:16 2.2.2.1',
                                            ],
                                            'local_addr': '1.1.1.1',
                                            'seq_number': 0,
                                            'ip_dup_detection': {
                                                'status': 'Timer not running',
                                            },
                                            'label2_included': 'No',
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
