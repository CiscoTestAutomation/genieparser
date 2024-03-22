expected_output = {
    'bgp': {
        '65001': {
            'address_family': {
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
        }
    },
    'l2vpn_global': {
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
                    }
                }
            }
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
        }
    }
}
