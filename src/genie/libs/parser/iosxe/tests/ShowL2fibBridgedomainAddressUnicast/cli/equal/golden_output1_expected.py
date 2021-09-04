# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.

expected_output = {
        'mac_addr': 'aabb.0000.0002',
        'reference_count': 1,
        'epoch': 0,
        'producer': 'BGP',
        'flags': ['None'],
        'adjacency': {
            'type': 'MPLS_UC',
            'desc': 'PL:5(1) T:MPLS_UC [MAC]16@2.2.2.1',
            'path_list': {
                'path_list_id': 5,
                'path_list_count': 1,
                'path_list_type': 'MPLS_UC',
                'path_list_desc': '[MAC]16@2.2.2.1'
            }
        },
        'pd_adjacency': {
            'type': 'MPLS_UC',
            'desc': 'PL:5(1) T:MPLS_UC [MAC]16@2.2.2.1',
            'path_list': {
                'path_list_id': 5,
                'path_list_count': 1,
                'path_list_type': 'MPLS_UC',
                'path_list_desc': '[MAC]16@2.2.2.1'
            }
        },
        'packet_count': 0,
        'bytes': 0
    }