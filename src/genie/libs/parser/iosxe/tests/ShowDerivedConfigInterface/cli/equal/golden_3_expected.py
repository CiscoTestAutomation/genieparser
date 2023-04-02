expected_output = {
    'derived_config': {
        'GigabitEthernet1/0/10': {
            'description': 'Sourcing interface template beta',
            'switchport_mode': 'trunk',
            'allowed_vlan': '4,456,987'
        },
        'GigabitEthernet1/0/11': {
            'description': 'Sourcing interface template',
            'switchport_mode': 'trunk',
            'allowed_vlan': '456-987'
        }
    }
}