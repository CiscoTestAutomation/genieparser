# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        1: {
            'eth_tag': {
                0: {
                    'producer': {
                        'BGP': {
                            'mac_addr': {
                                '0011.0011.0011': {
                                    'esi': '0000.0000.0000.0000.0000',
                                    'flags': 'BInt(Brm)',
                                    'next_hops': [
                                        'L:17 2.2.2.1'
                                    ],
                                    'no_of_default_gws': 2,
                                    'no_of_macip_rts': 2,
                                    'seq_number': 0
                                },
                                'aabb.0000.0002': {
                                    'esi': '0000.0000.0000.0000.0000',
                                    'flags': 'B()',
                                    'next_hops': [
                                        'L:17 2.2.2.1'
                                    ],
                                    'no_of_macip_rts': 3,
                                    'seq_number': 0
                                },
                                'aabb.0000.0005': {
                                    'esi': '0000.0000.0000.0000.0000',
                                    'flags': 'B()',
                                    'next_hops': [
                                        'L:16 99.99.99.1'
                                    ],
                                    'no_of_macip_rts': 3,
                                    'seq_number': 0
                                },
                                'aabb.0000.0006': {
                                    'esi': '0000.0000.0000.0000.0000',
                                    'flags': 'B()',
                                    'next_hops': [
                                        'L:16 98.98.98.1'
                                    ],
                                    'no_of_macip_rts': 3,
                                    'seq_number': 0
                                }
                            }
                        },
                        'L2VPN': {
                            'mac_addr': {
                                '0011.0011.0011': {
                                    'esi': '0000.0000.0000.0000.0000',
                                    'flags': 'Int(Brm)',
                                    'next_hops': [
                                        'BD11:0'
                                    ],
                                    'no_of_default_gws': 2,
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