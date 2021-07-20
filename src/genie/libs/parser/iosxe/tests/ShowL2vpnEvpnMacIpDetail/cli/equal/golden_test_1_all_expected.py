# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'ip_addr': {
        '192.168.11.11': {
            'stale': False,
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0001',
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                'L:17 Ethernet1/0 service instance 11',
            ],
            'seq_number': 0,
            'ip_dup_detection': {
                'status': 'Timer not running',
            },
            'label2_included': False,
        },
        '192.168.11.20': {
            'stale': False,
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0020',
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                'L:17 Ethernet1/0 service instance 11',
            ],
            'seq_number': 5,
            'ip_dup_detection': {
                'status': 'Timer not running',
            },
            'label2_included': False,
        },
        '192.168.11.21': {
            'stale': False,
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'ccdd.0011.0022',
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                'L:17 Ethernet1/0 service instance 11',
            ],
            'seq_number': 0,
            'ip_dup_detection': {
                'status': 'Duplicate IP address detected',
            },
            'last_local_mac_sent': 'aabb.0011.0022',
            'label2_included': False,
        },
        '2001:11::11': {
            'stale': False,
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0001',
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                'L:17 Ethernet1/0 service instance 11',
            ],
            'seq_number': 0,
            'ip_dup_detection': {
                'status': 'Timer not running',
            },
            'label2_included': False,
        },
        '2001:11::20': {
            'stale': False,
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0021',
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                'L:17 Ethernet1/0 service instance 11',
                'L:16 2.2.2.1',
            ],
            'local_addr': '1.1.1.1',
            'seq_number': 6,
            'ip_dup_detection': {
                'status': 'Timer not running',
            },
            'label2_included': False,
        },
        '2001:11::21': {
            'stale': False,
            'evi': 1,
            'bd_id': 11,
            'mac_addr': 'aabb.0011.0023',
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                'L:17 Ethernet1/0 service instance 11',
            ],
            'seq_number': 0,
            'ip_dup_detection': {
                'status': 'IP moves 4, limit 5',
                'moves_count': 4,
                'moves_limit': 5,
                'expiry_time': '09:21:25',
            },
            'label2_included': False,
        },
        '192.168.12.11': {
            'stale': False,
            'evi': 2,
            'bd_id': 12,
            'mac_addr': 'aabb.0012.0001',
            'esi': '0000.0000.0000.0000.0000',
            'eth_tag': 0,
            'next_hops': [
                'L:16 2.2.2.1',
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
