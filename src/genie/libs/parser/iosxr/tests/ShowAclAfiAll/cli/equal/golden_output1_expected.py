expected_output = {
            'acl_name': {
                'name': 'acl_name',
                'type': 'ipv4-acl-type',
                'aces': {
                    10: {
                        'name': '10',
                        'matches': {
                            'l3': {
                                'ipv4': {
                                    'source_ipv4_network': {
                                        'any': {
                                            'source_ipv4_network': 'any',
                                            },
                                        },
                                    'destination_ipv4_network': {
                                        'any': {
                                            'destination_ipv4_network': 'any',
                                            },
                                        },
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            'logging': 'log-none',
                            },
                        },
                    },
                },
            'ipv4_acl': {
                'name': 'ipv4_acl',
                'type': 'ipv4-acl-type',
                'aces': {
                    10: {
                        'name': '10',
                        'matches': {
                            'l3': {
                                'ipv4': {
                                    'source_ipv4_network': {
                                        'any': {
                                            'source_ipv4_network': 'any',
                                            },
                                        },
                                    'destination_ipv4_network': {
                                        'any': {
                                            'destination_ipv4_network': 'any',
                                            },
                                        },
                                    },
                                },
                            'l4': {
                                'tcp': {
                                    'destination_port': {
                                        'operator': {
                                            'operator': 'eq',
                                            'port': 'www',
                                            },
                                        },
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            'logging': 'log-none',
                            },
                        },
                    20: {
                        'name': '20',
                        'matches': {
                            'l3': {
                                'ipv4': {
                                    'source_ipv4_network': {
                                        'any': {
                                            'source_ipv4_network': 'any',
                                            },
                                        },
                                    'destination_ipv4_network': {
                                        'any': {
                                            'destination_ipv4_network': 'any',
                                            },
                                        },
                                    },
                                },
                            'l4': {
                                'tcp': {
                                    'destination_port': {
                                        'operator': {
                                            'operator': 'eq',
                                            'port': 'ssh',
                                            },
                                        },
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            'logging': 'log-none',
                            },
                        },
                    30: {
                        'name': '30',
                        'matches': {
                            'l3': {
                                'ipv4': {
                                    'source_ipv4_network': {
                                        'any': {
                                            'source_ipv4_network': 'any',
                                            },
                                        },
                                    'destination_ipv4_network': {
                                        'any': {
                                            'destination_ipv4_network': 'any',
                                            },
                                        },
                                    },
                                },
                            'l4': {
                                'tcp': {
                                    'destination_port': {
                                        'operator': {
                                            'operator': 'eq',
                                            'port': '443',
                                            },
                                        },
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            'logging': 'log-none',
                            },
                        },
                    },
                },
            'test22': {
                'name': 'test22',
                'type': 'ipv4-acl-type',
                'aces': {
                    10: {
                        'name': '10',
                        'matches': {
                            'l3': {
                                'ipv4': {
                                    'source_ipv4_network': {
                                        '192.168.1.0 0.0.0.255': {
                                            'source_ipv4_network': '192.168.1.0 0.0.0.255',
                                            },
                                        },
                                    'destination_ipv4_network': {
                                        '192.168.1.0 0.0.0.255': {
                                            'destination_ipv4_network': 'host 10.4.1.1',
                                            },
                                        },
                                    },
                                },
                            'l4': {
                                'tcp': {
                                    'established': True,
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            'logging': 'log-syslog',
                            },
                        },
                    20: {
                        'name': '20',
                        'matches': {
                            'l3': {
                                'ipv4': {
                                    'source_ipv4_network': {
                                        'host 10.16.2.2': {
                                            'source_ipv4_network': 'host 10.16.2.2',
                                            },
                                        },
                                    'destination_ipv4_network': {
                                        'host 10.16.2.2': {
                                            'destination_ipv4_network': 'any',
                                            },
                                        },
                                    'precedence': 'network',
                                    'ttl': 255,
                                    'ttl_operator': 'eq',
                                    },
                                },
                            'l4': {
                                'tcp': {
                                    'source-port': {
                                        'operator': {
                                            'operator': 'eq',
                                            'port': 'www',
                                            },
                                        },
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            'logging': 'log-none',
                            },
                        },
                    30: {
                        'name': '30',
                        'matches': {
                            'l3': {
                                'ipv4': {
                                    'source_ipv4_network': {
                                        'any': {
                                            'source_ipv4_network': 'any',
                                            },
                                        },
                                    'destination_ipv4_network': {
                                        'any': {
                                            'destination_ipv4_network': 'any',
                                            },
                                        },
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'deny',
                            'logging': 'log-none',
                            },
                        },
                    },
                },
            'ipv6_acl': {
                'name': 'ipv6_acl',
                'type': 'ipv6-acl-type',
                'aces': {
                    10: {
                        'name': '10',
                        'matches': {
                            'l3': {
                                'ipv6': {
                                    'source_ipv6_network': {
                                        'any': {
                                            'source_ipv6_network': 'any',
                                            },
                                        },
                                    'destination_ipv6_network': {
                                        'any': {
                                            'destination_ipv6_network': 'any',
                                            },
                                        },
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            'logging': 'log-syslog',
                            },
                        },
                    20: {
                        'name': '20',
                        'matches': {
                            'l3': {
                                'ipv6': {
                                    'source_ipv6_network': {
                                        'host 2001::1': {
                                            'source_ipv6_network': 'host 2001::1',
                                            },
                                        },
                                    'destination_ipv6_network': {
                                        'host 2001::1': {
                                            'destination_ipv6_network': 'host 2001:1::2',
                                            },
                                        },
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            'logging': 'log-none',
                            },
                        },
                    30: {
                        'name': '30',
                        'matches': {
                            'l3': {
                                'ipv6': {
                                    'source_ipv6_network': {
                                        'any': {
                                            'source_ipv6_network': 'any',
                                            },
                                        },
                                    'destination_ipv6_network': {
                                        'any': {
                                            'destination_ipv6_network': 'host 2001:2::2',
                                            },
                                        },
                                    },
                                },
                            'l4': {
                                'tcp': {
                                    'source-port': {
                                        'operator': {
                                            'operator': 'eq',
                                            'port': '8443',
                                            },
                                        },
                                    },
                                },
                            },
                        'actions': {
                            'forwarding': 'permit',
                            'logging': 'log-none',
                            },
                        },
                    },
                },
            }

