expected_output = {
    'isis': {
        'CORE': {
            'process_id': 'CORE',
            'routes_found': True,
            'level': {
                '1': {
                    'level': '1',
                    'system_id': {
                        'XRv9k-PE1': {
                            'system_id': 'XRv9k-PE1',
                            'metric': '--'
                        }
                    }
                },
                '2': {
                    'level': '2',
                    'system_id': {
                        'XRv9k-PE1': {
                            'system_id': 'XRv9k-PE1',
                            'metric': '--'
                        }
                    }
                }
            }
        },
        'ACCESS': {
            'process_id': 'ACCESS',
            'routes_found': True,
            'level': {
                '2': {
                    'level': '2',
                    'system_id': {
                        'XRv9k-PE1': {
                            'system_id': 'XRv9k-PE1',
                            'metric': '--'
                        },
                        'AGG-PE-A': {
                            'Gi0/0/0/0': {
                                'interface_name': 'Gi0/0/0/0',
                                'system_id': 'AGG-PE-A',
                                'metric': '10',
                                'next_hop': 'AGG-PE-A',
                                'snpa': '5001.0002.0001'
                            }
                        },
                        'XRv9k-PE2': {
                            'Gi0/0/0/1': {
                                'interface_name': 'Gi0/0/0/1',
                                'system_id': 'XRv9k-PE2',
                                'metric': '20',
                                'next_hop': 'AGG-PE-B',
                                'snpa': '5001.0006.0003'
                            },
                            'Gi0/0/0/0': {
                                'interface_name': 'Gi0/0/0/0',
                                'system_id': 'XRv9k-PE2',
                                'metric': '20',
                                'next_hop': 'AGG-PE-A',
                                'snpa': '5001.0002.0001'
                            }
                        },
                        'AGG-PE-B': {
                            'Gi0/0/0/1': {
                                'interface_name': 'Gi0/0/0/1',
                                'system_id': 'AGG-PE-B',
                                'metric': '10',
                                'next_hop': 'AGG-PE-B',
                                'snpa': '5001.0006.0003'
                            }
                        }
                    }
                }
            }
        }
    }
}
