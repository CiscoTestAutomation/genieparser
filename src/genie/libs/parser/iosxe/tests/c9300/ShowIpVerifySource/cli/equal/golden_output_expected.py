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
            'ip_address': '20.1.1.11',
            'interface_name': 'GigabitEthernet3/0/24',
            'filter_type': 'ip-mac',
            'filter_mode': 'active',
            'vlan': '20',
            'mac_address': '00:12:01:00:00:01'
        },
        2: {
            'ip_address': 'deny-all',
            'interface_name': 'GigabitEthernet3/0/24',
            'filter_type': 'ip-mac',
            'filter_mode': 'active',
            'vlan': '10',
            'mac_address': 'deny-all'
        }
    }
}