
expected_output = {
    'vrf':
        {'default':
            {'interfaces':
                {'GigabitEthernet0/0/0/0':
                    {'address_family':
                        {'ipv4':
                            {'address': ['10.2.3.2'],
                            'bfd':
                                {'enable': False,
                                'interval': 0.150,
                                'detection_multiplier': 3,
                                },
                            'dr': 'this system',
                            'dr_priority': 1,
                            'flags': 'B P',
                            'hello_interval': 30,
                            'hello_expiration': '00:00:01',
                            'nbr_count': 1,
                            'neighbor_filter': '-',
                            'override_interval': 2500,
                            'oper_status': 'on',
                            'primary_address': '10.2.3.2',
                            'propagation_delay': 500}}},
                'GigabitEthernet0/0/0/1':
                    {'address_family':
                        {'ipv4':
                            {'address': ['10.1.2.2'],
                            'bfd':
                                {'enable': False,
                                'interval': 0.150,
                                'detection_multiplier': 3,
                                },
                            'dr': '10.1.2.3',
                            'dr_priority': 1,
                            'flags': 'NB P',
                            'hello_interval': 30,
                            'hello_expiration': '00:00:07',
                            'nbr_count': 2,
                            'neighbor_filter': '-',
                            'override_interval': 2500,
                            'oper_status': 'on',
                            'primary_address': '10.1.2.2',
                            'propagation_delay': 500}}},
                'Loopback0':
                    {'address_family':
                        {'ipv4':
                            {'address': ['10.16.2.2'],
                            'bfd':
                                {'enable': False,
                                'interval': 0.150,
                                'detection_multiplier': 3,
                                },
                            'dr': 'this system',
                            'dr_priority': 1,
                            'flags': 'B P V',
                            'hello_interval': 30,
                            'hello_expiration': '00:00:15',
                            'nbr_count': 1,
                            'neighbor_filter': '-',
                            'override_interval': 2500,
                            'oper_status': 'on',
                            'primary_address': '10.16.2.2',
                            'propagation_delay': 500}}}}}}}

