expected_output = {
    'vrf': {
        'Mgmt': {
            'unicast_configuration': {
                'address': {
                    '10.4.4.4': {
                        'type': {
                            'server': {
                                'address': '10.4.4.4',
                                'type': 'server',
                                'vrf': 'Mgmt',
                                'preferred': True,
                                'key_id': '5'
                            }
                        }
                    },
                    '10.3.3.3': {
                        'type': {
                            'server': {
                                'address': '10.3.3.3',
                                'type': 'server',
                                'vrf': 'Mgmt',
                                'key_id': '4'
                            }
                        }
                    },
                    '10.2.2.2': {
                        'type': {
                            'server': {
                                'address': '10.2.2.2',
                                'type': 'server',
                                'vrf': 'Mgmt',
                                'key_id': '3'
                            }
                        }
                    },
                    '10.1.1.1': {
                        'type': {
                            'server': {
                                'address': '10.1.1.1',
                                'type': 'server',
                                'vrf': 'Mgmt',
                                'key_id': '2'
                            }
                        }
                    }
                }
            }
        }
    }
}
