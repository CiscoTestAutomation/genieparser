expected_output = {
    'route_map': {
        'TC4-PBR-V6-A': {
            'cg_id': {
                5: {
                    'is_cgm_attach': 'Yes',
                    'protocol': 'IPv6',
                    'ref_cnt': 3,
                    'sequence_list': {
                        13: {
                            'adj_id': '0xf8004827',
                            'ip_addr': '2001:db8:10::2',
                            'seq_num': 10,
                            'table_id': 0,
                            'vrf_id': 0,
                        },
                        14: {
                            'adj_id': '0xf8004837',
                            'ip_addr': '2001:db8:20::2',
                            'seq_num': 20,
                            'table_id': 0,
                            'vrf_id': 0,
                        },
                        15: {
                            'adj_id': '0x0',
                            'ip_addr': '::',
                            'seq_num': 30,
                            'table_id': 0,
                            'vrf_id': 0,
                        },
                    },
                },
            },
        },
    },
}
