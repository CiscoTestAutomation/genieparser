expected_output = {
    'pid': 5,
    'address_family': 'ipv6',
    'router_id': '1.1.1.1',
    'area': 0,
    'spf_alg_executed_times': 1,
    'spf': {
        '1': {
            'executed_time': '16:03:11',
            'spf_type': 'Full',
            'spt': 0,
            'sum': 0,
            'ext': 0,
            'total': 0,
            'prefix': 0,
            'd_sum': 0,
            'd_ext': 0,
            'd_int': 0,
            'lsids': {
                'r': 1,
                'n': 0,
                'prefix': 0,
                'sn': 0,
                'sa': 0,
                'x7': 0
            },
            'lsa_changed': 1,
            'change_record': 'R',
            'adv_routers_list': ['1.1.1.1/0(R)'],
        }
    }
}