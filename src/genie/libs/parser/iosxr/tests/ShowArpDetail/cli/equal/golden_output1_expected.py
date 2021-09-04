expected_output = {
        'interfaces': {
                'GigabitEthernet0/0/0/0': {
                        'ipv4': {
                                'neighbors': {
                                        '10.1.2.1': {
                                                'age': '02:55:43',
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
                                        '10.2.3.3': {
                                                'age': '00:13:12',
                                                'ip': '10.2.3.3',
                                                'link_layer_address': '5e00.80ff.0209',
                                                'origin': 'dynamic',
                                                'type': 'ARPA'}
                                }
                        }
                }
        }
}

