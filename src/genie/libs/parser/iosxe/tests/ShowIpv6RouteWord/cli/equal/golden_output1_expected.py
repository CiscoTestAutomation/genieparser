expected_output = {
    'entry': {
        '201:201::/64': {
            'distance': '200',
            'ip': '201:201::',
            'known_via': 'bgp 65001',
            'mask': '64',
            'metric': '0',
            'paths': {
                1: {
                    'age': '00:04:59',
                    'fwd_intf': 'Vlan901',
                    'fwd_ip': '172.16.254.5',
                    'metric': '0',
                    'share_count': '1',
                },
                2: {
                    'age': '00:04:59',
                    'fwd_intf': 'Vlan901',
                    'fwd_ip': '172.16.254.4',
                    'metric': '0',
                    'share_count': '1',
                },
            },
            'route_count': '2/2',
            'share_count': '0',
            'tag_name': '65003',
            'tag_type': 'internal',
        },
    },
    'total_prefixes': 2,
}