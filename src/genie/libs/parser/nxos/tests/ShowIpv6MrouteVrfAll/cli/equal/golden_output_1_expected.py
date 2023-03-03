

expected_output = {
    'vrf': 
        {'VRF': 
            {'address_family': 
                {'ipv6': {}}},
                    'VRF1': 
                        {'address_family': 
                            {'ipv6': 
                                {'multicast_group': 
                                    {'ff1e:1111::1:0/128': 
                                        {'source_address': 
                                            {'*': 
                                                {'flags': 'ipv6 '                                                                                                                           'mld '
                                        'pim6',                                                                                                                  'incoming_interface_list': {'loopback10': {'rpf_nbr': '2001:db8:4401:9999::1'}},
                                'oil_count': '3',
                                'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                            'oil_uptime': '00:02:58'},
                                                            'Ethernet1/33.11': {'oil_flags': 'mld',
                                                                                'oil_uptime': '00:04:03'},
                                                            'port-channel1001': {'oil_flags': 'pim6',
                                                                                'oil_uptime': '00:04:01'}},
                                'uptime': '00:04:03'},
                        '2001::222:1:1:1234/128': {'flags': 'ipv6 '
                                                            'm6rib '
                                                            'pim6',
                                                    'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1234',
                                                                                                    'internal': True}},

                                                    'oil_count': '3',
                                                    'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                'oil_uptime': '00:02:58'},
                                                                                'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                    'oil_uptime': '00:04:03'},
                                                                                'port-channel1001': {'oil_flags': 'pim6',
                                                                                                    'oil_uptime': '00:04:01'}},
                                                    'uptime': '00:04:03'},
                        '2001::222:1:2:1234/128': {'flags': 'ipv6 '
                                                            'm6rib '
                                                            'pim6',
                                                    'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234',
                                                                                                    'internal': True}},
                                                    'oil_count': '3',
                                                    'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                'oil_uptime': '00:02:58'},
                                                                                'Ethernet1/33.11': {'oif_rpf': 'RPF',
                                                                                                    'oil_flags': 'm6rib',
                                                                                                    'oil_uptime': '00:04:03'},
                                                                                'port-channel1001': {'oil_flags': 'pim6',
                                                                                                    'oil_uptime': '00:04:01'}},
                                                    'uptime': '00:04:03'},
                        '2001::222:2:3:1234/128': {'flags': 'ipv6 '
                                                            'm6rib '
                                                            'pim6',
                                                    'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10',
                                                                                                 'internal': True}},
                                                    'oil_count': '1',
                                                    'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                    'oil_uptime': '00:04:03'}},
                                                    'uptime': '00:04:03'},
                        '2001::222:2:44:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                    'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10',
                                                                                                    'internal': True}},
                                                    'oil_count': '1',
                                                    'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                    'oil_uptime': '00:04:03'}},
                                                    'uptime': '00:04:03'}}},
'ff1e:1111:ffff::/128': {'source_address': {'*': {'flags': 'ipv6 '
                                            'mld '
                                            'pim6',
                                'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1'}},
                                'oil_count': '2',
                                'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                'oil_uptime': '00:04:01'},
                                                            'Ethernet1/33.11': {'oil_flags': 'mld',
                                                                                'oil_uptime': '00:04:03'}},
                                'uptime': '00:04:03'},
                            '2001::222:1:1:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1234',
                                                                                                        'internal': True}},
                                                        'oil_count': '3',
                                                        'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                    'oil_uptime': '00:02:58'},
                                                                                    'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:03'},
                                                                                    'port-channel1001': {'oil_flags': 'pim6',
                                                                                                        'oil_uptime': '00:04:00'}},
                                                        'uptime': '00:04:03'},
                            '2001::222:1:2:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234',
                                                                                                        'internal': True}},
                                                        'oil_count': '2',
                                                        'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                    'oil_uptime': '00:04:01'},
                                                                                    'Ethernet1/33.11': {'oif_rpf': 'RPF',
                                                                                                        'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:03'}},
                                                        'uptime': '00:04:03'},
                            '2001::222:2:3:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10',
                                                                                                    'internal': True}},
                                                        'oil_count': '1',
                                                        'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:03'}},
                                                        'uptime': '00:04:03'},
                            '2001::222:2:44:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10',
                                                                                                    'internal': True}},
                                                        'oil_count': '1',
                                                        'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:03'}},
                                                        'uptime': '00:04:03'}}},
'ff1e:2222:ffff::/128': {'source_address': {'*': {'flags': 'ipv6 '
                                            'mld '
                                            'pim6',
                                'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                'oil_count': '1',
                                'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'mld',
                                                                                'oil_uptime': '00:04:03'}},
                                'uptime': '00:04:03'},
                            '2001::222:1:1:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1234'}},
                                                        'oil_count': '2',
                                                        'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                    'oil_uptime': '00:04:01'},
                                                                                    'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:03'}},
                                                        'uptime': '00:04:03'},
                            '2001::222:1:2:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234'}},
                                                        'oil_count': '2',
                                                        'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                    'oil_uptime': '00:04:01'},
                                                                                    'Ethernet1/33.11': {'oif_rpf': 'RPF',
                                                                                                        'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:03'}},
                                                        'uptime': '00:04:03'},
                            '2001::222:2:3:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                                        'oil_count': '1',
                                                        'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:02'}},
                                                        'uptime': '00:04:02'},
                            '2001::222:2:44:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                                        'oil_count': '1',
                                                        'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:02'}},
                                                        'uptime': '00:04:02'}}},
