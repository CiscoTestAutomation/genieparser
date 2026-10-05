expected_output = {
    'route_map': {
        'TC1-PBR-A': {
            'cg_id': {
                1: {
                    'is_cgm_attach': 'Yes',
                    'protocol': 'IPv4',
                    'ref_cnt': 3,
                    'sequence_list': {
                        1: {
                            'adj_id': '0xf8004836',
                            'ip_addr': '10.1.1.2',
                            'seq_num': 10,
                            'table_id': 0,
                            'vrf_id': 0,
                        },
                        2: {
                            'adj_id': '0x0',
                            'ip_addr': '0.0.0.0',
                            'seq_num': 20,
                            'table_id': 0,
                            'vrf_id': 0,
                        },
                        3: {
                            'adj_id': '0x0',
                            'ip_addr': '0.0.0.0',
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
