

expected_output = {
    'eigrp_instance': {
        '100': {
            'vrf': {
                'VRF1': {
                    'address_family': {
                        'ipv4': {
                            'name': 'test',
                            'named_mode': True,
                            'eigrp_interface': {
                                'GigabitEthernet0/0/0/1.390': {
                                    'eigrp_nbr': {
                                        '10.23.90.3': {
                                            'peer_handle': 1,
                                            'hold': 14,
                                            'uptime': '01:41:47',
                                            'srtt': 0.004,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 15,
                                            'nbr_sw_ver': {
                                                'os_majorver': 8,
                                                'os_minorver': 0,
                                                'tlv_majorrev': 1,
                                                'tlv_minorrev': 2
                                            },
                                            'retransmit_count': 1,
                                            'retry_count': 0,
                                            'bfd': 'disabled',
                                            'prefixes': 3
                                        }
                                    }
                                },
                                'GigabitEthernet0/0/0/0.390': {
                                    'eigrp_nbr': {
                                        '10.12.90.1': {
                                            'peer_handle': 0,
                                            'hold': 13,
                                            'uptime': '02:54:01',
                                            'srtt': 0.816,
                                            'rto': 4896,
                                            'q_cnt': 0,
                                            'last_seq_number': 8,
                                            'nbr_sw_ver': {
                                                'os_majorver': 23,
                                                'os_minorver': 0,
                                                'tlv_majorrev': 2,
                                                'tlv_minorrev': 0
                                            },
                                            'retransmit_count': 0,
                                            'retry_count': 0,
                                            'bfd': 'disabled',
                                            'prefixes': 3
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
