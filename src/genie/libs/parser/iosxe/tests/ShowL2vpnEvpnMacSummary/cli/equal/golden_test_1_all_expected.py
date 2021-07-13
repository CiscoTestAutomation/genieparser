# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'evi': {
        1: {
            'bd_id': {
                11: {
                    'eth_tag': {
                        0: {
                            'remote_count': 4,
                            'local_count': 6,
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
                            'remote_count': 2,
                            'local_count': 2,
                            'dup_count': 0,
                        },
                    },
                },
            },
        },
    },
    'total': {
        'remote_count': 6,
        'local_count': 8,
        'dup_count': 1,
    },
}
