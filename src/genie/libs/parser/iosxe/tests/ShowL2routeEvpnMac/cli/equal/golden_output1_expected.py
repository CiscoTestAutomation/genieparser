# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.
expected_output = {
    'evi':{
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
                                },
                                'aabb.0012.0002': {
                                    'seq_number': 0,
                                    'next_hops': [
                                        'Gi4:11',
                                        'L:101 IP:1.1.1.1',
                                        'BD11:0'
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        },
        10: {
            'eth_tag': {
                0: {
                    'producer': {
                        'L2VPN': {
                            'mac_addr': {
                                '000A.000A.000A': {
                                    'seq_number': 0,
                                    'next_hops': [
                                        'Et0/0 EFP:1'
                                    ]
                                }
                            }
                        },
                        'BGP': {
                            'mac_addr': {
                                '000B.000B.000B': {
                                    'seq_number': 0,
                                    'next_hops': [
                                        'L:101 IP:1.1.1.1'
                                    ]
                                },
                                '000C.000C.000C': {
                                    'seq_number': 0,
                                    'next_hops': [
                                        'V:2002 IP:2.2.2.2'
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