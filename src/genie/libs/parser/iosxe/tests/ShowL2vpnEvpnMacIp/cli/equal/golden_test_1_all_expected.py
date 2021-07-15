# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'ip_addr': {
        '192.168.11.11': {
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0001',
            'next_hops': [
                {
                    'next_hop': 'Et1/0:11',
                },
            ],
        },
        '192.168.11.20': {
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0020',
            'next_hops': [
                {
                    'next_hop': 'Et1/0:11',
                },
            ],
        },
        '192.168.11.21': {
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'Duplicate',
            'next_hops': [
                {
                    'next_hop': 'Et1/0:11',
                },
            ],
        },
        '2001:11::11': {
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0001',
            'next_hops': [
                {
                    'next_hop': 'Et1/0:11',
                },
            ],
        },
        '2001:11::20': {
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0021',
            'next_hops': [
                {
                    'next_hop': 'Duplicate',
                },
            ],
        },
        '2001:11::21': {
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0023',
            'next_hops': [
                {
                    'next_hop': 'Et1/0:11',
                },
            ],
        },
        '192.168.12.11': {
            'evi': 2,
            'bd_id': 12,
            'mac_addr': 'aabb.0012.0001',
            'next_hops': [
                {
                    'next_hop': '2.2.2.1',
                },
            ],
        },
    },
}
