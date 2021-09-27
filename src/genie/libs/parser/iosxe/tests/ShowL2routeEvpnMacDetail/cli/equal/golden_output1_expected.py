# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {'evi': {
                        2: {
                            'eth_tag': {
                                0: {
                                    'producer': {
                                        'BGP': {
                                            'mac_addr': {
                                                '0012.0012.0012': {
                                                    'esi': '0000.0000.0000.0000.0000',
                                                    'flags': 'BInt(Brm)',
                                                    'next_hops': [
                                                        'L:16 2.2.2.1',
                                                        'L:17 5.5.5.1'
                                                    ],
                                                    'no_of_default_gws': 2,
                                                    'no_of_macip_rts': 2,
                                                    'seq_number': 0
                                                },
                                                'aabb.0012.0002': {
                                                    'esi': '0000.0000.0000.0000.0000',
                                                    'flags': 'B()',
                                                    'next_hops': [
                                                        'L:16 2.2.2.1'
                                                    ],
                                                    'no_of_macip_rts': 1,
                                                    'seq_number': 0
                                                },
                                                'aabb.cc82.2800': {
                                                    'esi': '03AA.BB00.0000.0200.0001',
                                                    'flags': 'Int()',
                                                    'next_hops': [
                                                        'L:17 5.5.5.1'
                                                    ],
                                                    'no_of_macip_rts': 2,
                                                    'seq_number': 0
                                                }
                                            }
                                        },
                                        'L2VPN': {
                                            'mac_addr': {
                                                '0012.0012.0012': {
                                                    'esi': '0000.0000.0000.0000.0000',
                                                    'flags': 'Int(Brm)',
                                                    'next_hops': [
                                                        'BD12:0',
                                                        'L:16 2.2.2.1',
                                                        'Et1/0:12'
                                                    ],
                                                    'no_of_default_gws': 2,
                                                    'no_of_macip_rts': 2,
                                                    'seq_number': 0
                                                },
                                                'aabb.cc02.2800': {
                                                    'esi': '03AA.BB00.0000.0200.0001',
                                                    'flags': 'B()',
                                                    'next_hops': [
                                                        'Et1/0:12'
                                                    ],
                                                    'no_of_macip_rts': 0,
                                                    'seq_number': 0
                                                },
                                                'aabb.cc82.2800': {
                                                    'esi': '03AA.BB00.0000.0200.0001',
                                                    'flags': 'B()',
                                                    'next_hops': [
                                                        'Et1/0:12'
                                                    ],
                                                    'no_of_macip_rts': 2,
                                                    'seq_number': 0
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }