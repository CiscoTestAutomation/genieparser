expected_output = {
        'interfaces': {
                'Ethernet1/14': {
                    'port_id': {
                        'PCI-ESlot1,Port2': {
                            'neighbors': {
                                'null': {
                                    'chassis_id': '3935-5A43-4A37-39373638-35303036574C',
                                    'enabled_capabilities': 'not advertised',
                                    'management_address_v4': '98f2.b3ff.07f4',
                                    'management_address_v6': 'not advertised',
                                    'port_description': 'ConnectX-4 Lx, 25G/10G/1G SFP',
                                    'system_capabilities': 'not advertised',
                                    'system_description': 'ProLiant DL360 Gen10',
                                    'system_name': 'null',
                                    'time_remaining': 40,
                                    'vlan_id': 'not advertised'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/38': {
                    'port_id': {
                        '0': {
                            'neighbors': {
                                'VPN-1': {
                                    'capabilities': {
                                        'router': {
                                            'enabled': True,
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': 'e0cb.bcff.4290',
                                    'management_address_v4': 'not advertised',
                                    'management_address_v6': 'not advertised',
                                    'port_description': 'internet port 0',
                                    'system_description': 'Meraki MX450 '
                                    'Cloud Managed Security Appliance',
                                    'system_name': 'VPN-1',
                                    'time_remaining': 101,
                                    'vlan_id': 'not advertised'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/40': {
                    'port_id': {
                        '1': {
                            'neighbors': {
                                'MX-L0': {
                                    'capabilities': {
                                        'router': {
                                            'enabled': True,
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': 'e0cb.bcff.7bab',
                                    'management_address_v4': 'not advertised',
                                    'management_address_v6': 'not advertised',
                                    'port_description': 'internet port 1',
                                    'system_description': 'Meraki MX450 Cloud '
                                    'Managed Security Appliance',
                                    'system_name': 'MX-L0',
                                    'time_remaining': 90,
                                    'vlan_id': 'not advertised'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/42': {
                    'port_id': {
                        'TenGigabitEthernet2/0/2': {
                            'neighbors': {
                                'CAT2960-CED1': {
                                    'capabilities': {
                                        'bridge': {
                                            'enabled': True,
                                            'name': 'bridge',
                                            'system': True
                                        },
                                        'router': {
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': '7018.a7ff.7d64',
                                    'management_address_v4': '10.22.134.6',
                                    'management_address_v6': 'not advertised',
                                    'port_description': '- NX1-2 (Eth1/43) -',
                                    'system_description': 'Cisco IOS Software, '
                                    'C2960X Software (C2960X-UNIVERSALK9-M), '
                                    'Version 15.2(4)E7, RELEASE SOFTWARE '
                                    '(fc2)\n'
                                    'Technical Support: '
                                    'http://www.cisco.com/techsupport\n'
                                    'Copyright (c) 1986-2018 by Cisco '
                                    'Systems, Inc.\n'
                                    'Compiled Tue 18-Sep-18 13:07 by '
                                    'prod_rel_team',
                                    'system_name': 'CAT2960-CED1',
                                    'time_remaining': 93,
                                    'vlan_id': '1'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/43': {
                    'port_id': {
                        'TenGigabitEthernet1/0/1': {
                            'neighbors': {
                                'RCAT2960': {
                                    'capabilities': {
                                        'bridge': {
                                            'enabled': True,
                                            'name': 'bridge',
                                            'system': True
                                        },
                                        'router': {
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': '7018.a7ff.7d64',
                                    'management_address_v4': '10.22.134.6',
                                    'management_address_v6': 'not advertised',
                                    'port_description': '- NX1-1 (Eth1/42) -',
                                    'system_description': 'Cisco IOS Software, '
                                    'C2960X Software (C2960X-UNIVERSALK9-M), '
                                    'Version 15.2(4)E7, RELEASE SOFTWARE '
                                    '(fc2)\n'
                                    'Technical Support: '
                                    'http://www.cisco.com/techsupport\n'
                                    'Copyright (c) 1986-2018 by Cisco Systems, '
                                    'Inc.\n'
                                    'Compiled Tue 18-Sep-18 13:07 by prod_rel_team',
                                    'system_name': 'RCAT2960',
                                    'time_remaining': 109,
                                    'vlan_id': 'not advertised'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/46': {
                    'port_id': {
                        'Ethernet1/46': {
                            'neighbors': {
                                'NX1-2': {
                                    'capabilities': {
                                        'bridge': {
                                            'enabled': True,
                                            'name': 'bridge',
                                            'system': True
                                        },
                                        'router': {
                                            'enabled': True,
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': '70ea.1aff.b6f6',
                                    'management_address_v4': '70ea.1aff.b6f6',
                                    'management_address_v6': 'not advertised',
                                    'port_description': '- NX1-1 (eth1/46) - '
                                    'vPC Peer Keepalive link',
                                    'system_description': 'Cisco Nexus Operating '
                                    'System (NX-OS) Software 9.2(3)\n'
                                    'TAC support: '
                                    'http://www.cisco.com/tac\n'
                                    'Copyright (c) 2002-2019, Cisco Systems, '
                                    'Inc. All rights reserved.\n',
                                    'system_name': 'NX1-2',
                                    'time_remaining': 116,
                                    'vlan_id': 'not advertised'
                                }
                            }
                        }
                    }
                },
                'Ethernet1/54': {
                    'port_id': {
                        'Ethernet1/54': {
                            'neighbors': {
                                'NX2-2': {
                                    'capabilities': {
                                        'bridge': {
                                            'enabled': True,
                                            'name': 'bridge',
                                            'system': True
                                        },
                                        'router': {
                                            'enabled': True,
                                            'name': 'router',
                                            'system': True
                                        }
                                    },
                                    'chassis_id': '70ea.1aff.854d',
                                    'management_address_v4': '70ea.1aff.854d',
                                    'management_address_v6': 'not advertised',
                                    'port_description': '- NX1 -',
                                    'system_description': 'Cisco Nexus Operating '
                                    'System (NX-OS) Software 9.2(3)\n'
                                    'TAC support: '
                                    'http://www.cisco.com/tac\n'
                                    'Copyright (c) 2002-2019, '
                                    'Cisco Systems, Inc. '
                                    'All rights reserved.\n',
                                    'system_name': 'NX2-2',
                                    'time_remaining': 116,
                                    'vlan_id': '1'
                                }
                            }
                        }
                    }
                }
            },
            'total_entries': 22
        }