

expected_output = {
    'vrf': {
        'VRF1': {
            'peer': {
                '10.4.1.1': {
                    'connect_source_address': '10.16.2.2',
                    'elapsed_time': '6d17h',
                    'nsr': {
                        'oper_downs': 0,
                        'state': 'Unknown',
                        'up_down_time': '6d17h',
                    },
                    'password': 'None',
                    'peer_as': 65000,
                    'peer_name': '?',
                    'reset': '0',
                    'sa_filter': {
                        'in': {
                            '(S,G)': {
                                'filter': 'none',
                            },
                            'RP': {
                                'filter': 'none',
                            },
                        },
                        'out': {
                            '(S,G)': {
                                'filter': 'none',
                            },
                            'RP': {
                                'filter': 'none',
                            },
                        },
                    },
                    'sa_request': {
                        'input_filter': 'none',
                        'sa_request_to_peer': 'disabled',
                    },
                    'session_state': 'Established',
                    'statistics': {
                        'conn_count_cleared': '6d17h',
                        'output_message_discarded': 0,
                        'queue': {
                            'size_input': 0,
                            'size_output': 0,
                        },
                        'received': {
                            'sa_message': 31080,
                            'tlv_message': 10361,
                        },
                        'sent': {
                            'tlv_message': 19335,
                        },
                    },
                    'timer': {
                        'keepalive_interval': 30,
                        'peer_timeout_interval': 75,
                    },
                    'ttl_threshold': 2,
                },
            },
        },
    },
}
