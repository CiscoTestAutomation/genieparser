# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        1: {
            'bd_id': {
                11: {
                    'eth_tag': {
                        0: {
                            'dup_count': 1,
                        },
                    },
                },
            },
        },
        2: {
            'bd_id': {
                12: {
                    'eth_tag': {
                        0: {
                            'dup_count': 0,
                        },
                    },
                },
            },
        },
    },
    'total': {
        'dup_count': 1,
    },
}
