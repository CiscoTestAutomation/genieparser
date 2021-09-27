# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.
expected_output = {
    'evi': {
        1: {
            'bd_id': {
                11: {
                    'eth_tag': {
                        0 : {
                            'mac_addr':{
                                '0050.56a9.f5af': {
                                    'esi': '0000.0000.0000.0000.0000',
                                    'next_hops': [
                                        '11.11.11.2'
                                    ]
                                },
                                'b4a8.b902.32d6': {
                                    'esi': '0000.0000.0000.0000.0000',
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
