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
                                'aabb.0011.0002': {
                                    'sticky': False,
                                    'stale': False,
                                    'esi': '0000.0000.0000.0000.0000',
                                    'next_hops': [
                                        'V:16 2.2.2.1',
                                    ],
                                    'local_addr': '1.1.1.1',
                                    'seq_number': 0,
                                    'mac_only_present': False,
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
