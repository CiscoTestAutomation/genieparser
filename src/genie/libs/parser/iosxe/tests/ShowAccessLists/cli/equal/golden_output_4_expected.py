expected_output = {
    'FQDN_v6ACL_WEBAUTH_REDIRECT': {
        'aces': {
            '1900000': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'udp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'udp': {
                            'destination_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 53,
                                },
                            },
                            'established': False,
                        },
                    },
                },
                'name': '1900000',
            },
            '1910000': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'tcp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'tcp': {
                            'destination_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 53,
                                },
                            },
                            'established': False,
                        },
                    },
                },
                'name': '1910000',
            },
            '1920000': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'icmp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'icmp': {
                            'established': False,
                            'msg_type': 'nd-ns',
                        },
                    },
                },
                'name': '1920000',
            },
            '1930000': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'icmp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'icmp': {
                            'established': False,
                            'msg_type': 'nd-na',
                        },
                    },
                },
                'name': '1930000',
            },
            '1940000': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'icmp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'icmp': {
                            'established': False,
                            'msg_type': 'router-solicitation',
                        },
                    },
                },
                'name': '1940000',
            },
            '1950000': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'icmp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'icmp': {
                            'established': False,
                            'msg_type': 'router-advertisement',
                        },
                    },
                },
                'name': '1950000',
            },
            '1960000': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'icmp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'icmp': {
                            'established': False,
                            'msg_type': 'redirect',
                        },
                    },
                },
                'name': '1960000',
            },
            '1970000': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'udp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'udp': {
                            'destination_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 546,
                                },
                            },
                            'established': False,
                            'source_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': '547',
                                },
                            },
                        },
                    },
                },
                'name': '1970000',
            },
            '1980000': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'udp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'udp': {
                            'destination_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 547,
                                },
                            },
                            'established': False,
                            'source_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': '546',
                                },
                            },
                        },
                    },
                },
                'name': '1980000',
            },
            '1990000': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'tcp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'tcp': {
                            'destination_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 80,
                                },
                            },
                            'established': False,
                        },
                    },
                },
                'name': '1990000',
            },
            '20000': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'host 1:1:2::23': {
                                    'destination_network': 'host 1:1:2::23',
                                },
                            },
                            'protocol': 'ipv6',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv6': {
                            'established': False,
                        },
                    },
                },
                'name': '20000',
            },
            '2000000': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'tcp',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'tcp': {
                            'destination_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 443,
                                },
                            },
                            'established': False,
                        },
                    },
                },
                'name': '2000000',
            },
            '20001': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'host 1:1:1::23': {
                                    'destination_network': 'host 1:1:1::23',
                                },
                            },
                            'protocol': 'ipv6',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv6': {
                            'established': False,
                        },
                    },
                },
                'name': '20001',
            },
            '20002': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'host 1:1:2::24': {
                                    'destination_network': 'host 1:1:2::24',
                                },
                            },
                            'protocol': 'ipv6',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv6': {
                            'established': False,
                        },
                    },
                },
                'name': '20002',
            },
            '20003': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'host 1:1:1::24': {
                                    'destination_network': 'host 1:1:1::24',
                                },
                            },
                            'protocol': 'ipv6',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv6': {
                            'established': False,
                        },
                    },
                },
                'name': '20003',
            },
            '4': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'host dynamic *.atoz.msn.com': {
                                    'destination_network': 'host dynamic *.atoz.msn.com',
                                },
                            },
                            'protocol': 'ipv6',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv6': {
                            'established': False,
                        },
                    },
                },
                'name': '4',
            },
            '5': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv6': {
                            'destination_network': {
                                'host dynamic www.ab.*.*.*.test.com': {
                                    'destination_network': 'host dynamic www.ab.*.*.*.test.com',
                                },
                            },
                            'protocol': 'ipv6',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv6': {
                            'established': False,
                        },
                    },
                },
                'name': '5',
            },
        },
        'acl_type': 'ipv6 fqdn',
        'name': 'FQDN_v6ACL_WEBAUTH_REDIRECT',
        'type': 'ipv6-acl-type',
    },
}
