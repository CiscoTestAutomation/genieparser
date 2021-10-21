expected_output = {
    'interfaces': {
        'TenGigE0/1/0/0': {
            'port_id': {
                'Bundle-Ether2': {
                    'neighbors': {
                        'geni5-genie': {
                            'chassis_id': 'ccd8.c1ff.49dc',
                            'port_description': '10G to ge1-genie port Ge1/1/1/1:GG1',
                            'system_name': 'geni5-genie',
                            'neighbor_id': 'geni5-genie',
                            'system_description': 'Cisco IOS XR Software, Version 6.5.3[Default]\nCopyright (c) 2019 by Cisco Systems, Inc., ASR9K Series\n',
                            'time_remaining': 99,
                            'hold_time': 120,
                            'capabilities': {
                                'router': {
                                    'system': True,
                                    'enabled': True
                                }
                            },
                            'management_address': '10.10.10.12',
                            'peer_mac': 'cc:d8:c1:ff:49:df'
                        }
                    }
                }
            }
        },
        'TenGigE0/5/0/5': {
            'port_id': {
                'TenGigabitEthernet0/1/0/3': {
                    'neighbors': {
                        'system3': {
                            'chassis_id': 'c471.feff.70c3',
                            'port_description': '10G link to genie1-genie port TEN 0/5/0/5 in BE 43 (with port 0/4/0/3)',
                            'system_name': 'system3',
                            'neighbor_id': 'system3',
                            'system_description': 'Cisco IOS XR Software, Version 6.4.2[Default]\nCopyright (c) 2019 by Cisco Systems, Inc., CRS\n',
                            'time_remaining': 108,
                            'hold_time': 120,
                            'capabilities': {
                                'router': {
                                    'system': True,
                                    'enabled': True
                                }
                            },
                            'management_address': '10.10.10.13',
                            'peer_mac': 'c4:71:fe:ff:73:3d'
                        }
                    }
                }
            }
        },
        'TenGigE0/5/0/6': {
            'port_id': {
                '1611153480': {
                    'neighbors': {
                        'GENIE02GEN2': {
                            'chassis_id': '8426.2bff.e85a',
                            'port_description': '2/1/9, 10-Gig Ethernet, "10G interface to genie1-genie port 0/5/0/6-DO NOT SHUT or REMOVE..Mitch"',
                            'system_name': 'GENIE02GEN2',
                            'neighbor_id': 'GENIE02GEN2',
                            'system_description': '',
                            'time_remaining': 105,
                            'hold_time': 121,
                            'capabilities': {
                                'bridge': {
                                    'system': True,
                                    'enabled': True
                                },
                                'router': {
                                    'system': True,
                                    'enabled': True
                                }
                            },
                            'management_address': '10.10.10.14',
                            'peer_mac': 'a0:f3:e4:ff:19:d4'
                        }
                    }
                }
            }
        },
        'TenGigE0/5/0/8': {
            'port_id': {
                '8426.2bff.e85a': {
                    'neighbors': {
                        'c4:71:fe:ff:73:3d': {
                            'chassis_id': '8426.2bff.e85a',
                            'port_description': 'not advertised',
                            'time_remaining': 74,
                            'hold_time': 14,
                            'peer_mac': 'c4:71:fe:ff:73:3d'
                        }
                    }
                }
            }
        }
    },
    'total_entries': 4
}
