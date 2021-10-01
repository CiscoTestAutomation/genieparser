

expected_output = {
    'eigrp_instance': {
        '100': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv4': {
                            'eigrp_interface': {
                                'Ethernet1/2.90': {
                                    'eigrp_nbr': {
                                        '10.13.90.1': {
                                            'peer_handle': 1,
                                            'hold': 13,
                                            'uptime': '01:56:49',
                                            'srtt': 0.001,
                                            'rto': 50,
                                            'q_cnt': 0,
                                            'last_seq_number': 16, }}},
                                'Ethernet1/1.90': {
                                    'eigrp_nbr': {
                                        '10.23.90.2': {
                                            'peer_handle': 0,
                                            'hold': 11,
                                            'uptime': '01:46:12',
                                            'srtt': 0.015,
                                            'rto': 90,
                                            'q_cnt': 0,
                                            'last_seq_number': 22, }}}}}}},
                'VRF1': {
                    'address_family': {
                        'ipv4': {
                            'eigrp_interface': {
                                'Ethernet1/2.390': {
                                    'eigrp_nbr': {
                                        '10.13.90.1': {
                                            'peer_handle': 1,
                                            'hold': 13,
                                            'uptime': '01:43:23',
                                            'srtt': 0.001,
                                            'rto': 50,
                                            'q_cnt': 0,
                                            'last_seq_number': 7
                                        }
                                    }
                                },
                                'Ethernet1/1.390': {
                                    'eigrp_nbr': {
                                        '10.23.90.2': {
                                            'peer_handle': 0,
                                            'hold': 13,
                                            'uptime': '01:44:12',
                                            'srtt': 0.01,
                                            'rto': 60,
                                            'q_cnt': 0,
                                            'last_seq_number': 9, }}}}}}}}}}}
