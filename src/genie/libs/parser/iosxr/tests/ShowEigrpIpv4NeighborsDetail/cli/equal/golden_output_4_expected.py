

expected_output = {
    'eigrp_instance': {
        '100': {
            'vrf': {
                'VRF1': {
                    'address_family': {
                        'ipv6': {
                            'name': 'test',
                            'named_mode': True,
                            'eigrp_interface': {
                                'GigabitEthernet0/0/0/1.390': {
                                    'eigrp_nbr': {
                                        'fe80::5c00:ff:fe02:7': {
                                            'peer_handle': 1,
                                            'hold': 11,
                                            'uptime': '01:42:44',
                                            'srtt': 0.009,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 14,
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
                                'GigabitEthernet0/0/0/0.390': {
                                    'eigrp_nbr': {
                                        'fe80::f816:3eff:feb4:b131': {
                                            'peer_handle': 0,
                                            'hold': 12,
                                            'uptime': '02:31:47',
                                            'srtt': 0.004,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 9,
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
