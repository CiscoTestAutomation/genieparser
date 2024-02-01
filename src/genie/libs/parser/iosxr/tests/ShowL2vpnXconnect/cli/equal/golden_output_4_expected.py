

expected_output = {
    'groups': {
        'genie_wqst': {
            'name': {
                'wsq_wqxt_ups2_cm2_21314': {
                    'status': 'UR',
                    'segment1': {
                        'Bundle-Ether2.61': {
                            'status': 'UR',
                            'segment2': {
                                'EVPN 21314,31314,10.4.1.1': {
                                    'status': 'DN',
                                },
                            },
                        },
                    },
                },
            },
        },
        'genie_CM-QF-CF': {
            'name': {
                'G2-2-2-34-422': {
                    'status': 'UP',
                    'segment1': {
                        'GigabitEthernet2/2/2/34.422': {
                            'status': 'UP',
                            'segment2': {
                                'EVPN 3223,4112,10.1.21.93': {
                                    'status': 'UP',
                                },
                            },
                        },
                    },
                },
            },
        },
        'genie_CM-3-EDQF': {
            'name': {
                'G2-2-2-34-322': {
                    'status': 'UP',
                    'segment1': {
                        'GigabitEthernet2/2/2/34.322': {
                            'status': 'UP',
                            'segment2': {
                                '10.154.219.82    9593211': {
                                    'status': 'UP',
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
