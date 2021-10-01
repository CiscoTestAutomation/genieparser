

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        'rip': {
                            'routes': {
                                '10.1.2.0/24': {
                                    'index': {
                                        1: {
                                            'metric': 0,
                                            'route_type': 'connected',
                                            'interface': 'GigabitEthernet0/0/0/0.100'
                                        }
                                    }
                                },
                                '10.1.3.0/24': {
                                    'index': {
                                        1: {
                                            'metric': 0,
                                            'route_type': 'connected',
                                            'interface': 'GigabitEthernet0/0/0/1.100'
                                        }
                                    }
                                },
                                '10.0.0.0/8': {
                                    'index': {
                                        1: {
                                            'summary_type': 'auto-summary'
                                        }
                                    }
                                },
                                '172.16.1.0/24': {
                                    'index': {
                                        1: {
                                            'metric': 3,
                                            'distance': 0,
                                            'redistributed': True
                                        }
                                    }
                                },
                                '172.16.11.0/24': {
                                    'index': {
                                        1: {
                                            'metric': 3,
                                            'distance': 1,
                                            'redistributed': True
                                        }
                                    }
                                },
                                '172.16.22.0/24': {
                                    'index': {
                                        1: {
                                            'metric': 11,
                                            'next_hop': '10.1.2.2',
                                            'up_time': '15s',
                                            'interface': 'GigabitEthernet0/0/0/0.100'
                                        }
                                    }
                                },
                                '172.16.0.0/16': {
                                    'index': {
                                        1: {
                                            'summary_type': 'auto-summary'
                                        }
                                    }
                                },
                                '192.168.1.1/32': {
                                    'index': {
                                        1: {
                                            'metric': 3,
                                            'distance': 0,
                                            'redistributed': True
                                        }
                                    }
                                },
                                '192.168.1.0/24': {
                                    'index': {
                                        1: {
                                            'summary_type': 'auto-summary'
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
}
