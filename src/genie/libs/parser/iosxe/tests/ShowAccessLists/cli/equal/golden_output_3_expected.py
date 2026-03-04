expected_output = {
    'FQDN_ACL_WEBAUTH_REDIRECT': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'host 100.8.12.107': {
                                    'destination_network': 'host 100.8.12.107',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '10',
            },
            '100000': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'host 100.8.12.107': {
                                    'destination_network': 'host 100.8.12.107',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '100000',
            },
            '20': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'host dynamic www.msft10.com': {
                                    'destination_network': 'host dynamic www.msft10.com',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '20',
            },
            '30': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'host dynamic www.msft11.com': {
                                    'destination_network': 'host dynamic www.msft11.com',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '30',
            },
            '40': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'host dynamic www.msft12.com': {
                                    'destination_network': 'host dynamic www.msft12.com',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '40',
            },
            '50': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'host dynamic www.msft13.com': {
                                    'destination_network': 'host dynamic www.msft13.com',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '50',
            },
        },
        'acl_type': 'extended',
        'name': 'FQDN_ACL_WEBAUTH_REDIRECT',
        'type': 'ipv4-acl-type',
    },
    'IP-Adm-V4-Int-ACL-global': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                'name': '10',
            },
            '20': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                'name': '20',
            },
        },
        'acl_type': 'extended',
        'name': 'IP-Adm-V4-Int-ACL-global',
        'type': 'ipv4-acl-type',
    },
    'implicit_deny': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '10',
            },
        },
        'acl_type': 'extended',
        'name': 'implicit_deny',
        'type': 'ipv4-acl-type',
    },
    'implicit_permit': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '10',
            },
        },
        'acl_type': 'extended',
        'name': 'implicit_permit',
        'type': 'ipv4-acl-type',
    },
    'meraki-fqdn-dns': {
        'acl_type': 'extended',
        'name': 'meraki-fqdn-dns',
        'type': 'ipv4-acl-type',
    },
    'preauth_v4': {
        'aces': {
            '10': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                'name': '10',
            },
            '20': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                'name': '20',
            },
            '30': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                            'established': False,
                            'source_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 'bootps',
                                },
                            },
                        },
                    },
                },
                'name': '30',
            },
            '40': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                                    'port': 68,
                                },
                            },
                            'established': False,
                        },
                    },
                },
                'name': '40',
            },
            '50': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                            'established': False,
                            'source_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 'bootpc',
                                },
                            },
                        },
                    },
                },
                'name': '50',
            },
            '60': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '60',
            },
        },
        'acl_type': 'extended',
        'name': 'preauth_v4',
        'type': 'ipv4-acl-type',
    },
    'xACSACLx-IP-CWA_PRE_AUTH-69692867': {
        'aces': {
            '1': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                                    'port': 67,
                                },
                            },
                            'established': False,
                            'source_port': {
                                'operator': {
                                    'operator': 'eq',
                                    'port': 'bootpc',
                                },
                            },
                        },
                    },
                },
                'name': '1',
            },
            '2': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                'name': '2',
            },
            '3': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                'name': '3',
            },
            '4': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                                    'port': 8443,
                                },
                            },
                            'established': False,
                        },
                    },
                },
                'name': '4',
            },
            '5': {
                'actions': {
                    'forwarding': 'permit',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
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
                'name': '5',
            },
            '6': {
                'actions': {
                    'forwarding': 'deny',
                    'logging': 'log-none',
                },
                'matches': {
                    'l3': {
                        'ipv4': {
                            'destination_network': {
                                'any': {
                                    'destination_network': 'any',
                                },
                            },
                            'protocol': 'ipv4',
                            'source_network': {
                                'any': {
                                    'source_network': 'any',
                                },
                            },
                        },
                    },
                    'l4': {
                        'ipv4': {
                            'established': False,
                        },
                    },
                },
                'name': '6',
            },
        },
        'acl_type': 'extended',
        'name': 'xACSACLx-IP-CWA_PRE_AUTH-69692867',
        'type': 'ipv4-acl-type',
    },
}

