expected_output = {
    'protocols': {
        'application': {
            'update_frequency': 0,
            'invalid': 0,
            'holddown': 0,
            'flushed': 0,
            'outgoing_filter_list': 'not set',
            'incoming_filter_list': 'not set',
            'maximum_path': 32,
            'preference': {
                'single_value': {
                    'all': 4
                }
            }
        },
        'isis': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv4': {
                            'instance': {
                                'sr': {
                                    'outgoing_filter_list':
                                    'not set',
                                    'incoming_filter_list':
                                    'not set',
                                    'redistributing':
                                    'isis',
                                    'maximum_path':
                                    4,
                                    'configured_interfaces': [
                                        'Loopback1', 'Ethernet2/0',
                                        'Ethernet2/1', 'Ethernet3/0',
                                        'Ethernet3/1', 'Ethernet4/0',
                                        'Ethernet4/1'
                                    ],
                                    'routing_information_sources': {
                                        'gateway': {
                                            '1.1.1.3': {
                                                'distance': 115,
                                                'last_update': '00:01:35'
                                            },
                                            '1.1.1.5': {
                                                'distance': 115,
                                                'last_update': '00:01:35'
                                            },
                                            '1.1.1.4': {
                                                'distance': 115,
                                                'last_update': '00:01:35'
                                            },
                                            '1.1.1.7': {
                                                'distance': 115,
                                                'last_update': '00:01:35'
                                            },
                                            '1.1.1.6': {
                                                'distance': 115,
                                                'last_update': '00:01:35'
                                            },
                                            '1.1.1.9': {
                                                'distance': 115,
                                                'last_update': '00:01:35'
                                            },
                                            '1.1.1.8': {
                                                'distance': 115,
                                                'last_update': '00:01:35'
                                            },
                                            '1.1.1.11': {
                                                'distance': 115,
                                                'last_update': '00:01:35'
                                            }
                                        }
                                    },
                                    'preference': {
                                        'single_value': {
                                            'all': 115
                                        }
                                    }
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
                                'ipv4': {
                                    'outgoing_filter_list': 'not set',
                                    'incoming_filter_list': 'not set',
                                    'igp_sync': False,
                                    'automatic_route_summarization': False,
                                    'maximum_path': 1,
                                    'preference': {
                                        'multi_values': {
                                            'external': 20,
                                            'internal': 200,
                                            'local': 200
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
