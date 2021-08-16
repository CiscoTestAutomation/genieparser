expected_output = {
    'interface': {
        'Ethernet1/1': {
            'description': 'genie test',
            'switchport': False,
            'mtu': 9216,
            'vrf_member': 'TEST',
            'ip_address': '10.1.1.1/30'
        },
        'port-channel5': {
            'description': 'Port Channel Config Tst',
            'switchport_mode': 'trunk',
            'trunk_native_vlan': '2253',
            'trunk_vlans': '2253',
            'speed': 10000,
            'vpc': '5'
        },
        'nve1': {
            'host_reachability_protocol': 'bgp',
            'member_vni': {'2000002': {'mcast_group': '227.1.1.1',
                                       'suppress_arp': True},
                           '2000003': {'mcast_group': '227.1.1.1',
                                       'suppress_arp': True},
                           '2000004': {'mcast_group': '227.1.1.1',
                                       'suppress_arp': True},
                           '2000005': {'mcast_group': '227.1.1.1',
                                       'suppress_arp': True},
                           '2000006': {'mcast_group': '227.1.1.1',
                                       'suppress_arp': True},
                           '2000007': {'mcast_group': '227.1.1.1',
                                       'suppress_arp': True},
                           '2000008': {'mcast_group': '227.1.1.1',
                                       'suppress_arp': True},
                           '2000009': {'mcast_group': '227.1.1.1',
                                       'suppress_arp': True},
                           '2000010': {'mcast_group': '227.1.1.1',
                                       'suppress_arp': True},
                           '3003002': {'associate_vrf': True},
                           '3003003': {'associate_vrf': True},
                           '3003004': {'associate_vrf': True},
                           '3003005': {'associate_vrf': True},
                           '3003006': {'associate_vrf': True},
                           '3003007': {'associate_vrf': True},
                           '3003008': {'associate_vrf': True},
                           '3003009': {'associate_vrf': True},
                           '3003010': {'associate_vrf': True}},
            'shutdown': False,
            'source_interface': 'loopback0'
        }
    }
}