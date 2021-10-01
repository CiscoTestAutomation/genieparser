

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
                                            'hold': 12,
                                            'uptime': '01:36:14',
                                            'srtt': 0.011,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 28
                                        }
                                    }
                                },
                                'GigabitEthernet0/0/0/0.90': {
                                    'eigrp_nbr': {
                                        'fe80::f816:3eff:feb4:b131': {
                                            'peer_handle': 0,
                                            'hold': 11,
                                            'uptime': '02:30:16',
                                            'srtt': 0.001,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 23
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
