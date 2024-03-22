expected_output = {
    'ipv4_add': {
        '0.0.0.0/0': {
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
            'da': 0,
            'ipv4route_id': '0x5b3620034e48',
            'npd': {
                'api_type': 'route(3)',
                'asic': 0,
                'device': 0,
                'devid': 0,
                'lspa_rec': 0,
                'sdk_oid': 1454
            },
            'obj_id': 101,
            'obj_name': 'IPNEXTHOP_ID',
            'sdk': {
                'is_host': 0,
                'l3_dest_id': '0x62faa7b15ba0',
                'l3_dest_name': 'la_l3_fec_impl_base(oid=1454)',
                'vrf_gid': 2,
                'vrf_oid': 697
            },
            'sdk_fec_dest': {
                'dest_type': '4b',
                'sdk_dev': 0,
                'sdk_oid': 1449
            },
            'sdk_nexthop': {
                'dev': 0,
                'gid': '0xa',
                'macaddr': 'a0f8.4910.ab57',
                'nh_type': 'normal(0)',
                'oid': 1449
            },
            'sdk_outgoing_port': {
                'out_oid': 2143,
                'porttype': 'svi(104)'
            },
            'tblid': 2
        }
    }
}