

expected_output = {
    'group': {
        'gr1': {
            'mp2mp': {
                'mp1': {
                    'state': 'up',
                    'vpn_id': 100,
                    'vpn_mtu': 1500,
                    'l2_encapsulation': 'VLAN',
                    'auto_discovery': {
                        'BGP': {
                            'state': 'Advertised',
                            'event_name': 'Service Connected',
                            'route_distinguisher': '(auto) 10.36.3.3:32770',
                        },
                    },
                    'import_route_targets': ['10.16.2.2:100'],
                    'export_route_targets': ['10.16.2.2:100'],
                    'signaling_protocol': {
                        'BGP': {
                            'ce_range': 10,
                        },
                    },
                },
            },
            'xc': {
                'mp1.1:2': {
                    'state': 'up',
                    'interworking': 'none',
                    'local_ce_id': 1,
                    'remote_ce_id': 2,
                    'discovery_state': 'Advertised',
                    'ac': {
                        'GigabitEthernet0/1/0/1.1': {
                            'state': 'up',
                            'type': 'VLAN',
                            'num_ranges': 1,
                            'vlan_ranges': ['1', '1'],
                            'mtu': 1500,
                            'xc_id': '0x2000013',
                            'interworking': 'none',
                        },
                    },
                    'pw': {
                        'neighbor': {
                            '10.4.1.1': {
                                'id': {
                                    65538: {
                                        'state': 'up ( established )',
                                        'pw_class': 'not set',
                                        'xc_id': '0x2000013',
                                        'encapsulation': 'MPLS',
                                        'protocol': 'BGP',
                                        'mpls': {
                                            'label': {
                                                'local': '16031',
                                                'remote': '16045',
                                            },
                                            'mtu': {
                                                'local': '1500',
                                                'remote': '1500',
                                            },
                                            'control_word': {
                                                'local': 'enabled',
                                                'remote': 'enabled',
                                            },
                                            'pw_type': {
                                                'local': 'Ethernet VLAN',
                                                'remote': 'Ethernet VLAN',
                                            },
                                            'ce_id': {
                                                'local': '1',
                                                'remote': '2',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
