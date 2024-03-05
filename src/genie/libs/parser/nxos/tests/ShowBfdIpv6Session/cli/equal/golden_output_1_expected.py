expected_output = {
    'vrf': {
        'default': {
            'our_address': {
                '2001:db8:10::1': {
                    'neighbor_address': {
                        '2001:db8:10::2': {
                            'holdown_timer': '6000',
                            'holdown_timer_multiplier': 3,
                            'interface': 'Ethernet1/33',
                            'ld_rd': '1090519056/1090519047',
                            'rh_rs': 'Up',
                            'state': 'Up',
                            'type': 'SH',
                            'vrf': 'default'
                        }
                    }
                },
                '2001:db8:12::1': {
                    'neighbor_address': {
                        '2001:db8:12::2': {
                            'holdown_timer': '6000',
                            'holdown_timer_multiplier': 3,
                            'interface': 'Ethernet1/35',
                            'ld_rd': '1090519054/1090519043',
                            'rh_rs': 'Up',
                            'state': 'Up',
                            'type': 'SH',
                            'vrf': 'default'
                        }
                    }
                },
                'fe80::1': {
                    'neighbor_address': {
                        'fe80::2': {
                            'holdown_timer': '150',
                            'holdown_timer_multiplier': 3,
                            'interface': 'Ethernet1/34',
                            'ld_rd': '1090519058/1090519045',
                            'rh_rs': 'Up',
                            'state': 'Up',
                            'type': 'SH',
                            'vrf': 'default'
                        }
                    }
                }
            }
        }
    }
}
