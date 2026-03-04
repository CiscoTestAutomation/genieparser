expected_output = {
    'interfaces': {
        'TenGigabitEthernet1/0/3': {
            'description': 'SPAN-ERSPAN-v6_VACl-CISF-ixia-8.1',
            'device_tracking_attach_policy': 'IPDT_MAX_10',
            'flow_monitor_in_sampler': 'monitor_ipv4_in',
            'flow_monitor_input_v6': 'monitor_ipv6_in',
            'input_sampler': 'k12_sampler',
            'keepalive': False,
            'load_interval': '30',
            'spanning_tree_portfast': True,
            'storm_control': {
                'action': 'shutdown',
            },
            'switchport_access_vlan': '122',
            'switchport_mode': 'access',
        },
    },
}

