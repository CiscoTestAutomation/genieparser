expected_output = {
    'index': {
        0: {
            'ip_address': 'deny-all',
            'interface_name': 'GigabitEthernet1/0/4',
            'filter_type': 'ip-mac',
            'filter_mode': 'active',
            'vlan': '10',
            'mac_address': 'deny-all'
        },
        1: {
            'interface_name': 'GigabitEthernet3/0/24',
            'filter_type': 'ip-mac',
            'filter_mode': 'inactive-trust-port',
        }
    }
}