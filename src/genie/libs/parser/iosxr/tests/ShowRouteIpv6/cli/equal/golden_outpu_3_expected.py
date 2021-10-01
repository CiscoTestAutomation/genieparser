

expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        '2001:db8:1234::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:1234::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:1579::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:1579::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:1981::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:1981::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:2222::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:2222::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:3456::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:3456::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:4021::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:4021::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:5354::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:5354::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:5555::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:5555::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:6666::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:6666::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:7654::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:7654::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:7777::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:7777::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:9843::8/128': {
                            'active': True,
                            'metric': 1,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::5054:ff:fef2:a625',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:03:00'
                                    }
                                }
                            },
                            'route': '2001:db8:9843::8/128',
                            'route_preference': 110,
                            'source_protocol': 'ospf',
                            'source_protocol_codes': 'O'
                        },
                        '2001:db8:abcd::/64': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/1': {
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:07:43'
                                    }
                                }
                            },
                            'route': '2001:db8:abcd::/64',
                            'source_protocol': 'connected',
                            'source_protocol_codes': 'C'
                        },
                        '2001:db8:abcd::1/128': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/1': {
                                        'outgoing_interface': 'GigabitEthernet0/0/0/1',
                                        'updated': '00:07:43'
                                    }
                                }
                            },
                            'route': '2001:db8:abcd::1/128',
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L'
                        },
                        '2001:db8:50e0:7b33:5054:ff:fe43:e2ee/128': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'MgmtEth0/RP0/CPU0/0': {
                                        'outgoing_interface': 'MgmtEth0/RP0/CPU0/0',
                                        'updated': '00:08:31'
                                    }
                                }
                            },
                            'route': '2001:db8:50e0:7b33:5054:ff:fe43:e2ee/128',
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L'
                        },
                        '2001:db8:50e0:7b33::/64': {
                            'active': True,
                            'next_hop': {
                                'outgoing_interface': {
                                    'MgmtEth0/RP0/CPU0/0': {
                                        'outgoing_interface': 'MgmtEth0/RP0/CPU0/0',
                                        'updated': '00:08:31'
                                    }
                                }
                            },
                            'route': '2001:db8:50e0:7b33::/64',
                            'source_protocol': 'connected',
                            'source_protocol_codes': 'C'
                        },
                        '::/0': {
                            'active': True,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::10ff:fe04:209e',
                                        'outgoing_interface': 'MgmtEth0/RP0/CPU0/0',
                                        'updated': '00:08:31'
                                    }
                                }
                            },
                            'route': '::/0',
                            'route_preference': 2,
                            'source_protocol': 'application route',
                            'source_protocol_codes': 'a*'
                        }
                    }
                },
            },
            'last_resort': {
                'gateway': 'fe80::10ff:fe04:209e',
                'to_network': '::'
            },
        },
    }
}
