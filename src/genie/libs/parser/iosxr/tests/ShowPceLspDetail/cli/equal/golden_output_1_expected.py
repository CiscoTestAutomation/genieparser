

expected_output = {
    'pcc': {
        '192.168.0.1': {
            'tunnel_name': 'rtrA_t1',
            'lsps': {
                0: {
                    'source': '192.168.0.1',
                    'destination': '192.168.0.4',
                    'tunnel_id': 1,
                    'lsp_id': 2,
                    'admin_state': 'up',
                    'operation_state': 'up',
                    'setup_type': 'segment routing',
                    'binding_sid': 24013,
                    'pcep_information': {
                        'plsp_id': 2,
                        'flags': {
                            'd': 1,
                            's': 0,
                            'r': 0,
                            'a': 1,
                            'o': 1,
                        }
                    },
                    'paths': {
                        'reported': {
                            'metric_type': 'TE',
                            'accumulated_metric': 42,
                            'sids': {
                                0: {
                                    'type': 'Adj',
                                    'label': 24000,
                                    'local_address': '10.10.10.1',
                                    'remote_address': '10.10.10.2'
                                },
                                1: {
                                    'type': 'Adj',
                                    'label': 24000,
                                    'local_address': '10.19.14.2',
                                    'remote_address': '10.19.14.4'
                                }
                            }
                        },
                        'computed': {
                            'metric_type': 'TE',
                            'accumulated_metric': 42,
                            'sids': {
                                0: {
                                    'type': 'Adj',
                                    'label': 24000,
                                    'local_address': '10.10.10.1',
                                    'remote_address': '10.10.10.2'
                                },
                                1: {
                                    'type': 'Adj',
                                    'label': 24000,
                                    'local_address': '10.19.14.2',
                                    'remote_address': '10.19.14.4'
                                }
                            }
                        },
                        'recorded': {}
                    }
                },
                'event_history': {
                    'June 13 2016 13:28:29': {
                        'report': {
                            'symbolic_name': 'rtrA_t1',
                            'lsp-id': 2,
                            'source': '192.168.0.1',
                            'destination': '192.168.0.4',
                            'flags': {
                                'd': 1,
                                'r': 0,
                                'a': 1,
                                'o': 1,
                                'sig_bw': 0,
                                'act_bw': 0
                            }
                        }
                    },
                    'June 13 2016 13:28:28': {
                        'report': {
                            'symbolic_name': 'rtrA_t1',
                            'lsp-id': 2,
                            'source': '192.168.0.1',
                            'destination': '192.168.0.4',
                            'flags': {
                                'd': 1,
                                'r': 0,
                                'a': 1,
                                'o': 1,
                                'sig_bw': 0,
                                'act_bw': 0
                            }
                        },
                        'create': {
                            'symbolic_name': 'rtrA_t1',
                            'plsp-id': 2,
                            'peer': '192.168.0.1'
                        }
                    }
                }
            }
        }
    }
}
