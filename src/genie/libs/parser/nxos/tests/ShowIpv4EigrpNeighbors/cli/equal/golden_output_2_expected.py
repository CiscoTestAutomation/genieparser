

expected_output = {
    'eigrp_instance': {
        '100': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv6': {
                            'eigrp_interface': {
                                'Ethernet1/1.90': {
                                    'eigrp_nbr': {
                                        'fe80::f816:3eff:fecf:5a5b': {
                                            'peer_handle': 0,
                                            'hold': 12,
                                            'uptime': '01:40:09',
                                            'srtt': 0.010,
                                            'rto': 60,
                                            'q_cnt': 0,
                                            'last_seq_number': 30}}},
                                'Ethernet1/2.90': {
                                    'eigrp_nbr': {
                                        'fe80::f816:3eff:fe62:65af': {
                                            'peer_handle': 1,
                                            'hold': 12,
                                            'uptime': '01:40:07',
                                            'srtt': 0.004,
                                            'rto': 50,
                                            'q_cnt': 0,
                                            'last_seq_number': 22}}}}}}},
                'VRF1': {
                    'address_family': {
                        'ipv6': {
                            'eigrp_interface': {
                                'Ethernet1/1.390': {
                                    'eigrp_nbr': {
                                        'fe80::f816:3eff:fecf:5a5b': {
                                            'peer_handle': 0,
                                            'hold': 10,
                                            'uptime': '01:44:27',
                                            'srtt': 0.010,
                                            'rto': 60,
                                            'q_cnt': 0,
                                            'last_seq_number': 10
                                        }
                                    }
                                },
                                'Ethernet1/2.390': {
                                    'eigrp_nbr': {
                                        'fe80::f816:3eff:fe62:65af': {
                                            'peer_handle': 1,
                                            'hold': 13,
                                            'uptime': '01:43:38',
                                            'srtt': 0.004,
                                            'rto': 50,
                                            'q_cnt': 0,
                                            'last_seq_number': 8 }}}}}}}}}}}
