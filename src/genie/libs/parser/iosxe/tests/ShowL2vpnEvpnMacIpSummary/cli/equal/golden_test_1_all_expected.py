# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'entry': {
        1: {
            11: {
                0: {
                    'remote_count': 4,
                    'local_count': 5,
                    'dup_count': 1,
                },
            },
        },
        2: {
            12: {
                0: {
                    'remote_count': 2,
                    'local_count': 2,
                    'dup_count': 0,
                },
            },
        },
    },
    'total': {
        'remote_count': 6,
        'local_count': 7,
        'dup_count': 1,
    },
}
