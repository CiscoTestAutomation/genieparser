

expected_output = {
    'vrf': {
        'all': {
            'peers': {
                '192.168.70.6': {
                    'label_space_id': {
                        0: {
                            'tcp_connection': '192.168.70.6:15332 - 192.168.1.1:646',
                            'graceful_restart': 'Yes (Reconnect Timeout: 120 sec, Recovery: 180 sec)',
                            'session_holdtime': 180,
                            'state': 'Oper',
                            'msg_sent': 851,
                            'msg_rcvd': 232,
                            'neighbor': 'Downstream-Unsolicited',
                            'uptime': '00:02:44',
                            'address_family': {
                                'ipv4': {
                                    'ldp_discovery_sources': {
                                        'interface': {
                                            'Bundle-Ether1.3': {}
                                        },
                                        'targeted_hello': {
                                            '192.168.1.1': {
                                                '192.168.70.6': {
                                                    'active': False,
                                                },
                                            },
                                        }
                                    },
                                    'address_bound': ['10.10.10.1', '10.126.249.223', '10.126.249.224', '10.76.23.2',
                                                      '10.219.1.2', '10.19.1.2', '10.76.1.2', '10.135.1.2',
                                                      '10.151.1.2', '192.168.106.1', '192.168.205.1', '192.168.51.1',
                                                      '192.168.196.1', '192.168.171.1', '192.168.70.6'],
                                }
                            },
                            'peer_holdtime': 180,
                            'ka_interval': 60,
                            'peer_state': 'Estab',
                            'nsr': 'Operational',
                            'clients': 'Session Protection',
                            'session_protection': {
                                'session_state': 'Ready',
                                'duration_int': 86400,
                            },
                            'capabilities': {
                                'sent': {
                                    '0x508': 'MP: Point-to-Multipoint (P2MP)',
                                    '0x509': 'MP: Multipoint-to-Multipoint (MP2MP)',
                                    '0x50b': 'Typed Wildcard FEC',
                                },
                                'received': {
                                    '0x508': 'MP: Point-to-Multipoint (P2MP)',
                                    '0x509': 'MP: Multipoint-to-Multipoint (MP2MP)',
                                    '0x50b': 'Typed Wildcard FEC',
                                },
                            },
                        },
                    },
                },
            },
        }
    }
}
