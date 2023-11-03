expected_output = {
    'bgp': {
        65001: {
            'as_number': 65001,
            'router_id': '172.16.255.4',
            'ipv4_unicast_state': False,
            'log_neighbor_change': True,
            'address_family': {
                'ipv4': {
                    'advertise_l2vpn_evpn': True,
                    'redistribute_connected': True,
                    'redistribute_static': True,
                },
                'ipv6': {
                    'advertise_l2vpn_evpn': True,
                    'redistribute_connected': True,
                    'redistribute_static': True,
                },
                'l2vpn evpn': {
                    'address_family_neighbor': {
                        '172.16.255.1': {
                            'community_attr_to_send': 'extended',
                        },
                        '172.16.255.2': {
                            'community_attr_to_send': 'extended',
                        },
                    },
                },
            },
        },
    },
}
