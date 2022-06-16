expected_output = {'nat': { 1: {'internal-interface': 'if1',
                                'external-interface:': 'if2',
                                'source': {
                                    'type': 'static',
                                    'object-name': 'obj_a',
                                    'natted-address': '1.1.1.1',
                                    'real-address-and-mask': '1.1.1.1/32',
                                    'natted-address-and-mask': '2.2.2.2/32'
                                },
                                'dns': True,
                                'proxy-arp': True,
                                'hits': {
                                    'translate': 5,
                                    'untranslate': 18
                                }
                            }},
                          { 2: {'internal-interface': 'if3',
                                'external-interface:': 'if4',
                                'source': {
                                    'type': 'static',
                                    'object-name': 'obj_b',
                                    'natted-address': '3.3.3.3'
                                    'real-address-and-mask': '3.3.3.3/32',
                                    'natted-address-and-mask': '4.4.4.4/32'
                                },
                                'dns': False,
                                'proxy-arp': True,
                                'hits': {
                                    'translate': 104,
                                    'untranslate': 203
                                }
                            }}, 
                          { 3: {'internal-interface': 'if5',
                                'external-interface:': 'if6',
                                'source': {
                                    'type': 'static',
                                    'object-name': 'obj_c',
                                    'natted-address': '6.6.6.6/32'
                                    'real-address-and-mask': '5.5.5.5/32',
                                    'natted-address-and-mask': '6.6.6.6/32'
                                }
                                'dns': True,
                                'proxy-arp': False,
                                'hits': {
                                    'translate': 1000,
                                    'untranslate': 506
                                }
                            }}
                  } 
