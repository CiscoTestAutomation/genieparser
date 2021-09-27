

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
                                        'fe80::5c00:ff:fe02:': {
                                            'peer_handle': 1,
                                            'hold': 12,
                                            'uptime': '01:40:51',
                                            'srtt': 0.009,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 14
                                        }
                                    }
                                },
                                'GigabitEthernet0/0/0/0.390': {
                                    'eigrp_nbr': {
                                        'fe80::f816:3eff:feb4:b131': {
                                            'peer_handle': 0,
                                            'hold': 12,
                                            'uptime': '02:29:54',
                                            'srtt': 0.004,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 9
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
