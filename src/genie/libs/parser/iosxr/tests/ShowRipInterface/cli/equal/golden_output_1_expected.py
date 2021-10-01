

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip': {
                            'interfaces': {
                                'GigabitEthernet0/0/0/0.100': {
                                    'authentication': {
                                        'auth_key_chain': {
                                            'key_chain': 'Not set'
                                        },
                                        'auth_key': {
                                            'crypto_algorithm': 'None'
                                        }
                                    },
                                    'cost': 0,
                                    'neighbors': {
                                        '10.1.2.2': {
                                            'address': '10.1.2.2',
                                            'uptime': 2,
                                            'version': 2,
                                            'packets_discarded': 0,
                                            'routes_discarded': 4733
                                        }
                                    },
                                    'out_of_memory_state': 'Normal',
                                    'broadcast_for_v2': False,
                                    'accept_metric_0': False,
                                    'send_versions': 2,
                                    'receive_versions': 2,
                                    'oper_status': 'Up',
                                    'address': '10.1.2.1/24',
                                    'passive': True,
                                    'split_horizon': True,
                                    'poison_reverse': False,
                                    'socket_set': {
                                        'multicast_group': True,
                                        'lpts_filter': True
                                    },
                                    'statistics': {
                                        'total_packets_received': 4877
                                    }
                                },
                                'GigabitEthernet0/0/0/1.100': {
                                    'authentication': {
                                        'auth_key_chain': {
                                            'key_chain': 'Not set'
                                        },
                                        'auth_key': {
                                            'crypto_algorithm': 'None'
                                        }
                                    },
                                    'cost': 0,
                                    'out_of_memory_state': 'Normal',
                                    'broadcast_for_v2': False,
                                    'accept_metric_0': False,
                                    'send_versions': 2,
                                    'receive_versions': 2,
                                    'oper_status': 'Up',
                                    'address': '10.1.3.1/24',
                                    'passive': False,
                                    'split_horizon': True,
                                    'poison_reverse': False,
                                    'socket_set': {
                                        'multicast_group': True,
                                        'lpts_filter': True
                                    },
                                    'statistics': {
                                        'total_packets_received': 0
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
