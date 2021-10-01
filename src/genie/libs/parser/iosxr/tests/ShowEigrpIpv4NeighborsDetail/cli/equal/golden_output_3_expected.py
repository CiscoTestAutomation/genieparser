

expected_output = {
    'eigrp_instance': {
        '100': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv6': {
                            'name': 'test',
                            'named_mode': True,
                            'eigrp_interface': {
                                'GigabitEthernet0/0/0/1.90': {
                                    'eigrp_nbr': {
                                        'fe80::5c00:ff:fe02:7': {
                                            'peer_handle': 1,
                                            'hold': 13,
                                            'uptime': '01:37:57',
                                            'srtt': 0.011,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 28,
                                            'nbr_sw_ver': {
                                                'os_majorver': 8,
                                                'os_minorver': 0,
                                                'tlv_majorrev': 1,
                                                'tlv_minorrev': 2
                                            },
                                            'retransmit_count': 1,
                                            'retry_count': 0,
                                            'bfd': 'disabled',
                                            'prefixes': 5
                                        }
                                    }
                                },
                                'GigabitEthernet0/0/0/0.90': {
                                    'eigrp_nbr': {
                                        'fe80::f816:3eff:feb4:b131': {
                                            'peer_handle': 0,
                                            'hold': 12,
                                            'uptime': '02:31:58',
                                            'srtt': 0.001,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 23,
                                            'nbr_sw_ver': {
                                                'os_majorver': 23,
                                                'os_minorver': 0,
                                                'tlv_majorrev': 2,
                                                'tlv_minorrev': 0
                                            },
                                            'retransmit_count': 1,
                                            'retry_count': 0,
                                            'bfd': 'disabled',
                                            'prefixes': 6
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
