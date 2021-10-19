
expected_output = {
    'interfaces':{
        'Port-channel1.1': {
                'encapsulation': {
                'first_dot1q': 1,
                'dot1q_native': True,
                'type': 'dot1Q'
            },
            'ipv4': { 'ip': '1.1.1.1',
                        'netmask': '255.255.255.252'},
            'ipv4_secondary': { '2.2.2.2': { 'ip': '2.2.2.2',
                                            'netmask': '255.255.255.252'},
                                '3.3.3.2': { 'ip': '3.3.3.2',
                                            'netmask': '255.255.255.252'},
                                },
            'vrf': 'TEST'
        }
    }
}