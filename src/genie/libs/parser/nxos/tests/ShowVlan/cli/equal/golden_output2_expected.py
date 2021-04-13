expected_output = {
    'vlans':{
        '1':{
            'vlan_id': '1',
            'name': 'default',
            'state': 'active',
            'shutdown': False,
            'interfaces': ['Port-channel4', 'Port-channel100', 'Ethernet1/2',
                            'Ethernet1/3', 'Ethernet1/4', 'Ethernet1/5',
                            'Ethernet1/6', 'Ethernet1/7', 'Ethernet1/8',
                            'Ethernet1/9', 'Ethernet1/10', 'Ethernet1/11',
                            'Ethernet1/12', 'Ethernet1/13', 'Ethernet1/14',
                            'Ethernet2/1','Ethernet2/2','Ethernet2/3','Ethernet2/4',
                            'Ethernet2/5','Ethernet2/6'],
            'mode': 'ce',
            'type': 'enet',
            },
        '2': {
            'vlan_id': '2',
            'name': 'VLAN0002',
            'state': 'active',
            'shutdown': False,
            'interfaces': ['Port-channel4', 'Port-channel100', 'Ethernet1/7',
                            'Ethernet1/8','Ethernet1/28']
            },
        '3': {
            'vlan_id': '3',
            'name': 'VLAN0003',
            'state': 'active',
            'shutdown': False,
            'interfaces': ['Port-channel4', 'Port-channel100', 'Ethernet1/7',
                            'Ethernet1/8', 'Ethernet1/28']
            },
        '4': {
            'vlan_id': '4',
            'name': 'VLAN0004',
            'state': 'active',
            'shutdown': False,
            'interfaces': ['Port-channel4', 'Port-channel100', 'Ethernet1/7',
                            'Ethernet1/8', 'Ethernet1/28']
            },
        '5': {
            'vlan_id': '5',
            'name': 'VLAN0005',
            'state': 'active',
            'shutdown': False,
            'interfaces': ['Port-channel4', 'Port-channel100', 'Ethernet1/7',
                            'Ethernet1/8', 'Ethernet1/28']
            },
        '6': {
            'vlan_id': '6',
            'name': 'VLAN0006',
            'state': 'suspend',
            'shutdown': True,
        },
        '10': {'remote_span_vlan': True},
        '20': {'remote_span_vlan': True},
        '30': {'remote_span_vlan': True},
        '31': {'remote_span_vlan': True},
        '32': {'remote_span_vlan': True},
        '33': {'remote_span_vlan': True},
        '303': {
            'private_vlan': {
                'primary': False,
                'type': 'community',
                'ports': ['FastEthernet2/3', 'FastEthernet3/5']
                },
            },
        '500': {
            'private_vlan': {
                'primary': False,
                'type': 'non-operational',
                },
            },
        '403': {
            'private_vlan': {
                'primary': True,
                'association': ['500'],
            },
        },

    },
}