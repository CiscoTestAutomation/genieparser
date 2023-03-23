expected_output= {
    'interface': {
        '1': {
            'interface': 'Tunnel13',
            'peer': {
                '11.0.1.1': {
                    'port': {
                        '500': {
                            'ike_sa': {
                                '1': {
                                    'local': '11.0.1.2',
                                    'local_port': '500',
                                    'remote': '11.0.1.1',
                                    'remote_port': '500',
                                    'sa_status': 'Active',
                                    'session_id': '0',
                                    'version': 'IKEv1',
                                },
                            },
                            'ipsec_flow': {
                                'permit 47 host 11.0.1.2 host 11.0.1.1': {
                                    'active_sas': 2,
                                    'origin': 'crypto map',
                                },
                            },
                        },
                    },
                },
            },
            'session_status': 'UP-ACTIVE',
        },
        '2': {
            'interface': 'GigabitEthernet0/1',
            'peer': {
                '2001:db8:4:4::4': {
                    'port': {
                        '500': {
                            'ike_sa': {
                                '1': {
                                    'local': '2001:db8:2:2::2',
                                    'local_port': '500',
                                    'remote': '2001:db8:4:4::4',
                                    'remote_port': '500',
                                    'sa_status': 'Active',
                                    'session_id': '0',
                                    'version': 'IKEv1',
                                },
                            },
                            'ipsec_flow': {
                                'permit ipv6 2001:db8:2:2::/64 2001:db8:5:5::/64': {
                                    'active_sas': 2,
                                    'origin': 'crypto map',
                                },
                            },
                        },
                    },
                },
            },
            'session_status': 'UP-ACTIVE',
        },
    }
}