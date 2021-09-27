

expected_output = {
    'interfaces': {
        'HundredGigE0/0/1/0': {
            'port_id': {
                'HundredGigE0/0/0/2': {
                    'neighbors': {
                        'system1': {
                            'capabilities': {
                                'router': {
                                    'enabled': True,
                                    'system': True,
                                },
                            },
                            'peer_mac': '00:8a:96:ff:13:13',
                            'chassis_id': '008a.96ff.178c',
                            'hold_time': 120,
                            'management_address': '10.10.10.11',
                            'neighbor_id': 'system1',
                            'port_description': 'to gen-8 nie  0/0/1/0 via gee1.dev 31-32',
                            'system_description': '',
                            'system_name': 'system1',
                            'time_remaining': 116,
                        },
                    },
                },
            },
        },
        'HundredGigE0/0/1/1': {
            'port_id': {
                'HundredGigE0/0/0/2': {
                    'neighbors': {
                        'system2': {
                            'capabilities': {
                                'router': {
                                    'enabled': True,
                                    'system': True,
                                },
                            },
                            'peer_mac': '00:8a:96:ff:2b:13',
                            'chassis_id': '008a.96ff.2f8c',
                            'hold_time': 120,
                            'management_address': '10.10.10.10',
                            'neighbor_id': 'system2',
                            'port_description': 'to gen-8 nie  0/0/1/1 via gee1.dev 29-30',
                            'system_description': '',
                            'system_name': 'system2',
                            'time_remaining': 96,
                        },
                    },
                },
            },
        },
        'TenGigE0/0/0/41': {
            'port_id': {
                'TenGigE0/0/0/0/0': {
                    'neighbors': {
                        'genie1-ggN1.ie-genie1': {
                            'capabilities': {
                                'router': {
                                    'enabled': True,
                                    'system': True,
                                },
                            },
                            'peer_mac': '00:bc:60:ff:7f:17',
                            'chassis_id': '00bc.60ff.7ff0',
                            'hold_time': 120,
                            'management_address': '10.10.10.2',
                            'neighbor_id': 'genie1-ggN1.ie-genie1',
                            'port_description': 'not advertised',
                            'system_description': '',
                            'system_name': 'genie1-ggN1.ie-genie1',
                            'time_remaining': 99,
                        },
                    },
                },
            },
        },
    },
    'total_entries': 3,
}
