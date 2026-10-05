expected_output = {
    'interfaces': {
        'Port-channel10': {
            'vlan': 100,
            'type': 'SOURCE',
            'status': 'ACTIVE',
            'mvr_vlans': ['100-101'],
        },
        'Port-channel201': {
            'vlan': 201,
            'type': 'RECEIVER',
            'status': 'ACTIVE',
            'mvr_vlans': ['100-101', '340'],
        },
        'Port-channel202': {
            'vlan': 202,
            'type': 'RECEIVER',
            'status': 'ACTIVE',
            'mvr_vlans': ['100-101', '340'],
        },
        'Port-channel203': {
            'vlan': 203,
            'type': 'RECEIVER',
            'status': 'ACTIVE',
            'mvr_vlans': ['100-101', '340'],
        },
        'Port-channel204': {
            'vlan': 204,
            'type': 'RECEIVER',
            'status': 'INACTIVE',
            'mvr_vlans': ['100-101', '340'],
        },
        'Ethernet1/9': {
            'vlan': 340,
            'type': 'SOURCE',
            'status': 'ACTIVE',
            'mvr_vlans': ['340'],
        },
        'Ethernet1/10': {
            'vlan': 20,
            'type': 'RECEIVER',
            'status': 'ACTIVE',
            'mvr_vlans': ['100-101', '340'],
        },
    },
}
