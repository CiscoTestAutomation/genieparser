# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        2: {
            'bd_id': {
                12: {
                    'ip_addr': {
                        '192.168.12.3': {
                            'mac_addr': {
                                'aabb.cc82.2800': {
                                    'next_hops': [
                                        'Et1/0:12',
                                        '3.3.3.1',
                                        '5.5.5.1',
                                    ]
                                }
                            }
                        },
                        '2001:12::3': {
                            'mac_addr': {
                                'aabb.cc82.2800': {
                                    'next_hops': [
                                            'Et1/0:12',
                                            '3.3.3.1',
                                            '5.5.5.1',
                                        ]
                                }
                            }
                        },
                        'FE80::A8BB:FF:FE12:2': {
                            'mac_addr': {
                                'aabb.0012.0002': {
                                    'next_hops': [
                                        '2.2.2.1',
                                    ]
                                }
                            }
                        },
                        'FE80::A8BB:CCFF:FE82:2800': {
                            'mac_addr': {
                                'aabb.cc82.2800': {
                                    'next_hops': [
                                        'Et1/0:12',
                                        '3.3.3.1',
                                        '5.5.5.1',
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
