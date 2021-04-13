expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': { 
                    'forced_down': {
                        'F': {
                            'down_interface': {
                                'Loopback2': {
                                    'address': '10.1.1.2/24',
                                    'up_interface': {
                                        'Loopback1': {
                                            'address': '10.1.1.1/24'
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'unnumbered_down_interface': {
                        'Tu2': {
                            'due_to': 'Tu1',
                            'up_interface': {
                                'Tu1': {
                                    'due_to': 'Loopback1'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
