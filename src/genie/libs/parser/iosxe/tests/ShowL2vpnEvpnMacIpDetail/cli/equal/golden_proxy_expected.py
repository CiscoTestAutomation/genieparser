# Copyright (c) 2024 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        11: {
            'bd_id': {
                11: {
                    'eth_tag': {
                        0: {
                            'ip_addr': {
                                '192.168.11.55': {
                                    'mac_addr': {
                                        'aaaa.bbbb.0055': {
                                            'stale': False,
                                            'esi': '03AA.AABB.BBCC.CC00.0001',
                                            'next_hops': [
                                                'V:20011 Ethernet0/1 service instance 11',
                                                'V:20011 2.2.2.2 (proxy)'
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
                                '192.168.11.56': {
                                    'mac_addr': {
                                        'aaaa.bbbb.0055': {
                                            'stale': False,
                                            'esi': '03AA.AABB.BBCC.CC00.0001',
                                            'next_hops': [
                                                'V:20011 Ethernet0/1 service instance 11 (proxy)',
                                                'V:20011 1.1.1.1'
                                            ],
                                            'local_addr': '2.2.2.2',
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
