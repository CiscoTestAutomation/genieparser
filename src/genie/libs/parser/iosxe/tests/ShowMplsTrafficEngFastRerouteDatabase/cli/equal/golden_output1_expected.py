expected_output = {
    'tunnel_head_end_item_frr_information': {
        'Tunnel500': {
            'protected_tunnel': 'Tunnel500',
            'in_label': 'Tun hd',
            'out_intf_label': 'AT4/0.100:Untagg',
            'frr_intf_label': 'Tu501:20',
            'status': 'ready',
        }
    },
    'prefix_item_frr_information': {
        '10.0.0.8/32': {
            'prefix': '10.0.0.8/32',
            'tunnel': 'Tu500',
            'in_label': '18',
            'out_intf_label': 'AT4/0.100:Pop ta',
            'frr_intf_label': 'Tu501:20',
            'status': 'ready',
        },
        '10.0.8.8/32': {
            'prefix': '10.0.8.8/32',
            'tunnel': 'Tu500',
            'in_label': '19',
            'out_intf_label': 'AT4/0.100:Untagg',
            'frr_intf_label': 'Tu501:20',
            'status': 'ready',
        },
        '10.8.9.0/24': {
            'prefix': '10.8.9.0/24',
            'tunnel': 'Tu500',
            'in_label': '22',
            'out_intf_label': 'AT4/0.100:Untagg',
            'frr_intf_label': 'Tu501:20',
            'status': 'ready',
        }
    }
}
