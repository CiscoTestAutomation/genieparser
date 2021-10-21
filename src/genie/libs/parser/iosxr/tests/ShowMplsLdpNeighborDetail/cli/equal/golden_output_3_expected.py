

expected_output = {
    'vrf': {
        'default': {
            'peers': {
                '10.16.0.7': {
                    'label_space_id': {
                        0: {
                            'tcp_connection': '10.16.0.7:646 - 10.16.0.9:19323',
                            'graceful_restart': 'No',
                            'session_holdtime': 180,
                            'state': 'Oper',
                            'msg_sent': 24671,
                            'msg_rcvd': 24693,
                            'neighbor': 'Downstream-Unsolicited',
                            'uptime': '2w1d',
                            'address_family': {
                                'ipv4': {
                                    'ldp_discovery_sources': {
                                        'interface': {
                                            'GigabitEthernet0/0/0/1': {}
                                        },
                                    },
                                    'address_bound': ['10.16.0.7', '10.16.27.7', '10.16.78.7', '10.16.79.7'],
                                }
                            },
                            'peer_holdtime': 180,
                            'ka_interval': 60,
                            'peer_state': 'Estab',
                            'nsr': 'Disabled',
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
