expected_output = {
    'ipv4_add': {
        '5.5.5.2/32': {
            'child': {
                'child_adj': {
                    'dstmac': 'a0f8.4910.ab57',
                    'ether_type': '0x8',
                    'iif_id': '0x553',
                    'nh_type': 'NHADJ_NORMAL',
                    'objid': 101,
                    'srcmac': 'f87a.4125.2f02'
                },
                'child_npd': {
                    'child_device': 0,
                    'child_fec_oid': 1454,
                    'cr_def': 0,
                    'l3port_valid': 1,
                    'nh_gid': 10,
                    'nh_oid': 1449,
                    'old_gid': 0,
                    'old_oid': 0,
                    'parent_oid': 2143,
                    'stale': 0,
                    'was_nor_nh': 1
                },
                'child_sdk': {
                    'cla_nhtype': 0
                }
            },
            'da': 1,
            'ipv4route_id': '0x5b36201934b8',
            'npd': {
                'api_type': 'host(1)',
                'device': 0,
                'lspa_rec': 0
            },
            'obj_id': 101,
            'obj_name': 'IPNEXTHOP_ID',
            'tblid': 2
        }
    }
}