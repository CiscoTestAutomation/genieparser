expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'multicast_group': {
                        'ff05::2/128': {
                            'source_address': {
                                '*': {
                                    'uptime': '2d18h',
                                    'flags': 'ipv6 mld pim6',
                                    'oil_count': '1',
                                    'incoming_interface_list': {
                                        'Null': {
                                            'rpf_nbr': '0::',
                                        },
                                    },
                                    'outgoing_interface_list': {
                                        'Ethernet1/8': {
                                            'oil_uptime': '2d18h',
                                            'oil_flags': 'mld',
                                        },
                                    },
                                },
                            },
                        },
                        'ff1e::/64': {
                            'source_address': {
                                '*': {
                                    'uptime': '2d19h',
                                    'flags': 'ipv6 pim6',
                                    'bidir': True,
                                    'oil_count': '1',
                                    'incoming_interface_list': {
                                        'Ethernet1/1': {
                                            'rpf_nbr':
                                                'fe80::4e71:dff:fe56:1143',
                                        },
                                    },
                                    'outgoing_interface_list': {
                                        'Ethernet1/1': {
                                            'oil_uptime': '2d18h',
                                            'oil_flags': 'pim6',
                                            'oif_rpf': 'RPF',
                                        },
                                    },
                                },
                            },
                        },
                        'ff1e::1:1:12/128': {
                            'source_address': {
                                '*': {
                                    'uptime': '12:45:01',
                                    'flags': 'ipv6 mld pim6',
                                    'bidir': True,
                                    'oil_count': '2',
                                    'incoming_interface_list': {
                                        'Ethernet1/1': {
                                            'rpf_nbr':
                                                'fe80::4e71:dff:fe56:1143',
                                        },
                                    },
                                    'outgoing_interface_list': {
                                        'Ethernet1/1': {
                                            'oil_uptime': '12:45:01',
                                            'oil_flags': 'pim6',
                                            'oif_rpf': 'RPF',
                                        },
                                        'Ethernet1/8': {
                                            'oil_uptime': '12:45:01',
                                            'oil_flags': 'mld',
                                        },
                                    },
                                },
                            },
                        },
                        'ff1e::1:1:13/128': {
                            'source_address': {
                                '*': {
                                    'uptime': '12:45:01',
                                    'flags': 'ipv6 mld pim6',
                                    'bidir': True,
                                    'oil_count': '2',
                                    'incoming_interface_list': {
                                        'Ethernet1/1': {
                                            'rpf_nbr':
                                                'fe80::4e71:dff:fe56:1143',
                                        },
                                    },
                                    'outgoing_interface_list': {
                                        'Ethernet1/1': {
                                            'oil_uptime': '12:45:01',
                                            'oil_flags': 'pim6',
                                            'oif_rpf': 'RPF',
                                        },
                                        'Ethernet1/8': {
                                            'oil_uptime': '12:45:01',
                                            'oil_flags': 'mld',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
