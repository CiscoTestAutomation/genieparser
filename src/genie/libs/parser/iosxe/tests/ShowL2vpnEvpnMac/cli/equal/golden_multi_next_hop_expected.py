# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'mac_addr': {
        'aabb.0012.0002': {
            'evi': 2,
            'bd_id': 12,
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                {
                    'next_hop': '2.2.2.1',
                },
            ],
        },
        'aabb.cc02.2800': {
            'evi': 2,
            'bd_id': 12,
            'esi': '03AA.BB00.0000.0200.0001',
            'eth_tag': 0,
            'next_hops': [
                {
                    'next_hop': '3.3.3.1',
                },
            ],
        },
        'aabb.cc82.2800': {
            'evi': 2,
            'bd_id': 12,
            'esi': '03AA.BB00.0000.0200.0001',
            'eth_tag': 0,
            'next_hops': [
                {
                    'next_hop': 'Et1/0:12',
                },
                {
                    'next_hop': '3.3.3.1',
                },
                {
                    'next_hop': '5.5.5.1',
                },
            ],
        },
    },
}
