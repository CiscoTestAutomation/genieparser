# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        1: {
            'bd_id': {
                11: {
                    'eth_tag': {
                        0: {
                            'mac_addr': {
                                'aabb.0011.0001': {
                                    'sticky': False,
                                    'stale': False,
                                    'esi': '0000.0000.0000.0000.0000',
                                    'next_hops': [
                                        'L:17 Ethernet1/0 service instance 11',
                                    ],
                                    'seq_number': 0,
                                    'mac_only_present': False,
                                    'mac_dup_detection': {
                                        'status': 'Timer not running',
                                    },
                                },
                                'aabb.0011.0020': {
                                    'sticky': False,
                                    'stale': False,
                                    'esi': '0000.0000.0000.0000.0000',
                                    'next_hops': [
                                        'L:17 Ethernet1/0 service instance 11',
                                    ],
                                    'seq_number': 5,
                                    'mac_only_present': False,
                                    'mac_dup_detection': {
                                        'status': 'MAC moves 3, limit 5',
                                        'moves_count': 3,
                                        'moves_limit': 5,
                                        'expiry_time': '09:56:34',
                                    },
                                },
                                'aabb.0011.0021': {
                                    'sticky': False,
                                    'stale': False,
                                    'esi': '0000.0000.0000.0000.0000',
                                    'next_hops': [
                                        'L:17 Ethernet1/0 service instance 11',
                                        'L:16 2.2.2.1',
                                    ],
                                    'local_addr': '1.1.1.1',
                                    'seq_number': 6,
                                    'mac_only_present': False,
                                    'mac_dup_detection': {
                                        'status': 'Duplicate MAC address detected',
                                    },
                                },
                            },
                        }
                    }
                }
            }
        }
    }
}
