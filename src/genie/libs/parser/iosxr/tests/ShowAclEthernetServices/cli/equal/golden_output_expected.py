expected_output = {
            'eth_acl': {
                'name': 'eth_acl',
                'type': 'eth-acl-type',
                'aces': {
                    10: {
                        'name': '10',
                        'matches': {
                            'l2': {
                                'eth': {
                                    'destination_mac_address': 'any',
                                    'source_mac_address': 'any',
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            },
                        },
                    },
                },
            'mac_acl': {
                'name': 'mac_acl',
                'type': 'eth-acl-type',
                'aces': {
                    10: {
                        'name': '10',
                        'matches': {
                            'l2': {
                                'eth': {
                                    'destination_mac_address': 'host 0000.0000.0000',
                                    'source_mac_address': 'host 0000.0000.0000',
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            },
                        },
                    20: {
                        'name': '20',
                        'matches': {
                            'l2': {
                                'eth': {
                                    'destination_mac_address': 'host 0000.0000.0000',
                                    'source_mac_address': 'host 0000.0000.0000',
                                    'ether_type': '8041',
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'deny',
                            },
                        },
                    30: {
                        'name': '30',
                        'matches': {
                            'l2': {
                                'eth': {
                                    'destination_mac_address': 'host 0000.0000.0000',
                                    'source_mac_address': 'host 0000.0000.0000',
                                    'vlan': 10,
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'deny',
                            },
                        },
                    40: {
                        'name': '40',
                        'matches': {
                            'l2': {
                                'eth': {
                                    'destination_mac_address': 'host bbbb.bbff.7777',
                                    'source_mac_address': 'host aaaa.aaff.5555',
                                    'ether_type': '80f3',
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            },
                        },
                    },
                },
            }
