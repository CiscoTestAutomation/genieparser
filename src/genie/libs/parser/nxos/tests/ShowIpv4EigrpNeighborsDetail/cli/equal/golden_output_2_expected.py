

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
                                            'uptime': '01:41:31',
                                            'srtt': 0.010,
                                            'rto': 60,
                                            'q_cnt': 0,
                                            'last_seq_number': 30,
                                            'nbr_sw_ver': {
                                                'os_majorver': 3,
                                                'os_minorver': 3,
                                                'tlv_majorrev': 2,
                                                'tlv_minorrev': 0
                                            },
                                            'retransmit_count': 1,
                                            'retry_count': 0,
                                            'bfd_state': 'N/A',
                                            'prefixes': 0
                                        }
                                    }
                                },
                                'Ethernet1/2.90': {
                                    'eigrp_nbr': {
                                        'fe80::f816:3eff:fe62:65af': {
                                            'peer_handle': 1,
                                            'hold': 12,
                                            'uptime': '01:41:30',
                                            'srtt': 0.004,
                                            'rto': 50,
                                            'q_cnt': 0,
                                            'last_seq_number': 22,
                                            'nbr_sw_ver': {
                                                'os_majorver': 23,
                                                'os_minorver': 0,
                                                'tlv_majorrev': 2,
                                                'tlv_minorrev': 0
                                            },
                                            'retransmit_count': 0,
                                            'retry_count': 0,
                                            'bfd_state': 'N/A',
                                            'prefixes': 0}}}}}}},
                'VRF1': {
                    'address_family': {
                        'ipv6': {
                            'eigrp_interface': {
                                'Ethernet1/1.390': {
                                    'eigrp_nbr': {
                                        'fe80::f816:3eff:fecf:5a5b': {
                                            'peer_handle': 0,
                                            'hold': 11,
                                            'uptime': '01:45:50',
                                            'srtt': 0.010,
                                            'rto': 60,
                                            'q_cnt': 0,
                                            'last_seq_number': 10,
                                            'nbr_sw_ver': {
                                                'os_majorver': 3,
                                                'os_minorver': 3,
                                                'tlv_majorrev': 2,
                                                'tlv_minorrev': 0
                                            },
                                            'retransmit_count': 2,
                                            'retry_count': 0,
                                            'bfd_state': 'N/A',
                                            'prefixes': 0
                                        }
                                    }
                                },
                                'Ethernet1/2.390': {
                                    'eigrp_nbr': {
                                        'fe80::f816:3eff:fe62:65af': {
                                            'peer_handle': 1,
                                            'hold': 14,
                                            'uptime': '01:45:01',
                                            'srtt': 0.004,
                                            'rto': 50,
                                            'q_cnt': 0,
                                            'last_seq_number': 8,
                                            'nbr_sw_ver': {
                                                'os_majorver': 23,
                                                'os_minorver': 0,
                                                'tlv_majorrev': 2,
                                                'tlv_minorrev': 0
                                            },
                                            'retransmit_count': 1,
                                            'retry_count': 0,
                                            'bfd_state': 'N/A',
                                            'prefixes': 0}}}}}}}}}}}
