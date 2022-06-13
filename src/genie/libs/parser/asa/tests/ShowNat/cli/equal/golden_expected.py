expected_output = {'nat': { 1: {'from-interface': 'if1',
                                'to-interface:': 'if2',
                                'type': 'static',
                                'dns': True,
                                'proxy-arp': True,
                                'object-name': 'obj_a',
                                'hits': {
                                    'translate': 5,
                                    'untranslate': 18
                                },
                                'source': '1.1.1.1/32',
                                'translated': '2.2.2.2/32'
                                }},
                          { 2: {'from-interface': 'if3',
                                'to-interface:': 'if4',
                                'type': 'static',
                                'dns': False,
                                'proxy-arp': True,
                                'object-name': 'obj_b',
                                'hits': {
                                    'translate': 104,
                                    'untranslate': 203
                                },
                                'source': '3.3.3.3/32',
                                'translated': '4.4.4.4/32'
                                }}, 
                          { 3: {'from-interface': 'if5',
                                'to-interface:': 'if6',
                                'type': 'static',
                                'dns': True,
                                'proxy-arp': False,
                                'object-name': 'obj_c',
                                'hits': {
                                    'translate': 1000,
                                    'untranslate': 506
                                },
                                'source': '5.5.5.5/32',
                                'translated': '6.6.6.6/32'
                                }}
                  } 
                   
