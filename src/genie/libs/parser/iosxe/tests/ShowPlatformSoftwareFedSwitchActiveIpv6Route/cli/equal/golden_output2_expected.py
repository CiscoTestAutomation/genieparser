expected_output = {
    'index': {
        1: {
            'ipv6_addr': 'fe80::',
            'mask_len': 10,
            'object_id': '0x560a323ae7d8',
            'parent_object_id': '0x0',
            'parent_type': 'RECV',
            'sgt': 0,
        },
        2: {
            'ipv6_addr': '::',
            'mask_len': 127,
            'object_id': '0x560a323ae6e8',
            'parent_object_id': '0x0',
            'parent_type': 'DROP',
            'sgt': 0,
        },
        3: {
            'ipv6_addr': '::',
            'mask_len': 0,
            'object_id': '0x560a323ab7e8',
            'parent_object_id': '0x0',
            'parent_type': 'DROP',
            'sgt': 0,
        },
    },
    'number_of_npi_ipv6route_entries': 3,
}
