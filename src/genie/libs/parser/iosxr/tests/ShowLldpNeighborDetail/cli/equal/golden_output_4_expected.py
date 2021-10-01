

expected_output = {
    'interfaces': {
        'TenGigE0/0/0/1': {
            'port_id': {
                '655': {
                    'neighbors': {
                        'MX480-01.comcast.net': {
                            'capabilities': {
                                'bridge': {
                                    'enabled': True,
                                    'system': True,
                                },
                                'router': {
                                    'enabled': True,
                                    'system': True,
                                },
                            },
                            'chassis_id': '0026.88ff.c416',
                            'hold_time': 120,
                            'management_address': '10.253.47.140',
                            'neighbor_id': 'MX480-01.comcast.net',
                            'port_description': 'PHY|BW|L3|CORE|type:CRAN-P2P|rhost:ASR-01|rport:TenGigE0/0/0/1',
                            'system_description': '',
                            'system_name': 'MX480-01.comcast.net',
                            'time_remaining': 98,
                        },
                    },
                },
            },
        },
        'TenGigE0/2/0/1': {
            'port_id': {
                'Ethernet1/4': {
                    'neighbors': {
                        '7280CR2A-01.comcast.net': {
                            'capabilities': {
                                'bridge': {
                                    'enabled': True,
                                    'system': True,
                                },
                                'router': {
                                    'enabled': True,
                                    'system': True,
                                },
                            },
                            'chassis_id': '444c.a8ff.39f5',
                            'hold_time': 120,
                            'management_address': '10.252.26.104',
                            'neighbor_id': '7280CR2A-01.comcast.net',
                            'port_description': 'PHY|BW|AGG-MEMBER|CORE|type:CRAN-P2P|rhost:ASR-01|rport:TenGigE0/2/0/1|lagg:Port-Channel10|ragg:Bundle-Ether10',
                            'system_description': '',
                            'system_name': '7280CR2A-01.comcast.net',
                            'time_remaining': 97,
                        },
                    },
                },
            },
        },
        'TenGigE0/2/0/11': {
            'port_id': {
                'TenGigabitEthernet0/0/0/0': {
                    'neighbors': {
                        'ASR9904.netlabs.nj.ula.comcast.net': {
                            'capabilities': {
                                'router': {
                                    'enabled': True,
                                    'system': True,
                                },
                            },
                            'chassis_id': '6c41.0eff.3712',
                            'hold_time': 120,
                            'management_address': '10.253.47.122',
                            'neighbor_id': 'ASR9904.netlabs.nj.ula.comcast.net',
                            'port_description': 'PHY|BW|L3|CORE|type:CRAN-P2P|rhost:ASR-01|rport:te0/2/0/11',
                            'system_description': 'Cisco IOS XR Software, Version 6.1.4[Default]\nCopyright (c) 2017 by Cisco Systems, Inc., ASR9K Series\n',
                            'system_name': 'ASR9904.netlabs.nj.ula.comcast.net',
                            'time_remaining': 116,
                        },
                    },
                },
            },
        },
        'TenGigE0/2/0/23': {
            'port_id': {
                'TenGigE0/0/0/4': {
                    'neighbors': {
                        'NCS5501': {
                            'capabilities': {
                                'router': {
                                    'enabled': True,
                                    'system': True,
                                },
                            },
                            'chassis_id': '7c31.0eff.203f',
                            'hold_time': 120,
                            'management_address': '10.253.47.30',
                            'neighbor_id': 'NCS5501',
                            'port_description': 'ASR-01 T0/2/0/23',
                            'system_description': '',
                            'system_name': 'NCS5501',
                            'time_remaining': 114,
                        },
                    },
                },
            },
        },
    },
    'total_entries': 4,
}
