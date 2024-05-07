expected_output = {
    'switch': {
        '1': {
            'test': {
                'mbist_tests': {
                    'status': True
                },
                'phy_loopback:_loopback_test': {
                    'module': {
                        '1': {
                            'status': True
                        },
                        '2': {
                            'status': True
                        },
                        '4': {
                            'status': True
                        }
                    }
                }
            }
        },
        '2': {
            'test': {
                'mbist_tests': {
                    'status': True
                },
                'phy_loopback:_loopback_test': {
                    'module': {
                        '1': {
                            'status': True
                        },
                        '2': {
                            'status': False
                        },
                        '4': {
                            'status': True
                        }
                    }
                }
            }
        }
    }
}
