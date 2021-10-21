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
                                'aabb.0012.0002': {
                                    'sticky': False,
                                    'stale': False,
                                    'esi': '0000.0000.0000.0000.0000',
                                    'next_hops': [
                                        'L:16 2.2.2.1',
                                    ],
                                    'local_addr': '4.4.4.1',
                                    'seq_number': 0,
                                    'mac_only_present': True,
                                    'mac_dup_detection': {
                                        'status': 'Timer not running',
                                    },
                                },
                                'aabb.cc02.2800': {
                                    'sticky': False,
                                    'stale': False,
                                    'esi': '03AA.BB00.0000.0200.0001',
                                    'next_hops': [
                                        'L:17 3.3.3.1',
                                    ],
                                    'local_addr': '4.4.4.1',
                                    'seq_number': 0,
                                    'mac_only_present': True,
                                    'mac_dup_detection': {
                                        'status': 'Timer not running',
                                    },
                                },
                                'aabb.cc82.2800': {
                                    'sticky': False,
                                    'stale': False,
                                    'esi': '03AA.BB00.0000.0200.0001',
                                    'next_hops': [
                                        'L:17 Ethernet1/0 service instance 12',
                                        'L:17 3.3.3.1',
                                        'L:17 5.5.5.1',
                                    ],
                                    'local_addr': '4.4.4.1',
                                    'seq_number': 0,
                                    'mac_only_present': True,
                                    'mac_dup_detection': {
                                        'status': 'Timer not running',
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
