expected_output = {
    'interfaces': {
        'TwoGigabitEthernet1/0/36': {
            'acl': {
                'inbound': {
                    'acl_name': '102',
                    'direction': 'in',
                },
            },
            'ip_ospf': {
                '1': {
                    'area': '0',
                },
            },
            'ip_verify_unicast_source_reachable_via': 'rx',
            'ip_verify_unicast_source_reachable_via_rx_acl': '102',
            'ip_verify_unicast_source_reachable_via_rx_allow_self_ping': True,
            'ipv4': {
                'ip': '50.0.0.2',
                'netmask': '255.255.255.0',
            },
            'ipv6': ['50::2/64'],
            'ipv6_enable': True,
            'ipv6_ospfv3': {
                '1': {
                    'area': '0',
                },
            },
        },
    },
}