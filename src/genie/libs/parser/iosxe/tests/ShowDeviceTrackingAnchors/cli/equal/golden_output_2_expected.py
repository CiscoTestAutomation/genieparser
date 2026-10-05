expected_output = {
    'vlan': {
        '2020': {
            'l3vni': 33001,
            'rmac': 'aabb.cc83.6500',
            'tunnel_src': '100.193.0.2',
            'num_anchors': 2,
            'anchors': {
                '0': {
                    'anchor_ip': '100.196.0.2',
                    'anchor_mac': 'aabb.cc82.1100',
                    'l2vni': 22020,
                },
                '1': {
                    'anchor_ip': '100.195.0.2',
                    'anchor_mac': 'aabb.cc82.5200',
                    'l2vni': 22020,
                },
            },
        },
    },
}
