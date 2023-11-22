expected_output = {
    'vrf': {
        'green': {
            'path': {
                '10.1.101.4 Vlan101': {
                    'directly_connected': True,
                    'distance_preferred_lookup': True,
                    'interface_name': 'Vlan101',
                    'lookup_topology': 'ipv4 multicast base',
                    'neighbor_address': '10.1.101.4',
                    'neighbor_host': '?',
                    'originated_topology': 'ipv4 '
                    'unicast '
                    'base',
                    'route_mask': '10.1.101.4/32',
                    'table_feature': 'static',
                    'table_type': 'unicast'
                }
            },
            'source_address': '10.1.101.4',
            'source_host': '?'
        }
    }
}
