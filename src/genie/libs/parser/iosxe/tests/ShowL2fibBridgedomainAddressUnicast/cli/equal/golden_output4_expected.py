# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
        'mac_addr': '000a.000a.000a',
        'reference_count': 1,
        'epoch': 0,
        'producer': 'BD-ENG',
        'flags': ['Age out', 'CP Learn', 'Flood Mac'],
        'adjacency': {
            'type': 'VXLAN_CP',
            'desc': 'L:20011:1.1.1.1 R:20012:2.2.2.2'
        },
        'pd_adjacency': {
            'type': 'VXLAN_CP',
            'desc': 'L:20011:1.1.1.1 R:20012:2.2.2.2'
        },
        'packet_count': 0,
        'bytes': 0
    }