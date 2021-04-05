expected_output = {
        'total_entries': 2,
        'interfaces': {
            'Ethernet1/1': {
                'port_id': {
                    'GigabitEthernet3': {
                        'neighbors': {
                            'R1_csr1000v.openstacklocal': {
                                'chassis_id': '001e.49ff.24f7',
                                'port_description': 'GigabitEthernet3',
                                'system_name': 'R1_csr1000v.openstacklocal',
                                'system_description': 'Cisco IOS Software [Everest], '
                                                      'Virtual XE Software ('
                                                      'X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.1, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2017 by Cisco Systems, Inc.\nCompiled Sat 22-Jul-17 05:51 by',
                                'time_remaining': 114,
                                'capabilities': {
                                    'bridge': {
                                        'name': 'bridge',
                                        'system': True,
                                    },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True
                                    }
                                },
                                'management_address_v4': '10.1.3.1',
                                'management_address_v6': 'not advertised',
                                'vlan_id': 'not advertised'
                            }
                        }
                    }
                }
            },
            'Ethernet1/2': {
                'port_id': {
                    'GigabitEthernet0/0/0/1': {
                        'neighbors': {
                            'R2_xrv9000': {
                                'chassis_id': '000d.bdff.4f04',
                                'system_name': 'R2_xrv9000',
                                'system_description': '6.2.2, IOS-XRv 9000',
                                'time_remaining': 95,
                                'capabilities': {
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True
                                    }
                                },
                                'management_address_v4': '10.2.3.2',
                                'management_address_v6': 'not advertised',
                                'vlan_id': 'not advertised'
                            }
                        }
                    }
                }
            }
        }
    }
