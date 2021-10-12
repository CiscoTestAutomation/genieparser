# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        1: {
            'bd_id': {
                11: {
                    'eth_tag': {
                        0: {
                            'ip_addr': {
                                '192.168.11.12': {
                                    'mac_addr': {
                                        'aabb.0011.0002': {
                                            'stale': False,
                                            'esi': '0000.0000.0000.0000.0000',
                                            'next_hops': [
                                                'V:16 2.2.2.1',
                                            ],
                                            'local_addr': '1.1.1.1',
                                            'seq_number': 0,
                                            'ip_dup_detection': {
                                                'status': 'Timer not running',
                                            },
                                            'label2_included': 'No',
                                        }
                                    }
                                },
                                '2001:11::12': {
                                    'mac_addr': {
                                        'aabb.0011.0002' : {
                                            'stale': False,
                                            'esi': '0000.0000.0000.0000.0000',
                                            'next_hops': [
                                                'V:16 2.2.2.1',
                                            ],
                                            'local_addr': '1.1.1.1',
                                            'seq_number': 0,
                                            'ip_dup_detection': {
                                                'status': 'Timer not running',
                                            },
                                            'label2_included': 'No',
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
