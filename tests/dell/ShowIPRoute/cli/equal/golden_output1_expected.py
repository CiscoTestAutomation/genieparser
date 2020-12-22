expected_output = {
    'routes': {
        'route-0_0_0_0': {
            'source_proto': 'S',
            'is_preferred': True,
            'prefix': '0.0.0.0/0',
            'subnet': '0.0.0.0',
            'mask': '0',
            'admin_dist': 254,
            'metric': 1,
            'next_hop': '10.10.21.1',
            'vlan': '20'
        },
        'route-10_10_21_0': {
            'source_proto': 'C',
            'is_preferred': True,
            'prefix': '10.10.21.0/24',
            'subnet': '10.10.21.0',
            'mask': '24',
            'admin_dist': 0,
            'metric': 0,
            'next_hop': 'connected',
            'vlan': '20'
        }
    }
}