'ff1e:2222:ffff::1:0/128': {'source_address': {'*': {'flags': 'ipv6 '
                                            'mld '
                                            'pim6',
                                    'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                    'oil_count': '1',
                                    'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'mld',
                                                                                    'oil_uptime': '00:04:03'}},
                                    'uptime': '00:04:03'},
                                '2001::222:1:1:1234/128': {'flags': 'ipv6 '
                                                                    'm6rib '
                                                                    'pim6',
                                                        'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1234'}},
                                                        'oil_count': '3',
                                                        'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                        'oil_uptime': '00:02:58'},
                                                                                    'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:03'},
                                                                                    'port-channel1001': {'oil_flags': 'pim6',
                                                                                                            'oil_uptime': '00:04:02'}},
                                                        'uptime': '00:04:03'},
                                '2001::222:1:2:1234/128': {'flags': 'ipv6 '
                                                                    'm6rib '
                                                                    'pim6',
                                                        'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234'}},
                                                        'oil_count': '2',
                                                        'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                        'oil_uptime': '00:04:02'},
                                                                                    'Ethernet1/33.11': {'oif_rpf': 'RPF',
                                                                                                        'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:03'}},
                                                        'uptime': '00:04:03'}}},
'ff1e:3333::1:0/128': {'source_address': {'*': {'flags': 'ipv6 '                                                                                                                           'mld '
                                        'pim6',                                                                                                                  'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                'oil_count': '1',
                                'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'mld',
                                                                                'oil_uptime': '00:04:03'}},
                                'uptime': '00:04:03'},
                        '2001::222:1:1:1234/128': {'flags': 'ipv6 '
                                                            'm6rib '
                                                            'pim6',
                                                    'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1234'}},
                                                    'oil_count': '2',
                                                    'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                'oil_uptime': '00:04:01'},
                                                                                'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                    'oil_uptime': '00:04:03'}},
                                                    'uptime': '00:04:03'},
                        '2001::222:1:2:1234/128': {'flags': 'ipv6 '
                                                            'm6rib '
                                                            'pim6',
                                                    'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234'}},
                                                    'oil_count': '3',
                                                    'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                'oil_uptime': '00:02:58'},
                                                                                'Ethernet1/33.11': {'oif_rpf': 'RPF',
                                                                                                    'oil_flags': 'm6rib',
                                                                                                    'oil_uptime': '00:04:03'},
                                                                                'port-channel1001': {'oil_flags': 'pim6',
                                                                                                    'oil_uptime': '00:04:01'}},
                                                    'uptime': '00:04:03'}}},
'ff1e:3333:ffff::/128': {'source_address': {'*': {'flags': 'ipv6 '
                                            'mld '
                                            'pim6',
                                'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                'oil_count': '1',
                                'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'mld',
                                                                                'oil_uptime': '00:04:03'}},
                                'uptime': '00:04:03'},
                            '2001::222:1:1:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/33.10': {'rpf_nbr': '2001::222:1:1:1234'}},
                                                        'oil_count': '3',
                                                        'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                    'oil_uptime': '00:02:58'},
                                                                                    'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:03'},
                                                                                    'port-channel1001': {'oil_flags': 'pim6',
                                                                                                        'oil_uptime': '00:04:01'}},
                                                        'uptime': '00:04:03'},
                            '2001::222:1:2:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/33.11': {'rpf_nbr': '2001::222:1:2:1234'}},
                                                        'oil_count': '2',
                                                        'outgoing_interface_list': {'Ethernet1/26': {'oil_flags': 'pim6',
                                                                                                    'oil_uptime': '00:04:01'},
                                                                                    'Ethernet1/33.11': {'oif_rpf': 'RPF',
                                                                                                        'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:03'}},
                                                        'uptime': '00:04:03'},
                            '2001::222:2:3:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                                        'oil_count': '1',
                                                        'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:01'}},
                                                        'uptime': '00:04:01'},
                            '2001::222:2:44:1234/128': {'flags': 'ipv6 '
                                                                'm6rib '
                                                                'pim6',
                                                        'incoming_interface_list': {'Ethernet1/26': {'rpf_nbr': 'fe80::10'}},
                                                        'oil_count': '1',
                                                        'outgoing_interface_list': {'Ethernet1/33.11': {'oil_flags': 'm6rib',
                                                                                                        'oil_uptime': '00:04:00'}},
                                                        'uptime': '00:04:00'}}},
                                                              'ff30::/12': {'source_address': {'*': {'flags': 'ipv6 '
                                                                                                              'pim6',
                                                                                                     'incoming_interface_list': {'Null': {'rpf_nbr': '0::'}},
                                                                                                     'oil_count': '0',
                                                                                                     'uptime': '19:55:47'}}}}}}},
     'default': {'address_family': {'ipv6': {'multicast_group': {'ff30::/12': {'source_address': {'*': {'flags': 'ipv6 '
                                                                                                                 'pim6',
                                                                                                        'incoming_interface_list': {'Null': {'rpf_nbr': '0::'}},
                                                                                                        'oil_count': '0',
                                                                                                        'uptime': '00:11:23'}}}}}}}}}

