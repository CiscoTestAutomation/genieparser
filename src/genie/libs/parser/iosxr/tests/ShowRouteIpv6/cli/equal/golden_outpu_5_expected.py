expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        'fc00:c000:1001::/48': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:1001::/48',
                            'active': True,
                            'behaviour': 'uN (shift)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '::',
                                        'updated': '1d21h'
                                    }
                                }
                            }
                        },
                        'fc00:c000:1001::/64': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:1001::/64',
                            'active': True,
                            'behaviour': 'uN (PSP/USD)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '::',
                                        'updated': '1d21h'
                                    }
                                }
                            }
                        },
                        'fc00:c001:1001::/48': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c001:1001::/48',
                            'active': True,
                            'behaviour': 'uN (shift)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '::',
                                        'updated': '1d21h'
                                    }
                                }
                            }
                        },
                        'fc00:c001:1001::/64': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c001:1001::/64',
                            'active': True,
                            'behaviour': 'uN (PSP/USD)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '::',
                                        'updated': '1d21h'
                                    }
                                }
                            }
                        },
                        'fc00:c000:1001:e000::/64': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:1001:e000::/64',
                            'active': True,
                            'behaviour': 'uDT4',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '::ffff:0.0.0.0',
                                        'updated': '1d21h',
                                        'nexthop_in_vrf': 'SRV6_L3VPN_BE'
                                    }
                                }
                            }
                        },
                        'fc00:c000:1001:e001::/64': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:1001:e001::/64',
                            'active': True,
                            'behaviour': 'uDT6',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '::',
                                        'updated': '1d21h',
                                        'nexthop_in_vrf': 'SRV6_L3VPN_BE'
                                    }
                                }
                            }
                        },
                        'fc00:c000:1001:e004::/64': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:1001:e004::/64',
                            'active': True,
                            'behaviour': 'uDT4',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': '::ffff:0.0.0.0',
                                        'updated': '1d21h',
                                        'nexthop_in_vrf': 'default'
                                    }
                                }
                            }
                        },
                        'fc00:c000:1001:e002::/64': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:1001:e002::/64',
                            'active': True,
                            'behaviour': 'uA (shift)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::250:56ff:fe94:9ba5',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                        'updated': '1d20h'
                                    }
                                }
                            }
                        },
                        'fc00:c000:1001:e002::/80': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:1001:e002::/80',
                            'active': True,
                            'behaviour': 'uA (PSP/USD)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::250:56ff:fe94:9ba5',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                        'updated': '1d20h'
                                    }
                                }
                            }
                        },
                        'fc00:c000:1001:e003::/64': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:1001:e003::/64',
                            'active': True,
                            'behaviour': 'uA (shift)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::250:56ff:fe94:ac68',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/2',
                                        'updated': '1d20h'
                                    }
                                }
                            }
                        },
                        'fc00:c000:1001:e003::/80': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:1001:e003::/80',
                            'active': True,
                            'behaviour': 'uA (PSP/USD)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::250:56ff:fe94:ac68',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/2',
                                        'updated': '1d20h'
                                    }
                                }
                            }
                        },
                        'fc00:c000:e002::/48': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:e002::/48',
                            'active': True,
                            'behaviour': 'uA (shift)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::250:56ff:fe94:9ba5',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                        'updated': '1d20h'
                                    }
                                }
                            }
                        },
                        'fc00:c000:e002::/64': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:e002::/64',
                            'active': True,
                            'behaviour': 'uA (PSP/USD)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::250:56ff:fe94:9ba5',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/0',
                                        'updated': '1d20h'
                                    }
                                }
                            }
                        },
                        'fc00:c000:e003::/48': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:e003::/48',
                            'active': True,
                            'behaviour': 'uA (shift)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::250:56ff:fe94:ac68',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/2',
                                        'updated': '1d20h'
                                    }
                                }
                            }
                        },
                        'fc00:c000:e003::/64': {
                            'source_protocol': 'local',
                            'source_protocol_codes': 'L',
                            'route': 'fc00:c000:e003::/64',
                            'active': True,
                            'behaviour': 'uA (PSP/USD)',
                            'route_preference': 0,
                            'metric': 0,
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop': 'fe80::250:56ff:fe94:ac68',
                                        'outgoing_interface': 'GigabitEthernet0/0/0/2',
                                        'updated': '1d20h'
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
