expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'routes': {
                        '2001:1:1:a::1/128': {
                            'route': '2001:1:1:a::1/128',
                            'next_hop': {
                                'next_hop_list': {
                                     1: {
                                         'index': 1,
                                         'next_hop_vrf': 'default',
                                         'rnh_active': False,
                                         'next_hop': '2001:10:1:3::1',
                                         'next_hop_netmask': '128',
                                         'outgoing_interface': 'Ethernet1/2',
                                         'bfd_enabled': False,
                                         'resolved_tid': 0,
                                         'preference': 1,
                                     },
                                     2: {
                                        'index': 2,
                                        'next_hop_vrf': 'default',
                                        'rnh_active': False,
                                        'next_hop': '2001:20:1:3::1',
                                        'next_hop_netmask': '128',
                                        'outgoing_interface': 'Ethernet1/3',
                                        'bfd_enabled': False,
                                        'resolved_tid': 0,
                                        'preference': 1,
                                     },
                                },
                            },
                        },
                        '2001:2:2:2::2/128': {
                            'route': '2001:2:2:2::2/128',
                            'next_hop': {
                                'next_hop_list': {
                                    1: {
                                        'index': 1,
                                        'next_hop_vrf': 'default',
                                        'rnh_active': False,
                                        'next_hop': '2001:10:2:3::2',
                                        'next_hop_netmask': '128',
                                        'outgoing_interface': 'Ethernet1/4',
                                        'bfd_enabled': False,
                                        'resolved_tid': 0,
                                        'preference': 1,
                                    },
                                    2: {
                                        'index': 2,
                                        'next_hop_vrf': 'default',
                                        'rnh_active': False,
                                        'next_hop': '2001:20:2:3::2',
                                        'next_hop_netmask': '128',
                                        'outgoing_interface': 'Ethernet1/1',
                                        'bfd_enabled': False,
                                        'resolved_tid': 0,
                                        'preference': 1,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
