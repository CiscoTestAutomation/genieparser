

expected_output = {
    'evi': {
        145: {
            'bridge_domain': 'tb1-core1',
            'type': 'PBB',
            'unicast_label': '16000',
            'multicast_label': '16001',
            'rd_config': 'none',
            'rd_auto': '(auto) 10.1.100.100:145',
            'rt_auto': '100:145',
            'route_target_in_use': {
                '100:145': {
                    'import': True,
                    'export': True,
                },
            },
        },
        165: {
            'bridge_domain': 'tb1-core2',
            'type': 'PBB',
            'unicast_label': '16002',
            'multicast_label': '16003',
            'rd_config': 'none',
            'rd_auto': '(auto) 10.1.100.100:165',
            'rt_auto': '100:165',
            'route_target_in_use': {
                '100:165': {
                    'import': True,
                    'export': True,
                },
            },
        },
        185: {
            'bridge_domain': 'tb1-core3',
            'type': 'PBB',
            'unicast_label': '16004',
            'multicast_label': '16005',
            'rd_config': 'none',
            'rd_auto': '(auto) 10.1.100.100:185',
            'rt_auto': '100:185',
            'route_target_in_use': {
                '100:185': {
                    'import': True,
                    'export': True,
                },
            },
        },
        65535: {
            'bridge_domain': 'ES:GLOBAL',
            'type': 'BD',
            'unicast_label': '0',
            'multicast_label': '0',
            'rd_config': 'none',
            'rd_auto': '(auto) 10.1.100.100:0',
            'rt_auto': 'none',
        },
    },
}
