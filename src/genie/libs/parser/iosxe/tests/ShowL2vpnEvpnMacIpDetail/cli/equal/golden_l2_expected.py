# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'ip_addr': {
        '192.168.11.12': {
            'stale': False,
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0002',
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                {
                    'next_hop': 'V:16 2.2.2.1',
                },
            ],
            'local_addr': '1.1.1.1',
            'seq_number': 0,
            'ip_dup_detection': {
                'status': 'Timer not running',
            },
            'label2_included': False,
        },
        '2001:11::12': {
            'stale': False,
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0002',
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                {
                    'next_hop': 'V:16 2.2.2.1',
                },
            ],
            'local_addr': '1.1.1.1',
            'seq_number': 0,
            'ip_dup_detection': {
                'status': 'Timer not running',
            },
            'label2_included': False,
        },
    },
}
