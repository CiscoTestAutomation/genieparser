# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        2: {
            'bd_id': {
                12: {
                    'eth_tag': {
                        0: {
                            'mac_addr': {
                                'aabb.0012.0002' : {
                                    'esi': '0000.0000.0000.0000.0000',
                                    'next_hops': [
                                        '2.2.2.1',
                                    ]
                                },
                                'aabb.cc02.2800': {
                                    'esi': '03AA.BB00.0000.0200.0001',
                                    'next_hops': [
                                        '3.3.3.1',
                                    ],
                                },
                                'aabb.cc82.2800': {
                                    'esi': '03AA.BB00.0000.0200.0001',
                                    'next_hops': [
                                        'Et1/0:12',
                                        '3.3.3.1',
                                        '5.5.5.1',
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        },
    },
}
