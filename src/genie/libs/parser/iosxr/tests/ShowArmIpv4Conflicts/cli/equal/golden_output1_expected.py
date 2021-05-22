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
                        'Tunnel2': {
                            'due_to': 'Tunnel1',
                            'up_interface': {
                                'Tunnel1': {
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
