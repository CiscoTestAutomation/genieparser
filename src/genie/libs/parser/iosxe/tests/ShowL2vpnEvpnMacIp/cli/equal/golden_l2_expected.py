# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'ip_addr': {
        '192.168.11.12': {
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0002',
            'next_hops': [
                {
                    'next_hop': '2.2.2.1',
                },
            ],
        },
        '2001:11::12': {
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0002',
            'next_hops': [
                {
                    'next_hop': '2.2.2.1',
                },
            ],
        },
    },
}
