expected_output = {
    'nat': {
        '1': {
            'dns': True,
            'external-interface': 'if2',
            'hits': {
                'translate': 5,
                'untranslate': 18
            },
            'internal-interface': 'if1',
            'proxy-arp': False,
            'source': {
                'type': 'static',
                'object-name': 'obj_a',
                'natted-address': '2.2.2.2',
                'real-address-and-mask': '1.1.1.1/32',
                'natted-address-and-mask': '2.2.2.2/32'
            }
        },
        '2': {
            'dns': False,
            'external-interface': 'if4',
            'hits': {
                'translate': 104,
                'untranslate': 203
            },
            'internal-interface': 'if3',
            'proxy-arp': False,
            'source': {
                'type': 'static',
                'object-name': 'obj_b',
                'natted-address': '4.4.4.4',
                'real-address-and-mask': '3.3.3.3/32',
                'natted-address-and-mask': '4.4.4.4/32'
            }
        },
        '3': {
            'dns': True,
            'external-interface': 'if6',
            'hits': {
                'translate': 1000,
                'untranslate': 506
            },
            'internal-interface': 'if5',
            'proxy-arp': True,
            'source': {
                'type': 'static',
                'object-name': 'obj_c',
                'natted-address': '6.6.6.6',
                'real-address-and-mask': '5.5.5.5/32',
                'natted-address-and-mask': '6.6.6.6/32'
            }
        }
    }
}