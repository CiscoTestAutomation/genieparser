expected_output = {
    'mac_table': {
        'vlans': {
            '10': {
                'mac_addresses': {
                    '0000.0c07.ac0a': {
                        'entry': '*',
                        'interfaces': {
                            'Port-channel4': {
                                'age': '0',
                                'interface': 'Port-channel4',
                                'mac_type': 'dynamic',
                            },
                        },
                        'mac_address': '0000.0c07.ac0a',
                        'ntfy': 'F',
                        'secure': 'F',
                    },
                },
                'vlan': '10',
            },
            '191': {
                'mac_addresses': {
                    'b4de.31f2.4a10': {
                        'entry': '*',
                        'interfaces': {
                            'Ethernet1/20': {
                                'age': '0',
                                'interface': 'Ethernet1/20',
                                'mac_type': 'dynamic',
                            },
                        },
                        'mac_address': 'b4de.31f2.4a10',
                        'ntfy': 'F',
                        'secure': 'F',
                    },
                },
                'vlan': '191',
            },
            '3156': {
                'mac_addresses': {
                    '0000.0c9f.fc54': {
                        'drop': {
                            'age': '-',
                            'drop': True,
                            'mac_type': 'static',
                        },
                        'entry': '*',
                        'mac_address': '0000.0c9f.fc54',
                        'ntfy': 'F',
                        'secure': 'F',
                    },
                },
                'vlan': '3156',
            },
            '392': {
                'mac_addresses': {
                    '40ce.2423.1f0b': {
                        'entry': '*',
                        'interfaces': {
                            'Port-channel100': {
                                'age': '0',
                                'interface': 'Port-channel100',
                                'mac_type': 'dynamic',
                            },
                        },
                        'mac_address': '40ce.2423.1f0b',
                        'ntfy': 'F',
                        'secure': 'F',
                    },
                },
                'vlan': '392',
            },
            '43': {
                'mac_addresses': {
                    '0000.0c9f.f02b': {
                        'entry': 'G',
                        'interfaces': {
                            'Vlan43(R)': {
                                'age': '-',
                                'interface': 'Vlan43(R)',
                                'mac_type': 'static',
                            },
                        },
                        'mac_address': '0000.0c9f.f02b',
                        'ntfy': 'F',
                        'secure': 'F',
                    },
                },
                'vlan': '43',
            },
        },
    },
}