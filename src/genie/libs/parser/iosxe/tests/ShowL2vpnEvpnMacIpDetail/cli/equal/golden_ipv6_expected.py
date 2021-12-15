# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        3: {
            'bd_id': {
                103: {
                    'eth_tag': {
                        0: {
                            'ip_addr': {
                                '192.168.101.11': {
                                    'mac_addr': {
                                        '0051.a101.0011': {
                                            'esi': '0000.0000.0000.0000.0000',
                                            'ip_dup_detection': {
                                                'status': 'Timer not running',
                                            },
                                            'label2_included': 'No',
                                            'local_addr': 'ABCD:2::2',
                                            'next_hops': ['V:20103 ABCD:1::2'],
                                            'seq_number': 0,
                                            'stale': False,
                                        },
                                    },
                                },
                                '192.168.101.12': {
                                    'mac_addr': {
                                        '0051.a101.0011': {
                                            'esi': '0000.0000.0000.0000.0000',
                                            'ip_dup_detection': {
                                                'status': 'Timer not running',
                                            },
                                            'label2_included': 'No',
                                            'local_addr': 'ABCD:2::2',
                                            'next_hops': ['V:20103 ABCD:1::2', 'V:20103 ABCD:1::3'],
                                            'seq_number': 0,
                                            'stale': False,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
