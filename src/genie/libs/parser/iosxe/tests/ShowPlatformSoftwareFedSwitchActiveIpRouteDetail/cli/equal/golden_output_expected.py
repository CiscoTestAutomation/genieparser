expected_output = {
    'ipv4_add': {
        '2.2.2.3/32': {
            'ipv4route_id': '0x5a4d1cf0f4d8',
            'obj_name': 'IPNEXTHOP_ID',
            'obj_id': '0x40',
            'tblid': 0,
            'da': 1,
            'state': 'success',
            'mac_addr': '00a7.429b.db7f',
            'l3port_oid': '0x6e6',
            'adj': {
                'objid': '0x40',
                'nh_type': 'NHADJ_NORMAL',
                'ipv4_addr': '2.2.2.3',
                'iif_id': '0x553',
                'ether_type': '0x8',
                'srcmac': '40b5.c1ff.d902',
                'dstmac': '00a7.429b.db7f'
            },
            'npd': {
                'child_device': 0,
                'nh_gid': 8,
                'nh_oid': '0x466',
                'old_gid': 0,
                'old_oid': '0x0',
                'parent_oid': '0x6e6'
            },
            'cla_nhtype': 0
        }
    }
}