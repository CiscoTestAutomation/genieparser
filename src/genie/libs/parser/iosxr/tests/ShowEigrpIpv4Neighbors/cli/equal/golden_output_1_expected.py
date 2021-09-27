

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
                                            'hold': 13,
                                            'uptime': '01:41:56',
                                            'srtt': 0.013,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 23
                                        }
                                    }
                                },
                                'GigabitEthernet0/0/0/0.90': {
                                    'eigrp_nbr': {
                                        '10.12.90.1': {
                                            'peer_handle': 0,
                                            'hold': 14,
                                            'uptime': '02:55:10',
                                            'srtt': 0.001,
                                            'rto': 200,
                                            'q_cnt': 0,
                                            'last_seq_number': 17
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
