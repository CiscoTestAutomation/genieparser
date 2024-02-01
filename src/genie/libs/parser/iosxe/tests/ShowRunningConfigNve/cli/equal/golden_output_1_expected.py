expected_output = {
    'bgp': {
        '65001': {
            'address_family': {
                'ipv4 blue': {
                    'advertise_l2vpn_evpn': True,
                    'redistribute_connected': True,
                    'redistribute_static': True
                },
                'ipv4 green': {
                    'advertise_l2vpn_evpn': True,
                    'redistribute_connected': True,
                    'redistribute_static': True
                },
                'ipv6 blue': {
                    'advertise_l2vpn_evpn': True,
                    'redistribute_connected': True,
                    'redistribute_static': True
                },
                'ipv6 green': {
                    'advertise_l2vpn_evpn': True,
                    'redistribute_connected': True,
                    'redistribute_static': True
                },
                'l2vpn evpn': {
                    'address_family_neighbor': {
                        '172.16.255.1': {
                            'community_attr_to_send': 'extended'
                        },
                        '172.16.255.2': {
                            'community_attr_to_send': 'extended'
                        }
                    }
                }
            },
        'as_number': '65001'
        }
    },
    'l2vpn_evi': {
        '101': {
            'encapsulation': 'vxlan',
            'replication_type': 'static',
            'type': 'vlan-based'
        },
        '102': {
            'encapsulation': 'vxlan',
            'replication_type': 'ingress',
            'type': 'vlan-based'
        },
        '201': {
            'encapsulation': 'vxlan',
            'replication_type': 'static',
            'type': 'vlan-based'
        },
        '202': {'encapsulation': 'vxlan',
                'replication_type': 'ingress',
                'type': 'vlan-based'
        }
    },
    'l2vpn_global': {
        'default_gateway': True,
        'replication_type': 'static',
        'router_id': 'Loopback1'
    },
    'nve_interfaces': {
        '1': {
            'host_reachability_protocol': 'bgp',
            'ip_addr_state': 'disabled',
            'source_interface': 'Loopback1',
            'vni': {
                'l2vni': {
                    '10101': {
                        'replication_mcast': '225.0.0.101',
                        'replication_type': 'static'},
                        '10102': {
                            'replication_type': 'ingress-replication'
                        },
                        '10201': {
                            'replication_mcast': '225.0.0.101',
                            'replication_type': 'static'
                        },
                        '10202': {
                            'replication_type': 'ingress-replication'
                        }
                },
                'l3vni': {
                    '50901': {
                        'vrf': 'green'
                    },
                    '50902': {
                        'vrf': 'blue'
                    }
                }
            }
        }
    },
    'overlay_interfaces': {
        'Loopback11': {
            'ipv4': '10.1.11.11 255.255.255.0',
            'vrf': 'green'
        },
        'Loopback12': {
            'ipv4': '10.1.12.12 255.255.255.0',
            'vrf': 'blue'
        }
    },
    'svis': {
        '101': {
            'ipv4': '10.1.101.1 255.255.255.0',
            'ipv6': ['2001:101::1/64'],
            'mac_addr': 'dead.beef.abcd',
            'svi_type': 'access',
            'vrf': 'green'
        },
        '102': {
            'ipv4': '10.1.102.1 255.255.255.0',
            'ipv6': ['2001:102::1/64'],
            'mac_addr': 'dead.beef.abcd',
            'svi_type': 'access',
            'vrf': 'green'
        },
        '201': {
            'ipv4': '10.1.201.1 255.255.255.0',
            'ipv6': ['2001:201::1/64'],
            'svi_type': 'access',
            'vrf': 'blue'
        },
        '202': {
            'ipv4': '10.1.202.1 255.255.255.0',
            'ipv6': ['2001:202::1/64'],
            'svi_type': 'access',
            'vrf': 'blue'
        },
        '901': {
            'autostate': False,
            'ipv6_enable': True,
            'svi_type': 'core',
            'unnumbered_interface': 'Loopback1',
            'vrf': 'green'
        },
        '902': {
            'autostate': False,
            'ipv6_enable': True,
            'svi_type': 'core',
            'unnumbered_interface': 'Loopback1',
            'vrf': 'blue'
        }
    },
    'vlans': {
        '101': {
            'evi': '101', 
            'vlan_type': 'access', 
            'vni': '10101'
        },
        '102': {
            'evi': '102', 
            'vlan_type': 'access', 
            'vni': '10102'
        },
        '201': {
           'evi': '201', 
           'vlan_type': 'access', 
           'vni': '10201'
        },
        '202': {
            'evi': '202', 
            'vlan_type': 'access', 
            'vni': '10202'
        },
        '901': {
            'vlan_type': 'core', 
            'vni': '50901'
        },
        '902': {
            'vlan_type': 'core', 
            'vni': '50902'
        }
    },
    'vrf': {
        'blue': {
            'address_family': {
                'ipv4': {
                    'route_target_export': ['2:2', '2:2 stitching'],
                    'route_target_import': ['2:2', '2:2 stitching']
                },
                'ipv6': {
                    'route_target_export': ['2:2', '2:2 stitching'],
                    'route_target_import': ['2:2', '2:2 stitching']
                    }
                },
                'description': 'test vrf',
                'route_distinguisher': '2:2'
            },
        'green': {
            'address_family': {
                'ipv4': {
                    'route_target_export': ['1:1', '1:1 stitching'],
                    'route_target_import': ['1:1', '1:1 stitching']
                },
                'ipv6': {
                    'route_target_export': ['1:1', '1:1 stitching'],
                    'route_target_import': ['1:1', '1:1 stitching']
                }
            },
            'description': 'test vrf',
            'route_distinguisher': '1:1'
        }
    }
}
