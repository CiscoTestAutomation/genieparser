expected_output = {
    'ipv4_add': {
        '127.0.0.0/8': {
            'SPECIAL_IPNEXTHOP_ID': {
                'ipnexthop_obj_id': 0
            },
            'da': 0,
            'ipv4route_id': '0x5b36200364c8',
            'npd': {
                'api_type': 'route(3)',
                'asic': 0,
                'device': 0,
                'devid': 0,
                'lspa_rec': 0,
                'sdk_oid': 535
            },
            'obj_id': 0,
            'obj_name': 'NHADJ_DROP',
            'sdk': {
                'is_host': 0,
                'l3_dest_id': '0x777838c13f80',
                'l3_dest_name': 'la_next_hop_base(oid=535)',
                'vrf_gid': 2,
                'vrf_oid': 697
            },
            'sdk_nexthop': {
                'dev': 0,
                'gid': '0x3',
                'macaddr': '0000.0000.0000',
                'nh_type': 'drop(3)',
                'oid': 535
            },
            'tblid': 2
        }
    }
}