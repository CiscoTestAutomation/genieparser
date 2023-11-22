expected_output = {
    'HundredGigE1/0/3': {
        'service_policy': {
            'input': {
                'policy_name': {
                    '2r3c': {
                        'class_map': {
                            'cm-dscp6': {
                                'match': ['dscp ''6'],
                                'match_evaluation': 'match-all',
                                'packets': 66561970,
                                'police': {
                                    'cir_bc_bytes': 62500000,
                                    'cir_bps': 2000000000,
                                    'conformed': {
                                        'actions': {
                                            'transmit': True
                                            },
                                        'bps': 472689000,
                                        'bytes': 22027975000
                                        },
                                    'exceeded': {
                                        'actions': {
                                            'set_dscp_transmit': 'dscp ' 'table ''tb1'
                                            },
                                        'bps': 472651000,
                                        'bytes': 22025930000
                                        },
                                    'pir_be_bytes': 125000000,
                                    'pir_bps': 4000000000,
                                    'violated': {
                                        'actions': {
                                            'set_dscp_transmit': 'dscp table tb2'
                                        },
                                        'bps': 6196321000,
                                        'bytes': 288755945000
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



