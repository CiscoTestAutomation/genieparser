expected_output = {
    'interfaces': {
        'FiveGigabitEthernet1/0/35': {
            'authentication_host_mode': 'multi-domain',
            'authentication_periodic': True,
            'authentication_port_control': 'auto',
            'authentication_priority': 'mab',
            'device_tracking_attach_policy': 'IPDT_POLICY',
            'input_policy': 'AutoQos-4.0-CiscoPhone-Input-Policy',
            'load_interval': '30',
            'mab': True,
            'output_policy': 'AutoQos-4.0-Output-Policy',
            'spanning_tree_portfast': True,
            'switchport_access_vlan': '19',
            'switchport_mode': 'access',
            'trust_device': 'cisco-phone',
        },
    },
}
