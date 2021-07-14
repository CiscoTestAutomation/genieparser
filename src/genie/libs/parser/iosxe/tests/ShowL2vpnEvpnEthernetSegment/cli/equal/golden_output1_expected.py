# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
    'esi': {
        "03AA.AABB.BBCC.CC00.0001": {
            "port": "Ethernet0/2",
            "redundancy_mode": "single-active",
            "df_wait_time": 3,
            "split_horizon_label": 16,
        },
        "03AA.BBCC.DDEE.FF00.0002": {
            "port": "Ethernet0/3",
            "redundancy_mode": "all-active",
            "df_wait_time": 3,
            "split_horizon_label": 17,
        },
    }
}

