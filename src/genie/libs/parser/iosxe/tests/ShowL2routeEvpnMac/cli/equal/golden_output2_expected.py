# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        1: {
            'eth_tag': {
                0: {
                    'producer': {
                        'L2VPN': {
                            'mac_addr': {
                                '0011.0011.0011': {
                                    'seq_number': 0,
                                    'next_hops': [
                                        'BD11:0'
                                    ]
                                }
                            }
                        },
                        'BGP': {
                            'mac_addr': {
                                '0011.0011.0011': {
                                    'seq_number': 0,
                                    'next_hops': [
                                        'L:17 2.2.2.1'
                                    ]
                                },
                                'aabb.0000.0002': {
                                    'seq_number': 0,
                                    'next_hops': [
                                        'L:17 2.2.2.1'
                                    ]
                                },
                                'aabb.0000.0005': {
                                    'seq_number': 0,
                                    'next_hops': [
                                        'L:16 99.99.99.1'
                                    ]
                                },
                                'aabb.0000.0006': {
                                    'seq_number': 0,
                                    'next_hops': [
                                        'L:16 98.98.98.1'
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}