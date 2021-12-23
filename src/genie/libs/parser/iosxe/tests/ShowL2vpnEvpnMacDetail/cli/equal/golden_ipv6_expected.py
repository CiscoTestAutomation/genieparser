# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        3: {
            'bd_id': {
                103: {
                    'eth_tag': {
                        0: {
                            'mac_addr': {
                                '0051.a101.0011': {
                                    'esi': '0000.0000.0000.0000.0000',
                                    'local_addr': 'ABCD:2::2',
                                    'mac_dup_detection': {
                                        'status': 'Timer not running',
                                    },
                                    'mac_only_present': True,
                                    'next_hops': ['V:20103 ABCD:1::2'],
                                    'seq_number': 0,
                                    'stale': False,
                                    'sticky': False,
                                },
                                '0051.a101.0012': {
                                    'esi': '0000.0000.0000.0000.0000',
                                    'local_addr': 'ABCD:2::2',
                                    'mac_dup_detection': {
                                        'status': 'Timer not running',
                                    },
                                    'mac_only_present': True,
                                    'next_hops': ['V:20103 ABCD:1::2', 'V:20104 ABCD:1::3'],
                                    'seq_number': 0,
                                    'stale': False,
                                    'sticky': False,
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
