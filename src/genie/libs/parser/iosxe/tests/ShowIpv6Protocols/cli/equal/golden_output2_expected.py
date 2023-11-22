expected_output = {
    'protocols': {
        'isis': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv6': {
                            'instance': {
                                'sr': {
                                    'configured_interfaces': [
                                        'Loopback1', 'Ethernet2/0',
                                        'Ethernet2/1', 'Ethernet3/0',
                                        'Ethernet3/1', 'Ethernet4/0',
                                        'Ethernet4/1'
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        },
        'bgp': {
            'instance': {
                'default': {
                    'bgp_id': 65000,
                    'vrf': {
                        'default': {
                            'address_family': {
                                'ipv6': {
                                    'redistribute': {},
                                    'igp_sync': False
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}