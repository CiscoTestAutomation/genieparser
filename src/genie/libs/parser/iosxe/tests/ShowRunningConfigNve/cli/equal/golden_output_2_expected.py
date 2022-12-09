expected_output = {
    'bgp': {
        '65001': {
            'address_family': {
                'l2vpn evpn': {
                    'address_family_neighbor': {
                        '172.16.255.2': {
                            'community_attr_to_send': 'extended'
                        },
                        '172.16.255.3': {
                            'community_attr_to_send': 'extended'
                        },
                        '172.16.255.4': {
                            'community_attr_to_send': 'extended'
                        }
                    }
                }
            },
        'as_number': '65001'
        }
    }
}
