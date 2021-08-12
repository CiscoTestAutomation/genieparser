# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'mac_addr': {
        'aabb.0011.0001': {
            'evi': 1,
            'bd_id': 11,
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                'Et1/0:11',
            ],
        },
        'aabb.0011.0020': {
            'evi': 1,
            'bd_id': 11,
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                'Et1/0:11',
            ],
        },
        'aabb.0011.0021': {
            'evi': 1,
            'bd_id': 11,
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                'Duplicate',
            ],
        },
    },
}
