# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.
expected_output = {
        'evi': {
            1: {
                'bd_id': {
                    11: {
                        'ip_addr': {
                            'FE80::250:56FF:FEA9:F5AF': {
                                'mac_addr': {
                                    '0050.56a9.f5af': {
                                        'next_hops': [
                                            '11.11.11.2'
                                        ]
                                    }
                                }
                            },
                            'FE80::B6A8:B9FF:FE02:32D6': {
                                'mac_addr': {
                                    'b4a8.b902.32d6': {
                                        'next_hops': [
                                            'Gi1/0/3:11'
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