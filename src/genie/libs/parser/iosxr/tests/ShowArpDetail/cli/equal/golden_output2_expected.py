expected_output = {
        'interfaces': {
                'GigabitEthernet0/0/0/0': {
                        'ipv4': {
                                'neighbors': {
                                        '10.1.2.1': {
                                                'age': '02:56:20',
                                                'ip': '10.1.2.1',
                                                'link_layer_address': 'fa16.3eff.06af',
                                                'origin': 'dynamic',
                                                'type': 'ARPA'},
                                        '10.1.2.2': {
                                                'age': '-',
                                                'ip': '10.1.2.2',
                                                'link_layer_address': 'fa16.3eff.f847',
                                                'origin': 'static',
                                                'type': 'ARPA'}
                                }
                        }
                },
                'GigabitEthernet0/0/0/1': {
                        'ipv4': {
                                'neighbors': {
                                        '10.2.3.2': {
                                                'age': '-',
                                                'ip': '10.2.3.2',
                                                'link_layer_address': 'fa16.3eff.c3f7',
                                                'origin': 'static',
                                                'type': 'ARPA'},
                                        '10.2.3.3': {'age': '00:13:49',
                                                'ip': '10.2.3.3',
                                                'link_layer_address': '5e00.80ff.0209',
                                                'origin': 'dynamic',
                                                'type': 'ARPA'}
                                }
                        }
                },
                'Bundle-Ether1': {
                        'ipv4': {
                                'neighbors': {
                                        '10.3.4.3': {
                                                'age': '-',
                                                'ip': '10.3.4.3',
                                        'link_layer_address': '6c6c.d3ff.468b',
                                        'origin': 'static',
                                        'type': 'ARPA'},
                                '10.3.4.4': {
                                                 'age': '01:55:46',
                                                'ip': '10.3.4.4',
                                        'link_layer_address': '0896.adff.66f8',
                                        'origin': 'dynamic',
                                        'type': 'ARPA'}
                                }
                        }
                }
        }
}

