expected_output = {
    'vrf': {
        'default': {
            'peers': {
                '192.168.20.2': {
                    'label_space_id': {
                        0: {
                            'address_bound': ['192.168.20.2', '3.3.3.3', '192.168.30.1'],
                            'capabilities': {
                                'received': {
                                    'ICCP': {
                                        'maj_ver': 1,
                                        'min_ver': 0,
                                        'type': '0x0405',
                                    },
                                    'dynamic_anouncement': '0x0506',
                                    'typed_wildcard': '0x050B',
                                },
                                'sent': {
                                    'ICCP': {
                                        'maj_ver': 1,
                                        'min_ver': 0,
                                        'type': '0x0405',
                                    },
                                    'dynamic_anouncement': '0x0506',
                                    'typed_wildcard': '0x050B',
                                },
                            },
                            'downstream': True,
                            'ka_interval_ms': 60000,
                            'last_tib_rev_sent': 11,
                            'ldp_discovery_sources': {
                                'interface': {
                                    'Port-channel20': {
                                        'ip_address': {
                                            '192.168.20.2': {
                                                'hello_interval_ms': 5000,
                                                'holdtime_ms': 15000,
                                            },
                                        },
                                    },
                                },
                            },
                            'local_ldp_ident': '2.2.2.2:0',
                            'mpls_ldp_session_protection': {
                                'duration_seconds': 86400,
                                'enabled': True,
                                'state': 'Ready',
                            },
                            'msg_rcvd': 93,
                            'msg_sent': 92,
                            'nsr': 'Not Ready',
                            'password': 'not required, none, in use',
                            'peer_holdtime_ms': 180000,
                            'peer_state': 'estab',
                            'state': 'oper',
                            'tcp_connection': '192.168.20.2.11669 - 2.2.2.2.646',
                            'uptime': '01:14:13',
                        },
                    },
                },
            },
        },
    },
}
