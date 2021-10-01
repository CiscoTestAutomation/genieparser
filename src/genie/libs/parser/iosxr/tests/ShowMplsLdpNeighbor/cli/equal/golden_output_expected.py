

expected_output = {
    'vrf': {
        'default': {
            'peers': {
                '10.16.0.2': {
                    'label_space_id': {
                        0: {
                            'tcp_connection': '10.16.0.2:646 - 10.16.0.9:38143',
                            'graceful_restart': 'No',
                            'session_holdtime': 180,
                            'state': 'Oper',
                            'msg_sent': 24710,
                            'msg_rcvd': 24702,
                            'neighbor': 'Downstream-Unsolicited',
                            'uptime': '2w0d',
                            'address_family': {
                                'ipv4': {
                                    'ldp_discovery_sources': {
                                        'interface': {
                                            'GigabitEthernet0/0/0/0': {}
                                        },
                                    },
                                    'address_bound': ['10.16.0.2', '10.16.27.2', '10.16.28.2', '10.16.29.2']
                                }
                            }
                        },
                    },
                },
                '10.16.0.7': {
                    'label_space_id': {
                        0: {
                            'tcp_connection': '10.16.0.7:646 - 10.16.0.9:19323',
                            'graceful_restart': 'No',
                            'session_holdtime': 180,
                            'state': 'Oper',
                            'msg_sent': 24664,
                            'msg_rcvd': 24686,
                            'neighbor': 'Downstream-Unsolicited',
                            'uptime': '2w0d',
                            'address_family': {
                                'ipv4': {
                                    'ldp_discovery_sources': {
                                        'interface': {
                                            'GigabitEthernet0/0/0/1': {}
                                        },
                                    },
                                    'address_bound': ['10.16.0.7', '10.16.27.7', '10.16.78.7', '10.16.79.7'],
                                }
                            }
                        },
                    },
                },
            },
        }
    }
}
