expected_output = {
        'enabled_nv_overlay': True,
        'evpn_multisite_border_gateway': 111111,
        'multisite_convergence_time': 185,
        'nve1': {
            'nve_name': 'nve1',
            'if_state': "up",
            'host_reachability_protocol': "bgp",
            'adv_vmac': True,
            'source_if': "loopback1",
            'multisite_bgw_if': "loopback3",
            'vni': {
                10100: {
                    'vni': 10100,
                    'associated_vrf': True,
                },
                10101: {
                    'vni': 10101,
                    'associated_vrf': False,
                    'multisite_ingress_replication': True,
                    'mcast_group': "231.100.1.1"
                },
                10102: {
                    'vni': 10102,
                    'associated_vrf': False,
                    'multisite_ingress_replication': True,
                    'mcast_group': "231.100.1.1"
                },
                10103: {
                    'vni': 10103,
                    'associated_vrf': False,
                    'multisite_mcast_group': "226.1.1.1",
                    'mcast_group': "231.100.1.1"
                },
                100000: {
                    'vni': 100000,
                    'associated_vrf': True,
                },
                100001: {
                    'vni': 100001,
                    'associated_vrf': True,
                },
                100002: {
                    'vni': 100002,
                    'associated_vrf': True,
                },
                100004: {
                    'vni': 100004,
                    'associated_vrf': True,
                    'multisite_ingress_replication_optimized': True,
                    'mcast_group': "231.200.1.1"
                },
                100006: {
                    'vni': 100006,
                    'associated_vrf': True,
                    'multisite_ingress_replication_optimized': True,
                    'mcast_group': "231.200.1.1"
                },
                100007: {
                    'vni': 100007,
                    'associated_vrf': True,
                    'multisite_mcast_group': "226.2.1.1",
                    'mcast_group': "231.200.1.1"
                },
                10202: {
                    'vni': 10202,
                    'associated_vrf': False,
                    'multisite_ingress_replication': True,
                    'mcast_group': "231.200.1.1"
                },
                10203: {
                    'vni': 10203,
                    'associated_vrf': False,
                    'ingress_replication_protocol_bgp': True
                },
            },
        },
        'multisite': {
            'fabric_links': {
                'Ethernet1/1': {
                    'if_name': 'Ethernet1/1',
                    'if_state': 'up',
                },
                'Ethernet1/2': {
                    'if_name': 'Ethernet1/2',
                    'if_state': 'up',
                }
            },
            'dci_links': {
                'Ethernet1/6': {
                    'if_name': 'Ethernet1/6',
                    'if_state': 'up',
                }
            },
        },
    }
