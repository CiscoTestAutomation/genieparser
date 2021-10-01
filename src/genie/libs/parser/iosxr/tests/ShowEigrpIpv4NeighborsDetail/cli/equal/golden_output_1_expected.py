

expected_output = {
    'eigrp_instance': {
        '100': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv4': {
                            'name': 'test',
                            'named_mode': True,
                            'eigrp_interface': {
                                'GigabitEthernet0/0/0/1.90': {
                                    'eigrp_nbr': {
                                        '10.23.90.3': {
                                            'peer_handle': 1,
                                            'hold': 11,
                                            'uptime': '01:43:15',
                                            'srtt': 0.013,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 23,
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
                                'GigabitEthernet0/0/0/0.90': {
                                    'eigrp_nbr': {
                                        '10.12.90.1': {
                                            'peer_handle': 0,
                                            'hold': 14,
                                            'uptime': '02:56:28',
                                            'srtt': 0.001,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 17,
                                            'nbr_sw_ver': {
                                                'os_majorver': 23,
                                                'os_minorver': 0,
                                                'tlv_majorrev': 2,
                                                'tlv_minorrev': 0
                                            },
                                            'retransmit_count': 1,
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
