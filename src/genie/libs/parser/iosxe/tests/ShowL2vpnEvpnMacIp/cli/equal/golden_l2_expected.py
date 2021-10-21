# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        1: {
            'bd_id': {
                11: {
                    'ip_addr': {
                        '192.168.11.12': {
                            'mac_addr': {
                                'aabb.0011.0002': {
                                    'next_hops': [
                                        '2.2.2.1',
                                    ]
                                }
                            }
                        },
                        '2001:11::12': {
                            'mac_addr': {
                                'aabb.0011.0002': {
                                    'next_hops': [
                                        '2.2.2.1',
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
