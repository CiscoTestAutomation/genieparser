expected_output = {
    'interfaces': {
        'Management0/0': {
            'name': 'management',
            'link_status': True,
            'line_protocol': True,
            'interface_state': True,
            'config_status': True,
            'mac_address': 'a29e.3600.0006',
            'mtu': 1500,
            'ipv4': {
                '1.1.1.1': {'ip': '1.1.1.1'}
            },
            'subnet': '255.255.255.0'
        },
        'nlp_int_tap': {
            'name': 'nlp_int_tap',
            'link_status': True,
            'line_protocol': True,
            'interface_state': True,
            'config_status': True,
            'mac_address': 'a29e.3600.0080',
            'mtu': 1500,
            'ipv4': {
                '169.254.21.1': {'ip': '169.254.21.1'}
            },
            'subnet': '255.255.255.248'
        }
    }
}
