expected_output = {
    'Vif1': {
        1: {
            'name': 'Vif1',
            'if_handle': 5997,
            'rep_cnt': 1,
            'hash_val': 10,
            'prefix': '33.0.0.0/24',
            1: {
                'src_filter': '66.1.1.0/24',
                'trans_src': '122.2.2.0',
                'trans_dst': '233.23.2.0/24',
                'octets': 0,
                'pkts': 0,
            }
        },
        2: {
            'name': 'Vif1',
            'if_handle': 5997,
            'rep_cnt': 1,
            'hash_val': 4,
            'prefix': '200.0.0.0/24',
            1: {
                'trans_src': '100.1.1.1',
                'trans_dst': '225.225.225.0/24',
                'octets': 0,
                'pkts': 0,
            }
        },
        3: {
            'name': 'Vif1',
            'if_handle': 5997,
            'ingress_name': 'GigabitEthernet5',
            'ingress_hdl': 10,
            'rep_cnt': 2,
            'hash_val': 2,
            'prefix': '66.0.0.7/32',
            1: {
                'trans_src': '10.1.1.3',
                'trans_dst': '239.4.4.0/32',
                'octets': 0,
                'pkts': 0,
            },
            2: {
                'trans_src': '10.1.1.2',
                'trans_dst': '239.3.3.0/32',
                'octets': 0,
                'pkts': 0,
            }
        }
    }
}
