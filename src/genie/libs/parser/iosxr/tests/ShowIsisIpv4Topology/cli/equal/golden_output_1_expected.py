expected_output = {
    'isis': {
        '1': {
            'process_id': '1',
            'routes_found': False
        },
        '10': {
            'process_id': '10',
            'routes_found': True,
            'level': {
                '2': {
                    'level': '2',
                    'system_id': {
                        'P-9001-1': {
                            'system_id': 'P-9001-1',
                            'metric': '--'
                        },
                        'PE-9001-1': {
                            'Gi0/0/0/1.19': {
                                'interface_name': 'Gi0/0/0/1.19',
                                'system_id': 'PE-9001-1',
                                'metric': '10',
                                'next_hop': 'PE-9001-1',
                                'snpa': '28c7.cebd.7c23'
                            },
                            'BE10.10': {
                                'interface_name': 'BE10.10',
                                'system_id': 'PE-9001-1',
                                'metric': '10',
                                'next_hop': 'PE-9001-1',
                                'snpa': '5087.890d.27c3'
                            }
                        }
                    }
                }
            }
        },
        '99': {
            'process_id': '99',
            'routes_found': True,
            'level': {
                '1': {
                    'level': '1',
                    'system_id': {
                        'P-9001-1': {
                            'system_id': 'P-9001-1',
                            'metric': '--'
                        }
                    }
                }
            }
        }
    }
}
