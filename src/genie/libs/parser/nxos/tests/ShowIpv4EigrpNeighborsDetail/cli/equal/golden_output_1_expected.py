

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
                                            'hold': 14,
                                            'uptime': '01:58:11',
                                            'srtt': 0.001,
                                            'rto': 50,
                                            'q_cnt': 0,
                                            'last_seq_number': 16,
                                            'nbr_sw_ver': {
                                                'os_majorver': 23,
                                                'os_minorver': 0,
                                                'tlv_majorrev': 2,
                                                'tlv_minorrev': 0
                                            },
                                            'retransmit_count': 1,
                                            'retry_count': 0,
                                            'bfd_state': 'N/A',
                                            'prefixes': 3, }, }, },
                                'Ethernet1/1.90': {
                                    'eigrp_nbr': {
                                        '10.23.90.2': {
                                            'peer_handle': 0,
                                            'hold': 13,
                                            'uptime': '01:47:34',
                                            'srtt': 0.015,
                                            'rto': 90,
                                            'q_cnt': 0,
                                            'last_seq_number': 22,
                                            'nbr_sw_ver': {
                                                'os_majorver': 3,
                                                'os_minorver': 3,
                                                'tlv_majorrev': 2,
                                                'tlv_minorrev': 0
                                            },
                                            'retransmit_count': 1,
                                            'retry_count': 0,
                                            'bfd_state': 'N/A',
                                            'prefixes': 3}}}}}}},
                'VRF1': {
                    'address_family': {
                        'ipv4': {
                            'eigrp_interface': {
                                'Ethernet1/2.390': {
                                    'eigrp_nbr': {
                                        '10.13.90.1': {
                                            'peer_handle': 1,
                                            'hold': 14,
                                            'uptime': '01:44:45',
                                            'srtt': 0.001,
                                            'rto': 50,
                                            'q_cnt': 0,
                                            'last_seq_number': 7,
                                            'nbr_sw_ver': {
                                                'os_majorver': 23,
                                                'os_minorver': 0,
                                                'tlv_majorrev': 2,
                                                'tlv_minorrev': 0
                                            },
                                            'retransmit_count': 1,
                                            'retry_count': 0,
                                            'bfd_state': 'N/A',
                                            'prefixes': 3}, }, },
                                'Ethernet1/1.390': {
                                    'eigrp_nbr': {
                                        '10.23.90.2': {
                                            'peer_handle': 0,
                                            'hold': 14,
                                            'uptime': '01:45:34',
                                            'srtt': 0.01,
                                            'rto': 60,
                                            'q_cnt': 0,
                                            'last_seq_number': 9,
                                            'nbr_sw_ver': {
                                                'os_majorver': 3,
                                                'os_minorver': 3,
                                                'tlv_majorrev': 2,
                                                'tlv_minorrev': 0
                                            },
                                            'retransmit_count': 1,
                                            'retry_count': 0,
                                            'bfd_state': 'N/A',
                                            'prefixes': 3}}}}}}}}}}}
