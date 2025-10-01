expected_output =  {
    'vlans': {
        '901': {
            'encapsulation': 'IEEE 802.1Q Encapsulation',
            'isl_subinterfaces': 'No subinterface configured with ISL VLAN ID 901',
            'protocols': {
                'IP': {
                    'received': 1,
                    'transmitted': 0,
                },
            },
            'subinterfaces': {
                'GigabitEthernet3.901': {
                    'vlan_id': 901,
                },
            },
            'trunk_interfaces': ['GigabitEthernet3.901'],
            'vlan_id': '901',
        },
    },
}

