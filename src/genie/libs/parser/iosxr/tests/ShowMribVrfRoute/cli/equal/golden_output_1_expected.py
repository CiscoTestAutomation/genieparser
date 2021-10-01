
expected_output = {
    'vrf':
        {'default':
            {'address_family':
                {'ipv4':
                    {'multicast_group':
                        {'224.0.0.0/24':
                            {'source_address':
                                {'*':
                                    {'flags': 'D P',
                                    'uptime': '00:00:58'}}},
                        '224.0.0.0/4':
                            {'source_address':
                                {'*':
                                    {'flags': 'C RPF P',
                                    'rpf_nbr': '0.0.0.0',
                                    'uptime': '00:00:58'}}},
                        '224.0.1.39':
                            {'source_address':
                                {'*':
                                    {'flags': 'S P',
                                    'uptime': '00:00:58'}}},
                        '227.1.1.1':
                            {'source_address':
                                {'*':
                                    {'flags': 'C RPF MD MH CD',
                                    'mdt_ifh': '0x803380',
                                    'mvpn_payload': 'ipv4',
                                    'mvpn_remote_tid': '0x0',
                                    'mvpn_tid': '0xe000001f',
                                    'outgoing_interface_list':
                                        {'Loopback0':
                                            {'flags': 'F NS',
                                            'uptime': '00:00:54'}},
                                    'rpf_nbr': '0.0.0.0',
                                    'uptime': '00:00:54'},
                                '192.168.0.12':
                                    {'flags': 'RPF ME MH',
                                    'incoming_interface_list':
                                        {'Loopback0':
                                            {'flags': 'F NS',
                                            'uptime': '00:00:58',
                                            'rpf_nbr': '192.168.0.12',}},
                                    'mdt_ifh': '0x803380',
                                    'mvpn_payload': 'ipv4',
                                    'mvpn_remote_tid': '0x0',
                                    'mvpn_tid': '0xe000001f',
                                    'outgoing_interface_list':
                                        {'Loopback0':
                                            {'flags': 'F A',
                                            'uptime': '00:00:54'}},
                                    'rpf_nbr': '192.168.0.12',
                                    'uptime': '00:00:54'}}},
                        '232.0.0.0/8':
                            {'source_address':
                                {'*':
                                    {'flags': 'D P',
                                    'uptime': '00:00:58'}}},
                        '232.1.1.1':
                            {'source_address':
                                {'172.16.1.2':
                                    {'flags': 'RPF',
                                    'incoming_interface_list':
                                        {'Bundle-Ether2.200':
                                            {'flags': 'A',
                                            'uptime': '1w3d',
                                            'rpf_nbr': '10.100.1.1',}},
                                    'outgoing_interface_list':
                                        {'Bundle-Ether1.100':
                                            {'flags': 'F NS',
                                            'uptime': '5d22h',
                                            'location': '0/12/CPU0'}},
                                    'rpf_nbr': '10.100.1.1',
                                    'uptime': '13w2d'}}},
                        '236.5.5.5':
                            {'source_address':
                                {'*':
                                    {'flags': 'C RPF MD MH CD',
                                    'mdt_ifh': '0x803480',
                                    'mvpn_remote_tid': '0xe0800018',
                                    'mvpn_tid': '0xe0000018',
                                    'outgoing_interface_list':
                                        {'Loopback0':
                                            {'flags': 'F NS',
                                            'uptime': '00:00:54'}},
                                    'rpf_nbr': '0.0.0.0',
                                    'uptime': '00:00:54'},
                                '192.168.0.12':
                                    {'flags': 'RPF ME MH',
                                    'incoming_interface_list':
                                        {'Loopback0':
                                            {'flags': 'F A',
                                            'uptime': '00:00:54',
                                            'rpf_nbr': '192.168.0.12',}},
                                    'mdt_ifh': '0x803480',
                                    'mvpn_remote_tid': '0xe0800018',
                                    'mvpn_tid': '0xe0000018',
                                    'outgoing_interface_list':
                                        {'Loopback0':
                                            {'flags': 'F A',
                                            'uptime': '00:00:54'}},
                                    'rpf_nbr': '192.168.0.12',
                                    'uptime': '00:00:54'},
                                '192.168.0.22':
                                    {'flags': 'C RPF MD MH CD',
                                    'mdt_ifh': '0x803480',
                                    'mvpn_remote_tid': '0xe0800018',
                                    'mvpn_tid': '0xe0000018',
                                    'outgoing_interface_list':
                                        {'GigabitEthernet0/1/0/1':
                                            {'flags': 'NS',
                                            'uptime': '00:00:01'},
                                        'Loopback0':
                                            {'flags': 'F NS',
                                            'uptime': '00:00:13'}},
                                    'rpf_nbr': '10.121.1.22',
                                    'uptime': '00:00:13'}}}}}}}}}
