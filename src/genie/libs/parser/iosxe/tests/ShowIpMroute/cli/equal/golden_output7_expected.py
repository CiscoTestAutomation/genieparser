expected_output = {
    'vrf': {
        'green': {
            'address_family': {
                'ipv4': {
                    'multicast_group': {
                        '239.1.1.1': {
                            'source_address': {
                                '10.1.101.4': {
                                    'expire': '00:02:33',
                                    'flags': 'FTGqx',
                                    'incoming_interface_list': {
                                        'Vlan101': {
                                            'rpf_nbr': '0.0.0.0'
                                            }
                                        },
                                    'msdp_learned': False,
                                    'outgoing_interface_list': {
                                        'Vlan102': {
                                            'expire': '00:02:49',
                                            'state_mode': 'forward/sparse',
                                            'uptime': '00:00:10'
                                        },
                                        'Vlan901': {
                                            'expire': '00:02:34',
                                            'state_mode': 'forward/sparse',
                                            'uptime': '00:00:28',
                                            'vxlan_nxthop': '239.1.1.1',
                                            'vxlan_version': 'v4',
                                            'vxlan_vni': '50901'
                                        }
                                    },
                                    'rp_bit': False,
                                    'rpf_nbr': '0.0.0.0',
                                    'uptime': '00:00:28'}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
